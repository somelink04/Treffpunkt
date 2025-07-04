# Treffpunkt

Eine Anwendung, um neue Personen durch gemeinsame Interessen im realen Leben kennenzulernen.

## Starten der Komponenten

* Benötigt npm, python und docker
* skripte sind für Debian ausgelegt

1. Backend Server einrichten und starten:

```bash
chmod 744 backend.sh # muss eventuell nicht durchgeführt werden
./backend.sh setup run
```

2. Installation aller Node-Packages und Starten des NPM-Development Servers:

```bash
cd front
npm install
npm start
```