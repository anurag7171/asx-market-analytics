"""
End-to-end pipeline: scrape -> build DB -> run queries -> export Excel.
Run on a schedule by .github/workflows/refresh.yml (and locally).

Usage (from repo root):  python3 scripts/refresh.py
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from src import scrape_companies, scrape_prices, build_db, run_queries, export_excel


def main():
    print("1/5  Scraping ASX 200 constituents …")
    scrape_companies.main()
    print("2/5  Scraping daily prices …")
    scrape_prices.main()
    print("3/5  Building relational database …")
    build_db.main()
    print("4/5  Running SQL analysis …")
    run_queries.main()
    print("5/5  Exporting Excel report …")
    export_excel.main()
    print("Done — data refreshed.")


if __name__ == "__main__":
    main()
