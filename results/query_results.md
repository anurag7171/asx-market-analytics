# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 49.92             | 148.3    | -24.77    |
| Healthcare       | 16        | 34.03             | 815.56   | -56.94    |
| Energy           | 11        | 19.93             | 63.24    | -30.82    |
| Industrials      | 24        | 15.8              | 123.82   | -50.24    |
| Financials       | 36        | 4.33              | 68.08    | -36.47    |
| Consumer Staples | 7         | 0.78              | 26.31    | -26.03    |
| Utilities        | 7         | 0.63              | 23.59    | -9.98     |
| Real Estate      | 17        | -5.77             | 12.87    | -48.57    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 815.6               |
| 2    | GGP  | Greatland Resources | Materials   | 148.3               |
| 3    | VAU  | Vault Minerals      | Materials   | 126.6               |
| 4    | NWH  | NRW Holdings        | Industrials | 123.8               |
| 5    | PLS  | PLS Group           | Materials   | 113.1               |
| 6    | OBM  | Ora Banda Mining    | Materials   | 100.7               |
| 7    | WGX  | Westgold Resources  | Materials   | 97.9                |
| 8    | ALK  | Alkane Resources    | Materials   | 95.0                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.6                 |
| DRO  | 254          | 104.2                 |
| EOS  | 254          | 99.8                  |
| LTR  | 254          | 79.5                  |
| OBM  | 254          | 78.5                  |
| ZIP  | 254          | 78.2                  |
| TUA  | 254          | 75.9                  |
| DYL  | 254          | 72.1                  |

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
| Materials              | 37                  |
| Financials             | 28                  |
| Real Estate            | 14                  |
| Industrials            | 13                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 12                  |
| Energy                 | 7                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.1          | -74.8          |
| DRO  | Droneshield        | Industrials            | 6.6      | 2.04         | -69.1          |
| WTC  | Wisetech Global    | Information Technology | 115.58   | 40.42        | -65.0          |
| 360  | Life360            | Information Technology | 55.44    | 23.5         | -57.6          |
| COH  | Cochlear           | Healthcare             | 307.14   | 131.68       | -57.1          |
| XRO  | Xero               | Information Technology | 172.7    | 77.4         | -55.2          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.92         | -53.2          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.25         | -52.8          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.1            |
| DRO  | Droneshield     | -74.3            |
| COH  | Cochlear        | -70.7            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.2            |
| CSL  | CSL             | -65.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.92                  |
| Information Technology | 45.81                  |
| Financials             | 44.25                  |
| Energy                 | 40.48                  |
| Healthcare             | 36.58                  |
| Consumer Staples       | 33.07                  |
| Consumer Discretionary | 27.63                  |
| Communication Services | 26.88                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 49.9           | 49.3               | 1.01                 |
| Healthcare             | 34.0           | 44.1               | 0.77                 |
| Energy                 | 19.9           | 41.8               | 0.48                 |
| Industrials            | 15.8           | 35.9               | 0.44                 |
| Financials             | 4.3            | 30.1               | 0.14                 |
| Consumer Staples       | 0.8            | 28.5               | 0.03                 |
| Utilities              | 0.6            | 28.4               | 0.02                 |
| Consumer Discretionary | -7.1           | 33.0               | -0.22                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 172.72       |
| BHP  | BHP                    | Materials              | 260.3            | 63.45        |
| WBC  | Westpac                | Financials             | 136.3            | 35.37        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.39        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.32        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 261.66       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.93        |
| CSL  | CSL                    | Healthcare             | 67.4             | 138.44       |
