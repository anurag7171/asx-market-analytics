# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 94.71             | 1812.5   | -58.89    |
| Materials        | 47        | 54.68             | 280.52   | -23.5     |
| Industrials      | 24        | 31.79             | 238.95   | -36.31    |
| Energy           | 11        | 13.06             | 51.89    | -31.36    |
| Financials       | 36        | 3.46              | 67.21    | -38.04    |
| Utilities        | 7         | 2.67              | 32.5     | -10.04    |
| Real Estate      | 17        | -0.66             | 23.04    | -37.56    |
| Consumer Staples | 7         | -1.49             | 34.05    | -36.41    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1812.5              |
| 2    | PLS  | PLS Group              | Materials              | 280.5               |
| 3    | EOS  | Electro Optic Systems  | Industrials            | 238.9               |
| 4    | MIN  | Mineral Resources      | Materials              | 188.3               |
| 5    | NWH  | NRW Holdings           | Industrials            | 150.5               |
| 6    | LTR  | Liontown Resources     | Materials              | 137.1               |
| 7    | CDA  | Codan                  | Information Technology | 118.5               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 115.1               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 142.3                 |
| EOS  | 253          | 108.6                 |
| DRO  | 253          | 107.9                 |
| TUA  | 253          | 81.8                  |
| LTR  | 253          | 81.7                  |
| OBM  | 253          | 79.0                  |
| ZIP  | 253          | 76.9                  |
| DYL  | 253          | 70.9                  |

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
| Financials             | 22                  |
| Industrials            | 21                  |
| Real Estate            | 14                  |
| Healthcare             | 13                  |
| Materials              | 12                  |
| Consumer Discretionary | 11                  |
| Consumer Staples       | 7                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.28         | -72.6          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 33.82        | -71.8          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.33         | -64.7          |
| COH  | Cochlear        | Healthcare             | 313.15   | 121.08       | -61.3          |
| XRO  | Xero            | Information Technology | 182.03   | 72.18        | -60.3          |
| CSL  | CSL             | Healthcare             | 265.45   | 115.39       | -56.5          |
| ASB  | Austal          | Industrials            | 8.76     | 4.0          | -54.3          |
| SEK  | Seek            | Communication Services | 28.65    | 13.21        | -53.9          |

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
| Materials              | 48.58                  |
| Information Technology | 45.49                  |
| Financials             | 44.18                  |
| Energy                 | 39.53                  |
| Healthcare             | 36.98                  |
| Consumer Staples       | 33.07                  |
| Consumer Discretionary | 27.44                  |
| Communication Services | 26.31                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 94.7           | 44.7               | 2.12                 |
| Materials        | 54.7           | 49.0               | 1.12                 |
| Industrials      | 31.8           | 35.9               | 0.89                 |
| Energy           | 13.1           | 41.3               | 0.32                 |
| Financials       | 3.5            | 29.8               | 0.12                 |
| Utilities        | 2.7            | 27.4               | 0.1                  |
| Real Estate      | -0.7           | 21.2               | -0.03                |
| Consumer Staples | -1.5           | 28.1               | -0.05                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 163.61       |
| BHP  | BHP                    | Materials              | 260.3            | 59.82        |
| WBC  | Westpac                | Financials             | 136.3            | 35.24        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.2         |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.79        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.01       |
| NAB  | National Australia Ban | Financials             | 69.8             | 37.89        |
| CSL  | CSL                    | Healthcare             | 67.4             | 115.39       |
