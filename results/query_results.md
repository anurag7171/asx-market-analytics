# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 41.66             | 102.43   | -22.28    |
| Energy           | 11        | 21.83             | 54.43    | -27.63    |
| Industrials      | 24        | 7.41              | 85.32    | -48.21    |
| Utilities        | 7         | 3.36              | 29.6     | -14.71    |
| Financials       | 36        | -0.36             | 73.62    | -49.12    |
| Consumer Staples | 7         | -4.25             | 44.67    | -29.97    |
| Healthcare       | 16        | -8.2              | 60.45    | -52.5     |
| Real Estate      | 16        | -16.11            | 5.88     | -53.44    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | S32  | South32             | Materials   | 102.4               |
| 2    | PLS  | PLS Group           | Materials   | 100.6               |
| 3    | RSG  | Resolute Mining     | Materials   | 95.9                |
| 4    | NWH  | NRW Holdings        | Industrials | 85.3                |
| 5    | SFR  | Sandfire Resources  | Materials   | 82.9                |
| 6    | SGM  | Sims Metal          | Materials   | 81.7                |
| 7    | GGP  | Greatland Resources | Materials   | 81.1                |
| 8    | SMR  | Stanmore Resources  | Materials   | 80.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 111.4                 |
| DRO  | 254          | 103.9                 |
| EOS  | 254          | 99.5                  |
| CTD  | 254          | 85.1                  |
| ZIP  | 254          | 79.5                  |
| LTR  | 254          | 79.3                  |
| OBM  | 254          | 78.4                  |
| TUA  | 254          | 75.7                  |

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
| Materials              | 35                  |
| Financials             | 12                  |
| Industrials            | 10                  |
| Energy                 | 10                  |
| Healthcare             | 8                   |
| Utilities              | 4                   |
| Communication Services | 4                   |
| Real Estate            | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.22         | -86.2          |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.1          | -74.8          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.75         | -73.6          |
| 360  | Life360                | Information Technology | 55.44    | 20.03        | -63.9          |
| WTC  | Wisetech Global        | Information Technology | 97.44    | 35.25        | -63.8          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 7.45         | -55.7          |
| GDG  | Generation Development | Financials             | 7.56     | 3.37         | -55.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.2          | -54.7          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -86.3            |
| TUA  | Tuas                   | -76.0            |
| DRO  | Droneshield            | -74.8            |
| WTC  | Wisetech Global        | -70.5            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.7            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 50.33                  |
| Information Technology | 45.12                  |
| Financials             | 44.07                  |
| Energy                 | 40.78                  |
| Healthcare             | 36.49                  |
| Consumer Staples       | 32.43                  |
| Consumer Discretionary | 27.56                  |
| Communication Services | 27.4                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 41.7           | 47.5               | 0.88                 |
| Energy                 | 21.8           | 41.8               | 0.52                 |
| Industrials            | 7.4            | 35.1               | 0.21                 |
| Utilities              | 3.4            | 27.5               | 0.12                 |
| Financials             | -0.4           | 30.7               | -0.01                |
| Consumer Staples       | -4.2           | 28.2               | -0.15                |
| Healthcare             | -8.2           | 42.9               | -0.19                |
| Information Technology | -23.4          | 48.2               | -0.49                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 158.69       |
| BHP  | BHP                    | Materials              | 260.3            | 62.55        |
| WBC  | Westpac                | Financials             | 136.3            | 34.58        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.94        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 75.22        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 246.86       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.87        |
| CSL  | CSL                    | Healthcare             | 67.4             | 174.8        |
