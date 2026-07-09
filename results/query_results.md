# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Healthcare             | 16        | 86.72             | 1665.22  | -58.37    |
| Materials              | 47        | 44.78             | 206.31   | -30.07    |
| Industrials            | 24        | 26.51             | 214.74   | -32.01    |
| Energy                 | 11        | 12.97             | 39.1     | -31.71    |
| Financials             | 36        | 5.77              | 79.77    | -32.5     |
| Consumer Staples       | 7         | 0.09              | 34.77    | -41.91    |
| Utilities              | 7         | -0.21             | 26.37    | -12.38    |
| Information Technology | 7         | -4.19             | 139.92   | -69.09    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1665.2              |
| 2    | EOS  | Electro Optic Systems  | Industrials            | 214.7               |
| 3    | PLS  | PLS Group              | Materials              | 206.3               |
| 4    | NWH  | NRW Holdings           | Industrials            | 141.5               |
| 5    | CDA  | Codan                  | Information Technology | 139.9               |
| 6    | MIN  | Mineral Resources      | Materials              | 137.7               |
| 7    | LYC  | Lynas Rare Earths      | Materials              | 103.6               |
| 8    | LTR  | Liontown Resources     | Materials              | 96.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.4                 |
| EOS  | 254          | 108.8                 |
| DRO  | 254          | 107.0                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 81.7                  |
| OBM  | 254          | 79.0                  |
| ZIP  | 254          | 76.7                  |
| CYL  | 254          | 72.1                  |

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
| Industrials            | 15                  |
| Healthcare             | 14                  |
| Real Estate            | 13                  |
| Consumer Discretionary | 10                  |
| Materials              | 9                   |
| Consumer Staples       | 7                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.29         | -72.5          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 34.63        | -71.2          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.29         | -65.3          |
| COH  | Cochlear        | Healthcare             | 313.15   | 123.68       | -60.5          |
| XRO  | Xero            | Information Technology | 181.0    | 74.34        | -58.9          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 17.7         | -55.5          |
| ASB  | Austal          | Industrials            | 8.76     | 3.93         | -55.1          |
| DYL  | Deep Yellow     | Energy                 | 2.91     | 1.34         | -53.8          |

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
| TLX  | Telix Pharmaceuticals | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.59                  |
| Information Technology | 45.23                  |
| Financials             | 44.07                  |
| Energy                 | 39.61                  |
| Healthcare             | 37.0                   |
| Consumer Staples       | 33.11                  |
| Consumer Discretionary | 27.64                  |
| Communication Services | 26.4                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 86.7           | 44.5               | 1.95                 |
| Materials              | 44.8           | 49.3               | 0.91                 |
| Industrials            | 26.5           | 36.0               | 0.74                 |
| Energy                 | 13.0           | 41.3               | 0.31                 |
| Financials             | 5.8            | 30.0               | 0.19                 |
| Consumer Staples       | 0.1            | 28.1               | 0.0                  |
| Utilities              | -0.2           | 27.3               | -0.01                |
| Information Technology | -4.2           | 46.6               | -0.09                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 168.11       |
| BHP  | BHP                    | Materials              | 260.3            | 56.87        |
| WBC  | Westpac                | Financials             | 136.3            | 36.2         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.76        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.87        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 252.2        |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.28        |
| CSL  | CSL                    | Healthcare             | 67.4             | 125.53       |
