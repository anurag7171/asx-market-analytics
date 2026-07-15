# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 74.52             | 1460.0   | -57.94    |
| Materials        | 47        | 41.85             | 194.6    | -31.21    |
| Industrials      | 24        | 21.22             | 130.46   | -39.45    |
| Energy           | 11        | 12.12             | 44.19    | -31.43    |
| Financials       | 36        | 4.27              | 65.16    | -34.31    |
| Utilities        | 7         | 1.05              | 27.33    | -10.15    |
| Consumer Staples | 7         | -1.69             | 29.17    | -39.54    |
| Real Estate      | 17        | -4.83             | 15.53    | -40.61    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1460.0              |
| 2    | PLS  | PLS Group              | Materials              | 194.6               |
| 3    | CDA  | Codan                  | Information Technology | 130.9               |
| 4    | NWH  | NRW Holdings           | Industrials            | 130.5               |
| 5    | EOS  | Electro Optic Systems  | Industrials            | 122.0               |
| 6    | MIN  | Mineral Resources      | Materials              | 118.5               |
| 7    | ALK  | Alkane Resources       | Materials              | 109.0               |
| 8    | VAU  | Vault Minerals         | Materials              | 88.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.5                 |
| EOS  | 254          | 107.6                 |
| DRO  | 254          | 104.7                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.5                  |
| OBM  | 254          | 78.2                  |
| ZIP  | 254          | 77.1                  |
| CYL  | 254          | 71.9                  |

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
| Financials             | 32                  |
| Industrials            | 14                  |
| Materials              | 13                  |
| Real Estate            | 12                  |
| Healthcare             | 12                  |
| Consumer Discretionary | 11                  |
| Consumer Staples       | 6                   |
| Information Technology | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.27         | -72.7          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 34.27        | -71.5          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.37         | -64.1          |
| XRO  | Xero            | Information Technology | 181.0    | 68.27        | -62.3          |
| COH  | Cochlear        | Healthcare             | 313.15   | 124.0        | -60.4          |
| ASB  | Austal          | Industrials            | 8.76     | 3.53         | -59.7          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 17.31        | -56.5          |
| PXA  | Pexa Group      | Real Estate            | 16.92    | 7.61         | -55.0          |

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
| TLX  | Telix Pharmaceuticals | -65.8            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.62                  |
| Information Technology | 45.18                  |
| Financials             | 44.04                  |
| Energy                 | 39.81                  |
| Healthcare             | 37.02                  |
| Consumer Staples       | 33.13                  |
| Consumer Discretionary | 27.68                  |
| Communication Services | 26.47                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 74.5           | 44.7               | 1.67                 |
| Materials              | 41.8           | 49.1               | 0.85                 |
| Industrials            | 21.2           | 35.9               | 0.59                 |
| Energy                 | 12.1           | 41.4               | 0.29                 |
| Financials             | 4.3            | 30.0               | 0.14                 |
| Utilities              | 1.0            | 27.4               | 0.04                 |
| Consumer Staples       | -1.7           | 28.2               | -0.06                |
| Information Technology | -7.7           | 46.7               | -0.16                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 170.0        |
| BHP  | BHP                    | Materials              | 260.3            | 60.56        |
| WBC  | Westpac                | Financials             | 136.3            | 36.58        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.95        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.88        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 258.16       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.27        |
| CSL  | CSL                    | Healthcare             | 67.4             | 121.75       |
