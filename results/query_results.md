# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 31.08             | 138.55   | -30.42    |
| Energy           | 11        | 20.33             | 80.26    | -32.84    |
| Industrials      | 23        | 5.83              | 78.93    | -54.38    |
| Financials       | 36        | -0.9              | 79.55    | -57.31    |
| Healthcare       | 16        | -0.96             | 172.91   | -50.73    |
| Utilities        | 7         | -0.99             | 28.98    | -11.29    |
| Consumer Staples | 7         | -3.08             | 43.54    | -26.69    |
| Real Estate      | 16        | -18.41            | 1.06     | -58.22    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare             | 172.9               |
| 2    | PDI  | Predictive Discovery | Materials              | 138.6               |
| 3    | S32  | South32              | Materials              | 94.8                |
| 4    | PLS  | PLS Group            | Materials              | 84.2                |
| 5    | SFR  | Sandfire Resources   | Materials              | 83.8                |
| 6    | SGM  | Sims Metal           | Materials              | 83.7                |
| 7    | VEA  | Viva Energy          | Energy                 | 80.3                |
| 8    | CDA  | Codan                | Information Technology | 79.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.6                 |
| DRO  | 254          | 103.6                 |
| EOS  | 254          | 99.0                  |
| CTD  | 254          | 89.0                  |
| ZIP  | 254          | 79.6                  |
| TUA  | 254          | 79.3                  |
| OBM  | 254          | 77.2                  |
| LTR  | 254          | 77.2                  |

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
| Materials              | 26                  |
| Financials             | 12                  |
| Industrials            | 9                   |
| Healthcare             | 8                   |
| Energy                 | 4                   |
| Communication Services | 3                   |
| Utilities              | 2                   |
| Information Technology | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.57         | -84.0          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.78         | -76.6          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.61         | -75.5          |
| WTC  | Wisetech Global        | Information Technology | 95.91    | 32.34        | -66.3          |
| 360  | Life360                | Information Technology | 55.44    | 19.23        | -65.3          |
| XRO  | Xero                   | Information Technology | 163.97   | 58.2         | -64.5          |
| GDG  | Generation Development | Financials             | 7.56     | 2.98         | -60.6          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.05         | -60.2          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -76.6            |
| DRO  | Droneshield            | -75.8            |
| WTC  | Wisetech Global        | -70.1            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.69                  |
| Information Technology | 44.91                  |
| Financials             | 44.11                  |
| Energy                 | 40.79                  |
| Healthcare             | 36.24                  |
| Consumer Staples       | 32.29                  |
| Consumer Discretionary | 27.69                  |
| Communication Services | 27.33                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 31.1           | 48.8               | 0.64                 |
| Energy                 | 20.3           | 41.3               | 0.49                 |
| Industrials            | 5.8            | 36.5               | 0.16                 |
| Healthcare             | -1.0           | 42.3               | -0.02                |
| Financials             | -0.9           | 30.7               | -0.03                |
| Utilities              | -1.0           | 27.5               | -0.04                |
| Consumer Staples       | -3.1           | 28.4               | -0.11                |
| Information Technology | -22.0          | 48.5               | -0.45                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 151.05       |
| BHP  | BHP                    | Materials              | 260.3            | 62.07        |
| WBC  | Westpac                | Financials             | 136.3            | 34.76        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.83        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 73.79        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 242.35       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.66        |
| CSL  | CSL                    | Healthcare             | 67.4             | 179.24       |
