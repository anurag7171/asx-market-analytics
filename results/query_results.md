# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 66.31             | 1412.5   | -61.59    |
| Materials        | 47        | 41.88             | 158.57   | -26.46    |
| Energy           | 11        | 17.88             | 51.69    | -17.62    |
| Industrials      | 24        | 16.66             | 124.13   | -54.8     |
| Financials       | 36        | 2.96              | 56.59    | -41.62    |
| Utilities        | 7         | 0.05              | 28.77    | -10.13    |
| Consumer Staples | 7         | -0.29             | 29.8     | -33.17    |
| Real Estate      | 17        | -4.27             | 17.95    | -53.27    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1412.5              |
| 2    | PLS  | PLS Group              | Materials              | 158.6               |
| 3    | NWH  | NRW Holdings           | Industrials            | 124.1               |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 108.4               |
| 5    | VAU  | Vault Minerals         | Materials              | 103.9               |
| 6    | MIN  | Mineral Resources      | Materials              | 102.8               |
| 7    | CDA  | Codan                  | Information Technology | 93.4                |
| 8    | GGP  | Greatland Resources    | Materials              | 87.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.9                 |
| EOS  | 254          | 109.3                 |
| DRO  | 254          | 102.9                 |
| TUA  | 254          | 81.5                  |
| LTR  | 254          | 81.2                  |
| OBM  | 254          | 78.2                  |
| ZIP  | 254          | 78.0                  |
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
| Consumer Discretionary | 12                  |
| Healthcare             | 10                  |
| Industrials            | 9                   |
| Materials              | 8                   |
| Consumer Staples       | 7                   |
| Communication Services | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.7          | -74.3          |
| TUA  | Tuas               | Communication Services | 8.32     | 2.16         | -74.0          |
| WTC  | Wisetech Global    | Information Technology | 118.99   | 36.3         | -69.5          |
| LTR  | Liontown Resources | Materials              | 2.64     | 0.96         | -63.4          |
| COH  | Cochlear           | Healthcare             | 312.26   | 119.94       | -61.6          |
| XRO  | Xero               | Information Technology | 180.99   | 70.0         | -61.3          |
| ASB  | Austal             | Industrials            | 8.76     | 3.61         | -58.8          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 7.42         | -56.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.8            |
| DRO  | Droneshield     | -74.3            |
| COH  | Cochlear        | -71.2            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.4            |
| XRO  | Xero            | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.69                  |
| Information Technology | 45.43                  |
| Financials             | 44.08                  |
| Energy                 | 40.27                  |
| Healthcare             | 36.72                  |
| Consumer Staples       | 33.11                  |
| Consumer Discretionary | 27.78                  |
| Communication Services | 26.74                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 66.3           | 44.3               | 1.5                  |
| Materials        | 41.9           | 49.3               | 0.85                 |
| Industrials      | 16.7           | 36.1               | 0.46                 |
| Energy           | 17.9           | 41.6               | 0.43                 |
| Financials       | 3.0            | 30.2               | 0.1                  |
| Utilities        | 0.1            | 28.0               | 0.0                  |
| Consumer Staples | -0.3           | 28.4               | -0.01                |
| Real Estate      | -4.3           | 21.5               | -0.2                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 177.53       |
| BHP  | BHP                    | Materials              | 260.3            | 60.31        |
| WBC  | Westpac                | Financials             | 136.3            | 37.87        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.31        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.36        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 253.09       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.33        |
| CSL  | CSL                    | Healthcare             | 67.4             | 123.06       |
