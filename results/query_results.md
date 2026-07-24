# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 44.95             | 1096.15  | -63.74    |
| Materials        | 47        | 31.64             | 118.47   | -27.41    |
| Industrials      | 24        | 17.43             | 128.04   | -39.47    |
| Energy           | 11        | 12.4              | 46.5     | -30.0     |
| Financials       | 36        | 4.01              | 57.12    | -41.43    |
| Utilities        | 7         | 1.14              | 31.0     | -10.25    |
| Consumer Staples | 7         | -1.27             | 30.83    | -39.93    |
| Real Estate      | 17        | -5.15             | 15.81    | -52.35    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1096.2              |
| 2    | NWH  | NRW Holdings           | Industrials            | 128.0               |
| 3    | PLS  | PLS Group              | Materials              | 118.5               |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 106.9               |
| 5    | CDA  | Codan                  | Information Technology | 94.8                |
| 6    | ALK  | Alkane Resources       | Materials              | 90.0                |
| 7    | VAU  | Vault Minerals         | Materials              | 86.8                |
| 8    | WGX  | Westgold Resources     | Materials              | 70.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.6                 |
| EOS  | 254          | 108.2                 |
| DRO  | 254          | 104.3                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 80.7                  |
| OBM  | 254          | 78.7                  |
| ZIP  | 254          | 77.2                  |
| CYL  | 254          | 72.3                  |

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
| Industrials            | 13                  |
| Real Estate            | 12                  |
| Materials              | 10                  |
| Healthcare             | 10                  |
| Consumer Staples       | 7                   |
| Consumer Discretionary | 7                   |
| Energy                 | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| WTC  | Wisetech Global | Information Technology | 120.11   | 30.02        | -75.0          |
| TUA  | Tuas            | Communication Services | 8.32     | 2.11         | -74.6          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.04         | -69.1          |
| XRO  | Xero            | Information Technology | 180.99   | 61.58        | -66.0          |
| COH  | Cochlear        | Healthcare             | 313.15   | 111.61       | -64.4          |
| 360  | Life360         | Information Technology | 55.44    | 23.07        | -58.4          |
| PXA  | Pexa Group      | Real Estate            | 16.92    | 7.19         | -57.5          |
| CSL  | CSL             | Healthcare             | 265.45   | 114.22       | -57.0          |

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
| Materials              | 48.6                   |
| Information Technology | 45.18                  |
| Financials             | 43.96                  |
| Energy                 | 40.1                   |
| Healthcare             | 36.79                  |
| Consumer Staples       | 33.11                  |
| Consumer Discretionary | 27.71                  |
| Communication Services | 26.56                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 45.0           | 44.1               | 1.02                 |
| Materials        | 31.6           | 49.3               | 0.64                 |
| Industrials      | 17.4           | 36.0               | 0.48                 |
| Energy           | 12.4           | 41.5               | 0.3                  |
| Financials       | 4.0            | 30.2               | 0.13                 |
| Utilities        | 1.1            | 27.7               | 0.04                 |
| Consumer Staples | -1.3           | 28.2               | -0.04                |
| Real Estate      | -5.2           | 21.3               | -0.24                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 174.03       |
| BHP  | BHP                    | Materials              | 260.3            | 58.85        |
| WBC  | Westpac                | Financials             | 136.3            | 37.14        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.47        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 87.25        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 255.04       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.39        |
| CSL  | CSL                    | Healthcare             | 67.4             | 114.22       |
