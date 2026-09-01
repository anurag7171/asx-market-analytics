# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 46.83             | 125.51   | -25.13    |
| Energy           | 11        | 19.17             | 50.03    | -26.34    |
| Healthcare       | 16        | 10.95             | 341.29   | -54.42    |
| Industrials      | 24        | 10.44             | 113.49   | -45.52    |
| Utilities        | 7         | 3.39              | 29.16    | -10.31    |
| Financials       | 36        | 0.34              | 92.91    | -51.23    |
| Consumer Staples | 7         | -6.13             | 42.53    | -29.78    |
| Real Estate      | 17        | -15.35            | 7.95     | -52.81    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 341.3               |
| 2    | PLS  | PLS Group           | Materials   | 125.5               |
| 3    | NWH  | NRW Holdings        | Industrials | 113.5               |
| 4    | RSG  | Resolute Mining     | Materials   | 110.1               |
| 5    | S32  | South32             | Materials   | 97.2                |
| 6    | GGP  | Greatland Resources | Materials   | 94.2                |
| 7    | L1G  | L1 Group            | Financials  | 92.9                |
| 8    | VAU  | Vault Minerals      | Materials   | 84.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 132.6                 |
| DRO  | 254          | 104.0                 |
| EOS  | 254          | 100.1                 |
| ZIP  | 254          | 79.3                  |
| LTR  | 254          | 79.2                  |
| OBM  | 254          | 78.6                  |
| TUA  | 254          | 76.1                  |
| DYL  | 254          | 72.4                  |

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
| Financials             | 14                  |
| Energy                 | 10                  |
| Healthcare             | 8                   |
| Industrials            | 7                   |
| Communication Services | 6                   |
| Information Technology | 5                   |
| Consumer Staples       | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.07         | -75.1          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.76         | -73.3          |
| 360  | Life360                | Information Technology | 55.44    | 20.17        | -63.6          |
| WTC  | Wisetech Global        | Information Technology | 99.08    | 39.7         | -59.9          |
| GDG  | Generation Development | Financials             | 7.58     | 3.06         | -59.6          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 7.15         | -57.5          |
| COH  | Cochlear               | Healthcare             | 296.77   | 134.35       | -54.7          |
| ARB  | ARB Corporation        | Consumer Discretionary | 39.02    | 19.25        | -50.7          |

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
| Materials              | 49.41                  |
| Information Technology | 45.53                  |
| Financials             | 43.98                  |
| Energy                 | 40.57                  |
| Healthcare             | 36.57                  |
| Consumer Staples       | 32.53                  |
| Consumer Discretionary | 27.53                  |
| Communication Services | 27.36                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 46.8           | 49.0               | 0.96                 |
| Energy                 | 19.2           | 41.7               | 0.46                 |
| Industrials            | 10.4           | 35.2               | 0.3                  |
| Healthcare             | 11.0           | 43.7               | 0.25                 |
| Utilities              | 3.4            | 27.5               | 0.12                 |
| Financials             | 0.3            | 30.7               | 0.01                 |
| Consumer Staples       | -6.1           | 28.2               | -0.22                |
| Information Technology | -18.1          | 48.1               | -0.38                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 159.15       |
| BHP  | BHP                    | Materials              | 260.3            | 66.84        |
| WBC  | Westpac                | Financials             | 136.3            | 34.36        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.34        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.08        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 247.57       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.5         |
| CSL  | CSL                    | Healthcare             | 67.4             | 172.31       |
