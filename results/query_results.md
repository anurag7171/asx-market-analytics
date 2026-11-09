# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 12.41             | 75.56    | -60.1     |
| Consumer Staples       | 7         | 9.38              | 55.34    | -21.2     |
| Energy                 | 11        | 5.56              | 50.6     | -49.55    |
| Industrials            | 23        | 4.14              | 67.33    | -61.35    |
| Utilities              | 7         | 1.58              | 25.98    | -13.33    |
| Financials             | 36        | 0.52              | 37.48    | -51.78    |
| Healthcare             | 16        | -3.75             | 84.68    | -49.05    |
| Information Technology | 7         | -12.2             | 66.54    | -53.79    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 84.7                |
| 2    | ALK  | Alkane Resources     | Materials              | 75.6                |
| 3    | PDI  | Predictive Discovery | Materials              | 71.9                |
| 4    | REH  | Reece Group          | Industrials            | 67.3                |
| 5    | CDA  | Codan                | Information Technology | 66.5                |
| 6    | BSL  | BlueScope            | Materials              | 59.5                |
| 7    | JHX  | James Hardie         | Materials              | 58.3                |
| 8    | WOW  | Woolworths Group     | Consumer Staples       | 55.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 106.5                 |
| CTD  | 253          | 96.9                  |
| DRO  | 253          | 95.4                  |
| EOS  | 253          | 95.1                  |
| ZIP  | 253          | 88.0                  |
| TUA  | 253          | 86.2                  |
| OBM  | 253          | 79.8                  |
| NXT  | 253          | 79.7                  |

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
| Materials              | 22                  |
| Real Estate            | 14                  |
| Industrials            | 14                  |
| Consumer Discretionary | 13                  |
| Healthcare             | 11                  |
| Communication Services | 7                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.46         | -81.0          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.55         | -77.9          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.68         | -74.4          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.26         | -73.4          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.83         | -71.3          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.1          | -68.1          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.34         | -65.6          |
| PLS  | PLS Group              | Materials              | 6.68     | 2.89         | -56.7          |

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
| Materials              | 49.36                  |
| Information Technology | 46.39                  |
| Financials             | 45.48                  |
| Energy                 | 41.88                  |
| Healthcare             | 36.11                  |
| Consumer Staples       | 32.35                  |
| Consumer Discretionary | 28.13                  |
| Communication Services | 27.96                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 9.4            | 28.7               | 0.33                 |
| Materials              | 12.4           | 49.7               | 0.25                 |
| Energy                 | 5.6            | 42.0               | 0.13                 |
| Industrials            | 4.1            | 36.9               | 0.11                 |
| Utilities              | 1.6            | 28.0               | 0.06                 |
| Financials             | 0.5            | 31.0               | 0.02                 |
| Healthcare             | -3.7           | 42.5               | -0.09                |
| Information Technology | -12.2          | 55.7               | -0.22                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 165.97       |
| BHP  | BHP                    | Materials              | 260.3            | 59.2         |
| WBC  | Westpac                | Financials             | 136.3            | 36.81        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.05        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 80.2         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 247.94       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.45        |
| CSL  | CSL                    | Healthcare             | 67.4             | 200.77       |
