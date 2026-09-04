# Support & Fehlerberichte – Visinovo Lite

Visinovo Lite ist eine **Freeware**: Support erfolgt auf
freiwilliger Basis über die Kanäle unten. Es besteht kein
Anspruch auf Support, Reparatur oder eine bestimmte Reaktionszeit.

## Wo ist Hilfe?

| Thema | Ort |
|---|---|
| Installation | [Installationsanleitung](INSTALLATION.md) |
| Deinstallation / Daten | [Deinstallationsanleitung](DEINSTALLATION.md) |
| Datenschutz | [Datenschutzhinweis](DATENSCHUTZ.md) |
| Changelog / bekannte Einschränkungen | [Changelog](../CHANGELOG.md) |
| Fehler, Ideen, Fragen | **GitHub Issues** (unten) |

## Fehlerbericht erstellen (GitHub Issues)

1. Gehe zu <https://github.com/visinovo/visinovo-lite/issues>.
2. Prüfe kurz, ob das Problem schon jemand gemeldet hat.
3. Erstelle ein neues Issue (englisch oder deutsch) und nimm
   möglichst diese Punkte auf:

- **Was ist passiert?** (kurz, ein Satz)
- **Was hast Du erwartet?**
- **Schritte zur Reproduktion** (z. B. „Listings anlegen →
  Analysieren → Score fehlt")
- **Version der App** (in der App: *Einstellungen* →
  „Version"; dort steht z. B. `0.1.0`)
- **Windows-Version** (z. B. „Windows 11 Pro 24H2")
- **Letzte Zeilen der Log-Datei** (siehe unten)
- **Screenshot** (optional, nur so weit, wie Du es teilen
  möchtest)

## Log-Datei (lokal)

Die App schreibt eine rotierende Log-Datei:

```
%LOCALAPPDATA%\Visinovo\logs\visinovo.log
```

(typischerweise
`C:\Benutzer\<DeinName>\AppData\Local\Visinovo\logs\visinovo.log`)

Nimm für einen Fehlerbericht die **letzten ~50 Zeilen** der
Log-Datei mit. **Vor der Weitergabe:**

- keine Datenbankdatei (`visinovo.sqlite3`) übermitteln;
- Listing-Texte/Markennamen, die Du nicht teilen willst,
  aus den Log-Zeilen streichen;
- lokale Pfade abkürzen, wenn gewünscht.

## Was bitte **nicht** mitgeschickt wird

- die lokale Datenbank `visinovo.sqlite3`
- den lokalen Secret-Key (`%LOCALAPPDATA%\Visinovo\data\secret.key`)
- `.env`-Dateien oder andere Secrets
- personenbezogene Daten, die Du nicht teilen willst

## Erwartbare Antwortzeiten

Freeware → **keine** garantierte SLA. Eine Antwort kann Tage bis
Wochen dauern oder ausbleiben. Danke für Dein Verständnis.

## Sicherheitshinweis

Wenn Du **sicher** bist, dass die heruntergeladene Datei
manipuliert wurde (Prüfsumme weicht ab, unerwartetes Verhalten),
**nicht** installieren bzw. sofort deinstallieren und den Fall
als **Sicherheit** labelled GitHub-Issue melden.
