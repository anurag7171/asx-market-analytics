# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 78.61             | 1557.14  | -59.3     |
| Materials        | 47        | 50.3              | 274.45   | -23.68    |
| Industrials      | 24        | 29.95             | 257.5    | -33.17    |
| Energy           | 11        | 11.91             | 45.91    | -33.72    |
| Financials       | 36        | 4.8               | 73.93    | -34.68    |
| Utilities        | 7         | 0.1               | 25.44    | -11.48    |
| Consumer Staples | 7         | -4.46             | 28.43    | -42.06    |
| Real Estate      | 17        | -5.29             | 20.38    | -40.45    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1557.1              |
| 2    | PLS  | PLS Group              | Materials              | 274.5               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 257.5               |
| 4    | MIN  | Mineral Resources      | Materials              | 181.1               |
| 5    | NWH  | NRW Holdings           | Industrials            | 152.3               |
| 6    | LTR  | Liontown Resources     | Materials              | 138.6               |
| 7    | CDA  | Codan                  | Information Technology | 123.4               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 113.8               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.5                 |
| EOS  | 254          | 108.7                 |
| DRO  | 254          | 107.0                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.6                  |
| OBM  | 254          | 79.4                  |
| ZIP  | 254          | 76.5                  |
| DYL  | 254          | 70.7                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| EOS  | Electro Optic Systems  | 2025-08-05 | 43.4           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |
| MSB  | Mesoblast              | 2025-07-18 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 24                  |
| Industrials            | 18                  |
| Real Estate            | 14                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 9                   |
| Materials              | 8                   |
| Consumer Staples       | 6                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| WTC  | Wisetech Global | Information Technology | 120.11   | 32.36        | -73.1          |
| TUA  | Tuas            | Communication Services | 8.32     | 2.26         | -72.8          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.39         | -63.8          |
| COH  | Cochlear        | Healthcare             | 313.15   | 120.35       | -61.6          |
| XRO  | Xero            | Information Technology | 181.0    | 71.23        | -60.6          |
| CSL  | CSL             | Healthcare             | 265.45   | 117.75       | -55.6          |
| SEK  | Seek            | Communication Services | 28.65    | 13.05        | -54.5          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 18.37        | -53.8          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name          | max_drawdown_pct |
| ---- | --------------------- | ---------------- |
| WTC  | Wisetech Global       | -76.1            |
| TUA  | Tuas                  | -76.0            |
| DRO  | Droneshield           | -74.0            |
| COH  | Cochlear              | -71.3            |
| ZIP  | Zip                   | -70.0            |
| 360  | Life360               | -67.7            |
| PME  | Pro Medicus           | -67.2            |
| TLX  | Telix Pharmaceuticals | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.51                  |
| Information Technology | 45.33                  |
| Financials             | 44.19                  |
| Energy                 | 39.48                  |
| Healthcare             | 36.98                  |
| Consumer Staples       | 33.18                  |
| Consumer Discretionary | 27.52                  |
| Communication Services | 26.31                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 78.6           | 44.5               | 1.76                 |
| Materials              | 50.3           | 49.1               | 1.03                 |
| Industrials            | 29.9           | 35.9               | 0.83                 |
| Energy                 | 11.9           | 41.3               | 0.29                 |
| Financials             | 4.8            | 29.9               | 0.16                 |
| Utilities              | 0.1            | 27.5               | 0.0                  |
| Consumer Staples       | -4.5           | 28.2               | -0.16                |
| Information Technology | -7.7           | 46.4               | -0.17                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 161.14       |
| BHP  | BHP                    | Materials              | 260.3            | 59.57        |
| WBC  | Westpac                | Financials             | 136.3            | 35.46        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 34.79        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 86.85        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.26       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.41        |
| CSL  | CSL                    | Healthcare             | 67.4             | 117.75       |
