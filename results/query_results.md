# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 47.32             | 1074.68  | -59.0     |
| Materials        | 47        | 46.93             | 152.2    | -23.55    |
| Industrials      | 24        | 18.05             | 125.66   | -47.9     |
| Energy           | 11        | 15.74             | 53.59    | -23.75    |
| Financials       | 36        | 4.89              | 60.77    | -33.65    |
| Consumer Staples | 7         | 1.01              | 30.25    | -29.72    |
| Utilities        | 7         | 0.26              | 23.57    | -12.22    |
| Real Estate      | 17        | -4.5              | 16.86    | -52.31    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 1074.7              |
| 2    | PLS  | PLS Group           | Materials   | 152.2               |
| 3    | NWH  | NRW Holdings        | Industrials | 125.7               |
| 4    | GGP  | Greatland Resources | Materials   | 114.3               |
| 5    | VAU  | Vault Minerals      | Materials   | 113.4               |
| 6    | WGX  | Westgold Resources  | Materials   | 98.7                |
| 7    | OBM  | Ora Banda Mining    | Materials   | 93.4                |
| 8    | ALK  | Alkane Resources    | Materials   | 89.0                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 140.4                 |
| DRO  | 254          | 104.1                 |
| EOS  | 254          | 100.7                 |
| TUA  | 254          | 81.5                  |
| LTR  | 254          | 81.3                  |
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
| Financials             | 31                  |
| Materials              | 29                  |
| Industrials            | 15                  |
| Real Estate            | 14                  |
| Healthcare             | 14                  |
| Consumer Discretionary | 12                  |
| Consumer Staples       | 7                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.16         | -74.0          |
| WTC  | Wisetech Global    | Information Technology | 116.31   | 39.3         | -66.2          |
| DRO  | Droneshield        | Industrials            | 6.6      | 2.28         | -65.5          |
| COH  | Cochlear           | Healthcare             | 307.7    | 125.99       | -59.1          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.08         | -59.1          |
| XRO  | Xero               | Information Technology | 178.83   | 75.45        | -57.8          |
| ASB  | Austal             | Industrials            | 8.76     | 3.84         | -56.2          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.63         | -54.9          |

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
| Materials              | 48.82                  |
| Information Technology | 45.46                  |
| Financials             | 44.19                  |
| Energy                 | 40.39                  |
| Healthcare             | 36.59                  |
| Consumer Staples       | 33.06                  |
| Consumer Discretionary | 27.78                  |
| Communication Services | 26.81                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 47.3           | 44.0               | 1.07                 |
| Materials              | 46.9           | 49.4               | 0.95                 |
| Industrials            | 18.1           | 35.8               | 0.5                  |
| Energy                 | 15.7           | 41.6               | 0.38                 |
| Financials             | 4.9            | 30.3               | 0.16                 |
| Consumer Staples       | 1.0            | 28.4               | 0.04                 |
| Utilities              | 0.3            | 28.2               | 0.01                 |
| Consumer Discretionary | -4.9           | 33.0               | -0.15                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 179.87       |
| BHP  | BHP                    | Materials              | 260.3            | 62.82        |
| WBC  | Westpac                | Financials             | 136.3            | 38.53        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.11        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 91.0         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 267.25       |
| NAB  | National Australia Ban | Financials             | 69.8             | 42.7         |
| CSL  | CSL                    | Healthcare             | 67.4             | 132.36       |
