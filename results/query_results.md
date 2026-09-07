# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 44.01             | 100.62   | -23.05    |
| Energy           | 11        | 21.57             | 51.32    | -26.9     |
| Industrials      | 24        | 7.49              | 81.78    | -47.38    |
| Utilities        | 7         | 2.81              | 29.36    | -13.73    |
| Financials       | 36        | 0.52              | 75.1     | -47.58    |
| Consumer Staples | 7         | -3.08             | 47.22    | -26.96    |
| Healthcare       | 16        | -8.05             | 60.03    | -52.25    |
| Real Estate      | 16        | -14.88            | 8.22     | -52.81    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | PLS  | PLS Group            | Materials   | 100.6               |
| 2    | S32  | South32              | Materials   | 99.3                |
| 3    | PDI  | Predictive Discovery | Materials   | 98.7                |
| 4    | RSG  | Resolute Mining      | Materials   | 93.9                |
| 5    | SGM  | Sims Metal           | Materials   | 85.8                |
| 6    | SFR  | Sandfire Resources   | Materials   | 82.7                |
| 7    | NWH  | NRW Holdings         | Industrials | 81.8                |
| 8    | GGP  | Greatland Resources  | Materials   | 81.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 111.5                 |
| DRO  | 253          | 104.1                 |
| EOS  | 253          | 99.7                  |
| CTD  | 253          | 85.3                  |
| ZIP  | 253          | 79.6                  |
| LTR  | 253          | 79.5                  |
| OBM  | 253          | 78.5                  |
| TUA  | 253          | 75.9                  |

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
| Materials              | 37                  |
| Financials             | 15                  |
| Energy                 | 10                  |
| Industrials            | 8                   |
| Healthcare             | 7                   |
| Communication Services | 5                   |
| Utilities              | 4                   |
| Consumer Staples       | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.2          | -86.3          |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.11         | -74.6          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.75         | -73.5          |
| 360  | Life360                | Information Technology | 55.44    | 20.03        | -63.9          |
| WTC  | Wisetech Global        | Information Technology | 97.44    | 36.26        | -62.8          |
| GDG  | Generation Development | Financials             | 7.56     | 3.36         | -55.5          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.19         | -55.1          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 7.55         | -55.1          |

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
| Materials              | 49.58                  |
| Information Technology | 45.18                  |
| Financials             | 44.07                  |
| Energy                 | 40.79                  |
| Healthcare             | 36.51                  |
| Consumer Staples       | 32.46                  |
| Consumer Discretionary | 27.57                  |
| Communication Services | 27.41                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 44.0           | 49.1               | 0.9                  |
| Energy                 | 21.6           | 41.8               | 0.52                 |
| Industrials            | 7.5            | 35.2               | 0.21                 |
| Utilities              | 2.8            | 27.5               | 0.1                  |
| Financials             | 0.5            | 30.7               | 0.02                 |
| Consumer Staples       | -3.1           | 28.2               | -0.11                |
| Healthcare             | -8.0           | 42.9               | -0.19                |
| Information Technology | -22.1          | 48.2               | -0.46                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 161.54       |
| BHP  | BHP                    | Materials              | 260.3            | 62.93        |
| WBC  | Westpac                | Financials             | 136.3            | 35.02        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.93        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.3         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.83       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.44        |
| CSL  | CSL                    | Healthcare             | 67.4             | 173.18       |
