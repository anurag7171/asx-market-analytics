# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 18.19             | 87.66    | -48.54    |
| Materials        | 47        | 12.87             | 75.85    | -36.99    |
| Consumer Staples | 7         | 3.22              | 53.13    | -21.76    |
| Industrials      | 23        | 1.55              | 66.7     | -75.19    |
| Utilities        | 7         | -1.79             | 25.66    | -12.85    |
| Financials       | 36        | -3.38             | 63.42    | -64.33    |
| Healthcare       | 16        | -8.26             | 78.73    | -54.46    |
| Real Estate      | 16        | -18.35            | -0.34    | -60.05    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | CDA  | Codan                | Information Technology | 103.5               |
| 2    | VEA  | Viva Energy          | Energy                 | 87.7                |
| 3    | 4DX  | 4DMedical            | Healthcare             | 78.7                |
| 4    | SGM  | Sims Metal           | Materials              | 75.8                |
| 5    | RHC  | Ramsay Health Care   | Healthcare             | 73.7                |
| 6    | PDI  | Predictive Discovery | Materials              | 70.3                |
| 7    | S32  | South32              | Materials              | 69.4                |
| 8    | NWH  | NRW Holdings         | Industrials            | 66.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 103.5                 |
| DRO  | 255          | 97.4                  |
| EOS  | 255          | 97.0                  |
| CTD  | 255          | 89.8                  |
| ZIP  | 255          | 80.0                  |
| TUA  | 255          | 79.3                  |
| LTR  | 255          | 77.5                  |
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
| Materials              | 9                   |
| Financials             | 7                   |
| Healthcare             | 6                   |
| Energy                 | 5                   |
| Consumer Staples       | 3                   |
| Consumer Discretionary | 3                   |
| Communication Services | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.28         | -85.8          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.66         | -78.3          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.62         | -75.5          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.8          | -69.7          |
| GDG  | Generation Development | Financials             | 7.56     | 2.6          | -65.6          |
| 360  | Life360                | Information Technology | 54.38    | 19.53        | -64.1          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 1.05         | -63.7          |
| XRO  | Xero                   | Information Technology | 157.07   | 57.79        | -63.2          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -78.3            |
| DRO  | Droneshield            | -76.1            |
| LTR  | Liontown Resources     | -70.1            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.1            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.42                  |
| Information Technology | 44.76                  |
| Financials             | 44.21                  |
| Energy                 | 40.83                  |
| Healthcare             | 35.76                  |
| Consumer Staples       | 32.01                  |
| Consumer Discretionary | 27.83                  |
| Communication Services | 27.27                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 18.2           | 41.5               | 0.44                 |
| Materials              | 12.9           | 48.5               | 0.27                 |
| Consumer Staples       | 3.2            | 28.4               | 0.11                 |
| Industrials            | 1.6            | 36.2               | 0.04                 |
| Utilities              | -1.8           | 27.7               | -0.06                |
| Financials             | -3.4           | 30.8               | -0.11                |
| Healthcare             | -8.3           | 41.8               | -0.2                 |
| Information Technology | -18.6          | 49.4               | -0.38                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 148.12       |
| BHP  | BHP                    | Materials              | 260.3            | 61.19        |
| WBC  | Westpac                | Financials             | 136.3            | 33.71        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.36        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 76.04        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 246.79       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.8         |
| CSL  | CSL                    | Healthcare             | 67.4             | 181.46       |
