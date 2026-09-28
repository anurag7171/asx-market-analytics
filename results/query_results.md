# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 25.06             | 125.85   | -31.22    |
| Energy           | 11        | 17.58             | 80.34    | -35.31    |
| Industrials      | 23        | 3.97              | 75.17    | -63.41    |
| Utilities        | 7         | -0.41             | 26.78    | -10.15    |
| Consumer Staples | 7         | -1.24             | 46.67    | -23.55    |
| Healthcare       | 16        | -1.4              | 122.22   | -47.9     |
| Financials       | 36        | -1.9              | 73.62    | -60.21    |
| Real Estate      | 16        | -20.32            | 0.2      | -57.63    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials              | 125.9               |
| 2    | 4DX  | 4DMedical            | Healthcare             | 122.2               |
| 3    | S32  | South32              | Materials              | 91.6                |
| 4    | SGM  | Sims Metal           | Materials              | 80.6                |
| 5    | VEA  | Viva Energy          | Energy                 | 80.3                |
| 6    | CDA  | Codan                | Information Technology | 79.1                |
| 7    | RHC  | Ramsay Health Care   | Healthcare             | 78.5                |
| 8    | NWH  | NRW Holdings         | Industrials            | 75.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 252          | 106.1                 |
| DRO  | 252          | 102.2                 |
| EOS  | 252          | 98.2                  |
| CTD  | 252          | 89.5                  |
| ZIP  | 252          | 80.6                  |
| TUA  | 252          | 79.6                  |
| LTR  | 252          | 77.8                  |
| OBM  | 252          | 77.3                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |
| TPG  | TPG Telecom            | 2025-11-13 | -32.1          |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Materials              | 20                  |
| Industrials            | 9                   |
| Financials             | 9                   |
| Healthcare             | 7                   |
| Energy                 | 4                   |
| Information Technology | 2                   |
| Consumer Staples       | 2                   |
| Consumer Discretionary | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.42         | -84.9          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.78         | -76.7          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.61         | -75.6          |
| WTC  | Wisetech Global        | Information Technology | 92.48    | 31.33        | -66.1          |
| 360  | Life360                | Information Technology | 55.44    | 19.32        | -65.2          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.94         | -64.4          |
| XRO  | Xero                   | Information Technology | 160.95   | 57.36        | -64.4          |
| GDG  | Generation Development | Financials             | 7.56     | 2.75         | -63.6          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -76.7            |
| DRO  | Droneshield            | -75.8            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| WTC  | Wisetech Global        | -69.0            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -65.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.55                  |
| Information Technology | 44.87                  |
| Financials             | 44.08                  |
| Energy                 | 40.8                   |
| Healthcare             | 36.02                  |
| Consumer Staples       | 32.26                  |
| Consumer Discretionary | 27.72                  |
| Communication Services | 27.34                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 25.1           | 48.8               | 0.51                 |
| Energy                 | 17.6           | 41.4               | 0.42                 |
| Industrials            | 4.0            | 36.4               | 0.11                 |
| Utilities              | -0.4           | 27.6               | -0.02                |
| Healthcare             | -1.4           | 42.2               | -0.03                |
| Consumer Staples       | -1.2           | 28.4               | -0.04                |
| Financials             | -1.9           | 30.8               | -0.06                |
| Information Technology | -22.2          | 48.7               | -0.46                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 150.83       |
| BHP  | BHP                    | Materials              | 260.3            | 60.72        |
| WBC  | Westpac                | Financials             | 136.3            | 34.49        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.84        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 73.61        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 239.53       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.54        |
| CSL  | CSL                    | Healthcare             | 67.4             | 176.95       |
