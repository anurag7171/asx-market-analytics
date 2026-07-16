# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 68.85             | 1357.69  | -58.11    |
| Materials        | 47        | 42.52             | 189.32   | -29.24    |
| Industrials      | 24        | 21.37             | 132.5    | -39.93    |
| Energy           | 11        | 9.98              | 44.3     | -31.17    |
| Financials       | 36        | 5.74              | 71.0     | -33.83    |
| Utilities        | 7         | 1.49              | 28.82    | -8.68     |
| Consumer Staples | 7         | -1.15             | 29.19    | -37.87    |
| Real Estate      | 17        | -3.41             | 16.7     | -38.53    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1357.7              |
| 2    | PLS  | PLS Group              | Materials              | 189.3               |
| 3    | NWH  | NRW Holdings           | Industrials            | 132.5               |
| 4    | CDA  | Codan                  | Information Technology | 127.1               |
| 5    | MIN  | Mineral Resources      | Materials              | 112.8               |
| 6    | EOS  | Electro Optic Systems  | Industrials            | 105.9               |
| 7    | ALK  | Alkane Resources       | Materials              | 105.9               |
| 8    | VAU  | Vault Minerals         | Materials              | 95.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.6                 |
| EOS  | 254          | 108.0                 |
| DRO  | 254          | 104.6                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 81.6                  |
| OBM  | 254          | 78.2                  |
| ZIP  | 254          | 77.1                  |
| CYL  | 254          | 71.8                  |

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
| Real Estate            | 15                  |
| Industrials            | 14                  |
| Healthcare             | 12                  |
| Consumer Discretionary | 12                  |
| Materials              | 9                   |
| Consumer Staples       | 5                   |
| Communication Services | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.32         | -72.1          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 34.98        | -70.9          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.32         | -64.8          |
| XRO  | Xero            | Information Technology | 181.0    | 69.08        | -61.8          |
| COH  | Cochlear        | Healthcare             | 313.15   | 123.27       | -60.6          |
| ASB  | Austal          | Industrials            | 8.76     | 3.55         | -59.5          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 17.5         | -56.0          |
| DYL  | Deep Yellow     | Energy                 | 2.91     | 1.3          | -55.2          |

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
| Materials              | 48.62                  |
| Information Technology | 45.17                  |
| Financials             | 44.07                  |
| Energy                 | 39.87                  |
| Healthcare             | 36.99                  |
| Consumer Staples       | 33.16                  |
| Consumer Discretionary | 27.65                  |
| Communication Services | 26.49                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 68.9           | 44.7               | 1.54                 |
| Materials        | 42.5           | 49.1               | 0.87                 |
| Industrials      | 21.4           | 36.0               | 0.59                 |
| Energy           | 10.0           | 41.4               | 0.24                 |
| Financials       | 5.7            | 30.0               | 0.19                 |
| Utilities        | 1.5            | 27.4               | 0.05                 |
| Consumer Staples | -1.2           | 28.2               | -0.04                |
| Real Estate      | -3.4           | 20.4               | -0.17                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 173.13       |
| BHP  | BHP                    | Materials              | 260.3            | 59.14        |
| WBC  | Westpac                | Financials             | 136.3            | 36.63        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.21        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 91.98        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 256.73       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.76        |
| CSL  | CSL                    | Healthcare             | 67.4             | 121.95       |
