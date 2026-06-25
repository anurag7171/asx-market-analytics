# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Healthcare             | 16        | 89.95             | 1728.0   | -59.65    |
| Materials              | 47        | 56.79             | 332.13   | -19.34    |
| Industrials            | 24        | 33.49             | 267.82   | -29.98    |
| Energy                 | 11        | 14.76             | 50.99    | -32.71    |
| Financials             | 36        | 4.23              | 66.62    | -35.79    |
| Utilities              | 7         | 4.06              | 33.1     | -10.52    |
| Real Estate            | 17        | -1.52             | 22.33    | -39.13    |
| Consumer Discretionary | 15        | -2.72             | 29.29    | -36.28    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1728.0              |
| 2    | PLS  | PLS Group              | Materials              | 332.1               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 267.8               |
| 4    | MIN  | Mineral Resources      | Materials              | 217.8               |
| 5    | LTR  | Liontown Resources     | Materials              | 158.8               |
| 6    | NWH  | NRW Holdings           | Industrials            | 157.6               |
| 7    | CDA  | Codan                  | Information Technology | 124.0               |
| 8    | ILU  | Iluka Resources        | Materials              | 107.4               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 141.5                 |
| EOS  | 254          | 108.5                 |
| DRO  | 254          | 108.3                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.4                  |
| OBM  | 254          | 79.0                  |
| ZIP  | 254          | 76.3                  |
| DYL  | 254          | 71.1                  |

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
| Financials             | 21                  |
| Industrials            | 19                  |
| Real Estate            | 14                  |
| Healthcare             | 13                  |
| Materials              | 11                  |
| Consumer Discretionary | 11                  |
| Consumer Staples       | 7                   |
| Utilities              | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| WTC  | Wisetech Global | Information Technology | 120.11   | 31.39        | -73.9          |
| TUA  | Tuas            | Communication Services | 8.32     | 2.27         | -72.7          |
| XRO  | Xero            | Information Technology | 194.21   | 67.85        | -65.1          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.41         | -63.5          |
| COH  | Cochlear        | Healthcare             | 313.15   | 116.55       | -62.8          |
| 360  | Life360         | Information Technology | 55.44    | 23.9         | -56.9          |
| SEK  | Seek            | Communication Services | 28.65    | 12.63        | -55.9          |
| CSL  | CSL             | Healthcare             | 265.45   | 117.65       | -55.7          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| WTC  | Wisetech Global | -76.1            |
| TUA  | Tuas            | -76.0            |
| DRO  | Droneshield     | -74.0            |
| COH  | Cochlear        | -71.3            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -67.2            |
| XRO  | Xero            | -66.5            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.53                  |
| Information Technology | 45.49                  |
| Financials             | 44.17                  |
| Energy                 | 39.47                  |
| Healthcare             | 36.89                  |
| Consumer Staples       | 33.17                  |
| Consumer Discretionary | 27.31                  |
| Communication Services | 26.23                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 90.0           | 44.6               | 2.02                 |
| Materials              | 56.8           | 49.0               | 1.16                 |
| Industrials            | 33.5           | 36.0               | 0.93                 |
| Energy                 | 14.8           | 41.3               | 0.36                 |
| Utilities              | 4.1            | 27.3               | 0.15                 |
| Financials             | 4.2            | 29.8               | 0.14                 |
| Real Estate            | -1.5           | 21.2               | -0.07                |
| Consumer Discretionary | -2.7           | 32.8               | -0.08                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 162.7        |
| BHP  | BHP                    | Materials              | 260.3            | 58.52        |
| WBC  | Westpac                | Financials             | 136.3            | 35.06        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 34.86        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.47        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.99       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.45        |
| CSL  | CSL                    | Healthcare             | 67.4             | 117.65       |
