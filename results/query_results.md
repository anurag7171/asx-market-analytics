# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 52.46             | 1196.0   | -63.24    |
| Materials        | 47        | 36.06             | 131.15   | -29.42    |
| Industrials      | 24        | 18.35             | 128.74   | -38.74    |
| Energy           | 11        | 12.74             | 45.02    | -33.01    |
| Financials       | 36        | 4.66              | 59.31    | -39.51    |
| Utilities        | 7         | 2.05              | 30.55    | -11.08    |
| Consumer Staples | 7         | -1.79             | 28.09    | -41.38    |
| Real Estate      | 17        | -5.24             | 15.21    | -42.47    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1196.0              |
| 2    | PLS  | PLS Group              | Materials              | 131.1               |
| 3    | NWH  | NRW Holdings           | Industrials            | 128.7               |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 119.5               |
| 5    | CDA  | Codan                  | Information Technology | 106.1               |
| 6    | ALK  | Alkane Resources       | Materials              | 102.9               |
| 7    | VAU  | Vault Minerals         | Materials              | 95.7                |
| 8    | MIN  | Mineral Resources      | Materials              | 78.8                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.5                 |
| EOS  | 254          | 108.1                 |
| DRO  | 254          | 104.2                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 80.4                  |
| OBM  | 254          | 78.6                  |
| ZIP  | 254          | 77.2                  |
| CYL  | 254          | 72.1                  |

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
| Financials             | 30                  |
| Materials              | 19                  |
| Industrials            | 15                  |
| Real Estate            | 13                  |
| Healthcare             | 11                  |
| Consumer Discretionary | 9                   |
| Consumer Staples       | 7                   |
| Energy                 | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.14         | -74.3          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 31.48        | -73.8          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.21         | -66.5          |
| XRO  | Xero            | Information Technology | 180.99   | 64.45        | -64.4          |
| COH  | Cochlear        | Healthcare             | 313.15   | 112.11       | -64.2          |
| ASB  | Austal          | Industrials            | 8.76     | 3.78         | -56.8          |
| 360  | Life360         | Information Technology | 55.44    | 24.12        | -56.5          |
| CSL  | CSL             | Healthcare             | 265.45   | 115.75       | -56.4          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| WTC  | Wisetech Global | -76.1            |
| TUA  | Tuas            | -76.0            |
| DRO  | Droneshield     | -74.0            |
| COH  | Cochlear        | -71.3            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.6            |
| CSL  | CSL             | -65.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.64                  |
| Information Technology | 45.12                  |
| Financials             | 43.95                  |
| Energy                 | 40.1                   |
| Healthcare             | 36.86                  |
| Consumer Staples       | 33.13                  |
| Consumer Discretionary | 27.68                  |
| Communication Services | 26.54                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 52.5           | 44.1               | 1.19                 |
| Materials        | 36.1           | 49.2               | 0.73                 |
| Industrials      | 18.3           | 35.9               | 0.51                 |
| Energy           | 12.7           | 41.5               | 0.31                 |
| Financials       | 4.7            | 30.2               | 0.15                 |
| Utilities        | 2.1            | 27.6               | 0.07                 |
| Consumer Staples | -1.8           | 28.2               | -0.06                |
| Real Estate      | -5.2           | 21.6               | -0.24                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 172.3        |
| BHP  | BHP                    | Materials              | 260.3            | 60.63        |
| WBC  | Westpac                | Financials             | 136.3            | 36.64        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.96        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 88.11        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 253.75       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.81        |
| CSL  | CSL                    | Healthcare             | 67.4             | 115.75       |
