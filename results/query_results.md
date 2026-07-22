# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 54.93             | 1229.41  | -63.11    |
| Materials        | 47        | 35.9              | 121.33   | -26.56    |
| Industrials      | 24        | 19.13             | 128.94   | -41.78    |
| Energy           | 11        | 10.39             | 49.53    | -32.32    |
| Financials       | 36        | 4.75              | 60.77    | -38.58    |
| Utilities        | 7         | 0.7               | 29.94    | -11.67    |
| Consumer Staples | 7         | -1.09             | 29.74    | -40.73    |
| Real Estate      | 17        | -5.05             | 16.53    | -42.22    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1229.4              |
| 2    | NWH  | NRW Holdings           | Industrials            | 128.9               |
| 3    | PLS  | PLS Group              | Materials              | 121.3               |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 109.4               |
| 5    | CDA  | Codan                  | Information Technology | 109.4               |
| 6    | ALK  | Alkane Resources       | Materials              | 106.9               |
| 7    | VAU  | Vault Minerals         | Materials              | 92.5                |
| 8    | RDX  | Redox                  | Industrials            | 75.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.4                 |
| EOS  | 254          | 108.2                 |
| DRO  | 254          | 104.3                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 80.4                  |
| OBM  | 254          | 78.6                  |
| ZIP  | 254          | 77.0                  |
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
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 31                  |
| Industrials            | 14                  |
| Real Estate            | 12                  |
| Healthcare             | 12                  |
| Materials              | 11                  |
| Consumer Discretionary | 10                  |
| Consumer Staples       | 6                   |
| Energy                 | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.2          | -73.6          |
| WTC  | Wisetech Global        | Information Technology | 120.11   | 33.84        | -71.8          |
| DRO  | Droneshield            | Industrials            | 6.6      | 2.16         | -67.3          |
| COH  | Cochlear               | Healthcare             | 313.15   | 112.19       | -64.2          |
| XRO  | Xero                   | Information Technology | 180.99   | 67.85        | -62.5          |
| ASB  | Austal                 | Industrials            | 8.76     | 3.72         | -57.5          |
| PXA  | Pexa Group             | Real Estate            | 16.92    | 7.35         | -56.6          |
| GDG  | Generation Development | Financials             | 7.58     | 3.34         | -55.9          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name          | max_drawdown_pct |
| ---- | --------------------- | ---------------- |
| WTC  | Wisetech Global       | -76.1            |
| TUA  | Tuas                  | -76.0            |
| DRO  | Droneshield           | -74.0            |
| COH  | Cochlear              | -71.3            |
| ZIP  | Zip                   | -70.0            |
| 360  | Life360               | -67.7            |
| PME  | Pro Medicus           | -67.0            |
| TLX  | Telix Pharmaceuticals | -65.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.64                  |
| Information Technology | 45.08                  |
| Financials             | 43.96                  |
| Energy                 | 40.08                  |
| Healthcare             | 36.89                  |
| Consumer Staples       | 33.11                  |
| Consumer Discretionary | 27.63                  |
| Communication Services | 26.52                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 54.9           | 44.2               | 1.24                 |
| Materials        | 35.9           | 49.2               | 0.73                 |
| Industrials      | 19.1           | 36.0               | 0.53                 |
| Energy           | 10.4           | 41.6               | 0.25                 |
| Financials       | 4.7            | 29.9               | 0.16                 |
| Utilities        | 0.7            | 27.6               | 0.03                 |
| Consumer Staples | -1.1           | 28.2               | -0.04                |
| Real Estate      | -5.1           | 21.3               | -0.24                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 171.69       |
| BHP  | BHP                    | Materials              | 260.3            | 59.76        |
| WBC  | Westpac                | Financials             | 136.3            | 36.34        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.73        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.9         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 254.93       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.27        |
| CSL  | CSL                    | Healthcare             | 67.4             | 117.94       |
