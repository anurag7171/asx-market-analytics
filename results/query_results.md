# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 87.02             | 1670.83  | -57.71    |
| Materials        | 47        | 52.43             | 242.95   | -26.34    |
| Industrials      | 24        | 30.76             | 271.79   | -29.93    |
| Energy           | 11        | 11.22             | 38.77    | -33.82    |
| Financials       | 36        | 6.25              | 75.39    | -32.39    |
| Utilities        | 7         | 0.82              | 25.49    | -11.07    |
| Consumer Staples | 7         | -3.19             | 31.17    | -41.89    |
| Real Estate      | 17        | -5.46             | 22.64    | -40.72    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1670.8              |
| 2    | EOS  | Electro Optic Systems  | Industrials            | 271.8               |
| 3    | PLS  | PLS Group              | Materials              | 243.0               |
| 4    | MIN  | Mineral Resources      | Materials              | 166.2               |
| 5    | NWH  | NRW Holdings           | Industrials            | 144.3               |
| 6    | LTR  | Liontown Resources     | Materials              | 132.0               |
| 7    | CDA  | Codan                  | Information Technology | 125.5               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 118.5               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.5                 |
| EOS  | 254          | 108.6                 |
| DRO  | 254          | 107.1                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.5                  |
| OBM  | 254          | 79.7                  |
| ZIP  | 254          | 76.7                  |
| CYL  | 254          | 72.4                  |

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
| Financials             | 28                  |
| Industrials            | 21                  |
| Materials              | 17                  |
| Real Estate            | 13                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 9                   |
| Consumer Staples       | 7                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| WTC  | Wisetech Global | Information Technology | 120.11   | 32.96        | -72.6          |
| TUA  | Tuas            | Communication Services | 8.32     | 2.32         | -72.1          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.41         | -63.5          |
| COH  | Cochlear        | Healthcare             | 313.15   | 124.96       | -60.1          |
| XRO  | Xero            | Information Technology | 181.0    | 72.25        | -60.1          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 18.17        | -54.3          |
| CSL  | CSL             | Healthcare             | 265.45   | 121.81       | -54.1          |
| SEK  | Seek            | Communication Services | 28.65    | 13.31        | -53.5          |

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
| Information Technology | 45.11                  |
| Financials             | 44.08                  |
| Energy                 | 39.47                  |
| Healthcare             | 36.95                  |
| Consumer Staples       | 33.11                  |
| Consumer Discretionary | 27.54                  |
| Communication Services | 26.31                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 87.0           | 44.6               | 1.95                 |
| Materials              | 52.4           | 49.2               | 1.06                 |
| Industrials            | 30.8           | 35.9               | 0.86                 |
| Energy                 | 11.2           | 41.2               | 0.27                 |
| Financials             | 6.3            | 30.0               | 0.21                 |
| Utilities              | 0.8            | 27.5               | 0.03                 |
| Consumer Staples       | -3.2           | 28.2               | -0.11                |
| Information Technology | -6.5           | 46.4               | -0.14                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 165.02       |
| BHP  | BHP                    | Materials              | 260.3            | 60.5         |
| WBC  | Westpac                | Financials             | 136.3            | 35.69        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.26        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 88.25        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 251.65       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.57        |
| CSL  | CSL                    | Healthcare             | 67.4             | 121.81       |
