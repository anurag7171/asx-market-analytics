# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 15.72             | 88.25    | -63.19    |
| Materials        | 47        | 7.86              | 67.65    | -45.6     |
| Consumer Staples | 7         | 4.74              | 56.71    | -24.08    |
| Industrials      | 23        | 1.69              | 53.07    | -73.67    |
| Utilities        | 7         | 0.28              | 29.48    | -12.47    |
| Healthcare       | 16        | -4.0              | 100.0    | -52.56    |
| Financials       | 36        | -4.16             | 42.66    | -63.18    |
| Real Estate      | 16        | -18.85            | -1.69    | -60.1     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical          | Healthcare             | 100.0               |
| 2    | VEA  | Viva Energy        | Energy                 | 88.2                |
| 3    | CDA  | Codan              | Information Technology | 88.0                |
| 4    | RHC  | Ramsay Health Care | Healthcare             | 75.4                |
| 5    | BSL  | BlueScope          | Materials              | 67.6                |
| 6    | NHC  | New Hope           | Energy                 | 61.1                |
| 7    | SGM  | Sims Metal         | Materials              | 58.8                |
| 8    | WOW  | Woolworths Group   | Consumer Staples       | 56.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 103.1                 |
| DRO  | 255          | 97.1                  |
| EOS  | 255          | 96.1                  |
| CTD  | 255          | 90.3                  |
| ZIP  | 255          | 80.6                  |
| TUA  | 255          | 79.3                  |
| LTR  | 255          | 77.4                  |
| OBM  | 255          | 76.7                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |
| TPG  | TPG Telecom            | 2025-11-13 | -32.1          |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 10                  |
| Industrials            | 8                   |
| Consumer Discretionary | 7                   |
| Materials              | 6                   |
| Healthcare             | 6                   |
| Energy                 | 6                   |
| Consumer Staples       | 5                   |
| Utilities              | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.62         | -83.7          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.62         | -78.8          |
| DRO  | Droneshield            | Industrials            | 5.64     | 1.49         | -73.7          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.72         | -72.7          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.86         | -70.3          |
| GDG  | Generation Development | Financials             | 7.56     | 2.68         | -64.5          |
| XRO  | Xero                   | Information Technology | 157.07   | 59.53        | -62.1          |
| PXA  | Pexa Group             | Real Estate            | 15.92    | 6.2          | -61.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.5            |
| DRO  | Droneshield            | -73.7            |
| LTR  | Liontown Resources     | -72.9            |
| DYL  | Deep Yellow            | -70.3            |
| COH  | Cochlear               | -69.2            |
| ZIP  | Zip                    | -68.9            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.21                  |
| Information Technology | 44.67                  |
| Financials             | 44.22                  |
| Energy                 | 41.02                  |
| Healthcare             | 35.81                  |
| Consumer Staples       | 31.8                   |
| Consumer Discretionary | 27.79                  |
| Communication Services | 27.36                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 15.7           | 41.5               | 0.38                 |
| Consumer Staples       | 4.7            | 28.1               | 0.17                 |
| Materials              | 7.9            | 48.4               | 0.16                 |
| Industrials            | 1.7            | 36.2               | 0.05                 |
| Utilities              | 0.3            | 27.8               | 0.01                 |
| Healthcare             | -4.0           | 42.0               | -0.1                 |
| Financials             | -4.2           | 30.7               | -0.14                |
| Information Technology | -19.6          | 49.6               | -0.39                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 151.17       |
| BHP  | BHP                    | Materials              | 260.3            | 60.86        |
| WBC  | Westpac                | Financials             | 136.3            | 34.69        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.3         |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.26        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.8        |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.55        |
| CSL  | CSL                    | Healthcare             | 67.4             | 184.59       |
