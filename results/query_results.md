# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 41.22             | 110.67   | -23.61    |
| Energy           | 11        | 23.52             | 56.23    | -25.35    |
| Industrials      | 24        | 7.81              | 83.88    | -44.19    |
| Utilities        | 7         | 3.51              | 30.79    | -12.22    |
| Financials       | 36        | -0.01             | 76.58    | -48.53    |
| Consumer Staples | 7         | -4.91             | 44.07    | -29.89    |
| Healthcare       | 16        | -5.02             | 106.57   | -53.82    |
| Real Estate      | 16        | -16.68            | 5.0      | -56.3     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | PLS  | PLS Group           | Materials   | 110.7               |
| 2    | S32  | South32             | Materials   | 108.7               |
| 3    | 4DX  | 4DMedical           | Healthcare  | 106.6               |
| 4    | GGP  | Greatland Resources | Materials   | 84.3                |
| 5    | NWH  | NRW Holdings        | Industrials | 83.9                |
| 6    | SFR  | Sandfire Resources  | Materials   | 83.2                |
| 7    | SGM  | Sims Metal          | Materials   | 82.9                |
| 8    | SMR  | Stanmore Resources  | Materials   | 81.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 107.9                 |
| DRO  | 254          | 103.8                 |
| EOS  | 254          | 99.5                  |
| CTD  | 254          | 85.7                  |
| ZIP  | 254          | 79.5                  |
| LTR  | 254          | 79.3                  |
| OBM  | 254          | 78.0                  |
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
| Materials              | 38                  |
| Financials             | 11                  |
| Energy                 | 10                  |
| Industrials            | 9                   |
| Healthcare             | 7                   |
| Utilities              | 4                   |
| Communication Services | 3                   |
| Real Estate            | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.0          | -87.6          |
| TUA  | Tuas                   | Communication Services | 8.17     | 2.09         | -74.4          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.73         | -73.8          |
| 360  | Life360                | Information Technology | 55.44    | 19.64        | -64.6          |
| WTC  | Wisetech Global        | Information Technology | 97.44    | 34.53        | -64.6          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 7.04         | -58.1          |
| GDG  | Generation Development | Financials             | 7.56     | 3.2          | -57.7          |
| XRO  | Xero                   | Information Technology | 163.97   | 71.63        | -56.3          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -75.5            |
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
| Information Technology | 45.04                  |
| Financials             | 44.1                   |
| Energy                 | 40.83                  |
| Healthcare             | 36.5                   |
| Consumer Staples       | 32.42                  |
| Consumer Discretionary | 27.59                  |
| Communication Services | 27.43                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 41.2           | 48.5               | 0.85                 |
| Energy                 | 23.5           | 41.8               | 0.56                 |
| Industrials            | 7.8            | 35.1               | 0.22                 |
| Utilities              | 3.5            | 27.5               | 0.13                 |
| Financials             | -0.0           | 30.7               | -0.0                 |
| Healthcare             | -5.0           | 42.7               | -0.12                |
| Consumer Staples       | -4.9           | 28.2               | -0.17                |
| Information Technology | -23.5          | 48.2               | -0.49                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 155.25       |
| BHP  | BHP                    | Materials              | 260.3            | 64.58        |
| WBC  | Westpac                | Financials             | 136.3            | 34.39        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.79        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 74.16        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.97       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.27        |
| CSL  | CSL                    | Healthcare             | 67.4             | 171.21       |
