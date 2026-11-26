# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Utilities              | 7         | 4.6               | 29.46    | -14.43    |
| Industrials            | 23        | 4.13              | 58.22    | -50.46    |
| Consumer Staples       | 7         | 3.19              | 51.04    | -32.3     |
| Financials             | 36        | 1.27              | 41.08    | -61.28    |
| Energy                 | 11        | 0.1               | 36.45    | -61.37    |
| Materials              | 47        | -1.75             | 66.03    | -68.89    |
| Information Technology | 7         | -5.94             | 59.57    | -51.81    |
| Healthcare             | 16        | -9.19             | 39.37    | -53.01    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | ALK  | Alkane Resources       | Materials              | 66.0                |
| 2    | CDA  | Codan                  | Information Technology | 59.6                |
| 3    | REH  | Reece Group            | Industrials            | 58.2                |
| 4    | WOW  | Woolworths Group       | Consumer Staples       | 51.0                |
| 5    | BSL  | BlueScope              | Materials              | 47.4                |
| 6    | EOS  | Electro Optic Systems  | Industrials            | 47.3                |
| 7    | JHX  | James Hardie           | Materials              | 43.0                |
| 8    | QBE  | QBE Insurance          | Financials             | 41.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.3                 |
| CTD  | 254          | 98.4                  |
| EOS  | 254          | 94.7                  |
| TUA  | 254          | 92.9                  |
| ZIP  | 253          | 88.4                  |
| DRO  | 254          | 85.3                  |
| OBM  | 254          | 81.2                  |
| NXT  | 254          | 79.8                  |

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
| Financials             | 23                  |
| Industrials            | 16                  |
| Real Estate            | 14                  |
| Healthcare             | 9                   |
| Utilities              | 7                   |
| Consumer Discretionary | 7                   |
| Communication Services | 7                   |
| Materials              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.54         | -79.7          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.62         | -78.7          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.68         | -78.0          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.07         | -77.3          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.74         | -76.7          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.75         | -73.4          |
| LLC  | Lendlease              | Real Estate            | 5.03     | 1.52         | -69.8          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.09         | -69.3          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -79.9            |
| DYL  | Deep Yellow            | -78.7            |
| DRO  | Droneshield            | -78.1            |
| CIA  | Champion Iron          | -75.2            |
| GQG  | GQG Partners           | -70.6            |
| 4DX  | 4DMedical              | -70.1            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.13                  |
| Information Technology | 46.18                  |
| Financials             | 45.55                  |
| Energy                 | 42.3                   |
| Healthcare             | 36.31                  |
| Consumer Staples       | 32.41                  |
| Communication Services | 27.8                   |
| Consumer Discretionary | 27.57                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Utilities              | 4.6            | 28.1               | 0.16                 |
| Industrials            | 4.1            | 36.8               | 0.11                 |
| Consumer Staples       | 3.2            | 28.8               | 0.11                 |
| Financials             | 1.3            | 30.9               | 0.04                 |
| Energy                 | 0.1            | 42.4               | 0.0                  |
| Materials              | -1.7           | 49.7               | -0.04                |
| Information Technology | -5.9           | 55.3               | -0.11                |
| Healthcare             | -9.2           | 42.2               | -0.22                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 169.99       |
| BHP  | BHP                    | Materials              | 260.3            | 53.99        |
| WBC  | Westpac                | Financials             | 136.3            | 35.72        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.81        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.64        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 226.45       |
| NAB  | National Australia Ban | Financials             | 69.8             | 36.24        |
| CSL  | CSL                    | Healthcare             | 67.4             | 208.82       |
