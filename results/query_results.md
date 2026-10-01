# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 20.48             | 133.56   | -34.29    |
| Energy                 | 11        | 16.79             | 80.11    | -43.07    |
| Industrials            | 23        | 1.92              | 73.93    | -70.12    |
| Utilities              | 7         | -1.46             | 25.17    | -11.31    |
| Consumer Staples       | 7         | -1.94             | 47.46    | -23.76    |
| Financials             | 36        | -2.62             | 68.42    | -60.86    |
| Healthcare             | 16        | -4.79             | 92.92    | -52.23    |
| Information Technology | 7         | -16.37            | 126.89   | -65.3     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials              | 133.6               |
| 2    | CDA  | Codan                | Information Technology | 126.9               |
| 3    | 4DX  | 4DMedical            | Healthcare             | 92.9                |
| 4    | S32  | South32              | Materials              | 83.5                |
| 5    | SGM  | Sims Metal           | Materials              | 81.3                |
| 6    | VEA  | Viva Energy          | Energy                 | 80.1                |
| 7    | NWH  | NRW Holdings         | Industrials            | 73.9                |
| 8    | RHC  | Ramsay Health Care   | Healthcare             | 70.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 104.5                 |
| DRO  | 254          | 99.1                  |
| EOS  | 254          | 97.8                  |
| CTD  | 254          | 89.6                  |
| ZIP  | 254          | 80.2                  |
| TUA  | 254          | 79.4                  |
| LTR  | 254          | 78.4                  |
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
| Materials              | 14                  |
| Industrials            | 8                   |
| Financials             | 7                   |
| Healthcare             | 6                   |
| Energy                 | 4                   |
| Communication Services | 3                   |
| Utilities              | 2                   |
| Consumer Staples       | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.3          | -85.7          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.68         | -78.1          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.72         | -74.0          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.79         | -70.1          |
| 360  | Life360                | Information Technology | 55.44    | 18.93        | -65.9          |
| XRO  | Xero                   | Information Technology | 160.95   | 55.31        | -65.6          |
| WTC  | Wisetech Global        | Information Technology | 90.31    | 31.34        | -65.3          |
| GDG  | Generation Development | Financials             | 7.56     | 2.74         | -63.7          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -78.1            |
| DRO  | Droneshield            | -76.1            |
| LTR  | Liontown Resources     | -70.1            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| WTC  | Wisetech Global        | -68.3            |
| 360  | Life360                | -67.7            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.49                  |
| Information Technology | 44.96                  |
| Financials             | 44.2                   |
| Energy                 | 40.79                  |
| Healthcare             | 35.96                  |
| Consumer Staples       | 32.23                  |
| Consumer Discretionary | 27.75                  |
| Communication Services | 27.35                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 20.5           | 48.8               | 0.42                 |
| Energy                 | 16.8           | 41.5               | 0.4                  |
| Industrials            | 1.9            | 36.3               | 0.05                 |
| Utilities              | -1.5           | 27.6               | -0.05                |
| Consumer Staples       | -1.9           | 28.4               | -0.07                |
| Financials             | -2.6           | 30.9               | -0.08                |
| Healthcare             | -4.8           | 42.1               | -0.11                |
| Information Technology | -16.4          | 49.4               | -0.33                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 149.71       |
| BHP  | BHP                    | Materials              | 260.3            | 60.26        |
| WBC  | Westpac                | Financials             | 136.3            | 33.9         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.19        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 75.73        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 245.84       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.89        |
| CSL  | CSL                    | Healthcare             | 67.4             | 178.24       |
