# Installationsanleitung – Visinovo Lite

Visinovo Lite ist eine **kostenlose** Windows-Desktop-App. Die
Installation läuft **ohne Administratorrechte** (User-Installation),
ohne Python und ohne Internetverbindung.

## Voraussetzungen

| | |
|---|---|
| Betriebssystem | Windows 10 oder 11, 64-Bit |
| Rechte | normale Benutzerkonto (kein Admin nötig) |
| Festplatte | ca. 150 MB frei (Installation) |
| Internet | **nicht erforderlich** für Installation und Nutzung |
| Desktop-Fenster | Microsoft Edge WebView2 Runtime (siehe unten) |

### Microsoft Edge WebView2 Runtime

Das Desktop-Fenster wird mit der Microsoft Edge WebView2 Runtime
gerendert:

- **Windows 11:** die Runtime ist bereits enthalten.
- **Windows 10:** in den meisten Fällen vorhanden (z. B. durch
  Microsoft Edge). Falls nicht: die App zeigt beim Start einen
  klaren Hinweis; die Runtime ist kostenlos von
  [Microsoft](https://go.microsoft.com/fwlink/p/?LinkId=2124703)
  verfügbar (System-Installation, einmalig).

Ohne Runtime startet die App nicht im Fenster-Modus – die
Installation selbst ist davon nicht betroffen.

## 1. Setup-Datei herunterladen

1. Gehe zu den [Releases](https://github.com/visinovo/visinovo-lite/releases).
2. Lade die aktuellste **`Visinovo-Lite-Setup-<version>.exe`**
   herunter (Assets des Releases).

> **Wichtig:** Lade die Datei ausschließlich über das offizielle
> GitHub-Repository `visinovo/visinovo-lite` herunter.

## 2. Prüfsumme prüfen (empfohlen)

Da die Setup-EXE (aktuell) nicht digital signiert ist, lässt sich
die Integrität unabhängig über die **SHA-256-Prüfsumme**
verifizieren. Der erwartete Wert steht im
[Changelog](../CHANGELOG.md), im jeweiligen Release und in
[`SHA256SUMS.txt`](../SHA256SUMS.txt).

Unter Windows mit PowerShell (im Download-Ordner):

```powershell
Get-FileHash .\Visinovo-Lite-Setup-0.1.0.exe -Algorithm SHA256
```

Vergleiche den ausgegebenen `Hash`-Wert (Groß-/Kleinschreibung
egal) mit dem Wert aus dem Changelog/Release:

```
311E10343E57F096F2EC8D0731ABE71049F780B6264A49EA1FE6218FE5BED830
```

**Weicht der Wert ab: Datei löschen, neu herunterladen, nicht
installieren.**

## 3. Installation starten

Doppelklick auf die `Visinovo-Lite-Setup-<version>.exe`.

### SmartScreen-Warnung (erwartbar)

Weil die EXE nicht signiert ist, kann Windows SmartScreen eine
Warnung zeigen („Windows hat den Computer geschützt" /
„Unbekannte App"). **Das ist kein Fehler und kein Virus-Hinweis
dieser App** – es ist die normale Windows-Reaktion auf
unsignierte Programme.

- Klicke auf **„Weitere Informationen"** → **„Trotzdem ausführen"**,
  wenn Du die Datei wie oben verifiziert hast.
- Es wird bewusst **keine** Windows-Sicherheitsfunktion umgangen.
- Die Warnung wird mit zunehmender Verbreitung (Download-Reputation)
  und mit einer späteren Code-Signierung abnehmen.

### Installer

1. Wähle den Zielordner (Standard ist in Ordnung:
   `%LOCALAPPDATA%\Programs\Visinovo Lite`).
2. Bestätige – **es erscheint keine UAC/Abfrage nach Admin-Rechten**.
3. Optional: Desktop-Verknüpfung anlegen.
4. Nach Abschluss: „Visinovo Lite starten" (optional).

Die Installation legt **nur** Dateien im Installationsordner an.
Deine Anwendungsdaten werden erst beim **ersten Start** der App
angelegt.

## 4. Erster Start

1. Starte die App (Startmenü-/Desktop-Verknüpfung
   „Visinovo Lite").
2. Beim ersten Start wird die lokale Datenbank unter
   `%LOCALAPPDATA%\Visinovo` angelegt und migriert (einmalig,
   wenige Sekunden).
3. Das Fenster öffnet sich **erst**, wenn der lokale Webserver
   bereit ist (Bindeadresse: ausschließlich `127.0.0.1`).
4. Du landest direkt im Dashboard – **kein Login nötig** (lokales
   Konto wird automatisch angemeldet).

### Fehlerbehebung (Erster Start)

| Symptom | Ursache / Abhilfe |
|---|---|
| Fenster öffnet sich nicht, Hinweis auf WebView2 | Runtime fehlt → siehe oben |
| Fehlermeldung „läuft bereits" | Zweiter Start, während eine Instanz läuft – erst die offene Instanz schließen (nur eine Instanz pro Datenordner) |
| App beendet sich sofort | Log-Datei prüfen: `%LOCALAPPDATA%\Visinovo\logs\visinovo.log` (letzte Zeilen) |

## 5. Update auf eine neue Version

Ein automatisches Update gibt es (bewusst) nicht. Zum Aktualisieren:

1. Aktuelle Release-EXE herunterladen und **Prüfsumme prüfen**
   (wie oben).
2. Über die Setup-EXE **neu installieren** – der Installer
   erkennt die bestehende Installation und aktualisiert sie
   (gleiche `AppId`); die lokalen Daten unter
   `%LOCALAPPDATA%\Visinovo` bleiben **unberührt** erhalten.
3. App neu starten.

> Hinweis: Schließe vor der Neuinstallation die laufende App
> (sonst meldet der Installer, dass die App noch läuft).

## Was die App wo ablegt

| Ort | Inhalt |
|---|---|
| `%LOCALAPPDATA%\Programs\Visinovo Lite` | die App (wird durch Installation/Deinstallation verwaltet) |
| `%LOCALAPPDATA%\Visinovo\data` | lokale SQLite-Datenbank, lokaler Secret-Key |
| `%LOCALAPPDATA%\Visinovo\logs` | Log-Dateien (rotierend, max. 4 Dateien) |
| `%LOCALAPPDATA%\Visinovo\exports` | Exporte/Berichte, die Du in der App erzeugst |
| Startmenü/Option: Desktop | Verknüpfungen |

Details: [Deinstallation](DEINSTALLATION.md) ·
[Datenschutz](DATENSCHUTZ.md) · [Support](SUPPORT.md)
