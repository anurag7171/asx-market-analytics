# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 9.68              | 69.91    | -60.51    |
| Industrials            | 23        | 8.39              | 73.06    | -62.04    |
| Consumer Staples       | 7         | 7.43              | 50.22    | -18.81    |
| Energy                 | 11        | 5.68              | 49.46    | -50.76    |
| Financials             | 36        | 2.38              | 40.42    | -52.16    |
| Utilities              | 7         | 1.81              | 25.37    | -9.22     |
| Healthcare             | 16        | -3.33             | 83.37    | -49.64    |
| Information Technology | 7         | -9.27             | 71.16    | -46.55    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care     | Healthcare             | 83.4                |
| 2    | REH  | Reece Group            | Industrials            | 73.1                |
| 3    | CDA  | Codan                  | Information Technology | 71.2                |
| 4    | PDI  | Predictive Discovery   | Materials              | 69.9                |
| 5    | ALK  | Alkane Resources       | Materials              | 66.3                |
| 6    | BSL  | BlueScope              | Materials              | 62.5                |
| 7    | JHX  | James Hardie           | Materials              | 60.5                |
| 8    | EOS  | Electro Optic Systems  | Industrials            | 54.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.3                 |
| CTD  | 254          | 96.8                  |
| DRO  | 254          | 95.3                  |
| EOS  | 254          | 94.8                  |
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
| Financials             | 31                  |
| Materials              | 24                  |
| Industrials            | 16                  |
| Real Estate            | 15                  |
| Consumer Discretionary | 13                  |
| Healthcare             | 12                  |
| Communication Services | 8                   |
| Utilities              | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.57         | -79.5          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.49         | -78.3          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.67         | -74.8          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.25         | -73.7          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.81         | -72.0          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.09         | -68.3          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.31         | -66.0          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.71         | -59.5          |

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
| COH  | Cochlear               | -68.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.4                   |
| Information Technology | 46.63                  |
| Financials             | 45.54                  |
| Energy                 | 41.93                  |
| Healthcare             | 36.15                  |
| Consumer Staples       | 32.4                   |
| Consumer Discretionary | 28.19                  |
| Communication Services | 27.93                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 7.4            | 28.5               | 0.26                 |
| Industrials            | 8.4            | 37.2               | 0.23                 |
| Materials              | 9.7            | 49.7               | 0.19                 |
| Energy                 | 5.7            | 42.0               | 0.14                 |
| Financials             | 2.4            | 31.1               | 0.08                 |
| Utilities              | 1.8            | 28.0               | 0.06                 |
| Healthcare             | -3.3           | 42.4               | -0.08                |
| Information Technology | -9.3           | 55.8               | -0.17                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 171.76       |
| BHP  | BHP                    | Materials              | 260.3            | 59.61        |
| WBC  | Westpac                | Financials             | 136.3            | 38.01        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.6         |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 81.03        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 246.82       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.77        |
| CSL  | CSL                    | Healthcare             | 67.4             | 204.54       |
