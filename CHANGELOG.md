# Changelog – Visinovo Lite

Alle nennenswerten Änderungen an den veröffentlichten
Installationsdateien werden hier dokumentiert. Format nach
[Keep a Changelog](https://keepachangelog.com/de/1.0.0/);
Versionierung nach [SemVer](https://semver.org/lang/de/).

Zu jedem Release sind die Größe und die **SHA-256-Prüfsumme** der
Setup-EXE angegeben (Details zur Verifikation:
[Installationsanleitung](docs/INSTALLATION.md)). Die maschinenlesbare
Fassung liegt in [`SHA256SUMS.txt`](SHA256SUMS.txt).

## [0.2.0] – 2026-09-08

Erste öffentliche Version von Visinovo Lite.

### Hinzugefügt

- **Demo-Listing beim ersten Start** („Stirnholzbrett aus Birke“ –
  handgemachtes Schneidebrett) mit drei Analysen und Score-Verlauf,
  8 Wochen Shopstatistik und einem abgeschlossenen
  Optimierungsexperiment; eindeutig erkennbare Beispieldaten, jederzeit
  löschbar.
- **Projekt unterstützen** (Footer und *Einstellungen*): offizielle
  Unterstützungs-Kanäle [GitHub Sponsors](https://github.com/sponsors/visinovo),
  [Ko-fi](https://ko-fi.com/visinovo) und
  [Liberapay](https://liberapay.com/visinovo).

### Behoben

- „Daten zurücksetzen“ konnte an einer vom laufenden Prozess
  gesperrten Windows-Datenbank-Datei scheitern; der Reset arbeitet
  jetzt zuverlässig mit geschütztem Datei-Handling.

### Bekannte Einschränkungen

- wie in [0.1.0] (unsigned EXE/SmartScreen, kein automatisches
  Update, WebView2-Runtime).

### Download & Integrität

| Datei | Größe | SHA-256 |
|---|---|---|
| `Visinovo-Lite-Setup-0.2.0.exe` | 40,9 MB | `AF06F8F2BA5506B95F4F67AB7F8B299160857B31062B031C8A88915F0A1BACFB` |

Download: <https://github.com/visinovo/visinovo-lite/releases/tag/lite-v0.2.0>

## [0.1.0] – 2026-09-03

Internes Erst-Build (nicht veröffentlicht; erste öffentliche Version
ist [0.2.0]).

### Hinzugefügt

- **Installation als Windows-Desktop-App** (ohne Administratorrechte):
  Setup-EXE installiert die App unter
  `%LOCALAPPDATA%\Programs\Visinovo Lite`; das native Fenster wird
  über Microsoft Edge WebView2 gerendert.
- **Listings verwalten** (max. **3** lokale Listings): Titel,
  Beschreibung, Kategorie, Produkttyp, Tags (max. 13), Preis,
  Währung, Hauptmarkt, Zielgruppe, Status; internes Naming und
  optionale Etsy-Listing-ID zur Verknüpfung importierter Statistiken.
- **Listing-Check (Analyse):** Qualitätsscore von 100 Punkten mit
  Teilbewertungen, konkreten Verbesserungsvorschlägen,
  Titelvorschlag und Tag-Vorschlägen (max. 13); Anzeige der
  erkannten Listingsprache.
- **Keyword-Analyse:** Chancen-Bewertung (0–100) für Suchbegriffe
  auf Basis der Listing-Daten.
- **CSV-Import** lokaler Statistik-Exporte (z. B. aus Etsy) mit
  Zuordnung zu bestehenden Listings (Listing-ID).
- **Experimente:** dokumentierte Tests von Listing-Änderungen
  (Titel/Beschreibung/Tags) mit Start-/Enddatum und Status.
- **Berichte:** druckbarer HTML- und PDF-Bericht je Analyse.
- **Dashboard** mit Übersicht (Zähler „x / 3", letzte Analysen,
  Hinweis auf lokale Daten).
- **Lokale Einstellungen:** Datenpfad, Versionsnummer,
  Listing-Limit, „Daten zurücksetzen" (explizite Bestätigung).
- **Lokale Datenhaltung:** SQLite-Datenbank ausschließlich unter
  `%LOCALAPPDATA%\Visinovo` (`data/`, `logs/`, `exports/`);
  keine Cloud, keine Telemetrie, kein Tracking.
- **Sicherheit:** Webserver bindet ausschließlich an `127.0.0.1`
  (nicht im Netzwerk erreichbar); Single-Instance-Sperre pro
  Datenbank; saubere Start-/Stopp-Abläufe.
- **Deinstallation** über Windows-Apps-Verwaltung; lokale Daten
  werden **nur nach expliziter Bestätigung** gelöscht
  (Standard: Daten bleiben erhalten).

### Bekannte Einschränkungen

- Die Setup-EXE ist (aktuell) **nicht digital signiert**; Windows
  SmartScreen kann beim ersten Start eine Warnung zeigen –
  erwartet und in der Installationsanleitung erklärt.
- Es gibt (bewusst) **kein** automatisches Update; Updates erfolgen
  durch manuelle Neuinstallation der aktuellen Release-Version
  (Daten bleiben erhalten).
- Desktop-Fenster benötigt die Microsoft Edge WebView2 Runtime
  (Windows 11: enthalten; Windows 10: meist vorhanden, sonst
  Installation über die Hinweise in der App).

### Download & Integrität

| Datei | Größe | SHA-256 |
|---|---|---|
| `Visinovo-Lite-Setup-0.1.0.exe` | 40,7 MB | `311E10343E57F096F2EC8D0731ABE71049F780B6264A49EA1FE6218FE5BED830` |

Download: <https://github.com/visinovo/visinovo-lite/releases/tag/lite-v0.1.0>
