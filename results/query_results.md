# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 55.28             | 146.05   | -29.83    |
| Energy                 | 11        | 23.41             | 69.64    | -27.69    |
| Healthcare             | 16        | 21.83             | 599.08   | -53.33    |
| Industrials            | 24        | 13.83             | 110.17   | -51.4     |
| Utilities              | 7         | 6.48              | 31.47    | -6.45     |
| Financials             | 36        | 1.89              | 98.77    | -38.21    |
| Consumer Staples       | 7         | -5.81             | 23.65    | -25.85    |
| Consumer Discretionary | 15        | -13.29            | 31.33    | -48.33    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name | one_year_return_pct |
| ---- | ---- | ---------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare  | 599.1               |
| 2    | PLS  | PLS Group              | Materials   | 146.0               |
| 3    | GGP  | Greatland Resources    | Materials   | 146.0               |
| 4    | RSG  | Resolute Mining        | Materials   | 123.8               |
| 5    | NWH  | NRW Holdings           | Industrials | 110.2               |
| 6    | VAU  | Vault Minerals         | Materials   | 109.7               |
| 7    | WGX  | Westgold Resources     | Materials   | 109.3               |
| 8    | EOS  | Electro Optic Systems  | Industrials | 108.1               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.3                 |
| DRO  | 254          | 104.4                 |
| EOS  | 254          | 101.1                 |
| LTR  | 254          | 79.6                  |
| ZIP  | 254          | 79.3                  |
| OBM  | 254          | 79.2                  |
| TUA  | 254          | 76.0                  |
| DYL  | 254          | 72.7                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Materials              | 36                  |
| Financials             | 19                  |
| Industrials            | 11                  |
| Energy                 | 9                   |
| Healthcare             | 8                   |
| Communication Services | 7                   |
| Consumer Staples       | 6                   |
| Consumer Discretionary | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.17         | -73.9          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.74         | -73.7          |
| WTC  | Wisetech Global    | Information Technology | 115.37   | 40.89        | -64.6          |
| 360  | Life360            | Information Technology | 55.44    | 20.48        | -63.1          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.2          | -54.5          |
| COH  | Cochlear           | Healthcare             | 296.77   | 137.71       | -53.6          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 8.02         | -52.6          |
| ASB  | Austal             | Industrials            | 8.76     | 4.21         | -51.9          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name       | max_drawdown_pct |
| ---- | ------------------ | ---------------- |
| TUA  | Tuas               | -76.0            |
| WTC  | Wisetech Global    | -75.1            |
| DRO  | Droneshield        | -74.3            |
| ZIP  | Zip                | -70.0            |
| COH  | Cochlear           | -69.7            |
| 360  | Life360            | -67.7            |
| PME  | Pro Medicus        | -66.2            |
| LTR  | Liontown Resources | -63.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.29                  |
| Information Technology | 45.88                  |
| Financials             | 43.93                  |
| Energy                 | 40.58                  |
| Healthcare             | 36.32                  |
| Consumer Staples       | 33.1                   |
| Consumer Discretionary | 27.43                  |
| Communication Services | 26.83                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 55.3           | 49.1               | 1.13                 |
| Energy                 | 23.4           | 41.9               | 0.56                 |
| Healthcare             | 21.8           | 44.4               | 0.49                 |
| Industrials            | 13.8           | 36.4               | 0.38                 |
| Utilities              | 6.5            | 27.7               | 0.23                 |
| Financials             | 1.9            | 30.4               | 0.06                 |
| Consumer Staples       | -5.8           | 28.9               | -0.2                 |
| Information Technology | -17.1          | 48.7               | -0.35                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 155.46       |
| BHP  | BHP                    | Materials              | 260.3            | 67.4         |
| WBC  | Westpac                | Financials             | 136.3            | 33.83        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.95        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 83.27        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 252.77       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.26        |
| CSL  | CSL                    | Healthcare             | 67.4             | 172.44       |
