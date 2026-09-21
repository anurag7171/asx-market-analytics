# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 30.15             | 137.07   | -30.51    |
| Energy           | 11        | 22.5              | 83.91    | -33.91    |
| Industrials      | 23        | 6.36              | 78.44    | -48.49    |
| Utilities        | 7         | 2.41              | 29.5     | -8.74     |
| Financials       | 36        | -0.67             | 69.16    | -57.29    |
| Healthcare       | 16        | -0.96             | 171.29   | -50.78    |
| Consumer Staples | 7         | -3.3              | 43.18    | -26.78    |
| Real Estate      | 16        | -18.83            | 1.34     | -57.58    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 171.3               |
| 2    | PDI  | Predictive Discovery | Materials   | 137.1               |
| 3    | S32  | South32              | Materials   | 91.0                |
| 4    | VEA  | Viva Energy          | Energy      | 83.9                |
| 5    | PLS  | PLS Group            | Materials   | 82.0                |
| 6    | SGM  | Sims Metal           | Materials   | 80.2                |
| 7    | NWH  | NRW Holdings         | Industrials | 78.4                |
| 8    | SFR  | Sandfire Resources   | Materials   | 77.9                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 106.7                 |
| DRO  | 253          | 104.0                 |
| EOS  | 253          | 98.8                  |
| CTD  | 253          | 88.7                  |
| ZIP  | 253          | 79.7                  |
| OBM  | 253          | 77.5                  |
| LTR  | 253          | 77.3                  |
| TUA  | 253          | 76.1                  |

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
| Materials              | 23                  |
| Financials             | 14                  |
| Industrials            | 8                   |
| Healthcare             | 7                   |
| Energy                 | 6                   |
| Utilities              | 5                   |
| Communication Services | 3                   |
| Information Technology | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.57         | -84.0          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.71         | -74.2          |
| TUA  | Tuas                   | Communication Services | 7.64     | 2.31         | -69.8          |
| WTC  | Wisetech Global        | Information Technology | 96.25    | 31.77        | -67.0          |
| 360  | Life360                | Information Technology | 55.44    | 18.68        | -66.3          |
| XRO  | Xero                   | Information Technology | 163.97   | 60.08        | -63.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.03         | -61.0          |
| GDG  | Generation Development | Financials             | 7.56     | 3.02         | -60.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| DRO  | Droneshield            | -75.8            |
| TUA  | Tuas                   | -73.8            |
| WTC  | Wisetech Global        | -70.2            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.76                  |
| Information Technology | 44.91                  |
| Financials             | 44.14                  |
| Energy                 | 40.81                  |
| Healthcare             | 36.31                  |
| Consumer Staples       | 32.32                  |
| Consumer Discretionary | 27.68                  |
| Communication Services | 27.3                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 30.2           | 48.8               | 0.62                 |
| Energy                 | 22.5           | 41.3               | 0.54                 |
| Industrials            | 6.4            | 36.5               | 0.17                 |
| Utilities              | 2.4            | 27.5               | 0.09                 |
| Healthcare             | -1.0           | 42.4               | -0.02                |
| Financials             | -0.7           | 30.7               | -0.02                |
| Consumer Staples       | -3.3           | 28.4               | -0.12                |
| Information Technology | -24.6          | 48.5               | -0.51                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 152.99       |
| BHP  | BHP                    | Materials              | 260.3            | 60.78        |
| WBC  | Westpac                | Financials             | 136.3            | 34.93        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.03        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 72.74        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 241.54       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.72        |
| CSL  | CSL                    | Healthcare             | 67.4             | 178.3        |
