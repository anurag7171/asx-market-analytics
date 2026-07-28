# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 55.72             | 1254.17  | -61.43    |
| Materials        | 47        | 37.93             | 137.65   | -25.87    |
| Industrials      | 24        | 19.31             | 129.14   | -39.83    |
| Energy           | 11        | 12.01             | 47.32    | -29.09    |
| Financials       | 36        | 4.56              | 57.12    | -41.2     |
| Utilities        | 7         | 2.36              | 30.85    | -8.63     |
| Consumer Staples | 7         | 0.94              | 32.48    | -37.08    |
| Real Estate      | 17        | -2.93             | 19.41    | -52.41    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1254.2              |
| 2    | PLS  | PLS Group              | Materials              | 137.6               |
| 3    | NWH  | NRW Holdings           | Industrials            | 129.1               |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 122.3               |
| 5    | VAU  | Vault Minerals         | Materials              | 106.5               |
| 6    | CDA  | Codan                  | Information Technology | 92.7                |
| 7    | WGX  | Westgold Resources     | Materials              | 83.0                |
| 8    | ALK  | Alkane Resources       | Materials              | 81.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.5                 |
| EOS  | 254          | 108.7                 |
| DRO  | 254          | 104.7                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 80.3                  |
| OBM  | 254          | 78.9                  |
| ZIP  | 254          | 77.4                  |
| CYL  | 254          | 72.5                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| EOS  | Electro Optic Systems  | 2025-08-05 | 43.4           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 29                  |
| Industrials            | 15                  |
| Real Estate            | 14                  |
| Consumer Discretionary | 13                  |
| Healthcare             | 11                  |
| Materials              | 10                  |
| Consumer Staples       | 7                   |
| Communication Services | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.21         | -73.4          |
| DRO  | Droneshield     | Industrials            | 6.6      | 1.8          | -72.7          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 34.71        | -71.1          |
| XRO  | Xero            | Information Technology | 180.99   | 67.69        | -62.6          |
| COH  | Cochlear        | Healthcare             | 313.15   | 119.88       | -61.7          |
| ASB  | Austal          | Industrials            | 8.76     | 3.66         | -58.2          |
| PXA  | Pexa Group      | Real Estate            | 16.92    | 7.41         | -56.2          |
| CSL  | CSL             | Healthcare             | 265.45   | 119.52       | -55.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| WTC  | Wisetech Global | -76.1            |
| TUA  | Tuas            | -76.0            |
| DRO  | Droneshield     | -74.0            |
| COH  | Cochlear        | -71.3            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.5            |
| XRO  | Xero            | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.52                  |
| Information Technology | 45.21                  |
| Financials             | 43.93                  |
| Energy                 | 40.12                  |
| Healthcare             | 36.65                  |
| Consumer Staples       | 33.05                  |
| Consumer Discretionary | 27.75                  |
| Communication Services | 26.65                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 55.7           | 44.1               | 1.26                 |
| Materials        | 37.9           | 49.4               | 0.77                 |
| Industrials      | 19.3           | 36.1               | 0.54                 |
| Energy           | 12.0           | 41.7               | 0.29                 |
| Financials       | 4.6            | 30.2               | 0.15                 |
| Utilities        | 2.4            | 27.8               | 0.09                 |
| Consumer Staples | 0.9            | 28.3               | 0.03                 |
| Real Estate      | -2.9           | 21.6               | -0.14                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 178.78       |
| BHP  | BHP                    | Materials              | 260.3            | 59.37        |
| WBC  | Westpac                | Financials             | 136.3            | 38.02        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.22        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.22        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 256.47       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.21        |
| CSL  | CSL                    | Healthcare             | 67.4             | 119.52       |
