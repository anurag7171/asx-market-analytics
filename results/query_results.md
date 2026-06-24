# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Healthcare             | 16        | 94.14             | 1812.0   | -60.84    |
| Materials              | 47        | 59.51             | 340.47   | -21.49    |
| Industrials            | 24        | 35.17             | 301.23   | -30.02    |
| Energy                 | 11        | 16.98             | 49.68    | -31.47    |
| Financials             | 36        | 4.93              | 71.0     | -35.53    |
| Utilities              | 7         | 4.3               | 30.87    | -8.82     |
| Real Estate            | 17        | -2.79             | 22.68    | -44.33    |
| Consumer Discretionary | 15        | -3.46             | 29.78    | -37.19    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1812.0              |
| 2    | PLS  | PLS Group              | Materials              | 340.5               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 301.2               |
| 4    | MIN  | Mineral Resources      | Materials              | 206.9               |
| 5    | LTR  | Liontown Resources     | Materials              | 175.4               |
| 6    | NWH  | NRW Holdings           | Industrials            | 152.3               |
| 7    | CDA  | Codan                  | Information Technology | 120.4               |
| 8    | ILU  | Iluka Resources        | Materials              | 119.2               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 141.3                 |
| DRO  | 254          | 109.8                 |
| EOS  | 254          | 108.6                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.0                  |
| OBM  | 254          | 79.0                  |
| ZIP  | 254          | 76.2                  |
| DYL  | 254          | 70.8                  |

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
| Materials              | 14                  |
| Real Estate            | 13                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 10                  |
| Consumer Staples       | 7                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| WTC  | Wisetech Global | Information Technology | 120.11   | 32.86        | -72.6          |
| TUA  | Tuas            | Communication Services | 8.32     | 2.31         | -72.2          |
| COH  | Cochlear        | Healthcare             | 313.15   | 113.45       | -63.8          |
| XRO  | Xero            | Information Technology | 194.21   | 70.31        | -63.8          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.55         | -61.4          |
| 360  | Life360         | Information Technology | 55.44    | 23.09        | -58.4          |
| CSL  | CSL             | Healthcare             | 265.45   | 114.99       | -56.7          |
| SEK  | Seek            | Communication Services | 28.65    | 12.75        | -55.5          |

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
| Materials              | 48.46                  |
| Information Technology | 45.41                  |
| Financials             | 44.15                  |
| Energy                 | 39.46                  |
| Healthcare             | 36.78                  |
| Consumer Staples       | 33.18                  |
| Consumer Discretionary | 27.25                  |
| Communication Services | 26.18                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 94.1           | 44.5               | 2.12                 |
| Materials              | 59.5           | 48.9               | 1.22                 |
| Industrials            | 35.2           | 36.0               | 0.98                 |
| Energy                 | 17.0           | 41.1               | 0.41                 |
| Financials             | 4.9            | 29.8               | 0.17                 |
| Utilities              | 4.3            | 27.3               | 0.16                 |
| Consumer Discretionary | -3.5           | 32.8               | -0.11                |
| Real Estate            | -2.8           | 21.1               | -0.13                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 164.79       |
| BHP  | BHP                    | Materials              | 260.3            | 59.5         |
| WBC  | Westpac                | Financials             | 136.3            | 35.78        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.64        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 87.27        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.12       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.75        |
| CSL  | CSL                    | Healthcare             | 67.4             | 114.99       |
