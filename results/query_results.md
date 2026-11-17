# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Consumer Staples       | 7         | 8.41              | 53.16    | -16.24    |
| Industrials            | 23        | 6.4               | 74.91    | -59.23    |
| Utilities              | 7         | 3.87              | 30.96    | -13.32    |
| Materials              | 47        | 2.41              | 74.5     | -65.58    |
| Financials             | 36        | 1.95              | 40.05    | -54.16    |
| Energy                 | 11        | 0.39              | 50.3     | -56.71    |
| Healthcare             | 16        | -4.1              | 73.79    | -53.01    |
| Information Technology | 7         | -6.61             | 57.88    | -40.73    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | REH  | Reece Group          | Industrials            | 74.9                |
| 2    | ALK  | Alkane Resources     | Materials              | 74.5                |
| 3    | RHC  | Ramsay Health Care   | Healthcare             | 73.8                |
| 4    | CDA  | Codan                | Information Technology | 57.9                |
| 5    | JHX  | James Hardie         | Materials              | 57.6                |
| 6    | BSL  | BlueScope            | Materials              | 56.9                |
| 7    | WOW  | Woolworths Group     | Consumer Staples       | 53.2                |
| 8    | PDI  | Predictive Discovery | Materials              | 50.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.0                 |
| CTD  | 254          | 96.9                  |
| EOS  | 254          | 94.7                  |
| DRO  | 254          | 89.6                  |
| ZIP  | 254          | 87.9                  |
| TUA  | 254          | 86.3                  |
| OBM  | 254          | 80.2                  |
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
| Financials             | 23                  |
| Real Estate            | 15                  |
| Industrials            | 14                  |
| Consumer Discretionary | 12                  |
| Healthcare             | 11                  |
| Materials              | 9                   |
| Communication Services | 8                   |
| Utilities              | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.47         | -80.8          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.38         | -79.0          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.06         | -77.6          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.6          | -77.3          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.71         | -75.6          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.82         | -72.3          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.13         | -68.7          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.61         | -65.2          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| DRO  | Droneshield            | -77.6            |
| LTR  | Liontown Resources     | -77.3            |
| DYL  | Deep Yellow            | -76.8            |
| CIA  | Champion Iron          | -73.2            |
| 4DX  | 4DMedical              | -68.7            |
| COH  | Cochlear               | -67.5            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.49                  |
| Information Technology | 46.43                  |
| Financials             | 45.44                  |
| Energy                 | 42.05                  |
| Healthcare             | 36.07                  |
| Consumer Staples       | 32.44                  |
| Communication Services | 27.87                  |
| Consumer Discretionary | 27.86                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 8.4            | 28.5               | 0.3                  |
| Industrials            | 6.4            | 37.0               | 0.17                 |
| Utilities              | 3.9            | 28.1               | 0.14                 |
| Financials             | 2.0            | 31.0               | 0.06                 |
| Materials              | 2.4            | 49.7               | 0.05                 |
| Energy                 | 0.4            | 42.4               | 0.01                 |
| Healthcare             | -4.1           | 42.3               | -0.1                 |
| Information Technology | -6.6           | 55.8               | -0.12                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 170.44       |
| BHP  | BHP                    | Materials              | 260.3            | 54.38        |
| WBC  | Westpac                | Financials             | 136.3            | 37.23        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.49        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.79        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 232.12       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.77        |
| CSL  | CSL                    | Healthcare             | 67.4             | 199.55       |
