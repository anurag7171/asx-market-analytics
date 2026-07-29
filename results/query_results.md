# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 59.47             | 1287.23  | -60.88    |
| Materials        | 47        | 39.61             | 144.78   | -24.69    |
| Industrials      | 24        | 18.97             | 126.02   | -43.49    |
| Energy           | 11        | 14.49             | 51.55    | -27.64    |
| Financials       | 36        | 4.74              | 54.93    | -40.31    |
| Consumer Staples | 7         | 2.82              | 34.74    | -32.53    |
| Utilities        | 7         | 2.39              | 32.5     | -8.7      |
| Real Estate      | 17        | -1.34             | 23.26    | -53.71    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1287.2              |
| 2    | PLS  | PLS Group              | Materials              | 144.8               |
| 3    | NWH  | NRW Holdings           | Industrials            | 126.0               |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 112.4               |
| 5    | VAU  | Vault Minerals         | Materials              | 103.2               |
| 6    | GGP  | Greatland Resources    | Materials              | 95.2                |
| 7    | ALK  | Alkane Resources       | Materials              | 90.8                |
| 8    | CDA  | Codan                  | Information Technology | 89.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.4                 |
| EOS  | 254          | 108.7                 |
| DRO  | 254          | 104.7                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 80.6                  |
| OBM  | 254          | 78.8                  |
| ZIP  | 254          | 77.5                  |
| CYL  | 254          | 72.4                  |

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
| Real Estate            | 15                  |
| Industrials            | 15                  |
| Consumer Discretionary | 14                  |
| Healthcare             | 12                  |
| Materials              | 11                  |
| Consumer Staples       | 7                   |
| Communication Services | 7                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.15         | -74.2          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.79         | -72.9          |
| WTC  | Wisetech Global    | Information Technology | 119.84   | 35.52        | -70.4          |
| XRO  | Xero               | Information Technology | 180.99   | 70.47        | -61.1          |
| COH  | Cochlear           | Healthcare             | 313.15   | 122.5        | -60.9          |
| ASB  | Austal             | Industrials            | 8.76     | 3.56         | -59.4          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.1          | -58.1          |
| DYL  | Deep Yellow        | Energy                 | 2.91     | 1.27         | -56.4          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -76.0            |
| DRO  | Droneshield     | -74.0            |
| COH  | Cochlear        | -71.3            |
| ZIP  | Zip             | -70.0            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.5            |
| XRO  | Xero            | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.58                  |
| Information Technology | 45.28                  |
| Financials             | 44.02                  |
| Energy                 | 40.19                  |
| Healthcare             | 36.73                  |
| Consumer Staples       | 33.1                   |
| Consumer Discretionary | 27.79                  |
| Communication Services | 26.7                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 59.5           | 44.3               | 1.34                 |
| Materials        | 39.6           | 49.3               | 0.8                  |
| Industrials      | 19.0           | 36.1               | 0.53                 |
| Energy           | 14.5           | 41.6               | 0.35                 |
| Financials       | 4.7            | 30.2               | 0.16                 |
| Consumer Staples | 2.8            | 28.4               | 0.1                  |
| Utilities        | 2.4            | 27.8               | 0.09                 |
| Real Estate      | -1.3           | 21.6               | -0.06                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 178.66       |
| BHP  | BHP                    | Materials              | 260.3            | 60.18        |
| WBC  | Westpac                | Financials             | 136.3            | 37.94        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.73        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.61        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 254.95       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.2         |
| CSL  | CSL                    | Healthcare             | 67.4             | 128.07       |
