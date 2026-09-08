# Release-Checkliste – Visinovo Lite

**Für den Eigentümer.** Alle Schritte laufen **manuell**; in diesem
öffentlichen Repository findet **kein** Build statt (der Build
erfolgt im **privaten SaaS-Repository**, lokal auf einem
Windows-Rechner).

Legende: `[SaaS]` = im privaten SaaS-Repository,
`[Lite]` = in diesem öffentlichen Repository.

Vor jedem Release: `docs/RELEASE_CHECKLIST.md` kopieren und die
Checkboxen abarbeiten. Eine abgearbeitete Liste kann in das
jeweilige GitHub-Release (Abschnitt „Release-Notes“) verlinkt
oder als Issue vermerkt werden.

---

## 0. Vorbereitung (vor dem eigentlichen Release)

- [ ] **Version festlegen** (SemVer, z. B. `0.2.0`).
- [ ] Offene Punkte aus dem letzten Release abgearbeitet
  (Issues, Changelog „Unreleased“-Abschnitt).
- [ ] Sauberer Arbeitsstand im SaaS-Repository (`git status`
  ohne unbeabsichtigte Änderungen).

## 1. Versionsnummer setzen `[SaaS]`

Alle drei Stellen müssen zur gewählten Version passen:

| Stelle | Datei | Wert |
|---|---|---|
| Inno-Script / PyInstaller / Setup-Dateiname | `packaging/version.txt` | neue Version (z. B. `0.2.0`) – **Single Source of Truth** |
| Launcher / UI (Footer + *Einstellungen*) | `visinovo/settings_lite.py` → `LITE_VERSION` | dieselbe Version |
| Core (Health-Check, Support-Seite) | `visinovo/__init__.py` → `__version__` | **geteilt mit der SaaS-Version** – nur ändern, wenn auch die SaaS-Version mitgezogen wird; sonst konsistent lassen |

> `packaging/version.txt` und `LITE_VERSION` müssen **immer**
> übereinstimmen (eine wird dem Endnutzer angezeigt, die andere
> steuert den Dateinamen der Setup-EXE).

## 2. `CHANGELOG.md` aktualisieren `[Lite]`

- [ ] Im aktuellen `[Unreleased]`/Versionsabschnitt:
      Hinzugefügt / Geändert / Behoben / Bekannte
      Einschränkungen aufführen.
- [ ] **Noch ohne** SHA-256/Größe (werden in Schritt 4 eingetragen).

## 3. Lokal sauberen Build ausführen `[SaaS]`

Aus dem SaaS-Repository-Root (Windows, PowerShell):

```powershell
# einmalig: Build-Umgebung
python -m venv .venv
.venv\Scripts\pip install -r requirements-build.txt

# Build (Version kommt aus packaging\version.txt)
.\scripts\build.ps1
```

- [ ] Build erfolgreich: `dist\setup\Visinovo-Lite-Setup-<version>.exe`
      existiert.
- [ ] Am Ende der Ausgabe steht die **SHA-256** der Setup-EXE
      (wird automatisch ausgegeben).
- [ ] **Option:** vorher `dist\` und `build\` leeren, damit der
      Build garantiert sauber ist.

Details: `docs/BUILD_WINDOWS.md` im privaten SaaS-Repository
(Build-, Test- und SmartScreen-Hinweise).

## 4. SHA-256 dokumentieren `[Lite]`

- [ ] SHA-256 (und Größe) der Setup-EXE in `CHANGELOG.md`
      eintragen (Tabelle „Download & Integrität“ des neuen
      Versionsabschnitts).
- [ ] Neue Zeile in `SHA256SUMS.txt` ergänzen (Format:
      `<SHA-256>  Visinovo-Lite-Setup-<version>.exe`).
- [ ] `README.md`: Installationslink/Release-Tag prüfen
      (Standard: `…/releases/tag/lite-v<version>`).

Prüfsumme selbständig nachrechnen (im SaaS-Repository):

```powershell
Get-FileHash .\dist\setup\Visinovo-Lite-Setup-<version>.exe -Algorithm SHA256
```

## 5. Smoke-Test lokal `[SaaS]`

```powershell
.\scripts\test-build.ps1 -SkipBuild
```

- [ ] Installation (User-Install, ohne Admin) ok.
- [ ] **Erststart**: DB initialisiert, Health-Check ok.
- [ ] **Analyse** läuft (Qualitätsscore).
- [ ] **Zweiter Start**: Daten erhalten.
- [ ] **3-Listing-Limit**: 4. Listing wird abgelehnt
      (im Akzeptanzlauf).
- [ ] **Deinstallation**: App entfernt, **Daten erhalten**.
- [ ] (optional) `-WithDeleteData`: Deinstallationspfad
      „Daten löschen“ ok.

## 6. Release-EXE zum öffentlichen Repository kopieren `[Lite]`

- [ ] **Manuell** die Setup-EXE aus dem SaaS-Repository
      (`dist\setup\Visinovo-Lite-Setup-<version>.exe`) als
      **Asset** zum GitHub-Repository `visinovo/visinovo-lite`
      hochladen – **entweder**:
  - direkt als Asset des neuen Releases (Schritt 7), **oder**
  - vorab als Asset eines Draft-Release.
- [ ] **Wichtig:** Die EXE gehört **nie** in den Repository-
      Quellbaum (nur als Release-Asset).

## 7. GitHub-Release erstellen `[Lite]`

- [ ] **Manuell** unter
      `https://github.com/visinovo/visinovo-lite/releases/new`:
  - **Tag:** `lite-v<version>` (z. B. `lite-v0.1.0`)
  - **Titel:** `Visinovo Lite <version>`
  - **Assets:** die Setup-EXE aus Schritt 6
  - **Release-Notes (Body)** – zwingend enthalten:
    - die vollständigen Changelog-Einträge
    - die **SHA-256** der Setup-EXE in einer eigenen Zeile im
      Format `SHA-256: <64-stelliger Hex-Wert>`
      (wird vom Smoke-Workflow geparst, s. Schritt 11)
    - Hinweis auf SmartScreen (unsigned) mit Verweis auf
      `docs/INSTALLATION.md`
  - „Publish release“ klicken.

