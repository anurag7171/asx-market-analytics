# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Energy                 | 11        | 17.49             | 82.32    | -46.02    |
| Materials              | 47        | 16.25             | 92.5     | -36.77    |
| Industrials            | 23        | 2.46              | 79.02    | -72.5     |
| Consumer Staples       | 7         | 1.29              | 48.14    | -22.25    |
| Utilities              | 7         | -1.29             | 24.99    | -10.07    |
| Financials             | 36        | -2.61             | 77.29    | -62.71    |
| Healthcare             | 16        | -7.11             | 80.89    | -53.23    |
| Information Technology | 7         | -17.08            | 118.34   | -64.67    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | CDA  | Codan                | Information Technology | 118.3               |
| 2    | PDI  | Predictive Discovery | Materials              | 92.5                |
| 3    | S32  | South32              | Materials              | 84.0                |
| 4    | VEA  | Viva Energy          | Energy                 | 82.3                |
| 5    | 4DX  | 4DMedical            | Healthcare             | 80.9                |
| 6    | SGM  | Sims Metal           | Materials              | 79.5                |
| 7    | NWH  | NRW Holdings         | Industrials            | 79.0                |
| 8    | L1G  | L1 Group             | Financials             | 77.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 103.5                 |
| DRO  | 255          | 97.7                  |
| EOS  | 255          | 96.8                  |
| CTD  | 255          | 89.7                  |
| ZIP  | 255          | 80.0                  |
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
| Materials              | 12                  |
| Financials             | 11                  |
| Industrials            | 10                  |
| Healthcare             | 6                   |
| Energy                 | 4                   |
| Consumer Staples       | 3                   |
| Consumer Discretionary | 3                   |
| Communication Services | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.22         | -86.2          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.69         | -77.9          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.73         | -73.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.83         | -68.6          |
| GDG  | Generation Development | Financials             | 7.56     | 2.67         | -64.7          |
| XRO  | Xero                   | Information Technology | 157.69   | 55.71        | -64.7          |
| WTC  | Wisetech Global        | Information Technology | 87.8     | 31.9         | -63.7          |
| 360  | Life360                | Information Technology | 54.86    | 20.12        | -63.3          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -78.1            |
| DRO  | Droneshield            | -76.1            |
| LTR  | Liontown Resources     | -70.1            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.4            |
| WTC  | Wisetech Global        | -67.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.32                  |
| Information Technology | 44.75                  |
| Financials             | 44.13                  |
| Energy                 | 40.69                  |
| Healthcare             | 35.73                  |
| Consumer Staples       | 32.05                  |
| Consumer Discretionary | 27.76                  |
| Communication Services | 27.23                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 17.5           | 41.4               | 0.42                 |
| Materials              | 16.3           | 48.6               | 0.33                 |
| Industrials            | 2.5            | 36.2               | 0.07                 |
| Consumer Staples       | 1.3            | 28.4               | 0.05                 |
| Utilities              | -1.3           | 27.6               | -0.05                |
| Financials             | -2.6           | 30.8               | -0.08                |
| Healthcare             | -7.1           | 41.9               | -0.17                |
| Information Technology | -17.1          | 49.5               | -0.35                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 152.38       |
| BHP  | BHP                    | Materials              | 260.3            | 62.86        |
| WBC  | Westpac                | Financials             | 136.3            | 34.66        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.86        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 75.86        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.02       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.7         |
| CSL  | CSL                    | Healthcare             | 67.4             | 178.68       |
