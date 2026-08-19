# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 43.92             | 122.49   | -33.33    |
| Energy           | 11        | 21.96             | 56.9     | -23.28    |
| Healthcare       | 16        | 20.79             | 576.79   | -53.01    |
| Industrials      | 24        | 13.5              | 111.89   | -50.39    |
| Utilities        | 7         | 4.23              | 26.43    | -7.32     |
| Financials       | 36        | 2.66              | 81.96    | -39.63    |
| Consumer Staples | 7         | -3.31             | 26.39    | -27.54    |
| Real Estate      | 17        | -11.68            | 10.83    | -51.59    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 576.8               |
| 2    | GGP  | Greatland Resources  | Materials   | 122.5               |
| 3    | VAU  | Vault Minerals       | Materials   | 121.0               |
| 4    | NWH  | NRW Holdings         | Industrials | 111.9               |
| 5    | PLS  | PLS Group            | Materials   | 108.8               |
| 6    | PDI  | Predictive Discovery | Materials   | 88.9                |
| 7    | OBM  | Ora Banda Mining     | Materials   | 85.3                |
| 8    | EMR  | Emerald Resources    | Materials   | 84.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.4                 |
| DRO  | 254          | 104.1                 |
| EOS  | 254          | 99.7                  |
| LTR  | 254          | 79.0                  |
| ZIP  | 254          | 78.6                  |
| OBM  | 254          | 78.5                  |
| TUA  | 254          | 76.1                  |
| 360  | 254          | 72.4                  |

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
| Materials              | 35                  |
| Financials             | 18                  |
| Industrials            | 13                  |
| Healthcare             | 13                  |
| Energy                 | 9                   |
| Communication Services | 6                   |
| Information Technology | 5                   |
| Consumer Staples       | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.09         | -74.9          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.89         | -71.4          |
| WTC  | Wisetech Global    | Information Technology | 115.37   | 39.58        | -65.7          |
| 360  | Life360            | Information Technology | 55.44    | 20.94        | -62.2          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.15         | -56.4          |
| COH  | Cochlear           | Healthcare             | 297.81   | 137.3        | -53.9          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.91         | -53.3          |
| ARB  | ARB Corporation    | Consumer Discretionary | 39.79    | 19.02        | -52.2          |

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
| XRO  | Xero            | -64.1            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.06                  |
| Information Technology | 45.75                  |
| Financials             | 44.14                  |
| Energy                 | 40.47                  |
| Healthcare             | 36.82                  |
| Consumer Staples       | 33.08                  |
| Consumer Discretionary | 27.61                  |
| Communication Services | 26.92                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 43.9           | 49.3               | 0.89                 |
| Energy                 | 22.0           | 41.7               | 0.53                 |
| Healthcare             | 20.8           | 44.3               | 0.47                 |
| Industrials            | 13.5           | 36.6               | 0.37                 |
| Utilities              | 4.2            | 27.8               | 0.15                 |
| Financials             | 2.7            | 30.2               | 0.09                 |
| Consumer Staples       | -3.3           | 28.8               | -0.11                |
| Information Technology | -14.6          | 48.6               | -0.3                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 160.71       |
| BHP  | BHP                    | Materials              | 260.3            | 63.71        |
| WBC  | Westpac                | Financials             | 136.3            | 34.44        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.62        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 84.26        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 254.21       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.92        |
| CSL  | CSL                    | Healthcare             | 67.4             | 166.48       |
