# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 78.5              | 1529.17  | -58.28    |
| Materials        | 47        | 41.62             | 174.55   | -30.4     |
| Industrials      | 24        | 22.15             | 138.51   | -37.3     |
| Energy           | 11        | 14.07             | 48.85    | -30.0     |
| Financials       | 36        | 4.96              | 71.73    | -31.52    |
| Utilities        | 7         | 0.65              | 27.46    | -10.07    |
| Consumer Staples | 7         | -0.47             | 30.81    | -38.88    |
| Real Estate      | 17        | -4.01             | 16.73    | -38.59    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1529.2              |
| 2    | PLS  | PLS Group              | Materials              | 174.5               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 138.5               |
| 4    | NWH  | NRW Holdings           | Industrials            | 133.2               |
| 5    | CDA  | Codan                  | Information Technology | 126.7               |
| 6    | MIN  | Mineral Resources      | Materials              | 111.1               |
| 7    | ALK  | Alkane Resources       | Materials              | 106.6               |
| 8    | VAU  | Vault Minerals         | Materials              | 94.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.5                 |
| EOS  | 254          | 108.1                 |
| DRO  | 254          | 105.6                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.5                  |
| OBM  | 254          | 78.3                  |
| ZIP  | 254          | 76.7                  |
| CYL  | 254          | 71.9                  |

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
| Financials             | 32                  |
| Industrials            | 14                  |
| Healthcare             | 14                  |
| Real Estate            | 13                  |
| Materials              | 12                  |
| Consumer Discretionary | 11                  |
| Consumer Staples       | 7                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.3          | -72.4          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 34.75        | -71.1          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.29         | -65.3          |
| XRO  | Xero            | Information Technology | 181.0    | 70.8         | -60.9          |
| COH  | Cochlear        | Healthcare             | 313.15   | 123.2        | -60.7          |
| ASB  | Austal          | Industrials            | 8.76     | 3.53         | -59.7          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 17.91        | -55.0          |
| DYL  | Deep Yellow     | Energy                 | 2.91     | 1.32         | -54.6          |

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
| Materials              | 48.59                  |
| Information Technology | 45.2                   |
| Financials             | 44.0                   |
| Energy                 | 39.73                  |
| Healthcare             | 37.0                   |
| Consumer Staples       | 33.1                   |
| Consumer Discretionary | 27.66                  |
| Communication Services | 26.45                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 78.5           | 44.7               | 1.76                 |
| Materials              | 41.6           | 49.1               | 0.85                 |
| Industrials            | 22.2           | 36.0               | 0.62                 |
| Energy                 | 14.1           | 41.4               | 0.34                 |
| Financials             | 5.0            | 30.0               | 0.17                 |
| Utilities              | 0.7            | 27.4               | 0.02                 |
| Consumer Staples       | -0.5           | 28.2               | -0.02                |
| Information Technology | -6.7           | 46.7               | -0.14                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 169.3        |
| BHP  | BHP                    | Materials              | 260.3            | 58.71        |
| WBC  | Westpac                | Financials             | 136.3            | 36.64        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.11        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 91.25        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 253.04       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.71        |
| CSL  | CSL                    | Healthcare             | 67.4             | 122.96       |
