# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 93.1              | 1787.5   | -58.66    |
| Materials        | 47        | 51.45             | 276.03   | -23.22    |
| Industrials      | 24        | 32.76             | 261.4    | -35.51    |
| Energy           | 11        | 12.58             | 52.17    | -31.36    |
| Financials       | 36        | 4.42              | 70.46    | -37.86    |
| Utilities        | 7         | 3.72              | 31.59    | -9.46     |
| Consumer Staples | 7         | -2.15             | 32.33    | -37.46    |
| Real Estate      | 17        | -2.23             | 21.66    | -37.18    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1787.5              |
| 2    | PLS  | PLS Group              | Materials              | 276.0               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 261.4               |
| 4    | MIN  | Mineral Resources      | Materials              | 187.9               |
| 5    | NWH  | NRW Holdings           | Industrials            | 158.1               |
| 6    | LTR  | Liontown Resources     | Materials              | 140.7               |
| 7    | CDA  | Codan                  | Information Technology | 121.9               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 109.8               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.0                 |
| EOS  | 254          | 108.6                 |
| DRO  | 254          | 107.8                 |
| TUA  | 254          | 81.6                  |
| LTR  | 254          | 81.5                  |
| OBM  | 254          | 79.1                  |
| ZIP  | 254          | 76.8                  |
| DYL  | 254          | 70.8                  |

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
| Financials             | 26                  |
| Industrials            | 20                  |
| Real Estate            | 14                  |
| Healthcare             | 14                  |
| Materials              | 11                  |
| Consumer Discretionary | 11                  |
| Consumer Staples       | 6                   |
| Utilities              | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.27         | -72.7          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 33.0         | -72.5          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.42         | -63.3          |
| COH  | Cochlear        | Healthcare             | 313.15   | 121.75       | -61.1          |
| XRO  | Xero            | Information Technology | 182.03   | 72.22        | -60.3          |
| CSL  | CSL             | Healthcare             | 265.45   | 114.74       | -56.8          |
| ASB  | Austal          | Industrials            | 8.76     | 4.05         | -53.8          |
| EBO  | EBOS Group      | Healthcare             | 36.51    | 17.07        | -53.3          |

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
| Materials              | 48.6                   |
| Information Technology | 45.52                  |
| Financials             | 44.22                  |
| Energy                 | 39.51                  |
| Healthcare             | 36.99                  |
| Consumer Staples       | 33.07                  |
| Consumer Discretionary | 27.46                  |
| Communication Services | 26.32                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 93.1           | 44.7               | 2.08                 |
| Materials        | 51.5           | 49.0               | 1.05                 |
| Industrials      | 32.8           | 35.8               | 0.91                 |
| Energy           | 12.6           | 41.3               | 0.3                  |
| Financials       | 4.4            | 29.8               | 0.15                 |
| Utilities        | 3.7            | 27.4               | 0.14                 |
| Consumer Staples | -2.2           | 28.0               | -0.08                |
| Real Estate      | -2.2           | 21.3               | -0.1                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 164.62       |
| BHP  | BHP                    | Materials              | 260.3            | 59.4         |
| WBC  | Westpac                | Financials             | 136.3            | 35.21        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.35        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.4         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.29       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.86        |
| CSL  | CSL                    | Healthcare             | 67.4             | 114.74       |
