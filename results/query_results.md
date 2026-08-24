# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 54.05             | 153.24   | -31.55    |
| Energy           | 11        | 24.58             | 68.1     | -25.32    |
| Healthcare       | 16        | 20.64             | 579.63   | -54.18    |
| Industrials      | 24        | 12.62             | 118.86   | -49.44    |
| Utilities        | 7         | 4.02              | 27.26    | -9.07     |
| Financials       | 36        | 0.31              | 91.46    | -39.69    |
| Consumer Staples | 7         | -5.83             | 21.55    | -27.79    |
| Real Estate      | 17        | -14.57            | 6.71     | -52.15    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 579.6               |
| 2    | PLS  | PLS Group           | Materials   | 153.2               |
| 3    | GGP  | Greatland Resources | Materials   | 144.7               |
| 4    | OBM  | Ora Banda Mining    | Materials   | 129.5               |
| 5    | NWH  | NRW Holdings        | Industrials | 118.9               |
| 6    | VAU  | Vault Minerals      | Materials   | 118.4               |
| 7    | GMD  | Genesis Minerals    | Materials   | 101.6               |
| 8    | WGX  | Westgold Resources  | Materials   | 98.8                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 138.5                 |
| DRO  | 253          | 103.8                 |
| EOS  | 253          | 98.9                  |
| OBM  | 253          | 79.5                  |
| LTR  | 253          | 79.4                  |
| ZIP  | 253          | 79.2                  |
| TUA  | 253          | 76.1                  |
| DYL  | 253          | 72.9                  |

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
| Financials             | 16                  |
| Healthcare             | 12                  |
| Industrials            | 10                  |
| Energy                 | 10                  |
| Communication Services | 7                   |
| Utilities              | 5                   |
| Information Technology | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.09         | -74.9          |
| DRO  | Droneshield     | Industrials            | 6.6      | 1.81         | -72.5          |
| 360  | Life360         | Information Technology | 55.44    | 20.78        | -62.5          |
| WTC  | Wisetech Global | Information Technology | 115.37   | 43.49        | -62.3          |
| COH  | Cochlear        | Healthcare             | 296.77   | 135.77       | -54.3          |
| PXA  | Pexa Group      | Real Estate            | 16.92    | 7.9          | -53.3          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 18.89        | -52.5          |
| ASB  | Austal          | Industrials            | 8.76     | 4.2          | -52.1          |

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
| Materials              | 49.24                  |
| Information Technology | 45.82                  |
| Financials             | 44.01                  |
| Energy                 | 40.42                  |
| Healthcare             | 36.37                  |
| Consumer Staples       | 33.02                  |
| Consumer Discretionary | 27.45                  |
| Communication Services | 26.83                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 54.0           | 49.2               | 1.1                  |
| Energy                 | 24.6           | 41.8               | 0.59                 |
| Healthcare             | 20.6           | 44.3               | 0.47                 |
| Industrials            | 12.6           | 36.2               | 0.35                 |
| Utilities              | 4.0            | 27.7               | 0.15                 |
| Financials             | 0.3            | 30.3               | 0.01                 |
| Consumer Staples       | -5.8           | 29.0               | -0.2                 |
| Information Technology | -16.4          | 48.7               | -0.34                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 156.88       |
| BHP  | BHP                    | Materials              | 260.3            | 67.12        |
| WBC  | Westpac                | Financials             | 136.3            | 33.74        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.86        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 82.35        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 247.87       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.01        |
| CSL  | CSL                    | Healthcare             | 67.4             | 169.11       |
