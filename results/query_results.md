# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 16.88             | 82.22    | -61.38    |
| Consumer Staples | 7         | 9.06              | 52.16    | -19.81    |
| Industrials      | 23        | 6.71              | 70.61    | -65.97    |
| Energy           | 11        | 5.91              | 55.43    | -52.52    |
| Utilities        | 7         | 2.13              | 28.48    | -10.08    |
| Financials       | 36        | 1.71              | 39.96    | -52.54    |
| Healthcare       | 16        | -2.01             | 85.38    | -47.69    |
| Real Estate      | 16        | -10.66            | 5.43     | -49.93    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 85.4                |
| 2    | ALK  | Alkane Resources     | Materials              | 82.2                |
| 3    | PDI  | Predictive Discovery | Materials              | 72.0                |
| 4    | REH  | Reece Group          | Industrials            | 70.6                |
| 5    | CDA  | Codan                | Information Technology | 62.7                |
| 6    | BSL  | BlueScope            | Materials              | 61.6                |
| 7    | 4DX  | 4DMedical            | Healthcare             | 59.1                |
| 8    | VEA  | Viva Energy          | Energy                 | 55.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 107.1                 |
| CTD  | 254          | 96.6                  |
| DRO  | 254          | 96.0                  |
| EOS  | 254          | 95.0                  |
| ZIP  | 254          | 88.1                  |
| TUA  | 254          | 86.1                  |
| OBM  | 254          | 79.8                  |
| NXT  | 254          | 79.5                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| NXT  | NextDC                 | 2026-11-05 | 50.8           |
| NXT  | NextDC                 | 2026-10-20 | -41.7          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 28                  |
| Materials              | 20                  |
| Real Estate            | 16                  |
| Industrials            | 16                  |
| Consumer Discretionary | 13                  |
| Healthcare             | 12                  |
| Communication Services | 8                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.44         | -81.2          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.67         | -77.2          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.67         | -74.6          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.76         | -74.1          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.31         | -72.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.07         | -68.6          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.41         | -64.6          |
| PLS  | PLS Group              | Materials              | 6.68     | 2.83         | -57.6          |

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
| Materials              | 49.24                  |
| Information Technology | 46.1                   |
| Financials             | 44.75                  |
| Energy                 | 41.71                  |
| Healthcare             | 35.97                  |
| Consumer Staples       | 32.21                  |
| Consumer Discretionary | 28.13                  |
| Communication Services | 27.89                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 16.9           | 49.5               | 0.34                 |
| Consumer Staples       | 9.1            | 28.6               | 0.32                 |
| Industrials            | 6.7            | 36.8               | 0.18                 |
| Energy                 | 5.9            | 41.9               | 0.14                 |
| Utilities              | 2.1            | 28.0               | 0.08                 |
| Financials             | 1.7            | 31.1               | 0.05                 |
| Healthcare             | -2.0           | 42.5               | -0.05                |
| Information Technology | -14.1          | 55.7               | -0.25                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 166.29       |
| BHP  | BHP                    | Materials              | 260.3            | 59.0         |
| WBC  | Westpac                | Financials             | 136.3            | 36.64        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 40.1         |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 81.54        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 258.4        |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.96        |
| CSL  | CSL                    | Healthcare             | 67.4             | 202.4        |
