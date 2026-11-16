# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Consumer Staples       | 7         | 9.26              | 53.71    | -15.56    |
| Industrials            | 23        | 8.18              | 76.21    | -56.92    |
| Materials              | 47        | 5.47              | 76.97    | -62.66    |
| Financials             | 36        | 3.38              | 40.05    | -51.62    |
| Energy                 | 11        | 2.96              | 48.69    | -54.57    |
| Utilities              | 7         | 2.61              | 28.67    | -13.56    |
| Healthcare             | 16        | -2.86             | 78.0     | -49.72    |
| Information Technology | 7         | -5.67             | 71.55    | -41.16    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 78.0                |
| 2    | ALK  | Alkane Resources     | Materials              | 77.0                |
| 3    | REH  | Reece Group          | Industrials            | 76.2                |
| 4    | CDA  | Codan                | Information Technology | 71.6                |
| 5    | JHX  | James Hardie         | Materials              | 60.9                |
| 6    | BSL  | BlueScope            | Materials              | 60.4                |
| 7    | WOW  | Woolworths Group     | Consumer Staples       | 53.7                |
| 8    | PDI  | Predictive Discovery | Materials              | 51.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 106.2                 |
| CTD  | 253          | 97.0                  |
| EOS  | 253          | 94.7                  |
| DRO  | 253          | 89.7                  |
| ZIP  | 253          | 88.0                  |
| TUA  | 253          | 86.4                  |
| OBM  | 253          | 80.3                  |
| NXT  | 253          | 79.6                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| NXT  | NextDC                 | 2026-11-04 | 50.8           |
| NXT  | NextDC                 | 2026-10-20 | -41.7          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 26                  |
| Industrials            | 17                  |
| Real Estate            | 15                  |
| Materials              | 15                  |
| Consumer Discretionary | 13                  |
| Healthcare             | 12                  |
| Communication Services | 8                   |
| Utilities              | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.51         | -80.2          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.49         | -78.3          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.12         | -76.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.64         | -75.8          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.74         | -74.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.98         | -69.9          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.19         | -67.8          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.66         | -62.3          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -77.3            |
| DYL  | Deep Yellow            | -76.8            |
| DRO  | Droneshield            | -76.4            |
| CIA  | Champion Iron          | -73.2            |
| 4DX  | 4DMedical              | -68.4            |
| COH  | Cochlear               | -67.5            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.37                  |
| Information Technology | 46.34                  |
| Financials             | 45.38                  |
| Energy                 | 42.02                  |
| Healthcare             | 36.09                  |
| Consumer Staples       | 32.43                  |
| Communication Services | 27.86                  |
| Consumer Discretionary | 27.85                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 9.3            | 28.5               | 0.32                 |
| Industrials            | 8.2            | 37.0               | 0.22                 |
| Materials              | 5.5            | 49.6               | 0.11                 |
| Financials             | 3.4            | 31.0               | 0.11                 |
| Utilities              | 2.6            | 28.1               | 0.09                 |
| Energy                 | 3.0            | 42.3               | 0.07                 |
| Healthcare             | -2.9           | 42.4               | -0.07                |
| Information Technology | -5.7           | 55.7               | -0.1                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 171.14       |
| BHP  | BHP                    | Materials              | 260.3            | 57.21        |
| WBC  | Westpac                | Financials             | 136.3            | 37.77        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.81        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 80.16        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 241.18       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.84        |
| CSL  | CSL                    | Healthcare             | 67.4             | 202.52       |
