"""
Scrape the current S&P/ASX 200 constituents from Wikipedia.

Output: data/companies.csv  (code, company, sector, market_cap, headquarters)
"""

import csv
import os
import re

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/S%26P/ASX_200"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "companies.csv")


def scrape() -> list[dict]:
    resp = requests.get(URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Find the constituents table (has a "Code" header).
    target = None
    for table in soup.find_all("table", class_="wikitable"):
        heads = [th.get_text(strip=True).lower() for th in table.find_all("th")]
        if "code" in heads and "company" in heads and "sector" in heads:
            target = table
            break
    if target is None:
        raise RuntimeError("Constituents table not found on Wikipedia page")

    rows = []
    for tr in target.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
        if len(cells) < 4:
            continue
        code, company, sector, mcap = cells[0], cells[1], cells[2], cells[3]
        hq = cells[4] if len(cells) > 4 else ""
        market_cap = re.sub(r"[^\d]", "", mcap) or None
        rows.append({
            "code": code.strip().upper(),
            "company": company.strip(),
            "sector": sector.strip(),
            "market_cap": market_cap,
            "headquarters": hq.strip(),
        })
    return rows


def main():
    rows = scrape()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code", "company", "sector", "market_cap", "headquarters"])
        w.writeheader()
        w.writerows(rows)
    print(f"Scraped {len(rows)} ASX 200 companies -> {OUT}")
    sectors = sorted({r['sector'] for r in rows})
    print(f"Sectors ({len(sectors)}): {', '.join(sectors)}")


if __name__ == "__main__":
    main()