## 8. Öffentliches Repository pushen `[Lite]`

- [ ] Alle Änderungen (CHANGELOG, SHA256SUMS, Doku, ggf.
      Screenshots) lokal committen.
- [ ] **Manuell** `git push origin main` ausführen.
- [ ] Auf GitHub prüfen: README rendert (Screenshots vorhanden?),
      License-Datei wird angezeigt, FUNDING-Buttons korrekt.

## 9. FUNDING-Links befüllen `[Lite]`

- [ ] `.github/FUNDING.yml`:
  - `github:` → echtes GitHub-Sponsors-Profil
  - `ko_fi:` → echtes Ko-fi-Profil
  - `liberapay:` → echtes Liberapay-Profil
  - nicht genutzte Kanäle die Zeile löschen.
- [ ] Die App-Links (`LITE_SPONSOR_LINKS` im SaaS-Repository,
      `visinovo/settings_lite.py`) auf dieselben Profile zeigen
      lassen: Env `LITE_SPONSORS_URL`, `LITE_KO_FI_URL`,
      `LITE_LIBERAPAY_URL` (leerer Wert blendet den Kanal im UI aus).
- [ ] `README.md` (Sektion „Lizenz & Support“) bei geänderten
      Kanälen/Profilen mit anpassen.
- [ ] Mit dem nächsten Build (Schritt 3) übernehmen.

## 10. EULA final prüfen `[Lite]`

- [ ] `LICENSE.md` auf Aktualität prüfen (Fassung/Stand-Datum).
- [ ] Bei Änderungen: neue Fassung im Release dokumentieren
      („Lizenz: EULA-Fassung x.y“).
- [ ] Prüfen, dass die EULA-Fassung, die dem Release zugeordnet
      ist, mit der installierten Version korrespondiert
      (siehe EULA Abschnitt 6.2).
- [ ] **Option:** EULA in den Inno-Setup-Installer aufnehmen
      (`packaging/visinovo-lite.iss` → `[Setup] LicenseFile=`),
      damit sie beim Installieren angezeigt wird.

## 11. Optional: Smoke-Test-Workflow auslösen `[Lite]`

- [ ] Auf GitHub → *Actions* → Workflow **Release Smoke-Test** →
      „Run workflow“ (prüft die **aktuelle** Release-EXE:
      Download → SHA-256 → Installation → Erststart → Analyse →
      Deinstallation → Daten erhalten).
- [ ] Workflow-Run grün? Falls rot: Release-Asset ggf. ersetzen
      (neue EXE hochladen, SHA-256 in Release/CHANGELOG/
      SHA256SUMS aktualisieren).

> Der Workflow triggert **nur** manuell oder bei neuen
> Releases – es läuft **kein** automatischer Build.

## 12. Nach dem Release

- [ ] GitHub-Issues mit der neuen Version markieren/schließen.
- [ ] Bei bekannten Einschränkungen (z. B. SmartScreen) die
      betroffenen Issues verlinken.
- [ ] `PROJECT_STATUS.md` im SaaS-Repository aktualisieren
      (Abschnitt „Windows Lite“: durchgeführtes Release,
      offene Punkte).

---

## Häufige Stolpersteine

| Problem | Ursache / Abhilfe |
|---|---|
| Setup-Dateiname passt nicht zur Version | `packaging/version.txt` nicht geändert → Schritt 1 |
| SHA-256 weicht ab (Smoke-Workflow rot) | EXE erneut gebaut, aber SHA-256/SHA256SUMS/Release nicht synchron aktualisiert → Schritt 4 |
| Smoke-Workflow findet keine EXE | Release-Asset nicht hochgeladen → Schritt 6 |
| SmartScreen-Warnung | unsigned → erwartet; Doku in `docs/INSTALLATION.md` |
| UI zeigt alte Version | `LITE_VERSION` nicht geändert → Schritt 1 |
