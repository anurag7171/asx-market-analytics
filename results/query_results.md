# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Consumer Staples       | 7         | 8.04              | 53.91    | -18.56    |
| Industrials            | 23        | 7.51              | 76.52    | -57.55    |
| Utilities              | 7         | 5.12              | 30.2     | -9.14     |
| Materials              | 47        | 3.64              | 83.29    | -65.24    |
| Financials             | 36        | 3.35              | 42.61    | -55.08    |
| Energy                 | 11        | 2.09              | 46.39    | -54.89    |
| Information Technology | 7         | -2.42             | 64.61    | -39.5     |
| Healthcare             | 16        | -3.49             | 74.73    | -55.03    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | ALK  | Alkane Resources   | Materials              | 83.3                |
| 2    | REH  | Reece Group        | Industrials            | 76.5                |
| 3    | RHC  | Ramsay Health Care | Healthcare             | 74.7                |
| 4    | CDA  | Codan              | Information Technology | 64.6                |
| 5    | BSL  | BlueScope          | Materials              | 58.5                |
| 6    | WOW  | Woolworths Group   | Consumer Staples       | 53.9                |
| 7    | VEA  | Viva Energy        | Energy                 | 46.4                |
| 8    | 4DX  | 4DMedical          | Healthcare             | 44.8                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 105.9                 |
| CTD  | 254          | 97.0                  |
| EOS  | 254          | 94.5                  |
| DRO  | 254          | 89.5                  |
| ZIP  | 254          | 87.7                  |
| TUA  | 254          | 86.5                  |
| OBM  | 254          | 80.6                  |
| NXT  | 254          | 79.4                  |

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
| Industrials            | 12                  |
| Consumer Discretionary | 11                  |
| Healthcare             | 10                  |
| Communication Services | 8                   |
| Utilities              | 7                   |
| Materials              | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.38         | -82.0          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.18         | -80.2          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.04         | -78.1          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.59         | -77.7          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.71         | -75.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.75         | -73.4          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.15         | -68.4          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.59         | -66.3          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| DRO  | Droneshield            | -78.1            |
| LTR  | Liontown Resources     | -77.7            |
| DYL  | Deep Yellow            | -76.8            |
| CIA  | Champion Iron          | -73.4            |
| 4DX  | 4DMedical              | -68.7            |
| COH  | Cochlear               | -67.5            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.56                  |
| Information Technology | 46.47                  |
| Financials             | 45.51                  |
| Energy                 | 42.1                   |
| Healthcare             | 36.09                  |
| Consumer Staples       | 32.43                  |
| Consumer Discretionary | 27.87                  |
| Communication Services | 27.87                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 8.0            | 28.5               | 0.28                 |
| Industrials            | 7.5            | 36.9               | 0.2                  |
| Utilities              | 5.1            | 28.1               | 0.18                 |
| Financials             | 3.4            | 30.9               | 0.11                 |
| Materials              | 3.6            | 49.6               | 0.07                 |
| Energy                 | 2.1            | 42.3               | 0.05                 |
| Information Technology | -2.4           | 55.3               | -0.04                |
| Healthcare             | -3.5           | 42.3               | -0.08                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 170.88       |
| BHP  | BHP                    | Materials              | 260.3            | 54.34        |
| WBC  | Westpac                | Financials             | 136.3            | 36.82        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.02        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.18        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 230.52       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.04        |
| CSL  | CSL                    | Healthcare             | 67.4             | 199.38       |
