# Datenschutzhinweis – Visinovo Lite

Visinovo Lite ist eine **lokal laufende** Windows-Desktop-App.
Dieser Hinweis beschreibt, welche Daten die App verarbeitet, wo
sie liegen und dass **keine** Daten an einen Server oder Dritte
gesendet werden.

## Der wichtigste Satz

**Alle Daten bleiben auf Deinem Computer.** Es gibt keinen
Cloud-Upload, keine Telemetrie, kein Tracking, keinen Account und
keinen Versand von Daten an den Anbieter oder Dritte.

## Welche Daten verarbeite ich (die App)?

Die App verarbeitet **ausschließlich** Daten, die **Du** selbst
eingibst oder importierst:

- Listing-Daten (Titel, Beschreibung, Tags, Preis, Kategorie,
  Zielgruppe, Markt, Status)
- Analyse-Ergebnisse und -Vorschläge (lokal berechnet)
- Importierte CSV-Statistiken (lokal auf Deiner Festplatte)
- Experiment-Dokumente (Titel-/Beschreibungs-/Tag-Änderungen)
- Berichte (HTML/PDF, lokal erzeugt)
- Technische App-Daten: lokale Konfiguration, lokale
  Secret-Key-Datei (für die lokale Session), Log-Dateien

Die App fragt **nicht** nach personenbezogenen Daten wie Name,
E-Mail-Adresse oder Passwort. Ein lokales Systemkonto
(Standardname `local`) wird beim ersten Start automatisch erzeugt
und ist nicht mit einer Identität verknüpft.

## Wo liegen die Daten?

Alle Daten liegen **ausschließlich** unter
`%LOCALAPPDATA%\Visinovo` (typischerweise
`C:\Benutzer\<DeinName>\AppData\Local\Visinovo`):

| Unterverzeichnis | Inhalt |
|---|---|
| `data/` | lokale SQLite-Datenbank (`visinovo.sqlite3`), lokaler Secret-Key |
| `logs/` | rotierende Log-Dateien (`visinovo.log`, max. 4 Dateien) |
| `exports/` | von Dir erzeugte Exporte/Berichte |

Die installierte App selbst liegt unter
`%LOCALAPPDATA%\Programs\Visinovo Lite` (wird durch
Installation/Deinstallation verwaltet).

## Netzwerk & Internet

- Der integrierte Webserver bindet **ausschließlich an
  `127.0.0.1`** (nur Dein eigener Rechner; nicht im Netzwerk
  sichtbar).
- Für **keine** Kernfunktion ist eine Internetverbindung
  erforderlich: Installation, Analyse, Import, Berichte,
  Einstellungen – alles läuft offline.
- Die App nimmt **keine** ausgehenden Netzwerkverbindungen zu
  Diensten des Anbieters oder Dritter auf (keine Telemetrie,
  kein Update-Check, keine externe Analyse).
- Einzige Ausnahme: Wenn Du **aktiv** auf einen externen Link in
  der App klickst (z. B. „Projekt unterstützen"), öffnet sich
  Dein Standardbrowser – das ist eine bewusste Aktion von Dir,
  keine automatische Verbindung der App.

## Keine Weitergabe, keine Aufzeichnung

- Es werden **keine** Nutzungsdaten, Fehlermeldungen,
  Leistungsdaten oder Inhalte an Server übertragen.
- Es werden **keine** Cookies, Fingerabdrücke oder Tracking-
  Mechanismen externer Dienste eingesetzt.
- Es findet **kein** Logging von Dateninhalten auf
  Nicht-Deinem-Rechner statt.

## Deine Rechte / Umgang mit Deinen Daten

Da alle Daten lokal sind, stehen Dir folgende Möglichkeiten
**unmittelbar** zur Verfügung (ohne Anfrage an den Anbieter):

| Recht | Umsetzung |
|---|---|
| **Auskunft** | Öffnen der lokalen Datenbank bzw. der App (Listings/Analysen) |
| **Berichtigung** | Direkt in der App bearbeiten |
| **Löschung** | *Einstellungen → Daten zurücksetzen* (App bleibt installiert) oder Deinstallation mit „Daten löschen" bzw. manuelles Löschen von `%LOCALAPPDATA%\Visinovo` (siehe [Deinstallation](DEINSTALLATION.md)) |
| **Datensicherung** | Kopieren des Ordners `%LOCALAPPDATA%\Visinovo` (bei geschlossener App) |

## Besondere Hinweise

- **Keine Gewähr für Vertraulichkeit Deiner Geräte:** Da die Daten
  lokal sind, gilt die Sicherheit Deines Computers (Benutzer-
  konto, Festplattenverschlüsselung, Antivirus).
- **Logs:** Die Log-Dateien enthalten technische Informationen
  (Start/Stopp, Fehler). Bitte entferne vor einer Weitergabe an
  Dritte (z. B. im Support) sensible Inhalte aus den Log-Dateien
  (siehe [Support](SUPPORT.md)).
- **Kein Kinderschutz-Hinweis erforderlich:** Die App richtet
  sich an Personen, die eigene digitale Listings erstellen
  (in der Regel volljährige Händler); es finden keine
  Kommunikation oder Interaktion mit Kindern statt.

## Kontakt / Fragen

Fragen zum Datenschutz oder Hinweise auf Probleme:
[GitHub Issues](https://github.com/visinovo/visinovo-lite/issues)
(„Datenschutz" als Label verwenden). Es besteht kein Anspruch auf
Reaktion; es werden **keine** personenbezogenen Daten über diesen
Kanal erhoben, wenn Du keine angibst.
