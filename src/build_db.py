"""
Build a normalised SQLite database from the scraped ASX 200 CSVs.

Schema (3NF, foreign keys enforced):
    sectors ──< companies ──< daily_prices

Run:  python3 src/build_db.py   ->  asx.db
"""

import csv
import os
import sqlite3

HERE = os.path.dirname(__file__)
DB = os.path.join(HERE, "..", "asx.db")
COMPANIES = os.path.join(HERE, "..", "data", "companies.csv")
PRICES = os.path.join(HERE, "..", "data", "prices.csv")


def main():
    if os.path.exists(DB):
        os.remove(DB)
    con = sqlite3.connect(DB)
    con.execute("PRAGMA foreign_keys = ON;")
    cur = con.cursor()

    cur.executescript("""
    CREATE TABLE sectors (
        sector_id   INTEGER PRIMARY KEY,
        sector_name TEXT NOT NULL UNIQUE
    );
    CREATE TABLE companies (
        code         TEXT PRIMARY KEY,
        company_name TEXT NOT NULL,
        sector_id    INTEGER NOT NULL REFERENCES sectors(sector_id),
        market_cap   INTEGER,
        headquarters TEXT
    );
    CREATE TABLE daily_prices (
        price_id  INTEGER PRIMARY KEY AUTOINCREMENT,
        code      TEXT NOT NULL REFERENCES companies(code),
        trade_date TEXT NOT NULL,
        open      REAL, high REAL, low REAL,
        close     REAL NOT NULL,
        adj_close REAL NOT NULL,   -- split/dividend-adjusted; used for returns
        volume    INTEGER,
        UNIQUE (code, trade_date)
    );
    """)

    with open(COMPANIES, encoding="utf-8") as f:
        companies = list(csv.DictReader(f))

    sectors = {}
    for r in companies:
        s = r["sector"].strip()
        if s not in sectors:
            cur.execute("INSERT INTO sectors(sector_name) VALUES (?)", (s,))
            sectors[s] = cur.lastrowid

    for r in companies:
        cur.execute("""
            INSERT INTO companies(code, company_name, sector_id, market_cap, headquarters)
            VALUES (?,?,?,?,?)
        """, (r["code"], r["company"], sectors[r["sector"].strip()],
              int(r["market_cap"]) if r["market_cap"] else None, r["headquarters"]))

    valid = {r["code"] for r in companies}
    with open(PRICES, encoding="utf-8") as f:
        rows = [
            (p["code"], p["date"],
             float(p["open"]) if p["open"] else None,
             float(p["high"]) if p["high"] else None,
             float(p["low"]) if p["low"] else None,
             float(p["close"]),
             float(p["adj_close"]) if p.get("adj_close") else float(p["close"]),
             int(p["volume"]) if p["volume"] else None)
            for p in csv.DictReader(f) if p["code"] in valid and p["close"]
        ]
    cur.executemany("""
        INSERT OR IGNORE INTO daily_prices(code, trade_date, open, high, low, close, adj_close, volume)
        VALUES (?,?,?,?,?,?,?,?)
    """, rows)

    cur.executescript("""
        CREATE INDEX idx_prices_code ON daily_prices(code);
        CREATE INDEX idx_prices_date ON daily_prices(trade_date);
        CREATE INDEX idx_companies_sector ON companies(sector_id);
    """)
    con.commit()
    for t in ("sectors", "companies", "daily_prices"):
        n = cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  {t:<13} {n:>7,} rows")
    con.close()
    print(f"Built {DB}")


if __name__ == "__main__":
    main()
