# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 55.36             | 1180.0   | -60.32    |
| Materials        | 47        | 37.01             | 174.92   | -28.75    |
| Industrials      | 24        | 18.67             | 127.1    | -43.73    |
| Energy           | 11        | 8.03              | 43.31    | -33.15    |
| Financials       | 36        | 4.62              | 62.23    | -34.31    |
| Utilities        | 7         | 2.45              | 31.45    | -7.51     |
| Consumer Staples | 7         | -1.09             | 30.09    | -39.33    |
| Real Estate      | 17        | -3.94             | 16.27    | -41.09    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1180.0              |
| 2    | PLS  | PLS Group              | Materials              | 174.9               |
| 3    | NWH  | NRW Holdings           | Industrials            | 127.1               |
| 4    | CDA  | Codan                  | Information Technology | 113.6               |
| 5    | MIN  | Mineral Resources      | Materials              | 104.6               |
| 6    | ALK  | Alkane Resources       | Materials              | 100.8               |
| 7    | EOS  | Electro Optic Systems  | Industrials            | 90.0                |
| 8    | VAU  | Vault Minerals         | Materials              | 82.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.5                 |
| EOS  | 254          | 108.3                 |
| DRO  | 254          | 104.5                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 81.7                  |
| OBM  | 254          | 78.4                  |
| ZIP  | 254          | 77.3                  |
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
| Financials             | 31                  |
| Industrials            | 16                  |
| Real Estate            | 15                  |
| Healthcare             | 13                  |
| Consumer Discretionary | 12                  |
| Consumer Staples       | 6                   |
| Materials              | 5                   |
| Energy                 | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.31         | -72.2          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 34.95        | -70.9          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.14         | -67.6          |
| COH  | Cochlear        | Healthcare             | 313.15   | 119.48       | -61.8          |
| XRO  | Xero            | Information Technology | 181.0    | 69.72        | -61.5          |
| ASB  | Austal          | Industrials            | 8.76     | 3.41         | -61.1          |
| DYL  | Deep Yellow     | Energy                 | 2.91     | 1.23         | -57.7          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 17.79        | -55.3          |

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
| Materials              | 48.67                  |
| Information Technology | 45.16                  |
| Financials             | 44.11                  |
| Energy                 | 39.96                  |
| Healthcare             | 37.01                  |
| Consumer Staples       | 33.21                  |
| Consumer Discretionary | 27.67                  |
| Communication Services | 26.52                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 55.4           | 44.8               | 1.24                 |
| Materials        | 37.0           | 49.2               | 0.75                 |
| Industrials      | 18.7           | 35.9               | 0.52                 |
| Energy           | 8.0            | 41.5               | 0.19                 |
| Financials       | 4.6            | 30.0               | 0.15                 |
| Utilities        | 2.4            | 27.4               | 0.09                 |
| Consumer Staples | -1.1           | 28.2               | -0.04                |
| Real Estate      | -3.9           | 20.3               | -0.19                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 171.78       |
| BHP  | BHP                    | Materials              | 260.3            | 57.54        |
| WBC  | Westpac                | Financials             | 136.3            | 36.56        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.06        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 92.8         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 258.41       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.85        |
| CSL  | CSL                    | Healthcare             | 67.4             | 123.32       |
