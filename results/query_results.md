# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 44.14             | 148.11   | -23.75    |
| Energy           | 11        | 23.47             | 58.21    | -26.41    |
| Industrials      | 24        | 7.37              | 83.02    | -47.67    |
| Utilities        | 7         | 1.21              | 29.75    | -16.76    |
| Financials       | 36        | -1.1              | 72.13    | -51.32    |
| Healthcare       | 16        | -5.32             | 118.87   | -53.31    |
| Consumer Staples | 7         | -5.85             | 41.22    | -31.5     |
| Real Estate      | 16        | -17.56            | 3.54     | -57.99    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | PLS  | PLS Group           | Materials   | 148.1               |
| 2    | 4DX  | 4DMedical           | Healthcare  | 118.9               |
| 3    | S32  | South32             | Materials   | 111.2               |
| 4    | IGO  | IGO                 | Materials   | 93.7                |
| 5    | SGM  | Sims Metal          | Materials   | 87.9                |
| 6    | SFR  | Sandfire Resources  | Materials   | 86.3                |
| 7    | GGP  | Greatland Resources | Materials   | 85.8                |
| 8    | NWH  | NRW Holdings        | Industrials | 83.0                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 107.7                 |
| DRO  | 254          | 103.8                 |
| EOS  | 254          | 99.5                  |
| CTD  | 254          | 85.9                  |
| ZIP  | 254          | 79.5                  |
| OBM  | 254          | 77.9                  |
| LTR  | 254          | 77.2                  |
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
| Energy                 | 10                  |
| Industrials            | 7                   |
| Healthcare             | 6                   |
| Utilities              | 4                   |
| Communication Services | 3                   |
| Consumer Discretionary | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.13         | -86.7          |
| TUA  | Tuas                   | Communication Services | 8.03     | 2.05         | -74.5          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.7          | -74.2          |
| WTC  | Wisetech Global        | Information Technology | 97.44    | 33.97        | -65.1          |
| 360  | Life360                | Information Technology | 55.44    | 19.42        | -65.0          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 6.89         | -59.0          |
| GDG  | Generation Development | Financials             | 7.56     | 3.14         | -58.5          |
| XRO  | Xero                   | Information Technology | 163.97   | 68.79        | -58.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -75.1            |
| DRO  | Droneshield            | -74.8            |
| WTC  | Wisetech Global        | -70.5            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.7            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 50.32                  |
| Information Technology | 44.9                   |
| Financials             | 44.11                  |
| Energy                 | 40.83                  |
| Healthcare             | 36.46                  |
| Consumer Staples       | 32.4                   |
| Consumer Discretionary | 27.61                  |
| Communication Services | 27.41                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 44.1           | 48.3               | 0.91                 |
| Energy                 | 23.5           | 41.8               | 0.56                 |
| Industrials            | 7.4            | 35.1               | 0.21                 |
| Utilities              | 1.2            | 27.5               | 0.04                 |
| Financials             | -1.1           | 30.6               | -0.04                |
| Healthcare             | -5.3           | 42.7               | -0.12                |
| Consumer Staples       | -5.8           | 28.2               | -0.21                |
| Information Technology | -25.1          | 48.2               | -0.52                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 153.2        |
| BHP  | BHP                    | Materials              | 260.3            | 63.44        |
| WBC  | Westpac                | Financials             | 136.3            | 33.85        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.65        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 73.52        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.33       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.72        |
| CSL  | CSL                    | Healthcare             | 67.4             | 169.5        |
