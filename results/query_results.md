# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Healthcare             | 16        | 91.77             | 1741.67  | -56.91    |
| Materials              | 47        | 49.51             | 235.17   | -25.2     |
| Industrials            | 24        | 29.22             | 267.43   | -30.44    |
| Energy                 | 11        | 8.42              | 37.12    | -33.32    |
| Financials             | 36        | 5.85              | 80.5     | -28.48    |
| Utilities              | 7         | -0.22             | 24.35    | -13.09    |
| Consumer Staples       | 7         | -4.64             | 28.95    | -44.04    |
| Information Technology | 7         | -5.44             | 128.41   | -66.65    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1741.7              |
| 2    | EOS  | Electro Optic Systems  | Industrials            | 267.4               |
| 3    | PLS  | PLS Group              | Materials              | 235.2               |
| 4    | MIN  | Mineral Resources      | Materials              | 149.2               |
| 5    | NWH  | NRW Holdings           | Industrials            | 144.4               |
| 6    | CDA  | Codan                  | Information Technology | 128.4               |
| 7    | LTR  | Liontown Resources     | Materials              | 114.0               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 107.7               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 142.5                 |
| EOS  | 254          | 108.6                 |
| DRO  | 254          | 107.0                 |
| LTR  | 254          | 81.7                  |
| TUA  | 254          | 81.6                  |
| OBM  | 254          | 79.6                  |
| ZIP  | 254          | 76.7                  |
| CYL  | 254          | 72.5                  |

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
| Healthcare             | 14                  |
| Materials              | 13                  |
| Consumer Discretionary | 11                  |
| Real Estate            | 10                  |
| Consumer Staples       | 6                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.21         | -73.4          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 37.37        | -68.9          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.44         | -63.0          |
| COH  | Cochlear        | Healthcare             | 313.15   | 127.05       | -59.4          |
| XRO  | Xero            | Information Technology | 181.0    | 74.85        | -58.6          |
| DYL  | Deep Yellow     | Energy                 | 2.91     | 1.35         | -53.4          |
| ASB  | Austal          | Industrials            | 8.76     | 4.09         | -53.3          |
| CSL  | CSL             | Healthcare             | 265.45   | 123.97       | -53.3          |

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
| Materials              | 48.49                  |
| Information Technology | 45.16                  |
| Financials             | 44.02                  |
| Energy                 | 39.46                  |
| Healthcare             | 36.97                  |
| Consumer Staples       | 33.1                   |
| Consumer Discretionary | 27.57                  |
| Communication Services | 26.33                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 91.8           | 44.6               | 2.06                 |
| Materials              | 49.5           | 49.4               | 1.0                  |
| Industrials            | 29.2           | 35.9               | 0.81                 |
| Financials             | 5.9            | 30.0               | 0.2                  |
| Energy                 | 8.4            | 41.3               | 0.2                  |
| Utilities              | -0.2           | 27.3               | -0.01                |
| Information Technology | -5.4           | 46.6               | -0.12                |
| Consumer Staples       | -4.6           | 28.2               | -0.16                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 166.7        |
| BHP  | BHP                    | Materials              | 260.3            | 58.87        |
| WBC  | Westpac                | Financials             | 136.3            | 36.13        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.44        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.76        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 253.34       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.22        |
| CSL  | CSL                    | Healthcare             | 67.4             | 123.97       |
