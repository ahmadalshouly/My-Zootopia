# My Zootopia

Eine Python-App, die Tierdaten von der [API Ninjas Animals API](https://api-ninjas.com/api/animals) abruft und eine gestaltete HTML-Seite mit den Ergebnissen erstellt.

## Funktionen

- Ruft live Tierdaten von API Ninjas ab
- Erstellt eine gestaltete HTML-Seite aus einer Vorlage
- Eingabevalidierung mit erneuter Abfrage bei ungültigen oder nicht gefundenen Tieren

## Erste Schritte

### Voraussetzungen

- Python 3.12+
- API-Schlüssel von [api-ninjas.com](https://api-ninjas.com/register)

### Installation

1. Repository klonen
```bash
   git clone https://github.com/ahmadalshouly/My-Zootopia.git
   cd My-Zootopia
```

2. Virtuelle Umgebung erstellen und aktivieren
```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Mac/Linux
```

3. Abhängigkeiten installieren
```bash
   pip install requests python-dotenv
```

4. `.env` Datei im Projektverzeichnis erstellen
API_KEY=dein_api_schlüssel_hier

## Verwendung

```bash
python main.py
```

Du wirst aufgefordert, einen Tiernamen einzugeben:
Tiername eingeben: fuchs
Animals Web Generator wurde erfolgreich erstellt

Die Ausgabe wird als `animals.html` im Projektverzeichnis gespeichert.

## Projektstruktur
My-Zootopia/
├── main.py                    # Hauptanwendung
├── animals_web_generator.py   # HTML-Generierung
├── data_fetcher.py            # API-Abruf
├── animals_template.html      # HTML-Vorlage
├── requirements.txt           # Abhängigkeiten
├── .env                       # API-Schlüssel (nicht versioniert)
├── .gitignore
└── README.md

## Umgebungsvariablen

| Variable  | Beschreibung         |
|-----------|----------------------|
| `API_KEY` | API Ninjas API-Schlüssel |

## Abhängigkeiten

| Paket           | Zweck                               |
|-----------------|-------------------------------------|
| `requests`      | HTTP-Anfragen an die API            |
| `python-dotenv` | API-Schlüssel aus `.env` laden      |