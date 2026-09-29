# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 24.39             | 130.73   | -32.11    |
| Energy                 | 11        | 16.52             | 78.06    | -36.34    |
| Industrials            | 23        | 3.68              | 72.35    | -63.3     |
| Utilities              | 7         | -0.05             | 27.37    | -9.09     |
| Consumer Staples       | 7         | -0.39             | 48.27    | -23.84    |
| Healthcare             | 16        | -1.19             | 126.67   | -47.15    |
| Financials             | 36        | -1.21             | 72.13    | -60.5     |
| Information Technology | 7         | -16.25            | 120.86   | -64.49    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials              | 130.7               |
| 2    | 4DX  | 4DMedical            | Healthcare             | 126.7               |
| 3    | CDA  | Codan                | Information Technology | 120.9               |
| 4    | S32  | South32              | Materials              | 94.0                |
| 5    | SGM  | Sims Metal           | Materials              | 79.5                |
| 6    | RHC  | Ramsay Health Care   | Healthcare             | 79.1                |
| 7    | VEA  | Viva Energy          | Energy                 | 78.1                |
| 8    | NWH  | NRW Holdings         | Industrials            | 72.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 105.7                 |
| DRO  | 254          | 101.9                 |
| EOS  | 254          | 98.2                  |
| CTD  | 254          | 89.2                  |
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
| Financials             | 12                  |
| Industrials            | 11                  |
| Healthcare             | 8                   |
| Energy                 | 4                   |
| Utilities              | 2                   |
| Information Technology | 2                   |
| Consumer Staples       | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.34         | -85.4          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.74         | -77.2          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.61         | -75.5          |
| 360  | Life360                | Information Technology | 55.44    | 19.08        | -65.6          |
| WTC  | Wisetech Global        | Information Technology | 92.48    | 32.84        | -64.5          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.95         | -64.0          |
| GDG  | Generation Development | Financials             | 7.56     | 2.73         | -63.9          |
| XRO  | Xero                   | Information Technology | 160.95   | 58.04        | -63.9          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -77.7            |
| DRO  | Droneshield            | -76.1            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| WTC  | Wisetech Global        | -69.0            |
| 360  | Life360                | -67.7            |
| LTR  | Liontown Resources     | -65.7            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.48                  |
| Information Technology | 44.83                  |
| Financials             | 44.07                  |
| Energy                 | 40.74                  |
| Healthcare             | 35.96                  |
| Consumer Staples       | 32.17                  |
| Consumer Discretionary | 27.66                  |
| Communication Services | 27.29                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 24.4           | 48.8               | 0.5                  |
| Energy                 | 16.5           | 41.3               | 0.4                  |
| Industrials            | 3.7            | 36.3               | 0.1                  |
| Utilities              | -0.1           | 27.7               | -0.0                 |
| Consumer Staples       | -0.4           | 28.3               | -0.01                |
| Healthcare             | -1.2           | 42.2               | -0.03                |
| Financials             | -1.2           | 30.8               | -0.04                |
| Information Technology | -16.2          | 49.3               | -0.33                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 150.27       |
| BHP  | BHP                    | Materials              | 260.3            | 60.63        |
| WBC  | Westpac                | Financials             | 136.3            | 35.02        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.45        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 74.35        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 247.09       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.11        |
| CSL  | CSL                    | Healthcare             | 67.4             | 182.3        |
