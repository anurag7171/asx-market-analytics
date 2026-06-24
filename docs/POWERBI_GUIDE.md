# Power BI build guide — ASX 200 dashboard

This builds an interactive Power BI report from the scraped data. It mirrors the
analysis in the SQL layer so the project shows the same insights in Power BI.

> Power BI Desktop is Windows-only. On a Mac, run it in a Windows 11 VM
> (VMware Fusion is free for personal use) or use the browser Power BI Service.

## 1. Load the data
1. **Get Data → Text/CSV** → `data/companies.csv` → Load.
2. **Get Data → Text/CSV** → `data/prices.csv` → Load.
3. In **Power Query**, set types: `prices[date]` → Date; `adj_close`, `close`,
   `open`, `high`, `low` → Decimal; `volume` → Whole Number. Close & Apply.

## 2. Build the data model
1. Open the **Model** view.
2. Drag `prices[code]` onto `companies[code]` to create a **1-to-many**
   relationship (companies = dimension, prices = fact).
3. Add a date table: **Modeling → New Table**
   ```DAX
   DateTable = CALENDAR ( MIN ( prices[date] ), MAX ( prices[date] ) )
   ```
   Relate `DateTable[Date]` → `prices[date]`. Mark it as a date table.

## 3. DAX measures (Modeling → New Measure)
```DAX
Latest Adj Close =
VAR d = MAX ( prices[date] )
RETURN CALCULATE ( AVERAGE ( prices[adj_close] ), prices[date] = d )

First Adj Close =
VAR d = MIN ( prices[date] )
RETURN CALCULATE ( AVERAGE ( prices[adj_close] ), prices[date] = d )

1Y Return % =
DIVIDE ( [Latest Adj Close] - [First Adj Close], [First Adj Close] )

Avg Daily Turnover (A$m) =
AVERAGEX ( prices, prices[close] * prices[volume] ) / 1000000

Companies Tracked = DISTINCTCOUNT ( companies[code] )
```
Format `1Y Return %` as Percentage.

## 4. Visuals (one page)
1. **KPI cards**: `Companies Tracked`, `1Y Return %` (whole index).
2. **Bar chart** — Sector performance: Axis `companies[sector]`, Value `1Y Return %`, sort descending.
3. **Table** — Top performers: `companies[code]`, `companies[company_name]`,
   `companies[sector]`, `1Y Return %`; sort desc, Top-N filter = 15.
4. **Line chart** — Price trend: Axis `DateTable[Date]`, Value
   `Average of adj_close`, Legend `companies[sector]` (or a company slicer).
5. **Slicer** — `companies[sector]` to filter the whole page.
6. **Scatter** — Risk vs return: X `1Y Return %`, Y a volatility measure (optional), details `companies[code]`.

## 5. Polish & publish
- Title the page "ASX 200 Market Analytics", apply a clean theme.
- **File → Publish** to the Power BI Service for a shareable link, or export to PDF
  / screenshot for the portfolio README.
