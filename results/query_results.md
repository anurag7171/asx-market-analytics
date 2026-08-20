# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 54.52             | 142.41   | -31.06    |
| Healthcare             | 16        | 27.97             | 673.08   | -53.74    |
| Energy                 | 11        | 25.08             | 63.78    | -22.89    |
| Industrials            | 24        | 14.61             | 123.06   | -42.48    |
| Utilities              | 7         | 3.56              | 23.33    | -7.45     |
| Financials             | 36        | 2.04              | 87.08    | -37.82    |
| Consumer Staples       | 7         | -2.47             | 30.65    | -28.03    |
| Information Technology | 7         | -9.52             | 108.8    | -61.71    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare             | 673.1               |
| 2    | GGP  | Greatland Resources  | Materials              | 142.4               |
| 3    | VAU  | Vault Minerals       | Materials              | 141.0               |
| 4    | PLS  | PLS Group            | Materials              | 130.0               |
| 5    | NWH  | NRW Holdings         | Industrials            | 123.1               |
| 6    | OBM  | Ora Banda Mining     | Materials              | 120.1               |
| 7    | PDI  | Predictive Discovery | Materials              | 109.1               |
| 8    | CDA  | Codan                | Information Technology | 108.8               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 138.2                 |
| DRO  | 254          | 103.5                 |
| EOS  | 254          | 98.9                  |
| ZIP  | 254          | 80.4                  |
| OBM  | 254          | 79.5                  |
| LTR  | 254          | 79.1                  |
| TUA  | 254          | 76.1                  |
| 360  | 254          | 72.4                  |

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
| Financials             | 17                  |
| Healthcare             | 13                  |
| Industrials            | 11                  |
| Energy                 | 9                   |
| Consumer Discretionary | 9                   |
| Communication Services | 6                   |
| Utilities              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name       | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ------------------ | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas               | Communication Services | 8.32     | 2.06         | -75.2          |
| DRO  | Droneshield        | Industrials            | 6.6      | 1.95         | -70.5          |
| WTC  | Wisetech Global    | Information Technology | 115.37   | 43.19        | -62.6          |
| 360  | Life360            | Information Technology | 55.44    | 21.12        | -61.9          |
| LTR  | Liontown Resources | Materials              | 2.64     | 1.21         | -54.4          |
| COH  | Cochlear           | Healthcare             | 297.81   | 136.82       | -54.1          |
| PXA  | Pexa Group         | Real Estate            | 16.92    | 8.04         | -52.5          |
| ARB  | ARB Corporation    | Consumer Discretionary | 39.79    | 19.33        | -51.4          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.1            |
| DRO  | Droneshield     | -74.3            |
| ZIP  | Zip             | -70.0            |
| COH  | Cochlear        | -69.8            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.2            |
| XRO  | Xero            | -63.8            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.16                  |
| Information Technology | 45.84                  |
| Financials             | 44.2                   |
| Energy                 | 40.45                  |
| Healthcare             | 36.74                  |
| Consumer Staples       | 33.11                  |
| Consumer Discretionary | 27.62                  |
| Communication Services | 26.94                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 54.5           | 49.3               | 1.1                  |
| Healthcare             | 28.0           | 44.4               | 0.63                 |
| Energy                 | 25.1           | 41.6               | 0.6                  |
| Industrials            | 14.6           | 36.6               | 0.4                  |
| Utilities              | 3.6            | 27.7               | 0.13                 |
| Financials             | 2.0            | 30.3               | 0.07                 |
| Consumer Staples       | -2.5           | 29.1               | -0.08                |
| Information Technology | -9.5           | 48.9               | -0.19                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 156.44       |
| BHP  | BHP                    | Materials              | 260.3            | 65.75        |
| WBC  | Westpac                | Financials             | 136.3            | 33.82        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.01        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 84.34        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 252.3        |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.43        |
| CSL  | CSL                    | Healthcare             | 67.4             | 171.2        |
