# SEO Audit AI 🔍

**SEO Audit AI** è un'applicazione web basata su Flask che utilizza le API di OpenAI (GPT-4) per effettuare un'analisi SEO intelligente di qualsiasi sito web. Il progetto include anche funzionalità opzionali per il confronto competitivo utilizzando [SerpAPI](https://serpapi.com/).

---

## 🚀 Funzionalità principali

- Analisi automatica dei meta tag
- Valutazione della struttura degli heading (H1-H3)
- Analisi qualitativa dei contenuti testuali
- Analisi dei link interni/esterni presenti nella homepage
- Suggerimenti SEO personalizzati e contestuali
- Confronto con i principali competitor in SERP (opzionale)
- Generazione di un **report SEO in PDF** e HTML

---

## 🧠 Tecnologie utilizzate

- Python 3.10
- Flask
- OpenAI SDK >= 1.0.0
- SerpAPI (opzionale)
- pdfkit + wkhtmltopdf
- Docker

---

## 📂 Struttura dei file

```bash
.
├── app/
│   ├── analyzer.py          # Logica principale dell'analisi SEO
│   ├── routes.py            # Route Flask
│   ├── templates/
│   │   ├── form.html        # Form di input per analisi
│   │   └── report.html      # Visualizzazione del report
├── core/
│   ├── scraper.py           # Estrazione dati HTML dal sito
│   ├── prompts.py           # Prompt persona ottimizzati per OpenAI
│   ├── report_builder.py    # Generazione HTML per PDF
│   ├── serp_scraper.py      # (Opzionale) Scraping dei competitor da Google via SerpAPI
│   ├── comparator.py        # Confronto con i competitor (via GPT)
├── run.py                   # Entry point dell’app Flask
├── Dockerfile               # Per deploy containerizzato
├── requirements.txt         # Dipendenze Python
├── README.md                # Questo file
```

---

## 🛠 Requisiti

- Python 3.10+
- Chiave API OpenAI
- (Opzionale) Chiave API SerpAPI per confronto competitor
- `wkhtmltopdf` installato (automatico con Docker)

---

## ▶️ Come eseguire l'app (locale)

```bash
pip install -r requirements.txt
python run.py
```

Accedi all'interfaccia su [http://localhost:8080](http://localhost:8080)

---

## 🐳 Docker (consigliato)

### Build

```bash
docker build -t seo-audit-ai .
```

### Run

```bash
docker run -p 8080:8080 seo-audit-ai
```

---

## 🔑 API Key richieste

- **OpenAI API Key** – Obbligatoria
- **SerpAPI Key** – Facoltativa (inseribile via interfaccia web)

---

## 📤 Output

- Report dettagliato SEO in HTML
- File PDF scaricabile generato da HTML
- Suggerimenti SEO concreti e specifici per il sito

---

## 📌 Licenza

MIT © 2025 - Creato per uso analitico e didattico.
