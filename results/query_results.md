# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 80.08             | 1554.17  | -58.92    |
| Materials        | 47        | 40.42             | 171.52   | -29.9     |
| Industrials      | 24        | 22.15             | 140.0    | -37.12    |
| Energy           | 11        | 13.85             | 45.64    | -31.57    |
| Financials       | 36        | 5.69              | 76.85    | -30.01    |
| Utilities        | 7         | 1.03              | 26.7     | -10.37    |
| Consumer Staples | 7         | -0.38             | 32.17    | -41.09    |
| Real Estate      | 17        | -2.96             | 18.22    | -38.89    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1554.2              |
| 2    | PLS  | PLS Group              | Materials              | 171.5               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 140.0               |
| 4    | NWH  | NRW Holdings           | Industrials            | 133.9               |
| 5    | CDA  | Codan                  | Information Technology | 127.0               |
| 6    | MIN  | Mineral Resources      | Materials              | 108.0               |
| 7    | ALK  | Alkane Resources       | Materials              | 103.7               |
| 8    | VAU  | Vault Minerals         | Materials              | 91.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 142.8                 |
| EOS  | 253          | 108.3                 |
| DRO  | 253          | 105.8                 |
| TUA  | 253          | 81.8                  |
| LTR  | 253          | 81.7                  |
| OBM  | 253          | 78.4                  |
| ZIP  | 253          | 76.8                  |
| CYL  | 253          | 72.0                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| EOS  | Electro Optic Systems  | 2025-08-05 | 43.4           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |
| MSB  | Mesoblast              | 2025-07-18 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 31                  |
| Real Estate            | 15                  |
| Healthcare             | 14                  |
| Industrials            | 13                  |
| Consumer Discretionary | 11                  |
| Materials              | 10                  |
| Consumer Staples       | 7                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| WTC  | Wisetech Global | Information Technology | 120.11   | 33.32        | -72.3          |
| TUA  | Tuas            | Communication Services | 8.32     | 2.32         | -72.1          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.27         | -65.6          |
| COH  | Cochlear        | Healthcare             | 313.15   | 121.3        | -61.3          |
| XRO  | Xero            | Information Technology | 181.0    | 70.24        | -61.2          |
| ASB  | Austal          | Industrials            | 8.76     | 3.54         | -59.6          |
| 360  | Life360         | Information Technology | 55.44    | 24.94        | -55.0          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 18.03        | -54.7          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name          | max_drawdown_pct |
| ---- | --------------------- | ---------------- |
| WTC  | Wisetech Global       | -76.1            |
| TUA  | Tuas                  | -76.0            |
| DRO  | Droneshield           | -74.0            |
| COH  | Cochlear              | -71.3            |
| ZIP  | Zip                   | -70.0            |
| 360  | Life360               | -67.7            |
| PME  | Pro Medicus           | -67.2            |
| TLX  | Telix Pharmaceuticals | -65.8            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.65                  |
| Information Technology | 45.26                  |
| Financials             | 44.07                  |
| Energy                 | 39.71                  |
| Healthcare             | 37.04                  |
| Consumer Staples       | 33.14                  |
| Consumer Discretionary | 27.68                  |
| Communication Services | 26.47                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 80.1           | 44.7               | 1.79                 |
| Materials              | 40.4           | 49.2               | 0.82                 |
| Industrials            | 22.2           | 36.0               | 0.61                 |
| Energy                 | 13.9           | 41.4               | 0.33                 |
| Financials             | 5.7            | 30.0               | 0.19                 |
| Utilities              | 1.0            | 27.4               | 0.04                 |
| Consumer Staples       | -0.4           | 28.2               | -0.01                |
| Information Technology | -6.3           | 46.7               | -0.13                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 170.0        |
| BHP  | BHP                    | Materials              | 260.3            | 58.34        |
| WBC  | Westpac                | Financials             | 136.3            | 36.9         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.46        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 91.32        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 254.01       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.05        |
| CSL  | CSL                    | Healthcare             | 67.4             | 121.34       |
