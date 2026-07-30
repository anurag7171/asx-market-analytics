# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 55.98             | 1237.5   | -60.67    |
| Materials        | 47        | 35.11             | 144.06   | -26.56    |
| Industrials      | 24        | 16.29             | 119.97   | -45.44    |
| Energy           | 11        | 14.28             | 50.21    | -24.83    |
| Financials       | 36        | 3.07              | 52.0     | -41.05    |
| Utilities        | 7         | 1.02              | 28.65    | -10.25    |
| Consumer Staples | 7         | 0.59              | 32.38    | -34.03    |
| Real Estate      | 17        | -4.39             | 17.79    | -54.77    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1237.5              |
| 2    | PLS  | PLS Group              | Materials              | 144.1               |
| 3    | NWH  | NRW Holdings           | Industrials            | 120.0               |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 100.0               |
| 5    | VAU  | Vault Minerals         | Materials              | 95.5                |
| 6    | CDA  | Codan                  | Information Technology | 88.2                |
| 7    | MIN  | Mineral Resources      | Materials              | 87.8                |
| 8    | WGX  | Westgold Resources     | Materials              | 76.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.5                 |
| EOS  | 254          | 109.0                 |
| DRO  | 254          | 104.5                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.4                  |
| OBM  | 254          | 78.7                  |
| ZIP  | 254          | 77.6                  |
| CYL  | 254          | 72.5                  |

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
| Financials             | 27                  |
| Real Estate            | 14                  |
| Industrials            | 13                  |
| Consumer Discretionary | 13                  |
| Healthcare             | 11                  |
| Consumer Staples       | 7                   |
| Communication Services | 6                   |
| Materials              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.16         | -74.0          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.77         | -73.2          |
| WTC  | Wisetech Global    | Information Technology | 118.99   | 37.89        | -68.2          |
| LTR  | Liontown Resources | Materials              | 2.64     | 0.98         | -62.7          |
| COH  | Cochlear           | Healthcare             | 312.26   | 122.2        | -60.9          |
| XRO  | Xero               | Information Technology | 180.99   | 71.48        | -60.5          |
| ASB  | Austal             | Industrials            | 8.76     | 3.53         | -59.7          |
| DYL  | Deep Yellow        | Energy                 | 2.91     | 1.22         | -58.2          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.8            |
| DRO  | Droneshield     | -74.0            |
| COH  | Cochlear        | -71.2            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.4            |
| XRO  | Xero            | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.61                  |
| Information Technology | 45.36                  |
| Financials             | 44.04                  |
| Energy                 | 40.21                  |
| Healthcare             | 36.73                  |
| Consumer Staples       | 33.11                  |
| Consumer Discretionary | 27.8                   |
| Communication Services | 26.71                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 56.0           | 44.2               | 1.27                 |
| Materials        | 35.1           | 49.4               | 0.71                 |
| Industrials      | 16.3           | 36.1               | 0.45                 |
| Energy           | 14.3           | 41.6               | 0.34                 |
| Financials       | 3.1            | 30.2               | 0.1                  |
| Utilities        | 1.0            | 27.9               | 0.04                 |
| Consumer Staples | 0.6            | 28.4               | 0.02                 |
| Real Estate      | -4.4           | 21.6               | -0.2                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 178.25       |
| BHP  | BHP                    | Materials              | 260.3            | 59.15        |
| WBC  | Westpac                | Financials             | 136.3            | 38.15        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.51        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.22        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.0        |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.55        |
| CSL  | CSL                    | Healthcare             | 67.4             | 127.93       |
