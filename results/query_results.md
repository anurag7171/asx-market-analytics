# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 48.86             | 133.63   | -28.63    |
| Healthcare       | 16        | 24.18             | 613.73   | -53.42    |
| Energy           | 11        | 20.59             | 60.85    | -27.25    |
| Industrials      | 24        | 10.68             | 104.83   | -43.91    |
| Utilities        | 7         | 6.13              | 30.06    | -5.99     |
| Financials       | 36        | -0.1              | 90.73    | -48.77    |
| Consumer Staples | 7         | -4.93             | 42.67    | -27.42    |
| Real Estate      | 17        | -15.35            | 8.23     | -51.44    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical           | Healthcare  | 613.7               |
| 2    | GGP  | Greatland Resources | Materials   | 133.6               |
| 3    | PLS  | PLS Group           | Materials   | 120.1               |
| 4    | RSG  | Resolute Mining     | Materials   | 106.8               |
| 5    | NWH  | NRW Holdings        | Industrials | 104.8               |
| 6    | VAU  | Vault Minerals      | Materials   | 99.6                |
| 7    | WGX  | Westgold Resources  | Materials   | 96.2                |
| 8    | L1G  | L1 Group            | Financials  | 90.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.3                 |
| DRO  | 254          | 104.0                 |
| EOS  | 254          | 100.4                 |
| ZIP  | 254          | 79.3                  |
| LTR  | 254          | 79.2                  |
| OBM  | 254          | 78.8                  |
| TUA  | 254          | 76.0                  |
| DYL  | 254          | 72.6                  |

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
| Materials              | 35                  |
| Financials             | 14                  |
| Healthcare             | 9                   |
| Energy                 | 9                   |
| Industrials            | 8                   |
| Communication Services | 7                   |
| Consumer Discretionary | 6                   |
| Utilities              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.18         | -73.8          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.79         | -72.8          |
| 360  | Life360                | Information Technology | 55.44    | 19.98        | -64.0          |
| WTC  | Wisetech Global        | Information Technology | 101.69   | 39.55        | -61.1          |
| GDG  | Generation Development | Financials             | 7.58     | 3.25         | -57.1          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.15         | -56.6          |
| COH  | Cochlear               | Healthcare             | 296.77   | 137.76       | -53.6          |
| ASB  | Austal                 | Industrials            | 8.76     | 4.11         | -53.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name       | max_drawdown_pct |
| ---- | ------------------ | ---------------- |
| TUA  | Tuas               | -76.0            |
| DRO  | Droneshield        | -74.3            |
| WTC  | Wisetech Global    | -71.7            |
| ZIP  | Zip                | -70.0            |
| COH  | Cochlear           | -69.7            |
| 360  | Life360            | -67.7            |
| PME  | Pro Medicus        | -66.2            |
| LTR  | Liontown Resources | -63.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.26                  |
| Information Technology | 45.69                  |
| Financials             | 43.85                  |
| Energy                 | 40.53                  |
| Healthcare             | 36.27                  |
| Consumer Staples       | 32.95                  |
| Consumer Discretionary | 27.4                   |
| Communication Services | 26.79                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 48.9           | 49.1               | 1.0                  |
| Healthcare             | 24.2           | 44.5               | 0.54                 |
| Energy                 | 20.6           | 41.7               | 0.49                 |
| Industrials            | 10.7           | 35.3               | 0.3                  |
| Utilities              | 6.1            | 27.6               | 0.22                 |
| Financials             | -0.1           | 30.5               | -0.0                 |
| Consumer Staples       | -4.9           | 28.2               | -0.17                |
| Information Technology | -17.4          | 48.6               | -0.36                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 154.96       |
| BHP  | BHP                    | Materials              | 260.3            | 66.4         |
| WBC  | Westpac                | Financials             | 136.3            | 33.68        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.46        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 79.46        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.94       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.98        |
| CSL  | CSL                    | Healthcare             | 67.4             | 173.88       |
