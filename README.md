# ASX 200 Market Analytics

End-to-end data analytics pipeline on the Australian share market: **scrape** the
S&P/ASX 200, model it in **SQL**, analyse returns and risk with advanced queries,
and surface the results in **Power BI** and a formatted **Excel** report — refreshed
automatically by a **CI/CD** pipeline.

## What's inside
- **Scraped data** — 200 ASX 200 constituents (Wikipedia) and ~50,000 daily prices
  across 11 GICS sectors (Yahoo Finance), using split/dividend-adjusted closes.
- **Normalised SQL database** — a 3-table relational schema with foreign keys
  (`sectors → companies → daily_prices`).
- **Advanced SQL analysis** — 10 queries using multi-table JOINs, CTEs, and window
  functions (RANK, LAG, FIRST_VALUE, moving averages, running drawdown).
- **Power BI dashboard** — sector performance, top movers, price trends, risk vs
  return (build guide in [`docs/POWERBI_GUIDE.md`](docs/POWERBI_GUIDE.md)).
- **Excel report** — formatted multi-sheet workbook (`reports/asx-market-report.xlsx`).
- **CI/CD** — GitHub Actions re-scrapes and rebuilds everything on a weekday schedule.

## Tech stack
| Layer | Tools |
|---|---|
| Scraping | `requests`, `BeautifulSoup`, Yahoo Finance API |
| Storage | `SQLite` (normalised schema, foreign keys, indexes) |
| Analysis | advanced **SQL** (window functions, CTEs, JOINs) |
| Visualisation | **Power BI** + DAX, Excel (`openpyxl`) |
| Automation | **GitHub Actions** (scheduled CI/CD) |

## Data model
```
sectors (sector_id PK, sector_name)
   │ 1
   │ *
companies (code PK, company_name, sector_id FK, market_cap, headquarters)
   │ 1
   │ *
daily_prices (price_id PK, code FK, trade_date, open, high, low, close, adj_close, volume)
```

## Business case study
**Question.** Which ASX sectors and stocks delivered the best returns over the past
year, where is the risk concentrated, and which names carry momentum right now?

**Approach.** Scraped the index and a year of adjusted daily prices, modelled them in
a normalised SQL database, then computed returns, annualised volatility, maximum
drawdown, moving-average momentum, and sector liquidity using window functions.

**Findings (illustrative — refreshes with the data).**
- **Healthcare** and **Materials** led sector returns, powered by standout names
  (4DMedical, lithium/mining producers).
- **Risk clusters in small-cap growth** — the highest-volatility and deepest-drawdown
  names are concentrated in speculative Healthcare and Tech stocks.
- **Financials** dominate **liquidity** (daily traded value) despite mid-pack returns.

**Recommendation.** A risk-aware investor should favour sectors with the best
**return-per-unit-of-risk** rather than headline returns, and use the 50-day moving
-average momentum signal to time entries.

See [`results/query_results.md`](results/query_results.md) for the full query outputs.

## Run it locally
```bash
pip install -r requirements.txt
python3 scripts/refresh.py          # scrape -> build DB -> run SQL -> export Excel
sqlite3 asx.db < sql/queries.sql    # or explore the queries directly
```

## Pipeline scripts
| Script | Purpose |
|---|---|
| `src/scrape_companies.py` | ASX 200 constituents → `data/companies.csv` |
| `src/scrape_prices.py` | daily adjusted prices → `data/prices.csv` |
| `src/build_db.py` | normalised SQLite database |
| `src/run_queries.py` | runs `sql/queries.sql`, writes results |
| `src/export_excel.py` | formatted Excel report |
| `scripts/refresh.py` | full pipeline (used by CI) |

> Data note: prices are sourced live from Yahoo Finance for educational/portfolio use.
