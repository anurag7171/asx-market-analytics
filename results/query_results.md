# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 5.69              | 61.67    | -66.61    |
| Consumer Staples | 7         | 5.27              | 45.04    | -22.51    |
| Energy           | 11        | 4.85              | 52.36    | -59.48    |
| Industrials      | 23        | 4.6               | 62.31    | -65.8     |
| Utilities        | 7         | 0.82              | 29.61    | -11.9     |
| Financials       | 36        | -0.54             | 38.22    | -54.47    |
| Healthcare       | 16        | -5.54             | 78.08    | -48.93    |
| Real Estate      | 16        | -12.36            | 5.85     | -52.23    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 78.1                |
| 2    | REH  | Reece Group          | Industrials            | 62.3                |
| 3    | BSL  | BlueScope            | Materials              | 61.7                |
| 4    | CDA  | Codan                | Information Technology | 60.1                |
| 5    | ALK  | Alkane Resources     | Materials              | 55.1                |
| 6    | VEA  | Viva Energy          | Energy                 | 52.4                |
| 7    | PDI  | Predictive Discovery | Materials              | 51.4                |
| 8    | 4DX  | 4DMedical            | Healthcare             | 51.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.1                 |
| DRO  | 254          | 96.0                  |
| CTD  | 254          | 95.9                  |
| EOS  | 254          | 95.4                  |
| ZIP  | 254          | 86.7                  |
| TUA  | 254          | 86.0                  |
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
| Financials             | 27                  |
| Real Estate            | 15                  |
| Industrials            | 15                  |
| Consumer Discretionary | 13                  |
| Healthcare             | 12                  |
| Communication Services | 7                   |
| Consumer Staples       | 6                   |
| Materials              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.4          | -81.7          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.46         | -78.5          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.61         | -76.7          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.69         | -76.1          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.31         | -72.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.85         | -71.8          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.41         | -64.6          |
| CYL  | Catalyst Metals        | Materials              | 9.64     | 3.54         | -63.3          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -77.1            |
| DYL  | Deep Yellow            | -76.8            |
| DRO  | Droneshield            | -72.4            |
| CIA  | Champion Iron          | -71.8            |
| COH  | Cochlear               | -68.4            |
| NXT  | NextDC                 | -67.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.06                  |
| Information Technology | 45.39                  |
| Financials             | 44.54                  |
| Energy                 | 41.48                  |
| Healthcare             | 35.9                   |
| Consumer Staples       | 32.07                  |
| Consumer Discretionary | 28.01                  |
| Communication Services | 27.75                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 5.3            | 28.5               | 0.18                 |
| Industrials            | 4.6            | 36.7               | 0.13                 |
| Materials              | 5.7            | 48.6               | 0.12                 |
| Energy                 | 4.9            | 41.8               | 0.12                 |
| Utilities              | 0.8            | 28.0               | 0.03                 |
| Financials             | -0.5           | 30.9               | -0.02                |
| Healthcare             | -5.5           | 42.2               | -0.13                |
| Information Technology | -21.4          | 52.6               | -0.41                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 167.23       |
| BHP  | BHP                    | Materials              | 260.3            | 56.42        |
| WBC  | Westpac                | Financials             | 136.3            | 36.82        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 40.34        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.46        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 254.26       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.97        |
| CSL  | CSL                    | Healthcare             | 67.4             | 198.72       |
