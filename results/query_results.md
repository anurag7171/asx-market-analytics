# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 78.45             | 1540.0   | -57.77    |
| Materials        | 47        | 44.32             | 217.57   | -28.68    |
| Industrials      | 24        | 26.8              | 227.68   | -33.16    |
| Energy           | 11        | 9.74              | 41.08    | -33.72    |
| Financials       | 36        | 5.62              | 79.04    | -31.27    |
| Utilities        | 7         | -0.26             | 25.86    | -10.01    |
| Consumer Staples | 7         | -1.83             | 32.29    | -42.66    |
| Real Estate      | 17        | -4.75             | 20.1     | -39.76    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1540.0              |
| 2    | EOS  | Electro Optic Systems  | Industrials            | 227.7               |
| 3    | PLS  | PLS Group              | Materials              | 217.6               |
| 4    | MIN  | Mineral Resources      | Materials              | 143.2               |
| 5    | NWH  | NRW Holdings           | Industrials            | 140.4               |
| 6    | CDA  | Codan                  | Information Technology | 128.5               |
| 7    | LYC  | Lynas Rare Earths      | Materials              | 107.0               |
| 8    | LTR  | Liontown Resources     | Materials              | 106.3               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.7                 |
| EOS  | 254          | 108.9                 |
| DRO  | 254          | 107.0                 |
| LTR  | 254          | 81.8                  |
| TUA  | 254          | 81.6                  |
| OBM  | 254          | 79.3                  |
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
| Financials             | 33                  |
| Industrials            | 15                  |
| Real Estate            | 13                  |
| Healthcare             | 13                  |
| Materials              | 12                  |
| Consumer Discretionary | 10                  |
| Consumer Staples       | 7                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.21         | -73.4          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 34.65        | -71.2          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.32         | -64.8          |
| COH  | Cochlear        | Healthcare             | 313.15   | 124.82       | -60.1          |
| XRO  | Xero            | Information Technology | 181.0    | 73.97        | -59.1          |
| ASB  | Austal          | Industrials            | 8.76     | 3.83         | -56.3          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 17.87        | -55.1          |
| DYL  | Deep Yellow     | Energy                 | 2.91     | 1.34         | -54.0          |

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
| Information Technology | 45.25                  |
| Financials             | 44.1                   |
| Energy                 | 39.55                  |
| Healthcare             | 37.02                  |
| Consumer Staples       | 33.15                  |
| Consumer Discretionary | 27.64                  |
| Communication Services | 26.41                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 78.4           | 44.6               | 1.76                 |
| Materials              | 44.3           | 49.3               | 0.9                  |
| Industrials            | 26.8           | 36.0               | 0.75                 |
| Energy                 | 9.7            | 41.3               | 0.24                 |
| Financials             | 5.6            | 30.0               | 0.19                 |
| Utilities              | -0.3           | 27.3               | -0.01                |
| Consumer Staples       | -1.8           | 28.2               | -0.07                |
| Information Technology | -6.7           | 46.6               | -0.14                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 168.18       |
| BHP  | BHP                    | Materials              | 260.3            | 57.51        |
| WBC  | Westpac                | Financials             | 136.3            | 36.25        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.87        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 90.18        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 252.04       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.59        |
| CSL  | CSL                    | Healthcare             | 67.4             | 124.3        |
