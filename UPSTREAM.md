# Upstream-Referenz

- Upstream-Repository: michaz1988/michaz1988.github.io
- Referenzbranch: addons
- Zweck: Beobachtung neuer Versionen und technischer Änderungen.

## Regeln

- Keine automatische Codeübernahme.
- Kein Merge und kein Cherry-Pick.
- Neue Funktionen müssen eigenständig für Python 2.7 und Kodi 18.9 nachgebildet werden.

## Analyseprozess

1. Neue Upstream-Commits, Tags und Releases erkennen.
2. Geänderte Dateien und Funktionen identifizieren.
3. Änderungen funktional erklären.
4. Python-3-spezifische Implementierungen von der eigentlichen Funktionalität unterscheiden.
5. Eine native Python-2.7-Umsetzung vorschlagen.
6. Betroffene VAVOO-Dateien und erforderliche Tests nennen.
7. Keine Änderungen am Port ohne separaten Entwicklungsauftrag.

Der Monitor muss direkt den echten Upstream abfragen, nicht einen lokalen, veralteten Klon der addons-Branch.
