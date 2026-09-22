# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 30.39             | 134.63   | -32.71    |
| Energy           | 11        | 23.0              | 85.65    | -31.44    |
| Industrials      | 23        | 7.26              | 80.67    | -49.85    |
| Utilities        | 7         | 1.78              | 30.57    | -8.68     |
| Financials       | 36        | -0.24             | 75.84    | -57.43    |
| Healthcare       | 16        | -0.85             | 163.37   | -50.74    |
| Consumer Staples | 7         | -3.31             | 42.54    | -25.96    |
| Real Estate      | 16        | -18.77            | 1.06     | -58.24    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 163.4               |
| 2    | PDI  | Predictive Discovery | Materials   | 134.6               |
| 3    | S32  | South32              | Materials   | 91.4                |
| 4    | VEA  | Viva Energy          | Energy      | 85.6                |
| 5    | PLS  | PLS Group            | Materials   | 82.0                |
| 6    | SFR  | Sandfire Resources   | Materials   | 81.6                |
| 7    | SGM  | Sims Metal           | Materials   | 80.8                |
| 8    | NWH  | NRW Holdings         | Industrials | 80.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.6                 |
| DRO  | 254          | 103.8                 |
| EOS  | 254          | 98.9                  |
| CTD  | 254          | 88.8                  |
| ZIP  | 254          | 79.6                  |
| OBM  | 254          | 77.3                  |
| LTR  | 254          | 77.2                  |
| TUA  | 254          | 75.9                  |

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
| Materials              | 22                  |
| Financials             | 14                  |
| Industrials            | 9                   |
| Healthcare             | 8                   |
| Communication Services | 5                   |
| Energy                 | 4                   |
| Utilities              | 3                   |
| Information Technology | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.74         | -82.9          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.66         | -74.8          |
| TUA  | Tuas                   | Communication Services | 7.64     | 2.33         | -69.5          |
| WTC  | Wisetech Global        | Information Technology | 96.25    | 32.68        | -66.0          |
| 360  | Life360                | Information Technology | 55.44    | 19.23        | -65.3          |
| XRO  | Xero                   | Information Technology | 163.97   | 61.05        | -62.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.02         | -61.4          |
| GDG  | Generation Development | Financials             | 7.56     | 3.01         | -60.2          |

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
| Materials              | 49.7                   |
| Information Technology | 44.88                  |
| Financials             | 44.08                  |
| Energy                 | 40.79                  |
| Healthcare             | 36.27                  |
| Consumer Staples       | 32.27                  |
| Consumer Discretionary | 27.66                  |
| Communication Services | 27.26                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 30.4           | 48.8               | 0.62                 |
| Energy                 | 23.0           | 41.3               | 0.56                 |
| Industrials            | 7.3            | 36.5               | 0.2                  |
| Utilities              | 1.8            | 27.5               | 0.06                 |
| Financials             | -0.2           | 30.6               | -0.01                |
| Healthcare             | -0.9           | 42.3               | -0.02                |
| Consumer Staples       | -3.3           | 28.4               | -0.12                |
| Information Technology | -22.8          | 48.5               | -0.47                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 152.33       |
| BHP  | BHP                    | Materials              | 260.3            | 61.22        |
| WBC  | Westpac                | Financials             | 136.3            | 34.91        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.15        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 73.32        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 242.27       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.61        |
| CSL  | CSL                    | Healthcare             | 67.4             | 180.72       |
