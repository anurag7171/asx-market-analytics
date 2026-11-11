# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 13.31             | 78.38    | -58.73    |
| Consumer Staples       | 7         | 9.0               | 52.71    | -18.1     |
| Industrials            | 23        | 8.96              | 76.61    | -61.03    |
| Energy                 | 11        | 6.71              | 53.53    | -47.15    |
| Utilities              | 7         | 2.88              | 25.95    | -10.87    |
| Financials             | 36        | 1.97              | 39.88    | -51.93    |
| Healthcare             | 16        | -3.01             | 86.73    | -49.05    |
| Information Technology | 7         | -11.32            | 71.32    | -54.56    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 86.7                |
| 2    | PDI  | Predictive Discovery | Materials              | 78.4                |
| 3    | REH  | Reece Group          | Industrials            | 76.6                |
| 4    | ALK  | Alkane Resources     | Materials              | 72.9                |
| 5    | CDA  | Codan                | Information Technology | 71.3                |
| 6    | JHX  | James Hardie         | Materials              | 61.0                |
| 7    | BSL  | BlueScope            | Materials              | 60.9                |
| 8    | VEA  | Viva Energy          | Energy                 | 53.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.3                 |
| CTD  | 254          | 96.7                  |
| DRO  | 254          | 95.2                  |
| EOS  | 254          | 94.8                  |
| ZIP  | 254          | 87.9                  |
| TUA  | 254          | 86.1                  |
| OBM  | 254          | 80.0                  |
| NXT  | 254          | 79.7                  |

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
| Financials             | 30                  |
| Materials              | 26                  |
| Industrials            | 16                  |
| Real Estate            | 15                  |
| Consumer Discretionary | 14                  |
| Healthcare             | 12                  |
| Information Technology | 7                   |
| Communication Services | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.5          | -80.4          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.65         | -77.3          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.71         | -72.9          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.29         | -72.8          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.88         | -69.8          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.18         | -66.9          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.37         | -65.1          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.78         | -55.5          |

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
| Materials              | 49.41                  |
| Information Technology | 46.53                  |
| Financials             | 45.58                  |
| Energy                 | 41.91                  |
| Healthcare             | 36.15                  |
| Consumer Staples       | 32.39                  |
| Consumer Discretionary | 28.17                  |
| Communication Services | 27.96                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 9.0            | 28.5               | 0.32                 |
| Materials              | 13.3           | 49.6               | 0.27                 |
| Industrials            | 9.0            | 37.2               | 0.24                 |
| Energy                 | 6.7            | 42.0               | 0.16                 |
| Utilities              | 2.9            | 28.0               | 0.1                  |
| Financials             | 2.0            | 31.0               | 0.06                 |
| Healthcare             | -3.0           | 42.4               | -0.07                |
| Information Technology | -11.3          | 55.9               | -0.2                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 166.94       |
| BHP  | BHP                    | Materials              | 260.3            | 60.39        |
| WBC  | Westpac                | Financials             | 136.3            | 37.29        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.98        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 81.14        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.23       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.56        |
| CSL  | CSL                    | Healthcare             | 67.4             | 201.68       |
