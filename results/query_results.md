# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 11.61             | 66.81    | -61.91    |
| Consumer Staples | 7         | 10.03             | 54.49    | -19.74    |
| Industrials      | 23        | 5.51              | 66.49    | -62.5     |
| Energy           | 11        | 5.15              | 54.69    | -50.97    |
| Utilities        | 7         | 1.83              | 28.56    | -10.27    |
| Financials       | 36        | 0.86              | 42.2     | -53.49    |
| Healthcare       | 16        | -2.95             | 83.74    | -51.38    |
| Real Estate      | 16        | -11.09            | 2.97     | -50.6     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 83.7                |
| 2    | ALK  | Alkane Resources     | Materials              | 66.8                |
| 3    | PDI  | Predictive Discovery | Materials              | 66.7                |
| 4    | REH  | Reece Group          | Industrials            | 66.5                |
| 5    | CDA  | Codan                | Information Technology | 62.6                |
| 6    | BSL  | BlueScope            | Materials              | 56.3                |
| 7    | 4DX  | 4DMedical            | Healthcare             | 55.6                |
| 8    | VEA  | Viva Energy          | Energy                 | 54.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 107.2                 |
| CTD  | 254          | 96.7                  |
| DRO  | 254          | 95.4                  |
| EOS  | 254          | 94.9                  |
| ZIP  | 254          | 88.2                  |
| TUA  | 254          | 86.1                  |
| OBM  | 254          | 79.8                  |
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
| Financials             | 25                  |
| Real Estate            | 16                  |
| Industrials            | 14                  |
| Consumer Discretionary | 13                  |
| Materials              | 12                  |
| Healthcare             | 11                  |
| Communication Services | 7                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.46         | -80.9          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.64         | -77.3          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.65         | -75.6          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.76         | -74.1          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.27         | -73.1          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.06         | -68.7          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.28         | -66.5          |
| CYL  | Catalyst Metals        | Materials              | 9.64     | 4.08         | -57.7          |

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
| Materials              | 49.3                   |
| Information Technology | 46.29                  |
| Financials             | 44.83                  |
| Energy                 | 41.8                   |
| Healthcare             | 36.09                  |
| Consumer Staples       | 32.26                  |
| Consumer Discretionary | 28.15                  |
| Communication Services | 27.93                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 10.0           | 28.7               | 0.35                 |
| Materials              | 11.6           | 49.6               | 0.23                 |
| Industrials            | 5.5            | 36.8               | 0.15                 |
| Energy                 | 5.1            | 41.9               | 0.12                 |
| Utilities              | 1.8            | 28.0               | 0.07                 |
| Financials             | 0.9            | 31.1               | 0.03                 |
| Healthcare             | -3.0           | 42.5               | -0.07                |
| Information Technology | -13.7          | 55.7               | -0.25                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 167.51       |
| BHP  | BHP                    | Materials              | 260.3            | 57.62        |
| WBC  | Westpac                | Financials             | 136.3            | 37.03        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 40.34        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 81.33        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.86       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.0         |
| CSL  | CSL                    | Healthcare             | 67.4             | 202.04       |
