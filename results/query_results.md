# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 36.21             | 158.42   | -31.37    |
| Energy           | 11        | 20.07             | 60.88    | -32.49    |
| Industrials      | 24        | 7.45              | 78.23    | -46.75    |
| Utilities        | 7         | 1.82              | 30.5     | -11.88    |
| Financials       | 36        | -0.89             | 61.75    | -56.76    |
| Healthcare       | 16        | -1.96             | 141.46   | -54.05    |
| Consumer Staples | 7         | -4.93             | 42.63    | -30.87    |
| Real Estate      | 16        | -19.16            | 2.71     | -58.99    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials   | 158.4               |
| 2    | 4DX  | 4DMedical            | Healthcare  | 141.5               |
| 3    | S32  | South32              | Materials   | 96.4                |
| 4    | ALK  | Alkane Resources     | Materials   | 94.2                |
| 5    | PLS  | PLS Group            | Materials   | 83.8                |
| 6    | SFR  | Sandfire Resources   | Materials   | 81.2                |
| 7    | SGM  | Sims Metal           | Materials   | 80.9                |
| 8    | NWH  | NRW Holdings         | Industrials | 78.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 107.1                 |
| DRO  | 254          | 103.8                 |
| EOS  | 254          | 99.2                  |
| CTD  | 254          | 88.5                  |
| ZIP  | 254          | 79.6                  |
| OBM  | 254          | 77.4                  |
| LTR  | 254          | 77.3                  |
| TUA  | 254          | 76.0                  |

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
| Materials              | 24                  |
| Financials             | 13                  |
| Industrials            | 10                  |
| Healthcare             | 8                   |
| Energy                 | 7                   |
| Utilities              | 4                   |
| Communication Services | 4                   |
| Information Technology | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.66         | -83.4          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.72         | -73.9          |
| TUA  | Tuas                   | Communication Services | 7.64     | 2.26         | -70.4          |
| WTC  | Wisetech Global        | Information Technology | 96.25    | 32.06        | -66.7          |
| 360  | Life360                | Information Technology | 55.44    | 19.02        | -65.7          |
| XRO  | Xero                   | Information Technology | 163.97   | 62.78        | -61.7          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.02         | -61.4          |
| GDG  | Generation Development | Financials             | 7.56     | 2.98         | -60.6          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| DRO  | Droneshield            | -75.8            |
| TUA  | Tuas                   | -73.8            |
| WTC  | Wisetech Global        | -70.2            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 50.17                  |
| Information Technology | 45.38                  |
| Financials             | 44.49                  |
| Energy                 | 41.31                  |
| Healthcare             | 36.7                   |
| Consumer Staples       | 32.53                  |
| Consumer Discretionary | 27.88                  |
| Communication Services | 27.54                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 36.2           | 48.9               | 0.74                 |
| Energy                 | 20.1           | 41.4               | 0.48                 |
| Industrials            | 7.4            | 35.1               | 0.21                 |
| Utilities              | 1.8            | 27.5               | 0.07                 |
| Financials             | -0.9           | 30.5               | -0.03                |
| Healthcare             | -2.0           | 42.7               | -0.05                |
| Consumer Staples       | -4.9           | 28.3               | -0.17                |
| Information Technology | -23.8          | 48.4               | -0.49                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 152.43       |
| BHP  | BHP                    | Materials              | 260.3            | 61.05        |
| WBC  | Westpac                | Financials             | 136.3            | 34.75        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.68        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 73.03        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 238.62       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.47        |
| CSL  | CSL                    | Healthcare             | 67.4             | 175.59       |
