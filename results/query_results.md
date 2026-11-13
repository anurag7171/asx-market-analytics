# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Industrials            | 23        | 8.83              | 73.99    | -47.56    |
| Consumer Staples       | 7         | 7.76              | 52.64    | -18.1     |
| Materials              | 47        | 5.28              | 66.13    | -62.4     |
| Energy                 | 11        | 4.75              | 53.12    | -53.31    |
| Financials             | 36        | 2.58              | 40.82    | -53.54    |
| Utilities              | 7         | 2.17              | 28.48    | -12.78    |
| Healthcare             | 16        | -2.97             | 79.34    | -48.92    |
| Information Technology | 7         | -8.37             | 67.08    | -46.56    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 79.3                |
| 2    | REH  | Reece Group          | Industrials            | 74.0                |
| 3    | CDA  | Codan                | Information Technology | 67.1                |
| 4    | ALK  | Alkane Resources     | Materials              | 66.1                |
| 5    | PDI  | Predictive Discovery | Materials              | 61.8                |
| 6    | JHX  | James Hardie         | Materials              | 56.6                |
| 7    | 4DX  | 4DMedical            | Healthcare             | 56.5                |
| 8    | BSL  | BlueScope            | Materials              | 55.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.1                 |
| CTD  | 254          | 96.8                  |
| EOS  | 254          | 94.8                  |
| DRO  | 254          | 90.2                  |
| ZIP  | 254          | 87.9                  |
| TUA  | 254          | 86.3                  |
| OBM  | 254          | 80.1                  |
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
| Financials             | 27                  |
| Materials              | 19                  |
| Industrials            | 16                  |
| Real Estate            | 15                  |
| Consumer Discretionary | 13                  |
| Healthcare             | 12                  |
| Communication Services | 8                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.55         | -79.7          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.49         | -78.3          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.18         | -75.1          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.66         | -75.0          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.78         | -73.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.05         | -68.9          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.3          | -66.2          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.7          | -59.8          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -77.3            |
| DYL  | Deep Yellow            | -76.8            |
| DRO  | Droneshield            | -75.1            |
| CIA  | Champion Iron          | -73.2            |
| 4DX  | 4DMedical              | -68.4            |
| COH  | Cochlear               | -67.5            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.4                   |
| Information Technology | 46.57                  |
| Financials             | 45.46                  |
| Energy                 | 41.92                  |
| Healthcare             | 36.12                  |
| Consumer Staples       | 32.39                  |
| Consumer Discretionary | 28.0                   |
| Communication Services | 27.89                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 7.8            | 28.5               | 0.27                 |
| Industrials            | 8.8            | 37.0               | 0.24                 |
| Materials              | 5.3            | 49.6               | 0.11                 |
| Energy                 | 4.8            | 42.2               | 0.11                 |
| Utilities              | 2.2            | 28.0               | 0.08                 |
| Financials             | 2.6            | 31.0               | 0.08                 |
| Healthcare             | -3.0           | 42.4               | -0.07                |
| Information Technology | -8.4           | 55.7               | -0.15                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 170.87       |
| BHP  | BHP                    | Materials              | 260.3            | 58.86        |
| WBC  | Westpac                | Financials             | 136.3            | 37.83        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.59        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 80.82        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 244.17       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.86        |
| CSL  | CSL                    | Healthcare             | 67.4             | 202.92       |
