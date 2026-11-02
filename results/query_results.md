# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 9.05              | 63.08    | -57.14    |
| Materials        | 47        | 5.78              | 62.54    | -66.07    |
| Consumer Staples | 7         | 4.25              | 43.41    | -23.17    |
| Industrials      | 23        | 3.7               | 58.37    | -65.4     |
| Utilities        | 7         | 0.29              | 29.84    | -14.57    |
| Financials       | 36        | -1.1              | 38.65    | -56.29    |
| Healthcare       | 16        | -4.66             | 79.79    | -49.16    |
| Real Estate      | 16        | -14.82            | 2.9      | -54.73    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care | Healthcare             | 79.8                |
| 2    | CDA  | Codan              | Information Technology | 66.0                |
| 3    | VEA  | Viva Energy        | Energy                 | 63.1                |
| 4    | 4DX  | 4DMedical          | Healthcare             | 63.0                |
| 5    | BSL  | BlueScope          | Materials              | 62.5                |
| 6    | REH  | Reece Group        | Industrials            | 58.4                |
| 7    | ALK  | Alkane Resources   | Materials              | 54.6                |
| 8    | NHC  | New Hope           | Energy                 | 52.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 106.0                 |
| DRO  | 253          | 96.2                  |
| CTD  | 253          | 96.1                  |
| EOS  | 253          | 95.5                  |
| ZIP  | 253          | 86.7                  |
| TUA  | 253          | 86.0                  |
| OBM  | 253          | 78.6                  |
| LTR  | 253          | 75.7                  |

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
| Financials             | 22                  |
| Real Estate            | 14                  |
| Industrials            | 13                  |
| Healthcare             | 11                  |
| Consumer Discretionary | 11                  |
| Materials              | 8                   |
| Consumer Staples       | 6                   |
| Communication Services | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.35         | -82.3          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.48         | -78.3          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.6          | -77.1          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.73         | -74.7          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.32         | -72.0          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.89         | -71.4          |
| NXT  | NextDC                 | Information Technology | 16.49    | 5.95         | -63.9          |
| CYL  | Catalyst Metals        | Materials              | 9.64     | 3.63         | -62.3          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -77.1            |
| DYL  | Deep Yellow            | -76.8            |
| DRO  | Droneshield            | -72.0            |
| CIA  | Champion Iron          | -71.6            |
| COH  | Cochlear               | -68.4            |
| NXT  | NextDC                 | -67.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.11                  |
| Information Technology | 45.4                   |
| Financials             | 44.5                   |
| Energy                 | 41.43                  |
| Healthcare             | 35.91                  |
| Consumer Staples       | 32.06                  |
| Consumer Discretionary | 28.02                  |
| Communication Services | 27.76                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 9.1            | 41.6               | 0.22                 |
| Consumer Staples       | 4.2            | 28.5               | 0.15                 |
| Materials              | 5.8            | 48.7               | 0.12                 |
| Industrials            | 3.7            | 36.7               | 0.1                  |
| Utilities              | 0.3            | 28.0               | 0.01                 |
| Financials             | -1.1           | 30.9               | -0.04                |
| Healthcare             | -4.7           | 42.2               | -0.11                |
| Information Technology | -21.2          | 52.7               | -0.4                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 165.05       |
| BHP  | BHP                    | Materials              | 260.3            | 56.74        |
| WBC  | Westpac                | Financials             | 136.3            | 37.19        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 40.56        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.12        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 251.33       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.91        |
| CSL  | CSL                    | Healthcare             | 67.4             | 201.16       |
