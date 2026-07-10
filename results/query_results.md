# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 81.41             | 1585.11  | -59.02    |
| Materials        | 47        | 45.76             | 203.61   | -30.65    |
| Industrials      | 24        | 24.96             | 190.0    | -36.41    |
| Energy           | 11        | 15.58             | 44.54    | -31.57    |
| Financials       | 36        | 5.65              | 79.77    | -29.29    |
| Utilities        | 7         | 0.44              | 26.49    | -10.47    |
| Consumer Staples | 7         | -0.93             | 32.55    | -41.53    |
| Real Estate      | 17        | -5.21             | 17.6     | -40.37    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1585.1              |
| 2    | PLS  | PLS Group              | Materials              | 203.6               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 190.0               |
| 4    | NWH  | NRW Holdings           | Industrials            | 143.8               |
| 5    | MIN  | Mineral Resources      | Materials              | 134.0               |
| 6    | CDA  | Codan                  | Information Technology | 133.3               |
| 7    | ALK  | Alkane Resources       | Materials              | 111.2               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 100.6               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.5                 |
| EOS  | 254          | 109.0                 |
| DRO  | 254          | 107.0                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 81.4                  |
| OBM  | 254          | 79.1                  |
| ZIP  | 254          | 76.6                  |
| CYL  | 254          | 72.2                  |

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
| TUA  | Tuas            | Communication Services | 8.32     | 2.31         | -72.2          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 34.0         | -71.7          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.29         | -65.3          |
| COH  | Cochlear        | Healthcare             | 313.15   | 121.62       | -61.2          |
| XRO  | Xero            | Information Technology | 181.0    | 73.4         | -59.4          |
| ASB  | Austal          | Industrials            | 8.76     | 3.72         | -57.5          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 17.53        | -55.9          |
| 360  | Life360         | Information Technology | 55.44    | 25.68        | -53.7          |

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
| Information Technology | 45.22                  |
| Financials             | 44.05                  |
| Energy                 | 39.59                  |
| Healthcare             | 36.99                  |
| Consumer Staples       | 33.08                  |
| Consumer Discretionary | 27.64                  |
| Communication Services | 26.42                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 81.4           | 44.6               | 1.83                 |
| Materials              | 45.8           | 49.3               | 0.93                 |
| Industrials            | 25.0           | 36.0               | 0.69                 |
| Energy                 | 15.6           | 41.3               | 0.38                 |
| Financials             | 5.7            | 30.0               | 0.19                 |
| Utilities              | 0.4            | 27.3               | 0.02                 |
| Consumer Staples       | -0.9           | 28.1               | -0.03                |
| Information Technology | -5.2           | 46.6               | -0.11                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 168.86       |
| BHP  | BHP                    | Materials              | 260.3            | 58.28        |
| WBC  | Westpac                | Financials             | 136.3            | 36.54        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.05        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.7         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 254.49       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.61        |
| CSL  | CSL                    | Healthcare             | 67.4             | 122.89       |
