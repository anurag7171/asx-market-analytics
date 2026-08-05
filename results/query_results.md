# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 61.87             | 1308.96  | -60.33    |
| Materials        | 47        | 46.86             | 153.96   | -23.07    |
| Industrials      | 24        | 19.09             | 131.49   | -45.25    |
| Energy           | 11        | 17.19             | 58.07    | -22.37    |
| Financials       | 36        | 5.37              | 62.23    | -33.1     |
| Utilities        | 7         | 0.93              | 26.54    | -13.17    |
| Consumer Staples | 7         | 0.49              | 30.16    | -29.01    |
| Real Estate      | 17        | -3.54             | 20.49    | -52.17    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 1309.0              |
| 2    | PLS  | PLS Group           | Materials   | 154.0               |
| 3    | NWH  | NRW Holdings        | Industrials | 131.5               |
| 4    | VAU  | Vault Minerals      | Materials   | 106.7               |
| 5    | GGP  | Greatland Resources | Materials   | 106.3               |
| 6    | WGX  | Westgold Resources  | Materials   | 97.0                |
| 7    | OBM  | Ora Banda Mining    | Materials   | 94.6                |
| 8    | ALK  | Alkane Resources    | Materials   | 92.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 141.3                 |
| DRO  | 254          | 104.0                 |
| EOS  | 254          | 100.8                 |
| TUA  | 254          | 81.5                  |
| LTR  | 254          | 81.3                  |
| OBM  | 254          | 78.6                  |
| ZIP  | 254          | 78.3                  |
| CYL  | 254          | 72.2                  |

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
| Financials             | 33                  |
| Materials              | 28                  |
| Industrials            | 19                  |
| Real Estate            | 15                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 12                  |
| Consumer Staples       | 7                   |
| Communication Services | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.2          | -73.6          |
| DRO  | Droneshield        | Industrials            | 6.6      | 2.19         | -66.8          |
| WTC  | Wisetech Global    | Information Technology | 116.31   | 39.91        | -65.7          |
| COH  | Cochlear           | Healthcare             | 307.7    | 122.0        | -60.4          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.06         | -59.8          |
| XRO  | Xero               | Information Technology | 178.83   | 75.14        | -58.0          |
| ASB  | Austal             | Industrials            | 8.76     | 3.8          | -56.6          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.7          | -54.5          |

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
| Materials              | 48.76                  |
| Information Technology | 45.49                  |
| Financials             | 44.17                  |
| Energy                 | 40.38                  |
| Healthcare             | 36.63                  |
| Consumer Staples       | 33.06                  |
| Consumer Discretionary | 27.79                  |
| Communication Services | 26.77                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 61.9           | 44.1               | 1.4                  |
| Materials        | 46.9           | 49.4               | 0.95                 |
| Industrials      | 19.1           | 35.8               | 0.53                 |
| Energy           | 17.2           | 41.6               | 0.41                 |
| Financials       | 5.4            | 30.3               | 0.18                 |
| Utilities        | 0.9            | 28.2               | 0.03                 |
| Consumer Staples | 0.5            | 28.4               | 0.02                 |
| Real Estate      | -3.5           | 21.4               | -0.16                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 178.23       |
| BHP  | BHP                    | Materials              | 260.3            | 62.54        |
| WBC  | Westpac                | Financials             | 136.3            | 38.53        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.01        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 91.28        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 267.09       |
| NAB  | National Australia Ban | Financials             | 69.8             | 42.53        |
| CSL  | CSL                    | Healthcare             | 67.4             | 130.66       |
