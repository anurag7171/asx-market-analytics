# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 47.87             | 120.58   | -26.63    |
| Energy           | 11        | 17.7              | 46.29    | -26.57    |
| Healthcare       | 16        | 13.27             | 369.68   | -53.82    |
| Industrials      | 24        | 10.01             | 109.12   | -46.61    |
| Utilities        | 7         | 2.79              | 28.45    | -13.71    |
| Financials       | 36        | 0.31              | 88.54    | -49.0     |
| Consumer Staples | 7         | -6.44             | 41.84    | -29.78    |
| Real Estate      | 17        | -16.14            | 7.66     | -55.91    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 369.7               |
| 2    | PLS  | PLS Group           | Materials   | 120.6               |
| 3    | NWH  | NRW Holdings        | Industrials | 109.1               |
| 4    | GGP  | Greatland Resources | Materials   | 108.6               |
| 5    | RSG  | Resolute Mining     | Materials   | 108.0               |
| 6    | S32  | South32             | Materials   | 97.6                |
| 7    | VAU  | Vault Minerals      | Materials   | 89.7                |
| 8    | L1G  | L1 Group            | Financials  | 88.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 252          | 133.0                 |
| DRO  | 252          | 104.4                 |
| EOS  | 252          | 100.5                 |
| ZIP  | 252          | 79.5                  |
| LTR  | 252          | 79.2                  |
| OBM  | 252          | 78.8                  |
| TUA  | 252          | 76.4                  |
| 360  | 252          | 72.6                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |

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
| PXA  | Pexa Group             | Real Estate            | 16.81    | 6.68         | -60.3          |
| WTC  | Wisetech Global        | Information Technology | 99.08    | 40.61        | -59.0          |
| GDG  | Generation Development | Financials             | 7.58     | 3.2          | -57.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.2          | -54.7          |
| COH  | Cochlear               | Healthcare             | 296.77   | 136.1        | -54.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name       | max_drawdown_pct |
| ---- | ------------------ | ---------------- |
| TUA  | Tuas               | -76.0            |
| DRO  | Droneshield        | -74.3            |
| WTC  | Wisetech Global    | -71.0            |
| ZIP  | Zip                | -70.0            |
| COH  | Cochlear           | -69.7            |
| 360  | Life360            | -67.7            |
| PME  | Pro Medicus        | -66.2            |
| LTR  | Liontown Resources | -63.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.35                  |
| Information Technology | 45.46                  |
| Financials             | 43.87                  |
| Energy                 | 40.54                  |
| Healthcare             | 35.95                  |
| Consumer Staples       | 32.41                  |
| Consumer Discretionary | 27.37                  |
| Communication Services | 26.85                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 47.9           | 49.0               | 0.98                 |
| Energy                 | 17.7           | 41.7               | 0.42                 |
| Healthcare             | 13.3           | 43.9               | 0.3                  |
| Industrials            | 10.0           | 35.3               | 0.28                 |
| Utilities              | 2.8            | 27.6               | 0.1                  |
| Financials             | 0.3            | 30.7               | 0.01                 |
| Consumer Staples       | -6.4           | 28.2               | -0.23                |
| Information Technology | -17.3          | 48.2               | -0.36                |

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
