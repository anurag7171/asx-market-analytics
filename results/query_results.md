# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 53.33             | 1190.57  | -61.09    |
| Materials        | 47        | 36.11             | 131.46   | -28.65    |
| Industrials      | 24        | 19.39             | 129.22   | -42.95    |
| Energy           | 11        | 8.81              | 44.64    | -32.95    |
| Financials       | 36        | 3.85              | 57.85    | -38.64    |
| Utilities        | 7         | 1.34              | 30.19    | -10.85    |
| Consumer Staples | 7         | -1.15             | 30.01    | -41.4     |
| Real Estate      | 17        | -3.79             | 18.44    | -41.01    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1190.6              |
| 2    | PLS  | PLS Group              | Materials              | 131.5               |
| 3    | NWH  | NRW Holdings           | Industrials            | 129.2               |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 109.4               |
| 5    | CDA  | Codan                  | Information Technology | 108.0               |
| 6    | ALK  | Alkane Resources       | Materials              | 102.3               |
| 7    | VAU  | Vault Minerals         | Materials              | 90.3                |
| 8    | MIN  | Mineral Resources      | Materials              | 75.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 143.5                 |
| EOS  | 254          | 108.2                 |
| DRO  | 254          | 104.3                 |
| TUA  | 254          | 81.7                  |
| LTR  | 254          | 80.6                  |
| OBM  | 254          | 78.4                  |
| ZIP  | 254          | 77.1                  |
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
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 30                  |
| Industrials            | 15                  |
| Real Estate            | 13                  |
| Healthcare             | 12                  |
| Consumer Discretionary | 10                  |
| Materials              | 9                   |
| Consumer Staples       | 7                   |
| Communication Services | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.22         | -73.3          |
| WTC  | Wisetech Global        | Information Technology | 120.11   | 34.0         | -71.7          |
| DRO  | Droneshield            | Industrials            | 6.6      | 2.17         | -67.1          |
| COH  | Cochlear               | Healthcare             | 313.15   | 118.0        | -62.3          |
| XRO  | Xero                   | Information Technology | 180.99   | 69.67        | -61.5          |
| ASB  | Austal                 | Industrials            | 8.76     | 3.52         | -59.8          |
| ARB  | ARB Corporation        | Consumer Discretionary | 39.79    | 17.59        | -55.8          |
| GDG  | Generation Development | Financials             | 7.58     | 3.37         | -55.6          |

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
| Materials              | 48.6                   |
| Information Technology | 45.06                  |
| Financials             | 43.96                  |
| Energy                 | 40.01                  |
| Healthcare             | 36.88                  |
| Consumer Staples       | 33.09                  |
| Consumer Discretionary | 27.61                  |
| Communication Services | 26.5                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 53.3           | 44.2               | 1.21                 |
| Materials        | 36.1           | 49.2               | 0.73                 |
| Industrials      | 19.4           | 35.9               | 0.54                 |
| Energy           | 8.8            | 41.6               | 0.21                 |
| Financials       | 3.9            | 29.9               | 0.13                 |
| Utilities        | 1.3            | 27.5               | 0.05                 |
| Consumer Staples | -1.2           | 28.2               | -0.04                |
| Real Estate      | -3.8           | 20.6               | -0.18                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 170.49       |
| BHP  | BHP                    | Materials              | 260.3            | 58.29        |
| WBC  | Westpac                | Financials             | 136.3            | 36.22        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.7         |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 91.84        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 254.75       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.3         |
| CSL  | CSL                    | Healthcare             | 67.4             | 121.38       |
