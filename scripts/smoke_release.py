"""Release-Smoke-Test: Kernpfad einer installierten Visinovo-Lite-Instanz.

Dieses Skript prueft eine **installierte** App (Setup-EXE aus dem
GitHub-Release) ueber HTTP – exakt so, wie sie beim Endnutzer laeuft
(Waitress auf 127.0.0.1, Auto-Login, CSRF). Es nutzt nur die
Python-Standardbibliothek.

Geprueft wird:

1. ``/healthz/`` antwortet
2. Das Dashboard rendert (Auto-Login, keine Login-UI)
3. Drei Listings werden angelegt
4. Das vierte Listing wird abgelehnt (3-Listing-Limit)
5. Ein Listing wird analysiert (Qualitätsscore + Vorschläge)

Start (Port kommt aus der Instanz-Sperre, s. Workflow/README):

    python scripts/smoke_release.py --port 8765

Exit-Code 0 = alle Checks bestanden.
"""

import argparse
import http.cookiejar
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import urllib.response

FAILURES = []


class Session:
    """Kleiner HTTP-Client mit Cookie-Jar (Session + CSRF-Cookie)."""

    def __init__(self):
        jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(jar)
        )

    def get(self, url: str) -> urllib.response.addinfourl:
        return self.opener.open(url, timeout=30)

    def post(self, url: str, data: dict) -> urllib.response.addinfourl:
        body = urllib.parse.urlencode(data).encode("utf-8")
        return self.opener.open(
            urllib.request.Request(url, data=body, method="POST"), timeout=60
        )


def check(label: str, ok: bool, detail: str = "") -> None:
    status = "ok  " if ok else "FAIL"
    print(f"{status} {label}" + (f"  ({detail})" if detail and not ok else ""))
    if not ok:
        FAILURES.append(label)


def csrf_token(html: str) -> str:
    match = re.search(r'name="csrfmiddlewaretoken"\s+value="([^"]+)"', html)
    if match is None:
        raise RuntimeError("CSRF-Token nicht im Formular gefunden")
    return match.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    base = f"http://127.0.0.1:{args.port}"
    s = Session()

    # 1. Health-Check
    try:
        r = s.get(f"{base}/healthz/")
        check("Health-Check /healthz/", r.status == 200, f"Status {r.status}")
    except (urllib.error.URLError, OSError) as exc:
        check("Health-Check /healthz/", False, repr(exc))
        return 1

    # 2. Dashboard (Auto-Login, keine Login-UI)
    r = s.get(f"{base}/app/")
    body = r.read().decode("utf-8", "replace")
    check(
        "Dashboard rendert (Auto-Login)",
        r.status == 200 and "Dashboard" in body,
        f"Status {r.status}",
    )
    check("Keine Login-UI in der Lite-Navigation", "Anmelden" not in body)

    # 3./4. Drei Listings anlegen, viertes wird abgelehnt (3-Listing-Limit)
    listing_data = {
        "title": "Tagesplan für Kinder – visuelle Routinekarte zum Ausdrucken, PDF",
        "description": (
            "Der visuelle Tagesplan zeigt den Kindergarten-Alltag Schritt für "
            "Schritt. Ideal als Routinenkarte für Kinder zwischen 3 und 6 Jahren: "
            "weniger Stress am Morgen, mehr Selbstständigkeit. Einfach PDF "
            "herunterladen und ausdrucken."
        ),
        "category": "Papeterie > Druckvorlagen",
        "tags": (
            "routinenkarte\ntagesplan\nkindergarten\nkind\nvisuell\npdf\n"
            "druckvorlage\nalltag\nvisualisieren\nmaterial\neltern\n"
            "morgenroutine\nkindergartenroutine"
        ),
        "product_type": "digital",
        "price": "4,90",
        "currency": "EUR",
        "primary_market": "DE",
        "status": "draft",
    }
    detail_url = None
    for i in range(1, 5):
        form = s.get(f"{base}/app/listings/neu/").read().decode("utf-8", "replace")
        data = {
            **listing_data,
            "name": f"Listing {i}",
            "csrfmiddlewaretoken": csrf_token(form),
        }
        r = s.post(f"{base}/app/listings/neu/", data)
        final_url = r.geturl()
        body = r.read().decode("utf-8", "replace")
        if i <= 3:
            ok = re.search(r"/app/listings/\d+/$", final_url) is not None
            check(f"Listing {i} angelegt", ok, f"Final-URL {final_url}")
            if i == 1:
                detail_url = final_url
        else:
            ok = (
                final_url.rstrip("/").endswith("/app/listings/neu")
                and "maximal 3 gespeicherte Listings" in body
            )
            check(
                "4. Listing abgelehnt (3-Listing-Limit)", ok, f"Final-URL {final_url}"
            )

    # 5. Analyse des ersten Listings (Analyseaustausch)
    if detail_url is not None:
        pk = detail_url.rstrip("/").rsplit("/", 1)[1]
        form = s.get(f"{base}/app/listings/{pk}/analysieren/").read().decode(
            "utf-8", "replace"
        )
        data = {
            "title": listing_data["title"],
            "description": listing_data["description"],
            "tags": listing_data["tags"],
            "category": listing_data["category"],
            "product_type": listing_data["product_type"],
            "audience": "Eltern von Vorschulkindern",
            "top_keywords": "tagesplan kinder\nroutinenkarte kindergarten",
            "price": "4,90",
            "currency": "EUR",
            "primary_market": "DE",
            "csrfmiddlewaretoken": csrf_token(form),
        }
        r = s.post(f"{base}/app/listings/{pk}/analysieren/", data)
        body = r.read().decode("utf-8", "replace")
        check(
            "Analyse läuft (Qualitätsscore + Vorschläge)",
            r.status == 200
            and "Qualitätsscore von 100 Punkten" in body
            and "Vorschlag:" in body,
            f"Status {r.status}",
        )

    print(f"\n{'=' * 40}\n{len(FAILURES)} Fehler")
    if FAILURES:
        for label in FAILURES:
            print(f"  {label}")
        return 1
    print("Alle Release-Smoke-Checks bestanden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
