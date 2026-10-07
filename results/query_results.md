# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Energy                 | 11        | 18.07             | 82.75    | -44.36    |
| Materials              | 47        | 15.64             | 76.92    | -35.17    |
| Industrials            | 23        | 2.88              | 78.92    | -72.11    |
| Consumer Staples       | 7         | 1.83              | 49.55    | -22.9     |
| Utilities              | 7         | -0.67             | 25.48    | -10.78    |
| Financials             | 36        | -2.67             | 75.97    | -63.24    |
| Healthcare             | 16        | -7.22             | 76.55    | -53.84    |
| Information Technology | 7         | -18.49            | 107.88   | -64.51    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | CDA  | Codan                | Information Technology | 107.9               |
| 2    | VEA  | Viva Energy          | Energy                 | 82.8                |
| 3    | NWH  | NRW Holdings         | Industrials            | 78.9                |
| 4    | PDI  | Predictive Discovery | Materials              | 76.9                |
| 5    | 4DX  | 4DMedical            | Healthcare             | 76.5                |
| 6    | L1G  | L1 Group             | Financials             | 76.0                |
| 7    | S32  | South32              | Materials              | 75.4                |
| 8    | RHC  | Ramsay Health Care   | Healthcare             | 75.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 103.5                 |
| DRO  | 255          | 97.6                  |
| EOS  | 255          | 96.7                  |
| CTD  | 255          | 89.7                  |
| ZIP  | 255          | 80.1                  |
| TUA  | 255          | 79.3                  |
| LTR  | 255          | 77.7                  |
| OBM  | 255          | 76.7                  |

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
| Materials              | 11                  |
| Industrials            | 10                  |
| Financials             | 7                   |
| Healthcare             | 6                   |
| Energy                 | 4                   |
| Consumer Staples       | 3                   |
| Consumer Discretionary | 3                   |
| Communication Services | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.2          | -86.3          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.66         | -78.3          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.69         | -74.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.82         | -68.9          |
| GDG  | Generation Development | Financials             | 7.56     | 2.65         | -64.9          |
| 360  | Life360                | Information Technology | 54.86    | 19.47        | -64.5          |
| XRO  | Xero                   | Information Technology | 157.46   | 56.1         | -64.4          |
| WTC  | Wisetech Global        | Information Technology | 85.37    | 32.09        | -62.4          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -78.3            |
| DRO  | Droneshield            | -76.1            |
| LTR  | Liontown Resources     | -70.1            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.4            |
| WTC  | Wisetech Global        | -66.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.34                  |
| Information Technology | 44.77                  |
| Financials             | 44.14                  |
| Energy                 | 40.75                  |
| Healthcare             | 35.81                  |
| Consumer Staples       | 32.04                  |
| Consumer Discretionary | 27.8                   |
| Communication Services | 27.25                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 18.1           | 41.4               | 0.44                 |
| Materials              | 15.6           | 48.5               | 0.32                 |
| Industrials            | 2.9            | 36.2               | 0.08                 |
| Consumer Staples       | 1.8            | 28.4               | 0.06                 |
| Utilities              | -0.7           | 27.6               | -0.02                |
| Financials             | -2.7           | 30.8               | -0.09                |
| Healthcare             | -7.2           | 41.9               | -0.17                |
| Information Technology | -18.5          | 49.4               | -0.37                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 150.37       |
| BHP  | BHP                    | Materials              | 260.3            | 62.45        |
| WBC  | Westpac                | Financials             | 136.3            | 34.24        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.95        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 76.3         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.77       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.4         |
| CSL  | CSL                    | Healthcare             | 67.4             | 181.99       |
