# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 52.35             | 133.04   | -26.63    |
| Healthcare             | 16        | 30.38             | 658.33   | -53.76    |
| Energy                 | 11        | 22.27             | 62.36    | -27.22    |
| Industrials            | 24        | 10.14             | 105.34   | -46.48    |
| Utilities              | 7         | 5.16              | 29.61    | -9.24     |
| Financials             | 36        | -0.29             | 88.54    | -52.75    |
| Consumer Staples       | 7         | -5.59             | 43.89    | -28.05    |
| Information Technology | 7         | -15.72            | 61.15    | -59.17    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 658.3               |
| 2    | PLS  | PLS Group            | Materials   | 133.0               |
| 3    | GGP  | Greatland Resources  | Materials   | 132.3               |
| 4    | RSG  | Resolute Mining      | Materials   | 119.1               |
| 5    | NWH  | NRW Holdings         | Industrials | 105.3               |
| 6    | VAU  | Vault Minerals       | Materials   | 104.0               |
| 7    | S32  | South32              | Materials   | 99.8                |
| 8    | PDI  | Predictive Discovery | Materials   | 98.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.1                 |
| DRO  | 254          | 104.0                 |
| EOS  | 254          | 100.2                 |
| ZIP  | 254          | 79.3                  |
| LTR  | 254          | 79.2                  |
| OBM  | 254          | 78.8                  |
| TUA  | 254          | 76.1                  |
| DYL  | 254          | 72.6                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Materials              | 36                  |
| Financials             | 13                  |
| Energy                 | 10                  |
| Healthcare             | 9                   |
| Industrials            | 7                   |
| Consumer Discretionary | 7                   |
| Communication Services | 7                   |
| Information Technology | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.06         | -75.2          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.75         | -73.5          |
| 360  | Life360                | Information Technology | 55.44    | 20.5         | -63.0          |
| PXA  | Pexa Group             | Real Estate            | 16.92    | 6.68         | -60.5          |
| WTC  | Wisetech Global        | Information Technology | 101.46   | 40.61        | -60.0          |
| GDG  | Generation Development | Financials             | 7.58     | 3.2          | -57.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.2          | -54.7          |
| COH  | Cochlear               | Healthcare             | 296.77   | 136.1        | -54.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name       | max_drawdown_pct |
| ---- | ------------------ | ---------------- |
| TUA  | Tuas               | -76.0            |
| DRO  | Droneshield        | -74.3            |
| WTC  | Wisetech Global    | -71.7            |
| ZIP  | Zip                | -70.0            |
| COH  | Cochlear           | -69.7            |
| 360  | Life360            | -67.7            |
| PME  | Pro Medicus        | -66.2            |
| LTR  | Liontown Resources | -63.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.29                  |
| Information Technology | 45.66                  |
| Financials             | 43.86                  |
| Energy                 | 40.48                  |
| Healthcare             | 36.27                  |
| Consumer Staples       | 32.66                  |
| Consumer Discretionary | 27.42                  |
| Communication Services | 26.82                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 52.3           | 49.1               | 1.07                 |
| Healthcare             | 30.4           | 44.2               | 0.69                 |
| Energy                 | 22.3           | 41.7               | 0.53                 |
| Industrials            | 10.1           | 35.3               | 0.29                 |
| Utilities              | 5.2            | 27.6               | 0.19                 |
| Financials             | -0.3           | 30.7               | -0.01                |
| Consumer Staples       | -5.6           | 28.2               | -0.2                 |
| Information Technology | -15.7          | 48.7               | -0.32                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 157.25       |
| BHP  | BHP                    | Materials              | 260.3            | 67.3         |
| WBC  | Westpac                | Financials             | 136.3            | 33.9         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.73        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 79.79        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 251.78       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.29        |
| CSL  | CSL                    | Healthcare             | 67.4             | 172.32       |
