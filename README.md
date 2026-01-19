# CBN Circular PDF Scraper

A Python script to scrape circulars from the [Central Bank of Nigeria (CBN)](https://www.cbn.gov.ng/Documents/circulars.html) website, download the PDF documents, and save metadata to a JSON file.

---

## Features

- Scrapes circulars dynamically using **Selenium**.
- Downloads PDFs to a local folder (`cbn_pdfs/`).
- Saves a JSON file (`cbn_circulars.json`) containing:
  - `title` – Title of the circular
  - `date` – Publication date
  - `url` – Direct URL to the PDF
  - `local_file` – Path to the downloaded PDF
- Option to run **headless** (Firefox runs in background).

---

## Requirements

- Python 3.9+
- [Selenium](https://pypi.org/project/selenium/)
- [Requests](https://pypi.org/project/requests/)
- Firefox Browser
- [Geckodriver](https://github.com/mozilla/geckodriver/releases)

Install Python dependencies via pip:

```bash
pip install selenium requests
