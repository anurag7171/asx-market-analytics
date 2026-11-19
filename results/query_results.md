# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Industrials            | 23        | 8.32              | 77.87    | -45.43    |
| Consumer Staples       | 7         | 6.63              | 55.47    | -25.82    |
| Utilities              | 7         | 5.98              | 28.71    | -7.63     |
| Financials             | 36        | 3.37              | 41.41    | -60.21    |
| Information Technology | 7         | 0.01              | 71.72    | -36.57    |
| Energy                 | 11        | -0.82             | 43.86    | -57.5     |
| Materials              | 47        | -0.88             | 67.22    | -66.62    |
| Healthcare             | 16        | -2.0              | 76.7     | -54.42    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | REH  | Reece Group        | Industrials            | 77.9                |
| 2    | RHC  | Ramsay Health Care | Healthcare             | 76.7                |
| 3    | CDA  | Codan              | Information Technology | 71.7                |
| 4    | ALK  | Alkane Resources   | Materials              | 67.2                |
| 5    | 4DX  | 4DMedical          | Healthcare             | 57.5                |
| 6    | WOW  | Woolworths Group   | Consumer Staples       | 55.5                |
| 7    | BSL  | BlueScope          | Materials              | 52.1                |
| 8    | JHX  | James Hardie       | Materials              | 51.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.0                 |
| CTD  | 254          | 97.3                  |
| EOS  | 254          | 94.5                  |
| ZIP  | 254          | 87.7                  |
| DRO  | 254          | 87.4                  |
| TUA  | 254          | 86.5                  |
| OBM  | 254          | 80.8                  |
| NXT  | 254          | 79.5                  |

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
| Financials             | 24                  |
| Real Estate            | 14                  |
| Industrials            | 14                  |
| Consumer Discretionary | 12                  |
| Healthcare             | 11                  |
| Communication Services | 8                   |
| Utilities              | 7                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.38         | -82.0          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.42         | -78.7          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.58         | -78.0          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.07         | -77.3          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.68         | -76.6          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.72         | -73.9          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.57         | -67.5          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.26         | -66.8          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| DRO  | Droneshield            | -78.1            |
| LTR  | Liontown Resources     | -78.0            |
| DYL  | Deep Yellow            | -76.8            |
| CIA  | Champion Iron          | -73.9            |
| 4DX  | 4DMedical              | -68.7            |
| COH  | Cochlear               | -67.5            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.57                  |
| Information Technology | 46.41                  |
| Financials             | 45.51                  |
| Energy                 | 42.15                  |
| Healthcare             | 36.11                  |
| Consumer Staples       | 32.43                  |
| Communication Services | 27.85                  |
| Consumer Discretionary | 27.82                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Industrials            | 8.3            | 36.8               | 0.23                 |
| Consumer Staples       | 6.6            | 28.7               | 0.23                 |
| Utilities              | 6.0            | 28.1               | 0.21                 |
| Financials             | 3.4            | 30.9               | 0.11                 |
| Information Technology | 0.0            | 55.3               | 0.0                  |
| Materials              | -0.9           | 49.8               | -0.02                |
| Energy                 | -0.8           | 42.4               | -0.02                |
| Healthcare             | -2.0           | 42.4               | -0.05                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 171.63       |
| BHP  | BHP                    | Materials              | 260.3            | 52.34        |
| WBC  | Westpac                | Financials             | 136.3            | 36.76        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.0         |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.51        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 224.92       |
| NAB  | National Australia Ban | Financials             | 69.8             | 36.72        |
| CSL  | CSL                    | Healthcare             | 67.4             | 199.85       |
