# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 48.09             | 142.8    | -23.89    |
| Healthcare             | 16        | 30.44             | 750.0    | -57.36    |
| Energy                 | 11        | 19.32             | 59.43    | -29.62    |
| Industrials            | 24        | 16.2              | 122.04   | -46.33    |
| Financials             | 36        | 5.29              | 62.23    | -34.8     |
| Consumer Staples       | 7         | 1.52              | 28.09    | -23.95    |
| Utilities              | 7         | 0.13              | 22.94    | -13.52    |
| Consumer Discretionary | 15        | -3.96             | 27.92    | -39.94    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 750.0               |
| 2    | GGP  | Greatland Resources | Materials   | 142.8               |
| 3    | VAU  | Vault Minerals      | Materials   | 125.4               |
| 4    | NWH  | NRW Holdings        | Industrials | 122.0               |
| 5    | PLS  | PLS Group           | Materials   | 102.6               |
| 6    | OBM  | Ora Banda Mining    | Materials   | 101.5               |
| 7    | WGX  | Westgold Resources  | Materials   | 95.6                |
| 8    | EMR  | Emerald Resources   | Materials   | 85.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.8                 |
| DRO  | 254          | 104.2                 |
| EOS  | 254          | 100.4                 |
| TUA  | 254          | 81.5                  |
| LTR  | 254          | 79.8                  |
| OBM  | 254          | 78.5                  |
| ZIP  | 254          | 78.2                  |
| 360  | 254          | 72.3                  |

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
| Materials              | 37                  |
| Financials             | 27                  |
| Healthcare             | 15                  |
| Real Estate            | 14                  |
| Industrials            | 12                  |
| Consumer Discretionary | 12                  |
| Communication Services | 8                   |
| Energy                 | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.16         | -74.0          |
| DRO  | Droneshield        | Industrials            | 6.6      | 2.12         | -67.9          |
| WTC  | Wisetech Global    | Information Technology | 115.58   | 40.84        | -64.7          |
| COH  | Cochlear           | Healthcare             | 307.14   | 130.21       | -57.6          |
| 360  | Life360            | Information Technology | 55.44    | 23.75        | -57.2          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.18         | -55.3          |
| XRO  | Xero               | Information Technology | 176.54   | 78.89        | -55.3          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.96         | -53.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.1            |
| DRO  | Droneshield     | -74.3            |
| COH  | Cochlear        | -70.7            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.2            |
| CSL  | CSL             | -65.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.92                  |
| Information Technology | 45.58                  |
| Financials             | 44.24                  |
| Energy                 | 40.45                  |
| Healthcare             | 36.56                  |
| Consumer Staples       | 33.14                  |
| Consumer Discretionary | 27.7                   |
| Communication Services | 26.81                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 48.1           | 49.3               | 0.98                 |
| Healthcare             | 30.4           | 44.1               | 0.69                 |
| Energy                 | 19.3           | 41.8               | 0.46                 |
| Industrials            | 16.2           | 35.9               | 0.45                 |
| Financials             | 5.3            | 30.1               | 0.18                 |
| Consumer Staples       | 1.5            | 28.5               | 0.05                 |
| Utilities              | 0.1            | 28.2               | 0.0                  |
| Consumer Discretionary | -4.0           | 32.8               | -0.12                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 173.92       |
| BHP  | BHP                    | Materials              | 260.3            | 63.93        |
| WBC  | Westpac                | Financials             | 136.3            | 35.69        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.61        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.42        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 263.46       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.28        |
| CSL  | CSL                    | Healthcare             | 67.4             | 138.33       |
