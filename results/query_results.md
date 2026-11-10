# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 14.66             | 77.45    | -58.01    |
| Consumer Staples | 7         | 10.51             | 53.91    | -17.84    |
| Industrials      | 23        | 7.6               | 73.89    | -60.58    |
| Energy           | 11        | 7.33              | 54.59    | -47.13    |
| Financials       | 36        | 1.88              | 39.86    | -51.32    |
| Utilities        | 7         | 1.86              | 25.19    | -11.44    |
| Healthcare       | 16        | -3.14             | 86.18    | -49.05    |
| Real Estate      | 16        | -12.09            | 2.82     | -51.67    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 86.2                |
| 2    | ALK  | Alkane Resources     | Materials              | 77.5                |
| 3    | PDI  | Predictive Discovery | Materials              | 76.2                |
| 4    | REH  | Reece Group          | Industrials            | 73.9                |
| 5    | CDA  | Codan                | Information Technology | 69.7                |
| 6    | BSL  | BlueScope            | Materials              | 61.9                |
| 7    | JHX  | James Hardie         | Materials              | 61.7                |
| 8    | VEA  | Viva Energy          | Energy                 | 54.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.3                 |
| CTD  | 254          | 96.7                  |
| DRO  | 254          | 95.2                  |
| EOS  | 254          | 94.9                  |
| ZIP  | 254          | 87.9                  |
| TUA  | 254          | 86.1                  |
| OBM  | 254          | 79.9                  |
| NXT  | 254          | 79.6                  |

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
| Financials             | 29                  |
| Materials              | 24                  |
| Industrials            | 16                  |
| Real Estate            | 15                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 13                  |
| Communication Services | 7                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.45         | -81.0          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.57         | -77.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.69         | -73.9          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.28         | -72.9          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.88         | -69.9          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.21         | -66.4          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.35         | -65.4          |
| 360  | Life360                | Information Technology | 48.32    | 18.91        | -60.9          |

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
| Materials              | 49.35                  |
| Information Technology | 46.48                  |
| Financials             | 45.55                  |
| Energy                 | 41.87                  |
| Healthcare             | 36.11                  |
| Consumer Staples       | 32.36                  |
| Consumer Discretionary | 28.15                  |
| Communication Services | 27.95                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 10.5           | 28.7               | 0.37                 |
| Materials              | 14.7           | 49.7               | 0.3                  |
| Industrials            | 7.6            | 37.1               | 0.2                  |
| Energy                 | 7.3            | 42.0               | 0.17                 |
| Utilities              | 1.9            | 28.0               | 0.07                 |
| Financials             | 1.9            | 31.0               | 0.06                 |
| Healthcare             | -3.1           | 42.4               | -0.07                |
| Information Technology | -12.4          | 55.8               | -0.22                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 168.99       |
| BHP  | BHP                    | Materials              | 260.3            | 59.87        |
| WBC  | Westpac                | Financials             | 136.3            | 37.26        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.44        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 80.52        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 251.54       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.15        |
| CSL  | CSL                    | Healthcare             | 67.4             | 200.73       |
