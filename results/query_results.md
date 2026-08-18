# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 43.91             | 131.21   | -35.35    |
| Energy                 | 11        | 22.13             | 62.73    | -23.58    |
| Healthcare             | 16        | 17.41             | 553.91   | -51.4     |
| Industrials            | 24        | 12.45             | 110.75   | -51.3     |
| Utilities              | 7         | 4.53              | 23.7     | -5.59     |
| Financials             | 36        | 2.68              | 76.85    | -39.89    |
| Consumer Staples       | 7         | -2.75             | 25.24    | -28.19    |
| Consumer Discretionary | 15        | -11.43            | 29.36    | -44.44    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 553.9               |
| 2    | GGP  | Greatland Resources  | Materials   | 131.2               |
| 3    | VAU  | Vault Minerals       | Materials   | 119.9               |
| 4    | PLS  | PLS Group            | Materials   | 117.2               |
| 5    | NWH  | NRW Holdings         | Industrials | 110.7               |
| 6    | PDI  | Predictive Discovery | Materials   | 93.2                |
| 7    | OBM  | Ora Banda Mining     | Materials   | 93.0                |
| 8    | WGX  | Westgold Resources   | Materials   | 87.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.4                 |
| DRO  | 254          | 104.1                 |
| EOS  | 254          | 99.7                  |
| LTR  | 254          | 78.9                  |
| OBM  | 254          | 78.6                  |
| ZIP  | 254          | 78.5                  |
| TUA  | 254          | 76.1                  |
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
| Financials             | 22                  |
| Industrials            | 12                  |
| Healthcare             | 12                  |
| Energy                 | 10                  |
| Consumer Discretionary | 8                   |
| Information Technology | 6                   |
| Consumer Staples       | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.1          | -74.8          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.88         | -71.6          |
| WTC  | Wisetech Global    | Information Technology | 115.58   | 43.35        | -62.5          |
| 360  | Life360            | Information Technology | 55.44    | 22.49        | -59.4          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.21         | -54.4          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.88         | -53.4          |
| COH  | Cochlear           | Healthcare             | 297.81   | 141.2        | -52.6          |
| ASB  | Austal             | Industrials            | 8.76     | 4.23         | -51.7          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.1            |
| DRO  | Droneshield     | -74.3            |
| ZIP  | Zip             | -70.0            |
| COH  | Cochlear        | -69.8            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.2            |
| CSL  | CSL             | -65.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.01                  |
| Information Technology | 45.63                  |
| Financials             | 44.12                  |
| Energy                 | 40.42                  |
| Healthcare             | 36.67                  |
| Consumer Staples       | 33.12                  |
| Consumer Discretionary | 27.59                  |
| Communication Services | 26.92                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 43.9           | 49.3               | 0.89                 |
| Energy                 | 22.1           | 41.6               | 0.53                 |
| Healthcare             | 17.4           | 44.5               | 0.39                 |
| Industrials            | 12.4           | 36.5               | 0.34                 |
| Utilities              | 4.5            | 27.8               | 0.16                 |
| Financials             | 2.7            | 30.2               | 0.09                 |
| Consumer Staples       | -2.7           | 28.8               | -0.1                 |
| Information Technology | -12.7          | 48.5               | -0.26                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 162.63       |
| BHP  | BHP                    | Materials              | 260.3            | 63.85        |
| WBC  | Westpac                | Financials             | 136.3            | 34.66        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.68        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 84.22        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 255.42       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.2         |
| CSL  | CSL                    | Healthcare             | 67.4             | 157.82       |
