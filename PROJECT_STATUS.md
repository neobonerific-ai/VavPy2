# Project Status

Phase: 1 Setup / Arbeitspaket A (Python 2.7 Port) — in progress
Branch: kodi18-py2
Commit: 617e40a (CI pending)
Last Run: 42052501214 (failure on 3a5b96d; fixed by 617e40a)
Processed Run-IDs: 42041332854, 42042148762, 42043142676, 42044693828, 42045069053, 42048108905, 42049255467, 42050349077, 42050370005, 42052501214
Last Run: 42045069053 (success, artifact vavoo-py2/vavoo.zip, 30 files, compileall only)
Open tasks: Source inventory, full Python2 port, HTTP transport, Kodi18 playback, real CI tests, hardware test.

## Entwicklungspakete
- A Vollständiger Python-2.7-Port (offen)
- B HTTPX/Netzwerktransport (offen)
- C Kodi-18-Integration (offen)
- D Funktionstests/CI (offen)
- E Hardwaretest (offen / dokumentieren)

## Nächste konkrete Aufgabe
Inventar der Python3-spezifischen APIs in plugin.video.vavooto/ erstellen (urllib.parse, concurrent.futures, xbmcvfs.translatePath, os.replace, html-Modul, casefold, HTTPX, ListItemInfoTag, inputstream.ffmpegdirect usw.) und systematisch portieren.

## Letzter geprüfter Commit
133d0ab (HEAD)

## Tatsächlich bestandene Tests
- compileall (Python 2.7 container) — nur Syntax, keine Import-/Funktionstests.

## Bekannte Einschränkungen
- CI prüft nur compileall; keine realen Import-/Funktionstests.
- HTTPX teilweise entfernt, get_httpx() Aufrufe prüfen.
- Kein Hardwarezugriff bisher dokumentiert.

## Verarbeitete Run-IDs
42041332854, 42042148762, 42043142676, 42044693828, 42045069053, 42048108905