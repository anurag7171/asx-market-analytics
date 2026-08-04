# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 49.37             | 1111.27  | -59.97    |
| Materials        | 47        | 43.51             | 154.01   | -22.44    |
| Industrials      | 24        | 22.04             | 156.27   | -44.83    |
| Energy           | 11        | 17.71             | 52.22    | -17.83    |
| Financials       | 36        | 5.92              | 58.81    | -36.69    |
| Utilities        | 7         | 1.91              | 28.93    | -11.02    |
| Consumer Staples | 7         | 1.18              | 30.57    | -27.23    |
| Real Estate      | 17        | -2.57             | 21.31    | -51.77    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1111.3              |
| 2    | EOS  | Electro Optic Systems  | Industrials            | 156.3               |
| 3    | PLS  | PLS Group              | Materials              | 154.0               |
| 4    | NWH  | NRW Holdings           | Industrials            | 130.0               |
| 5    | GGP  | Greatland Resources    | Materials              | 96.6                |
| 6    | VAU  | Vault Minerals         | Materials              | 94.3                |
| 7    | MIN  | Mineral Resources      | Materials              | 93.0                |
| 8    | CDA  | Codan                  | Information Technology | 92.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 141.2                 |
| EOS  | 254          | 109.5                 |
| DRO  | 254          | 104.1                 |
| TUA  | 254          | 81.5                  |
| LTR  | 254          | 81.3                  |
| OBM  | 254          | 78.2                  |
| ZIP  | 254          | 78.1                  |
| CYL  | 254          | 72.3                  |

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
| Financials             | 32                  |
| Materials              | 18                  |
| Industrials            | 16                  |
| Real Estate            | 14                  |
| Healthcare             | 11                  |
| Consumer Discretionary | 11                  |
| Consumer Staples       | 7                   |
| Communication Services | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.19         | -73.7          |
| DRO  | Droneshield        | Industrials            | 6.6      | 2.08         | -68.5          |
| WTC  | Wisetech Global    | Information Technology | 116.31   | 37.86        | -67.4          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.03         | -61.0          |
| COH  | Cochlear           | Healthcare             | 307.7    | 122.32       | -60.2          |
| XRO  | Xero               | Information Technology | 178.83   | 73.8         | -58.7          |
| ASB  | Austal             | Industrials            | 8.76     | 3.64         | -58.4          |
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
| Materials              | 48.69                  |
| Information Technology | 45.4                   |
| Financials             | 44.1                   |
| Energy                 | 40.31                  |
| Healthcare             | 36.59                  |
| Consumer Staples       | 33.07                  |
| Consumer Discretionary | 27.74                  |
| Communication Services | 26.71                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 49.4           | 44.1               | 1.12                 |
| Materials        | 43.5           | 49.3               | 0.88                 |
| Industrials      | 22.0           | 36.2               | 0.61                 |
| Energy           | 17.7           | 41.6               | 0.43                 |
| Financials       | 5.9            | 30.3               | 0.2                  |
| Utilities        | 1.9            | 28.1               | 0.07                 |
| Consumer Staples | 1.2            | 28.4               | 0.04                 |
| Real Estate      | -2.6           | 21.5               | -0.12                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 180.72       |
| BHP  | BHP                    | Materials              | 260.3            | 60.52        |
| WBC  | Westpac                | Financials             | 136.3            | 38.82        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.17        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.99        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 263.19       |
| NAB  | National Australia Ban | Financials             | 69.8             | 42.85        |
| CSL  | CSL                    | Healthcare             | 67.4             | 128.83       |
