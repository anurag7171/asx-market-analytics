# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 78.52             | 1564.0   | -59.49    |
| Materials        | 47        | 55.41             | 283.27   | -20.86    |
| Industrials      | 24        | 32.34             | 256.23   | -32.18    |
| Energy           | 11        | 13.43             | 51.67    | -31.5     |
| Utilities        | 7         | 3.73              | 35.64    | -10.36    |
| Financials       | 36        | 3.5               | 65.92    | -38.09    |
| Real Estate      | 17        | -0.66             | 23.64    | -38.65    |
| Consumer Staples | 7         | -2.83             | 31.59    | -37.72    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1564.0              |
| 2    | PLS  | PLS Group              | Materials              | 283.3               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 256.2               |
| 4    | MIN  | Mineral Resources      | Materials              | 202.1               |
| 5    | NWH  | NRW Holdings           | Industrials            | 155.8               |
| 6    | LTR  | Liontown Resources     | Materials              | 137.1               |
| 7    | CDA  | Codan                  | Information Technology | 120.7               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 101.5               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 141.8                 |
| EOS  | 254          | 108.5                 |
| DRO  | 254          | 107.8                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.6                  |
| OBM  | 254          | 78.9                  |
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
| Industrials            | 20                  |
| Financials             | 20                  |
| Real Estate            | 14                  |
| Healthcare             | 13                  |
| Materials              | 12                  |
| Consumer Discretionary | 11                  |
| Consumer Staples       | 7                   |
| Information Technology | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| WTC  | Wisetech Global | Information Technology | 120.11   | 31.55        | -73.7          |
| TUA  | Tuas            | Communication Services | 8.32     | 2.23         | -73.2          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.28         | -65.5          |
| XRO  | Xero            | Information Technology | 184.0    | 69.05        | -62.5          |
| COH  | Cochlear        | Healthcare             | 313.15   | 118.03       | -62.3          |
| 360  | Life360         | Information Technology | 55.44    | 23.53        | -57.6          |
| CSL  | CSL             | Healthcare             | 265.45   | 114.87       | -56.7          |
| SEK  | Seek            | Communication Services | 28.65    | 12.61        | -56.0          |

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
| Materials              | 48.57                  |
| Information Technology | 45.62                  |
| Financials             | 44.2                   |
| Energy                 | 39.51                  |
| Healthcare             | 36.96                  |
| Consumer Staples       | 33.13                  |
| Consumer Discretionary | 27.38                  |
| Communication Services | 26.27                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 78.5           | 44.6               | 1.76                 |
| Materials        | 55.4           | 49.0               | 1.13                 |
| Industrials      | 32.3           | 36.0               | 0.9                  |
| Energy           | 13.4           | 41.3               | 0.33                 |
| Utilities        | 3.7            | 27.4               | 0.14                 |
| Financials       | 3.5            | 29.8               | 0.12                 |
| Real Estate      | -0.7           | 21.2               | -0.03                |
| Consumer Staples | -2.8           | 28.0               | -0.1                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 162.02       |
| BHP  | BHP                    | Materials              | 260.3            | 58.99        |
| WBC  | Westpac                | Financials             | 136.3            | 35.14        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.04        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.74        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.36       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.51        |
| CSL  | CSL                    | Healthcare             | 67.4             | 114.87       |
