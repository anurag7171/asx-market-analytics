# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 42.44             | 1015.49  | -60.48    |
| Materials        | 47        | 40.49             | 142.14   | -25.49    |
| Industrials      | 24        | 20.02             | 135.25   | -51.86    |
| Energy           | 11        | 17.43             | 51.94    | -18.72    |
| Financials       | 36        | 4.24              | 58.81    | -38.9     |
| Utilities        | 7         | 2.27              | 28.93    | -10.06    |
| Consumer Staples | 7         | 1.18              | 30.31    | -28.87    |
| Real Estate      | 17        | -3.87             | 18.71    | -53.1     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1015.5              |
| 2    | PLS  | PLS Group              | Materials              | 142.1               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 135.3               |
| 4    | NWH  | NRW Holdings           | Industrials            | 128.7               |
| 5    | CDA  | Codan                  | Information Technology | 92.3                |
| 6    | VAU  | Vault Minerals         | Materials              | 91.9                |
| 7    | GGP  | Greatland Resources    | Materials              | 91.3                |
| 8    | MIN  | Mineral Resources      | Materials              | 87.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 141.3                 |
| EOS  | 253          | 109.4                 |
| DRO  | 253          | 103.3                 |
| TUA  | 253          | 81.6                  |
| LTR  | 253          | 81.3                  |
| OBM  | 253          | 78.4                  |
| ZIP  | 253          | 78.1                  |
| CYL  | 253          | 72.4                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| EOS  | Electro Optic Systems  | 2025-08-05 | 43.4           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 31                  |
| Real Estate            | 14                  |
| Industrials            | 14                  |
| Consumer Discretionary | 14                  |
| Materials              | 12                  |
| Healthcare             | 11                  |
| Consumer Staples       | 7                   |
| Communication Services | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.14         | -74.3          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.81         | -72.5          |
| WTC  | Wisetech Global    | Information Technology | 116.31   | 36.74        | -68.4          |
| LTR  | Liontown Resources | Materials              | 2.64     | 0.99         | -62.5          |
| COH  | Cochlear           | Healthcare             | 307.7    | 120.74       | -60.8          |
| XRO  | Xero               | Information Technology | 178.83   | 71.31        | -60.1          |
| ASB  | Austal             | Industrials            | 8.76     | 3.65         | -58.3          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.42         | -56.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.3            |
| DRO  | Droneshield     | -74.3            |
| COH  | Cochlear        | -70.8            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.2            |
| XRO  | Xero            | -65.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.71                  |
| Information Technology | 45.42                  |
| Financials             | 44.08                  |
| Energy                 | 40.33                  |
| Healthcare             | 36.62                  |
| Consumer Staples       | 33.09                  |
| Consumer Discretionary | 27.75                  |
| Communication Services | 26.73                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 42.4           | 44.2               | 0.96                 |
| Materials              | 40.5           | 49.3               | 0.82                 |
| Industrials            | 20.0           | 36.1               | 0.55                 |
| Energy                 | 17.4           | 41.6               | 0.42                 |
| Financials             | 4.2            | 30.3               | 0.14                 |
| Utilities              | 2.3            | 28.2               | 0.08                 |
| Consumer Staples       | 1.2            | 28.5               | 0.04                 |
| Consumer Discretionary | -5.1           | 33.1               | -0.16                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 177.9        |
| BHP  | BHP                    | Materials              | 260.3            | 60.72        |
| WBC  | Westpac                | Financials             | 136.3            | 38.17        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.29        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.66        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 255.2        |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.6         |
| CSL  | CSL                    | Healthcare             | 67.4             | 124.3        |
