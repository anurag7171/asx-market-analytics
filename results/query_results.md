# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 77.91             | 1548.98  | -60.33    |
| Materials        | 47        | 50.62             | 277.12   | -23.48    |
| Industrials      | 24        | 30.55             | 238.06   | -31.61    |
| Energy           | 11        | 12.4              | 47.78    | -31.5     |
| Financials       | 36        | 5.13              | 71.51    | -32.37    |
| Utilities        | 7         | 2.97              | 30.0     | -9.86     |
| Consumer Staples | 7         | -3.68             | 29.41    | -39.45    |
| Real Estate      | 17        | -3.78             | 19.03    | -39.17    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1549.0              |
| 2    | PLS  | PLS Group              | Materials              | 277.1               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 238.1               |
| 4    | MIN  | Mineral Resources      | Materials              | 190.7               |
| 5    | NWH  | NRW Holdings           | Industrials            | 159.2               |
| 6    | LTR  | Liontown Resources     | Materials              | 148.2               |
| 7    | CDA  | Codan                  | Information Technology | 124.6               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 115.6               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.6                 |
| EOS  | 254          | 108.7                 |
| DRO  | 254          | 107.1                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.5                  |
| OBM  | 254          | 79.2                  |
| ZIP  | 254          | 76.7                  |
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
| Industrials            | 21                  |
| Real Estate            | 14                  |
| Healthcare             | 13                  |
| Materials              | 11                  |
| Consumer Discretionary | 11                  |
| Consumer Staples       | 6                   |
| Information Technology | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| WTC  | Wisetech Global | Information Technology | 120.11   | 32.88        | -72.6          |
| TUA  | Tuas            | Communication Services | 8.32     | 2.29         | -72.5          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.39         | -63.8          |
| COH  | Cochlear        | Healthcare             | 313.15   | 118.45       | -62.2          |
| XRO  | Xero            | Information Technology | 182.03   | 70.2         | -61.4          |
| CSL  | CSL             | Healthcare             | 265.45   | 118.37       | -55.4          |
| SEK  | Seek            | Communication Services | 28.65    | 13.23        | -53.8          |
| EBO  | EBOS Group      | Healthcare             | 36.51    | 17.18        | -53.0          |

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
| Financials             | 44.2                   |
| Energy                 | 39.48                  |
| Healthcare             | 36.98                  |
| Consumer Staples       | 33.12                  |
| Consumer Discretionary | 27.48                  |
| Communication Services | 26.31                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 77.9           | 44.6               | 1.75                 |
| Materials              | 50.6           | 49.1               | 1.03                 |
| Industrials            | 30.6           | 35.8               | 0.85                 |
| Energy                 | 12.4           | 41.3               | 0.3                  |
| Financials             | 5.1            | 30.0               | 0.17                 |
| Utilities              | 3.0            | 27.4               | 0.11                 |
| Consumer Staples       | -3.7           | 28.2               | -0.13                |
| Information Technology | -7.4           | 46.3               | -0.16                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 160.73       |
| BHP  | BHP                    | Materials              | 260.3            | 59.92        |
| WBC  | Westpac                | Financials             | 136.3            | 34.7         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 34.47        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.5         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 247.18       |
| NAB  | National Australia Ban | Financials             | 69.8             | 36.99        |
| CSL  | CSL                    | Healthcare             | 67.4             | 118.37       |
