# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 55.67             | 1266.67  | -63.16    |
| Materials        | 47        | 40.29             | 150.0    | -27.6     |
| Industrials      | 24        | 20.45             | 140.32   | -37.66    |
| Energy           | 11        | 11.69             | 44.06    | -31.45    |
| Financials       | 36        | 4.25              | 58.58    | -42.28    |
| Utilities        | 7         | 1.66              | 31.36    | -9.49     |
| Consumer Staples | 7         | -0.61             | 31.31    | -38.9     |
| Real Estate      | 17        | -4.25             | 17.41    | -53.5     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1266.7              |
| 2    | PLS  | PLS Group              | Materials              | 150.0               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 140.3               |
| 4    | NWH  | NRW Holdings           | Industrials            | 136.6               |
| 5    | VAU  | Vault Minerals         | Materials              | 108.9               |
| 6    | CDA  | Codan                  | Information Technology | 99.1                |
| 7    | ALK  | Alkane Resources       | Materials              | 91.0                |
| 8    | WGX  | Westgold Resources     | Materials              | 86.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 143.7                 |
| EOS  | 253          | 108.6                 |
| DRO  | 253          | 104.1                 |
| TUA  | 253          | 81.9                  |
| LTR  | 253          | 80.5                  |
| OBM  | 253          | 79.0                  |
| ZIP  | 253          | 77.5                  |
| CYL  | 253          | 72.5                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| EOS  | Electro Optic Systems  | 2025-08-05 | 43.4           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 29                  |
| Materials              | 18                  |
| Industrials            | 15                  |
| Real Estate            | 14                  |
| Healthcare             | 11                  |
| Consumer Discretionary | 9                   |
| Consumer Staples       | 7                   |
| Energy                 | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.16         | -74.0          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 32.12        | -73.3          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.08         | -68.5          |
| XRO  | Xero            | Information Technology | 180.99   | 65.29        | -63.9          |
| COH  | Cochlear        | Healthcare             | 313.15   | 114.5        | -63.4          |
| PXA  | Pexa Group      | Real Estate            | 16.92    | 7.24         | -57.2          |
| ASB  | Austal          | Industrials            | 8.76     | 3.79         | -56.7          |
| CSL  | CSL             | Healthcare             | 265.45   | 116.39       | -56.2          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| WTC  | Wisetech Global | -76.1            |
| TUA  | Tuas            | -76.0            |
| DRO  | Droneshield     | -74.0            |
| COH  | Cochlear        | -71.3            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.5            |
| XRO  | Xero            | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.57                  |
| Information Technology | 45.23                  |
| Financials             | 43.97                  |
| Energy                 | 40.11                  |
| Healthcare             | 36.7                   |
| Consumer Staples       | 33.07                  |
| Consumer Discretionary | 27.77                  |
| Communication Services | 26.62                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 55.7           | 44.2               | 1.26                 |
| Materials        | 40.3           | 49.4               | 0.82                 |
| Industrials      | 20.5           | 36.1               | 0.57                 |
| Energy           | 11.7           | 41.6               | 0.28                 |
| Financials       | 4.3            | 30.2               | 0.14                 |
| Utilities        | 1.7            | 27.8               | 0.06                 |
| Consumer Staples | -0.6           | 28.3               | -0.02                |
| Real Estate      | -4.2           | 21.6               | -0.2                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 176.07       |
| BHP  | BHP                    | Materials              | 260.3            | 60.1         |
| WBC  | Westpac                | Financials             | 136.3            | 37.68        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.89        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 87.4         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 257.93       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.94        |
| CSL  | CSL                    | Healthcare             | 67.4             | 116.39       |
