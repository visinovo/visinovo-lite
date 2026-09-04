# Changelog – Visinovo Lite

Alle nennenswerten Änderungen an den veröffentlichten
Installationsdateien werden hier dokumentiert. Format nach
[Keep a Changelog](https://keepachangelog.com/de/1.0.0/);
Versionierung nach [SemVer](https://semver.org/lang/de/).

Zu jedem Release sind die Größe und die **SHA-256-Prüfsumme** der
Setup-EXE angegeben (Details zur Verifikation:
[Installationsanleitung](docs/INSTALLATION.md)). Die maschinenlesbare
Fassung liegt in [`SHA256SUMS.txt`](SHA256SUMS.txt).

## [0.1.0] – 2026-09-03

Erstveröffentlichung (Erst-Release) von Visinovo Lite.

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
