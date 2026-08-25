# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 53.22             | 145.23   | -29.45    |
| Energy                 | 11        | 25.14             | 71.84    | -26.15    |
| Healthcare             | 16        | 23.29             | 618.52   | -53.48    |
| Industrials            | 24        | 13.32             | 110.46   | -45.68    |
| Utilities              | 7         | 4.52              | 29.43    | -8.08     |
| Financials             | 36        | 1.85              | 94.39    | -37.87    |
| Consumer Staples       | 7         | -4.65             | 22.52    | -27.92    |
| Consumer Discretionary | 15        | -14.09            | 27.92    | -45.82    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name | one_year_return_pct |
| ---- | ---- | ---------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare  | 618.5               |
| 2    | GGP  | Greatland Resources    | Materials   | 145.2               |
| 3    | PLS  | PLS Group              | Materials   | 138.0               |
| 4    | VAU  | Vault Minerals         | Materials   | 119.0               |
| 5    | OBM  | Ora Banda Mining       | Materials   | 117.1               |
| 6    | NWH  | NRW Holdings           | Industrials | 110.5               |
| 7    | EOS  | Electro Optic Systems  | Industrials | 109.9               |
| 8    | GMD  | Genesis Minerals       | Materials   | 104.0               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.3                 |
| DRO  | 254          | 103.8                 |
| EOS  | 254          | 101.2                 |
| LTR  | 254          | 79.7                  |
| OBM  | 254          | 79.6                  |
| ZIP  | 254          | 79.3                  |
| TUA  | 254          | 75.9                  |
| DYL  | 254          | 73.0                  |

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
| Materials              | 38                  |
| Financials             | 19                  |
| Industrials            | 10                  |
| Healthcare             | 10                  |
| Energy                 | 10                  |
| Consumer Discretionary | 9                   |
| Utilities              | 7                   |
| Communication Services | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.1          | -74.8          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.95         | -70.5          |
| 360  | Life360            | Information Technology | 55.44    | 20.99        | -62.1          |
| WTC  | Wisetech Global    | Information Technology | 115.37   | 45.47        | -60.6          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.21         | -54.2          |
| COH  | Cochlear           | Healthcare             | 296.77   | 137.84       | -53.6          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 8.05         | -52.4          |
| ASB  | Austal             | Industrials            | 8.76     | 4.25         | -51.5          |

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
| Information Technology | 45.83                  |
| Financials             | 44.0                   |
| Energy                 | 40.46                  |
| Healthcare             | 36.36                  |
| Consumer Staples       | 33.06                  |
| Consumer Discretionary | 27.43                  |
| Communication Services | 26.83                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 53.2           | 49.2               | 1.08                 |
| Energy                 | 25.1           | 41.7               | 0.6                  |
| Healthcare             | 23.3           | 44.4               | 0.52                 |
| Industrials            | 13.3           | 36.4               | 0.37                 |
| Utilities              | 4.5            | 27.7               | 0.16                 |
| Financials             | 1.9            | 30.4               | 0.06                 |
| Consumer Staples       | -4.6           | 29.1               | -0.16                |
| Information Technology | -14.8          | 48.6               | -0.3                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 157.01       |
| BHP  | BHP                    | Materials              | 260.3            | 67.67        |
| WBC  | Westpac                | Financials             | 136.3            | 34.02        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.03        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 82.69        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 252.0        |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.25        |
| CSL  | CSL                    | Healthcare             | 67.4             | 173.64       |
