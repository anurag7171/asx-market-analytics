# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 6.88              | 62.51    | -58.31    |
| Consumer Staples | 7         | 6.69              | 47.64    | -22.35    |
| Materials        | 47        | 5.84              | 64.0     | -67.25    |
| Industrials      | 23        | 3.37              | 61.62    | -70.91    |
| Utilities        | 7         | 1.74              | 31.02    | -14.19    |
| Financials       | 36        | -0.35             | 40.28    | -55.4     |
| Healthcare       | 16        | -6.83             | 79.37    | -50.77    |
| Real Estate      | 16        | -12.33            | 5.43     | -52.22    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 79.4                |
| 2    | CDA  | Codan                | Information Technology | 66.3                |
| 3    | BSL  | BlueScope            | Materials              | 64.0                |
| 4    | VEA  | Viva Energy          | Energy                 | 62.5                |
| 5    | REH  | Reece Group          | Industrials            | 61.6                |
| 6    | ALK  | Alkane Resources     | Materials              | 55.0                |
| 7    | PDI  | Predictive Discovery | Materials              | 51.8                |
| 8    | STO  | Santos               | Energy                 | 48.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.6                 |
| CTD  | 254          | 96.0                  |
| DRO  | 254          | 95.9                  |
| EOS  | 254          | 95.7                  |
| ZIP  | 254          | 86.7                  |
| TUA  | 254          | 85.9                  |
| OBM  | 254          | 78.5                  |
| LTR  | 254          | 75.6                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| NXT  | NextDC                 | 2026-10-20 | -41.7          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 25                  |
| Real Estate            | 15                  |
| Industrials            | 11                  |
| Healthcare             | 11                  |
| Consumer Discretionary | 11                  |
| Communication Services | 7                   |
| Consumer Staples       | 6                   |
| Information Technology | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.38         | -82.0          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.31         | -79.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.6          | -77.3          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.69         | -76.3          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.21         | -74.5          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.76         | -73.2          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.15         | -68.4          |
| CYL  | Catalyst Metals        | Materials              | 9.64     | 3.49         | -63.8          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -77.3            |
| DYL  | Deep Yellow            | -76.8            |
| DRO  | Droneshield            | -74.5            |
| CIA  | Champion Iron          | -73.2            |
| 4DX  | 4DMedical              | -68.4            |
| COH  | Cochlear               | -68.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.11                  |
| Information Technology | 45.5                   |
| Financials             | 44.58                  |
| Energy                 | 41.55                  |
| Healthcare             | 35.91                  |
| Consumer Staples       | 32.13                  |
| Consumer Discretionary | 28.01                  |
| Communication Services | 27.81                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 6.7            | 28.5               | 0.23                 |
| Energy                 | 6.9            | 41.7               | 0.16                 |
| Materials              | 5.8            | 48.6               | 0.12                 |
| Industrials            | 3.4            | 36.7               | 0.09                 |
| Utilities              | 1.7            | 28.0               | 0.06                 |
| Financials             | -0.3           | 30.9               | -0.01                |
| Healthcare             | -6.8           | 42.2               | -0.16                |
| Information Technology | -20.4          | 52.7               | -0.39                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 166.26       |
| BHP  | BHP                    | Materials              | 260.3            | 55.56        |
| WBC  | Westpac                | Financials             | 136.3            | 37.01        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 40.36        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.66        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.87       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.17        |
| CSL  | CSL                    | Healthcare             | 67.4             | 197.34       |
