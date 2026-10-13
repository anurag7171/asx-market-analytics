# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 19.02             | 93.72    | -57.25    |
| Materials        | 47        | 11.58             | 65.3     | -42.4     |
| Consumer Staples | 7         | 5.51              | 56.54    | -22.06    |
| Industrials      | 23        | 1.0               | 52.97    | -74.63    |
| Utilities        | 7         | 0.98              | 28.85    | -12.46    |
| Financials       | 36        | -3.04             | 49.69    | -62.52    |
| Healthcare       | 16        | -4.15             | 100.99   | -52.29    |
| Real Estate      | 16        | -18.5             | -0.85    | -59.69    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical          | Healthcare             | 101.0               |
| 2    | CDA  | Codan              | Information Technology | 95.6                |
| 3    | VEA  | Viva Energy        | Energy                 | 93.7                |
| 4    | RHC  | Ramsay Health Care | Healthcare             | 75.1                |
| 5    | SGM  | Sims Metal         | Materials              | 65.3                |
| 6    | BSL  | BlueScope          | Materials              | 64.5                |
| 7    | NHC  | New Hope           | Energy                 | 63.8                |
| 8    | S32  | South32            | Materials              | 62.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 103.2                 |
| DRO  | 254          | 97.5                  |
| EOS  | 254          | 96.9                  |
| CTD  | 254          | 90.0                  |
| ZIP  | 254          | 80.7                  |
| TUA  | 254          | 79.4                  |
| LTR  | 254          | 77.9                  |
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
| Financials             | 15                  |
| Industrials            | 9                   |
| Materials              | 7                   |
| Healthcare             | 7                   |
| Consumer Discretionary | 6                   |
| Energy                 | 5                   |
| Consumer Staples       | 5                   |
| Utilities              | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.41         | -85.0          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.57         | -79.5          |
| DRO  | Droneshield            | Industrials            | 6.03     | 1.53         | -74.6          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.71         | -72.9          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.89         | -69.6          |
| GDG  | Generation Development | Financials             | 7.56     | 2.71         | -64.1          |
| XRO  | Xero                   | Information Technology | 157.07   | 59.71        | -62.0          |
| 360  | Life360                | Information Technology | 52.99    | 20.3         | -61.7          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.5            |
| DRO  | Droneshield            | -74.6            |
| LTR  | Liontown Resources     | -72.9            |
| DYL  | Deep Yellow            | -69.6            |
| COH  | Cochlear               | -69.2            |
| ZIP  | Zip                    | -68.9            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.23                  |
| Information Technology | 44.71                  |
| Financials             | 44.18                  |
| Energy                 | 40.93                  |
| Healthcare             | 35.79                  |
| Consumer Staples       | 31.92                  |
| Consumer Discretionary | 27.78                  |
| Communication Services | 27.35                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 19.0           | 41.7               | 0.46                 |
| Materials              | 11.6           | 48.5               | 0.24                 |
| Consumer Staples       | 5.5            | 28.1               | 0.2                  |
| Utilities              | 1.0            | 27.9               | 0.04                 |
| Industrials            | 1.0            | 36.2               | 0.03                 |
| Healthcare             | -4.2           | 42.0               | -0.1                 |
| Financials             | -3.0           | 30.7               | -0.1                 |
| Information Technology | -18.6          | 49.7               | -0.37                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 154.5        |
| BHP  | BHP                    | Materials              | 260.3            | 61.28        |
| WBC  | Westpac                | Financials             | 136.3            | 35.16        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.39        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.76        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 251.9        |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.25        |
| CSL  | CSL                    | Healthcare             | 67.4             | 184.58       |
