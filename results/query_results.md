# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 49.37             | 158.76   | -23.78    |
| Healthcare       | 16        | 29.88             | 788.42   | -59.42    |
| Industrials      | 24        | 16.5              | 122.3    | -46.7     |
| Energy           | 11        | 15.61             | 53.32    | -26.07    |
| Financials       | 36        | 4.48              | 60.0     | -34.24    |
| Consumer Staples | 7         | 1.24              | 30.15    | -26.98    |
| Utilities        | 7         | -0.6              | 23.04    | -13.78    |
| Real Estate      | 17        | -4.6              | 15.3     | -50.48    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 788.4               |
| 2    | PLS  | PLS Group           | Materials   | 158.8               |
| 3    | GGP  | Greatland Resources | Materials   | 127.2               |
| 4    | NWH  | NRW Holdings        | Industrials | 122.3               |
| 5    | VAU  | Vault Minerals      | Materials   | 116.9               |
| 6    | WGX  | Westgold Resources  | Materials   | 97.1                |
| 7    | OBM  | Ora Banda Mining    | Materials   | 95.6                |
| 8    | MIN  | Mineral Resources   | Materials   | 92.9                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 139.5                 |
| DRO  | 254          | 104.2                 |
| EOS  | 254          | 100.2                 |
| LTR  | 254          | 81.8                  |
| TUA  | 254          | 81.5                  |
| OBM  | 254          | 78.6                  |
| ZIP  | 254          | 78.2                  |
| DYL  | 254          | 72.0                  |

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
| Materials              | 34                  |
| Financials             | 32                  |
| Industrials            | 15                  |
| Real Estate            | 14                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 12                  |
| Consumer Staples       | 7                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.16         | -74.0          |
| DRO  | Droneshield        | Industrials            | 6.6      | 2.18         | -67.0          |
| WTC  | Wisetech Global    | Information Technology | 116.31   | 40.98        | -64.8          |
| COH  | Cochlear           | Healthcare             | 307.7    | 124.86       | -59.4          |
| XRO  | Xero               | Information Technology | 178.83   | 76.56        | -57.2          |
| ASB  | Austal             | Industrials            | 8.76     | 3.84         | -56.2          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.18         | -55.3          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.81         | -53.8          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.3            |
| DRO  | Droneshield     | -74.3            |
| COH  | Cochlear        | -70.8            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.2            |
| XRO  | Xero            | -65.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.87                  |
| Information Technology | 45.51                  |
| Financials             | 44.22                  |
| Energy                 | 40.4                   |
| Healthcare             | 36.59                  |
| Consumer Staples       | 33.1                   |
| Consumer Discretionary | 27.78                  |
| Communication Services | 26.81                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 49.4           | 49.5               | 1.0                  |
| Healthcare             | 29.9           | 44.1               | 0.68                 |
| Industrials            | 16.5           | 35.8               | 0.46                 |
| Energy                 | 15.6           | 41.6               | 0.37                 |
| Financials             | 4.5            | 30.2               | 0.15                 |
| Consumer Staples       | 1.2            | 28.5               | 0.04                 |
| Utilities              | -0.6           | 28.2               | -0.02                |
| Consumer Discretionary | -5.7           | 33.0               | -0.17                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 178.01       |
| BHP  | BHP                    | Materials              | 260.3            | 62.97        |
| WBC  | Westpac                | Financials             | 136.3            | 37.93        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.73        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.1         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 264.45       |
| NAB  | National Australia Ban | Financials             | 69.8             | 42.23        |
| CSL  | CSL                    | Healthcare             | 67.4             | 132.19       |
