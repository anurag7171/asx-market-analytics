# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 47.28             | 141.63   | -23.4     |
| Healthcare             | 16        | 33.55             | 816.67   | -58.37    |
| Energy                 | 11        | 15.92             | 55.39    | -33.26    |
| Industrials            | 24        | 15.52             | 119.92   | -44.81    |
| Financials             | 36        | 5.17              | 58.58    | -34.15    |
| Consumer Staples       | 7         | 2.53              | 30.76    | -23.68    |
| Utilities              | 7         | -0.35             | 22.07    | -13.94    |
| Consumer Discretionary | 15        | -4.27             | 29.33    | -39.76    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 816.7               |
| 2    | GGP  | Greatland Resources | Materials   | 141.6               |
| 3    | VAU  | Vault Minerals      | Materials   | 123.6               |
| 4    | NWH  | NRW Holdings        | Industrials | 119.9               |
| 5    | PLS  | PLS Group           | Materials   | 104.3               |
| 6    | OBM  | Ora Banda Mining    | Materials   | 102.2               |
| 7    | WGX  | Westgold Resources  | Materials   | 94.6                |
| 8    | SGM  | Sims Metal          | Materials   | 85.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 138.8                 |
| DRO  | 253          | 104.3                 |
| EOS  | 253          | 100.4                 |
| TUA  | 253          | 81.6                  |
| LTR  | 253          | 79.9                  |
| OBM  | 253          | 78.7                  |
| ZIP  | 253          | 78.3                  |
| DYL  | 253          | 72.2                  |

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
| Financials             | 27                  |
| Real Estate            | 14                  |
| Industrials            | 14                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 12                  |
| Energy                 | 7                   |
| Consumer Staples       | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.14         | -74.3          |
| DRO  | Droneshield        | Industrials            | 6.6      | 2.18         | -67.0          |
| WTC  | Wisetech Global    | Information Technology | 115.58   | 41.05        | -64.5          |
| COH  | Cochlear           | Healthcare             | 307.14   | 127.11       | -58.6          |
| ASB  | Austal             | Industrials            | 8.76     | 3.84         | -56.2          |
| XRO  | Xero               | Information Technology | 176.54   | 77.75        | -56.0          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.2          | -54.5          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 8.01         | -52.7          |

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
| Information Technology | 45.55                  |
| Financials             | 44.25                  |
| Energy                 | 40.43                  |
| Healthcare             | 36.57                  |
| Consumer Staples       | 33.17                  |
| Consumer Discretionary | 27.73                  |
| Communication Services | 26.8                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 47.3           | 49.4               | 0.96                 |
| Healthcare             | 33.5           | 44.1               | 0.76                 |
| Industrials            | 15.5           | 35.8               | 0.43                 |
| Energy                 | 15.9           | 41.7               | 0.38                 |
| Financials             | 5.2            | 30.1               | 0.17                 |
| Consumer Staples       | 2.5            | 28.6               | 0.09                 |
| Utilities              | -0.3           | 28.2               | -0.01                |
| Consumer Discretionary | -4.3           | 32.9               | -0.13                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 174.27       |
| BHP  | BHP                    | Materials              | 260.3            | 63.52        |
| WBC  | Westpac                | Financials             | 136.3            | 35.7         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.09        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.54        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 264.07       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.22        |
| CSL  | CSL                    | Healthcare             | 67.4             | 134.47       |
