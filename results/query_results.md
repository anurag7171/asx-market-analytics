# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 27.47             | 120.48   | -32.68    |
| Energy           | 11        | 17.07             | 78.4     | -35.81    |
| Industrials      | 23        | 5.98              | 78.99    | -56.13    |
| Financials       | 36        | -0.96             | 73.62    | -59.81    |
| Consumer Staples | 7         | -1.1              | 47.22    | -24.51    |
| Utilities        | 7         | -1.11             | 27.35    | -11.51    |
| Healthcare       | 16        | -1.88             | 128.57   | -48.99    |
| Real Estate      | 16        | -20.27            | 0.47     | -58.5     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare             | 128.6               |
| 2    | PDI  | Predictive Discovery | Materials              | 120.5               |
| 3    | S32  | South32              | Materials              | 91.6                |
| 4    | SGM  | Sims Metal           | Materials              | 81.0                |
| 5    | NWH  | NRW Holdings         | Industrials            | 79.0                |
| 6    | CDA  | Codan                | Information Technology | 78.6                |
| 7    | VEA  | Viva Energy          | Energy                 | 78.4                |
| 8    | RHC  | Ramsay Health Care   | Healthcare             | 75.9                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 105.7                 |
| DRO  | 254          | 103.4                 |
| EOS  | 254          | 99.0                  |
| CTD  | 254          | 89.1                  |
| ZIP  | 254          | 80.3                  |
| TUA  | 254          | 79.3                  |
| LTR  | 254          | 77.6                  |
| OBM  | 254          | 77.2                  |

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
| Financials             | 11                  |
| Industrials            | 9                   |
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
| WTC  | Wisetech Global        | Information Technology | 94.14    | 31.33        | -66.7          |
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
| WTC  | Wisetech Global        | -69.6            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -65.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.66                  |
| Information Technology | 44.86                  |
| Financials             | 44.08                  |
| Energy                 | 40.81                  |
| Healthcare             | 36.13                  |
| Consumer Staples       | 32.24                  |
| Consumer Discretionary | 27.7                   |
| Communication Services | 27.32                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 27.5           | 48.7               | 0.56                 |
| Energy                 | 17.1           | 41.3               | 0.41                 |
| Industrials            | 6.0            | 36.4               | 0.16                 |
| Financials             | -1.0           | 30.8               | -0.03                |
| Utilities              | -1.1           | 27.6               | -0.04                |
| Healthcare             | -1.9           | 42.2               | -0.04                |
| Consumer Staples       | -1.1           | 28.3               | -0.04                |
| Information Technology | -22.4          | 48.5               | -0.46                |

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
