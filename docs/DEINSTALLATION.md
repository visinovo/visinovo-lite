# Deinstallationsanleitung – Visinovo Lite

**Kurzform:** Visinovo Lite wird wie jedes Programm über die
Windows-App-Verwaltung deinstalliert. **Deine lokalen Daten
(Listings, Analysen, Einstellungen) bleiben dabei standardmäßig
erhalten** – der Deinstaller fragt explizit, ob sie gelöscht
werden sollen.

## Wichtige Pfade

| Pfad | Inhalt |
|---|---|
| `%LOCALAPPDATA%\Programs\Visinovo Lite` | die installierte App |
| `%LOCALAPPDATA%\Visinovo` | **Deine Daten** (Datenbank, Logs, Exporte) |

Beispiel für den Pfad (typischer Benutzerordner):
`C:\Benutzer\<DeinName>\AppData\Local\Visinovo`.

## 1. App schließen

Schließe das Visinovo-Lite-Fenster, bevor Du die App entfernst.
(Läuft die App noch, meldet der Deinstaller das und bittet, sie
zuerst zu schließen.)

## 2. Deinstallieren über die Windows-App-Verwaltung

1. **Windows 11:** *Einstellungen → Apps → Installierte Apps*
   (oder: *Einstellungen → Apps → Apps und Features*).
2. **Windows 10:** *Einstellungen → Apps → Apps und Features*
   (alt: *Systemsteuerung → Programme → Programme oder Funktionen
   deinstallieren*).
3. Suche **„Visinovo Lite"** und wähle **Deinstallieren**.
4. Der Deinstaller fragt:
   **„Daten beim Entfernen löschen?"**
   - **Nein** (Standard-Empfehlung): die App wird entfernt,
     `%LOCALAPPDATA%\Visinovo` bleibt erhalten → spätere
     Neuinstallation nimmt die Daten wieder auf.
   - **Ja**: App **und** alle lokalen Daten werden gelöscht
     (unwiderruflich).
   - **Abbrechen**: Deinstallation wird abgebrochen, nichts wird
     entfernt.
5. Bestätige – die App-Dateien unter
   `%LOCALAPPDATA%\Programs\Visinovo Lite` werden entfernt,
   Startmenü-Verknüpfungen gelöscht.

## 3. Daten manuell entfernen (nur bei Bedarf)

Wenn Du die App deinstalliert hast und die Daten zusätzlich
löschen willst:

1. App **geschlossen** haben (Punkt 1).
2. Ordner `%LOCALAPPDATA%\Visinovo` im Datei-Explorer löschen.

Damit sind alle lokalen Daten vollständig entfernt.

## 4. Daten nur zurücksetzen (App bleibt installiert)

Alternative ohne Deinstallation – direkt in der App:

1. Visinovo Lite öffnen.
2. *Einstellungen* (Navigation) → **„Daten zurücksetzen"**.
3. Im Browser-Dialog bestätigen.

Das lokale Konto wird neu angelegt und der Datenbestand ist leer
(Listings, Analysen, Experimente, Importe). Der App-Ordner und die
Installation bleiben bestehen.

## Nach der Deinstallation

- Installation: vollständig entfernt (App-Ordner + Verknüpfungen).
- Daten: erhalten (falls „Nein" gewählt) oder entfernt (falls „Ja"
  bzw. manuelles Löschen).
- Eine spätere Neuinstallation fragt **nicht** erneut nach Daten,
  die bereits lokal vorhanden sind – sie setzt dort fort.
