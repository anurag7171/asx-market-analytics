# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 45.2              | 137.2    | -28.97    |
| Energy           | 11        | 19.53             | 53.72    | -26.07    |
| Healthcare       | 16        | 18.13             | 586.79   | -55.46    |
| Industrials      | 24        | 14.03             | 126.54   | -53.66    |
| Financials       | 36        | 4.01              | 61.5     | -40.36    |
| Utilities        | 7         | 3.19              | 24.03    | -6.94     |
| Consumer Staples | 7         | -0.33             | 26.66    | -21.75    |
| Real Estate      | 17        | -7.81             | 13.21    | -50.38    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare             | 586.8               |
| 2    | GGP  | Greatland Resources | Materials              | 137.2               |
| 3    | NWH  | NRW Holdings        | Industrials            | 126.5               |
| 4    | PLS  | PLS Group           | Materials              | 125.5               |
| 5    | VAU  | Vault Minerals      | Materials              | 116.9               |
| 6    | OBM  | Ora Banda Mining    | Materials              | 92.6                |
| 7    | WGX  | Westgold Resources  | Materials              | 89.2                |
| 8    | CDA  | Codan               | Information Technology | 86.8                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.6                 |
| DRO  | 254          | 104.2                 |
| EOS  | 254          | 99.5                  |
| LTR  | 254          | 78.9                  |
| OBM  | 254          | 78.6                  |
| ZIP  | 254          | 78.2                  |
| TUA  | 254          | 76.0                  |
| DYL  | 254          | 72.2                  |

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
| Financials             | 24                  |
| Consumer Discretionary | 12                  |
| Real Estate            | 11                  |
| Industrials            | 11                  |
| Healthcare             | 10                  |
| Energy                 | 7                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.22         | -73.3          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.96         | -70.3          |
| WTC  | Wisetech Global    | Information Technology | 115.58   | 43.38        | -62.5          |
| 360  | Life360            | Information Technology | 55.44    | 23.54        | -57.5          |
| COH  | Cochlear           | Healthcare             | 302.96   | 133.6        | -55.9          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.86         | -53.5          |
| XRO  | Xero               | Information Technology | 171.5    | 81.48        | -52.5          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.27         | -51.7          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.1            |
| DRO  | Droneshield     | -74.3            |
| COH  | Cochlear        | -70.3            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.2            |
| CSL  | CSL             | -65.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.99                  |
| Information Technology | 45.74                  |
| Financials             | 44.24                  |
| Energy                 | 40.43                  |
| Healthcare             | 36.55                  |
| Consumer Staples       | 33.07                  |
| Consumer Discretionary | 27.52                  |
| Communication Services | 26.96                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 45.2           | 49.3               | 0.92                 |
| Energy                 | 19.5           | 41.7               | 0.47                 |
| Healthcare             | 18.1           | 44.1               | 0.41                 |
| Industrials            | 14.0           | 36.1               | 0.39                 |
| Financials             | 4.0            | 30.1               | 0.13                 |
| Utilities              | 3.2            | 27.8               | 0.11                 |
| Consumer Staples       | -0.3           | 28.6               | -0.01                |
| Information Technology | -11.2          | 48.4               | -0.23                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 167.17       |
| BHP  | BHP                    | Materials              | 260.3            | 61.35        |
| WBC  | Westpac                | Financials             | 136.3            | 35.37        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.89        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 88.7         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 261.9        |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.37        |
| CSL  | CSL                    | Healthcare             | 67.4             | 136.5        |
