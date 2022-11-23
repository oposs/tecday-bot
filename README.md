# Tecdays Telegram Bot

Source code zum Workshop "M37 Ein GameBot für Telegram". In diesem Repostiory findest du folgendes:

- [QR Code Zähler](playground/qr_code_receiver.py): Zeigt einen QR code mit einem Zähler, welcher um eins erhöht wird,
  sobald eingescannt
- [Einfacher Telegram Bot](playground/simple_echo_bot.py): Einfacher Telegram bot welcher auf Nachrichten antworten kann
  und Katzenbilder versendet
- [Einfacher Server](playground/simple_server.py): Wird benötigt, wenn ein Telegram Game gebaut werden will
- [Popper Game](public/popper.html): Ein etwas komplexeres HTML Game
- [Server + Bot in einem](sanicbot/__init__.py): Vereint den Telegram Bot und den Server

## Anleitung

1. Python3 installieren:

- Windows: https://www.python.org/downloads/windows/
- MacOS: https://www.python.org/downloads/macos/
- Linux: `apt install python3`

2. Source code herunter laden:
    - Wenn du dich mit git auskennst: `git clone https://github.com/oposs/tecdays-bot.git`
    - Source code als zip herunterladen: Grüner Button "Code", dann "Download ZIP"
3. Projekt einrichten
    - Windows: Script [setup_project_win.cmd](setup_project_win.cmd) ausführen
    - Linux/MacOS: Script [setup_project_mac_linux.sh](setup_project_mac_linux.sh) ausführen
4. Telegram bot erstellen
    - Mit [@botfather](https://t.me/botfather) ein Gespräch anfangen
    - Der Befehl `/newbot` fragt dich nach einen Botnamen + Beschreibung
    - Das Token (welches in etwa so aussieht: `57xxxxxxxx:AAHRhXvlb0HqgLtZZZUUUHHNNEEDDCCEEFFSASAF`) aufschreiben
5. Token im file [simple_echo_bot.py](playground/simple_echo_bot.py) und [simple_server.py](playground/simple_server.py)
   eintragen
6. Bot starten
    - Windows: Script [start_echo_bot_win.cmd](playground/start_echo_bot_win.cmd) ausführen
    - Linux/MacOS: Script [start_echo_bot_linux_mac.sh](playground/start_echo_bot_linux_mac.sh) ausführen
    
## Game registrieren

- Mit @botfather eine Konversation starten
- `/setinline` - Inline mode aktivieren
- `/newgame` - Anweisungen folgen

## Game Server starten

Damit das Game funktioniert, brauchst brauchst du einen Computer der vom Internet aus direkt erreichbar ist. Da startest du dann den Game Server. Dieser medldet sich bei Telegram an und wartet auf bot requests. Gleichzeitig werden von dem Server auch die Gamefiles ausgeliefert und alfällige Score Updates an Telegram weitergeleitet.

Das Game selbst ist in JavaScript geschrieben und befindet sich im Ordner [public](public). Der Server ist in Python geschrieben und befindet sich im Ordner [sanicbot](sanicbot). Bevor du den Server startest, musst du im `config.ini` file den Token eintragen. Den Token bekommst du von @botfather (siehe oben).

```console
$ cp config.ini.dist config.ini
$ vim config.ini
$ . venv/bin/activate
$ sanic sanicbot:app -H 0.0.0.0 -p 8080 -d
```

## Etwas funktioniert nicht?

Du kannst uns entweder eine Mail an support[at]oetiker[dot]ch schreiben oder wenn Du ein Github account hast hier
ein [Issue](https://github.com/oposs/tecdays-bot/issues/new) aufmachen.

## Copyright notice

Code is published under [MIT](LICENSE.md)

Cat images are taken from wikipedia:

- [cat1](playground/public/cats/catO1.jpg): Alvesgaspar, 2010 GFDL 1.2
- [cat2](playground/public/cats/catO2.jpg): Hisashi, 2009 CC Attribution-Share Alike 2.0