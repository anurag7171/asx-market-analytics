# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Utilities              | 7         | 4.82              | 28.33    | -14.26    |
| Industrials            | 23        | 4.43              | 58.48    | -44.0     |
| Energy                 | 11        | 4.03              | 43.27    | -57.1     |
| Consumer Staples       | 7         | 3.04              | 50.69    | -34.2     |
| Financials             | 36        | 1.59              | 47.26    | -63.44    |
| Materials              | 47        | 0.74              | 71.7     | -68.48    |
| Information Technology | 7         | -4.56             | 63.93    | -49.07    |
| Healthcare             | 16        | -8.21             | 44.1     | -53.65    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | ALK  | Alkane Resources       | Materials              | 71.7                |
| 2    | CDA  | Codan                  | Information Technology | 63.9                |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 58.5                |
| 4    | REH  | Reece Group            | Industrials            | 52.0                |
| 5    | WOW  | Woolworths Group       | Consumer Staples       | 50.7                |
| 6    | BSL  | BlueScope              | Materials              | 48.9                |
| 7    | QBE  | QBE Insurance          | Financials             | 47.3                |
| 8    | JHX  | James Hardie           | Materials              | 44.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.8                 |
| CTD  | 254          | 98.4                  |
| EOS  | 254          | 94.7                  |
| TUA  | 254          | 92.9                  |
| ZIP  | 253          | 88.4                  |
| DRO  | 254          | 85.0                  |
| OBM  | 254          | 81.5                  |
| NXT  | 254          | 79.9                  |

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
| Industrials            | 15                  |
| Real Estate            | 14                  |
| Materials              | 10                  |
| Healthcare             | 9                   |
| Consumer Discretionary | 8                   |
| Communication Services | 8                   |
| Utilities              | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.57         | -78.2          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.68         | -78.1          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.68         | -76.6          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.79         | -76.4          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.12         | -76.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.77         | -73.0          |
| LLC  | Lendlease              | Real Estate            | 5.03     | 1.57         | -68.7          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.58         | -66.6          |

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
| Materials              | 49.08                  |
| Information Technology | 46.27                  |
| Financials             | 45.51                  |
| Energy                 | 42.3                   |
| Healthcare             | 36.28                  |
| Consumer Staples       | 32.36                  |
| Communication Services | 27.76                  |
| Consumer Discretionary | 27.49                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Utilities              | 4.8            | 28.1               | 0.17                 |
| Industrials            | 4.4            | 36.8               | 0.12                 |
| Consumer Staples       | 3.0            | 28.8               | 0.11                 |
| Energy                 | 4.0            | 42.5               | 0.09                 |
| Financials             | 1.6            | 30.9               | 0.05                 |
| Materials              | 0.7            | 49.8               | 0.01                 |
| Information Technology | -4.6           | 55.5               | -0.08                |
| Healthcare             | -8.2           | 42.2               | -0.19                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 169.29       |
| BHP  | BHP                    | Materials              | 260.3            | 55.06        |
| WBC  | Westpac                | Financials             | 136.3            | 35.74        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.98        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.12        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 230.77       |
| NAB  | National Australia Ban | Financials             | 69.8             | 36.33        |
| CSL  | CSL                    | Healthcare             | 67.4             | 206.88       |
