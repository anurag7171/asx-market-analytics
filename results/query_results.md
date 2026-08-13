# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 47.62             | 147.99   | -26.26    |
| Healthcare       | 16        | 26.65             | 697.96   | -56.39    |
| Energy           | 11        | 20.5              | 63.73    | -26.04    |
| Industrials      | 24        | 14.8              | 123.25   | -52.03    |
| Financials       | 36        | 4.88              | 68.08    | -38.71    |
| Utilities        | 7         | 3.84              | 23.13    | -6.82     |
| Consumer Staples | 7         | 0.28              | 26.55    | -23.31    |
| Real Estate      | 17        | -6.59             | 14.43    | -49.71    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 698.0               |
| 2    | GGP  | Greatland Resources | Materials   | 148.0               |
| 3    | PLS  | PLS Group           | Materials   | 127.1               |
| 4    | NWH  | NRW Holdings        | Industrials | 123.3               |
| 5    | VAU  | Vault Minerals      | Materials   | 122.4               |
| 6    | WGX  | Westgold Resources  | Materials   | 97.5                |
| 7    | OBM  | Ora Banda Mining    | Materials   | 95.7                |
| 8    | ALK  | Alkane Resources    | Materials   | 92.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.5                 |
| DRO  | 254          | 104.2                 |
| EOS  | 254          | 99.8                  |
| LTR  | 254          | 79.4                  |
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
| Materials              | 36                  |
| Financials             | 26                  |
| Industrials            | 13                  |
| Real Estate            | 12                  |
| Healthcare             | 12                  |
| Consumer Discretionary | 12                  |
| Energy                 | 7                   |
| Consumer Staples       | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.09         | -74.9          |
| DRO  | Droneshield        | Industrials            | 6.6      | 2.01         | -69.5          |
| WTC  | Wisetech Global    | Information Technology | 115.58   | 41.1         | -64.4          |
| 360  | Life360            | Information Technology | 55.44    | 23.46        | -57.7          |
| COH  | Cochlear           | Healthcare             | 307.14   | 133.93       | -56.4          |
| XRO  | Xero               | Information Technology | 171.5    | 77.2         | -55.0          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.23         | -53.4          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.88         | -53.4          |

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
| Materials              | 48.95                  |
| Information Technology | 45.76                  |
| Financials             | 44.27                  |
| Energy                 | 40.45                  |
| Healthcare             | 36.57                  |
| Consumer Staples       | 33.06                  |
| Consumer Discretionary | 27.58                  |
| Communication Services | 26.93                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 47.6           | 49.3               | 0.97                 |
| Healthcare             | 26.7           | 44.1               | 0.6                  |
| Energy                 | 20.5           | 41.7               | 0.49                 |
| Industrials            | 14.8           | 36.1               | 0.41                 |
| Financials             | 4.9            | 30.1               | 0.16                 |
| Utilities              | 3.8            | 28.0               | 0.14                 |
| Consumer Staples       | 0.3            | 28.6               | 0.01                 |
| Information Technology | -12.1          | 48.3               | -0.25                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 169.0        |
| BHP  | BHP                    | Materials              | 260.3            | 63.45        |
| WBC  | Westpac                | Financials             | 136.3            | 35.7         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.04        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 88.48        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 260.08       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.41        |
| CSL  | CSL                    | Healthcare             | 67.4             | 137.52       |
