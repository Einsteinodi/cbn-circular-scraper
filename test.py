import os
import time
import json
import requests
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# =========================
# CONFIGURATION
# =========================
BASE_URL = "https://www.cbn.gov.ng/Documents/circulars.html"
PDF_DIR = "cbn_pdfs"
os.makedirs(PDF_DIR, exist_ok=True)
HEADLESS = True  # Set False to see Firefox open

# =========================
# SETUP FIREFOX
# =========================
options = Options()
options.headless = HEADLESS
driver = webdriver.Firefox(options=options)

# =========================
# LOAD PAGE
# =========================
driver.get(BASE_URL)
time.sleep(3)  # wait for JavaScript to load circulars

# =========================
# SCRAPE TABLE ROWS
# =========================
circulars = []

# The circulars are listed in a table; each <tr> has date and <a> link
rows = driver.find_elements(By.CSS_SELECTOR, "table tr")

for row in rows:
    try:
        # Extract date (usually first <td>)
        tds = row.find_elements(By.TAG_NAME, "td")
        if len(tds) < 2:
            continue  # skip header or invalid rows

        date = tds[0].text.strip()
        link_el = tds[1].find_element(By.TAG_NAME, "a")
        title = link_el.text.strip()
        href = link_el.get_attribute("href")
        if not href:
            continue

        pdf_url = urljoin(BASE_URL, href)
        filename = os.path.basename(href).replace(" ", "_")
        local_path = os.path.join(PDF_DIR, filename)

        # Download PDF if not already downloaded
        if not os.path.exists(local_path):
            pdf_resp = requests.get(pdf_url)
            pdf_resp.raise_for_status()
            with open(local_path, "wb") as f:
                f.write(pdf_resp.content)
            print(f"Downloaded: {filename}")

        circulars.append({
            "title": title,
            "date": date,
            "url": pdf_url,
            "local_file": os.path.join("cbn_pdfs", filename)
        })

    except Exception as e:
        print(f"Skipping row due to error: {e}")
        continue

driver.quit()

# =========================
# SAVE JSON
# =========================
with open("cbn_circulars.json", "w", encoding="utf-8") as f:
    json.dump(circulars, f, ensure_ascii=False, indent=4)

print(f"\nExtracted {len(circulars)} circulars with dates. JSON saved to cbn_circulars.json")
