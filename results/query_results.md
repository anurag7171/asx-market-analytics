# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 42.57             | 124.8    | -26.58    |
| Energy           | 11        | 17.38             | 45.58    | -28.62    |
| Healthcare       | 16        | 11.37             | 340.26   | -53.22    |
| Industrials      | 24        | 8.43              | 96.95    | -44.72    |
| Utilities        | 7         | 4.31              | 32.41    | -11.58    |
| Financials       | 36        | -0.03             | 83.26    | -51.08    |
| Consumer Staples | 7         | -4.53             | 45.9     | -31.21    |
| Real Estate      | 17        | -14.66            | 8.54     | -53.3     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 340.3               |
| 2    | PLS  | PLS Group           | Materials   | 124.8               |
| 3    | NWH  | NRW Holdings        | Industrials | 97.0                |
| 4    | S32  | South32             | Materials   | 95.3                |
| 5    | RSG  | Resolute Mining     | Materials   | 93.7                |
| 6    | GGP  | Greatland Resources | Materials   | 84.4                |
| 7    | L1G  | L1 Group            | Financials  | 83.3                |
| 8    | VAU  | Vault Minerals      | Materials   | 83.0                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 132.6                 |
| DRO  | 254          | 103.9                 |
| EOS  | 254          | 100.1                 |
| ZIP  | 254          | 79.6                  |
| LTR  | 254          | 79.4                  |
| OBM  | 254          | 78.9                  |
| TUA  | 254          | 76.1                  |
| DYL  | 254          | 72.6                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Materials              | 34                  |
| Financials             | 16                  |
| Energy                 | 9                   |
| Healthcare             | 8                   |
| Industrials            | 6                   |
| Information Technology | 5                   |
| Communication Services | 5                   |
| Utilities              | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.11         | -74.6          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.72         | -74.0          |
| 360  | Life360                | Information Technology | 55.44    | 19.2         | -65.4          |
| WTC  | Wisetech Global        | Information Technology | 99.08    | 37.65        | -62.0          |
| GDG  | Generation Development | Financials             | 7.58     | 3.06         | -59.6          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 7.14         | -57.5          |
| COH  | Cochlear               | Healthcare             | 296.77   | 136.45       | -54.0          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.24         | -53.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name       | max_drawdown_pct |
| ---- | ------------------ | ---------------- |
| TUA  | Tuas               | -76.0            |
| DRO  | Droneshield        | -74.3            |
| WTC  | Wisetech Global    | -71.0            |
| ZIP  | Zip                | -70.0            |
| COH  | Cochlear           | -69.7            |
| 360  | Life360            | -67.7            |
| PME  | Pro Medicus        | -66.2            |
| LTR  | Liontown Resources | -63.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.49                  |
| Information Technology | 45.55                  |
| Financials             | 44.07                  |
| Energy                 | 40.67                  |
| Healthcare             | 36.6                   |
| Consumer Staples       | 32.67                  |
| Consumer Discretionary | 27.55                  |
| Communication Services | 27.43                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 42.6           | 49.1               | 0.87                 |
| Energy                 | 17.4           | 41.7               | 0.42                 |
| Healthcare             | 11.4           | 43.8               | 0.26                 |
| Industrials            | 8.4            | 35.2               | 0.24                 |
| Utilities              | 4.3            | 27.5               | 0.16                 |
| Financials             | -0.0           | 30.7               | -0.0                 |
| Consumer Staples       | -4.5           | 28.2               | -0.16                |
| Information Technology | -19.9          | 48.2               | -0.41                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 159.32       |
| BHP  | BHP                    | Materials              | 260.3            | 64.65        |
| WBC  | Westpac                | Financials             | 136.3            | 34.39        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.51        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.16        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.29       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.58        |
| CSL  | CSL                    | Healthcare             | 67.4             | 173.85       |
