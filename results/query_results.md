# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Energy                 | 11        | 17.72             | 88.77    | -51.24    |
| Materials              | 47        | 11.5              | 61.8     | -40.64    |
| Consumer Staples       | 7         | 2.99              | 55.09    | -20.18    |
| Industrials            | 23        | 1.0               | 61.38    | -76.29    |
| Utilities              | 7         | 0.22              | 29.09    | -14.14    |
| Financials             | 36        | -3.57             | 50.25    | -62.09    |
| Healthcare             | 16        | -8.46             | 73.82    | -53.5     |
| Information Technology | 7         | -16.85            | 105.48   | -62.07    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | CDA  | Codan              | Information Technology | 105.5               |
| 2    | VEA  | Viva Energy        | Energy                 | 88.8                |
| 3    | 4DX  | 4DMedical          | Healthcare             | 73.8                |
| 4    | RHC  | Ramsay Health Care | Healthcare             | 72.2                |
| 5    | SGM  | Sims Metal         | Materials              | 61.8                |
| 6    | NHC  | New Hope           | Energy                 | 61.4                |
| 7    | NWH  | NRW Holdings       | Industrials            | 61.4                |
| 8    | S32  | South32            | Materials              | 58.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 103.4                 |
| DRO  | 255          | 97.4                  |
| EOS  | 255          | 96.9                  |
| CTD  | 255          | 89.8                  |
| ZIP  | 255          | 80.1                  |
| TUA  | 255          | 79.3                  |
| LTR  | 255          | 77.6                  |
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
| Industrials            | 10                  |
| Financials             | 10                  |
| Materials              | 8                   |
| Healthcare             | 6                   |
| Energy                 | 6                   |
| Consumer Staples       | 6                   |
| Consumer Discretionary | 5                   |
| Utilities              | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.34         | -85.4          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.66         | -78.3          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.56         | -76.3          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.77         | -70.8          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.98         | -66.3          |
| GDG  | Generation Development | Financials             | 7.56     | 2.79         | -63.1          |
| 360  | Life360                | Information Technology | 54.38    | 20.34        | -62.6          |
| XRO  | Xero                   | Information Technology | 157.07   | 59.81        | -61.9          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -78.3            |
| DRO  | Droneshield            | -76.3            |
| LTR  | Liontown Resources     | -70.8            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.1            |
| DYL  | Deep Yellow            | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.35                  |
| Information Technology | 44.75                  |
| Financials             | 44.2                   |
| Energy                 | 40.88                  |
| Healthcare             | 35.79                  |
| Consumer Staples       | 31.96                  |
| Consumer Discretionary | 27.82                  |
| Communication Services | 27.33                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 17.7           | 41.6               | 0.43                 |
| Materials              | 11.5           | 48.5               | 0.24                 |
| Consumer Staples       | 3.0            | 28.4               | 0.11                 |
| Industrials            | 1.0            | 36.2               | 0.03                 |
| Utilities              | 0.2            | 27.7               | 0.01                 |
| Financials             | -3.6           | 30.7               | -0.12                |
| Healthcare             | -8.5           | 41.9               | -0.2                 |
| Information Technology | -16.9          | 49.5               | -0.34                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 149.29       |
| BHP  | BHP                    | Materials              | 260.3            | 60.94        |
| WBC  | Westpac                | Financials             | 136.3            | 33.72        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.18        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.35        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.37       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.68        |
| CSL  | CSL                    | Healthcare             | 67.4             | 183.84       |
