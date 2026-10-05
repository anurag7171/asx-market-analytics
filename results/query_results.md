# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Energy                 | 11        | 17.05             | 82.32    | -45.52    |
| Materials              | 47        | 16.05             | 106.25   | -36.98    |
| Industrials            | 23        | 2.62              | 80.82    | -71.3     |
| Consumer Staples       | 7         | 0.57              | 48.76    | -22.01    |
| Utilities              | 7         | -1.42             | 25.11    | -9.94     |
| Financials             | 36        | -3.01             | 72.7     | -62.99    |
| Healthcare             | 16        | -7.23             | 80.89    | -53.09    |
| Information Technology | 7         | -15.09            | 128.2    | -64.16    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | CDA  | Codan                | Information Technology | 128.2               |
| 2    | PDI  | Predictive Discovery | Materials              | 106.3               |
| 3    | VEA  | Viva Energy          | Energy                 | 82.3                |
| 4    | S32  | South32              | Materials              | 81.8                |
| 5    | 4DX  | 4DMedical            | Healthcare             | 80.9                |
| 6    | NWH  | NRW Holdings         | Industrials            | 80.8                |
| 7    | SGM  | Sims Metal           | Materials              | 78.8                |
| 8    | RHC  | Ramsay Health Care   | Healthcare             | 73.9                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 103.7                 |
| DRO  | 254          | 97.8                  |
| EOS  | 254          | 96.9                  |
| CTD  | 254          | 89.7                  |
| ZIP  | 254          | 80.2                  |
| TUA  | 254          | 79.4                  |
| LTR  | 254          | 77.8                  |
| OBM  | 254          | 76.9                  |

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
| Financials             | 10                  |
| Industrials            | 9                   |
| Healthcare             | 6                   |
| Energy                 | 4                   |
| Communication Services | 3                   |
| Utilities              | 2                   |
| Consumer Staples       | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.33         | -85.5          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.72         | -77.6          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.8          | -72.7          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.81         | -69.5          |
| GDG  | Generation Development | Financials             | 7.56     | 2.65         | -64.9          |
| XRO  | Xero                   | Information Technology | 157.69   | 56.51        | -64.2          |
| 360  | Life360                | Information Technology | 54.86    | 20.32        | -63.0          |
| WTC  | Wisetech Global        | Information Technology | 87.8     | 32.73        | -62.7          |

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
| Materials              | 49.31                  |
| Information Technology | 44.78                  |
| Financials             | 44.1                   |
| Energy                 | 40.7                   |
| Healthcare             | 35.74                  |
| Consumer Staples       | 32.07                  |
| Consumer Discretionary | 27.72                  |
| Communication Services | 27.2                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 17.1           | 41.5               | 0.41                 |
| Materials              | 16.0           | 48.6               | 0.33                 |
| Industrials            | 2.6            | 36.2               | 0.07                 |
| Consumer Staples       | 0.6            | 28.4               | 0.02                 |
| Utilities              | -1.4           | 27.6               | -0.05                |
| Financials             | -3.0           | 30.9               | -0.1                 |
| Healthcare             | -7.2           | 42.0               | -0.17                |
| Information Technology | -15.1          | 49.5               | -0.3                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 151.22       |
| BHP  | BHP                    | Materials              | 260.3            | 61.89        |
| WBC  | Westpac                | Financials             | 136.3            | 34.44        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.65        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 75.47        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.02       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.4         |
| CSL  | CSL                    | Healthcare             | 67.4             | 176.99       |
