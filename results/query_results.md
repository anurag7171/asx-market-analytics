# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 23.34             | 124.37   | -32.33    |
| Energy                 | 11        | 19.93             | 83.98    | -40.31    |
| Industrials            | 23        | 4.68              | 77.28    | -63.52    |
| Consumer Staples       | 7         | 0.57              | 50.57    | -22.77    |
| Utilities              | 7         | 0.35              | 26.68    | -10.13    |
| Financials             | 36        | -0.36             | 72.87    | -60.27    |
| Healthcare             | 16        | -1.58             | 114.65   | -48.89    |
| Information Technology | 7         | -15.72            | 125.66   | -64.43    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | CDA  | Codan                | Information Technology | 125.7               |
| 2    | PDI  | Predictive Discovery | Materials              | 124.4               |
| 3    | 4DX  | 4DMedical            | Healthcare             | 114.6               |
| 4    | S32  | South32              | Materials              | 89.8                |
| 5    | VEA  | Viva Energy          | Energy                 | 84.0                |
| 6    | SGM  | Sims Metal           | Materials              | 81.5                |
| 7    | RHC  | Ramsay Health Care   | Healthcare             | 78.8                |
| 8    | NWH  | NRW Holdings         | Industrials            | 77.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 105.4                 |
| DRO  | 254          | 101.8                 |
| EOS  | 254          | 97.8                  |
| CTD  | 254          | 89.3                  |
| ZIP  | 254          | 80.3                  |
| TUA  | 254          | 79.4                  |
| LTR  | 254          | 77.7                  |
| OBM  | 254          | 77.3                  |

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
| Materials              | 16                  |
| Financials             | 14                  |
| Industrials            | 11                  |
| Healthcare             | 7                   |
| Energy                 | 5                   |
| Consumer Staples       | 4                   |
| Consumer Discretionary | 3                   |
| Communication Services | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.46         | -84.7          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.71         | -77.6          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.7          | -74.2          |
| 360  | Life360                | Information Technology | 55.44    | 18.93        | -65.9          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.93         | -64.8          |
| XRO  | Xero                   | Information Technology | 160.95   | 56.92        | -64.6          |
| WTC  | Wisetech Global        | Information Technology | 90.31    | 32.46        | -64.1          |
| GDG  | Generation Development | Financials             | 7.56     | 2.75         | -63.6          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -77.7            |
| DRO  | Droneshield            | -76.1            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| WTC  | Wisetech Global        | -68.3            |
| 360  | Life360                | -67.7            |
| LTR  | Liontown Resources     | -65.7            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.53                  |
| Information Technology | 44.96                  |
| Financials             | 44.16                  |
| Energy                 | 40.83                  |
| Healthcare             | 35.98                  |
| Consumer Staples       | 32.22                  |
| Consumer Discretionary | 27.75                  |
| Communication Services | 27.36                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 23.3           | 48.7               | 0.48                 |
| Energy                 | 19.9           | 41.4               | 0.48                 |
| Industrials            | 4.7            | 36.4               | 0.13                 |
| Consumer Staples       | 0.6            | 28.3               | 0.02                 |
| Utilities              | 0.4            | 27.7               | 0.01                 |
| Financials             | -0.4           | 30.8               | -0.01                |
| Healthcare             | -1.6           | 42.2               | -0.04                |
| Information Technology | -15.7          | 49.3               | -0.32                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 151.01       |
| BHP  | BHP                    | Materials              | 260.3            | 60.82        |
| WBC  | Westpac                | Financials             | 136.3            | 35.07        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.31        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 76.61        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 246.1        |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.15        |
| CSL  | CSL                    | Healthcare             | 67.4             | 184.22       |
