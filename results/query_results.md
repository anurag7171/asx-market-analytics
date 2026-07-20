# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 53.83             | 1194.34  | -60.76    |
| Materials        | 47        | 34.01             | 135.39   | -28.65    |
| Industrials      | 24        | 18.65             | 124.28   | -45.06    |
| Energy           | 11        | 8.8               | 43.96    | -31.41    |
| Financials       | 36        | 4.38              | 56.39    | -36.05    |
| Utilities        | 7         | 2.45              | 30.83    | -9.77     |
| Consumer Staples | 7         | -0.72             | 29.52    | -40.13    |
| Real Estate      | 17        | -3.51             | 17.86    | -40.63    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1194.3              |
| 2    | PLS  | PLS Group              | Materials              | 135.4               |
| 3    | NWH  | NRW Holdings           | Industrials            | 124.3               |
| 4    | CDA  | Codan                  | Information Technology | 106.1               |
| 5    | ALK  | Alkane Resources       | Materials              | 103.1               |
| 6    | EOS  | Electro Optic Systems  | Industrials            | 101.5               |
| 7    | MIN  | Mineral Resources      | Materials              | 82.0                |
| 8    | VAU  | Vault Minerals         | Materials              | 81.7                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 143.8                 |
| EOS  | 253          | 108.3                 |
| DRO  | 253          | 104.5                 |
| TUA  | 253          | 81.8                  |
| LTR  | 253          | 80.6                  |
| OBM  | 253          | 78.5                  |
| ZIP  | 253          | 77.2                  |
| CYL  | 253          | 72.0                  |

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
| Industrials            | 16                  |
| Real Estate            | 14                  |
| Consumer Discretionary | 12                  |
| Healthcare             | 11                  |
| Consumer Staples       | 7                   |
| Materials              | 6                   |
| Communication Services | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.27         | -72.7          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 33.71        | -71.9          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.16         | -67.3          |
| XRO  | Xero            | Information Technology | 180.99   | 68.27        | -62.3          |
| COH  | Cochlear        | Healthcare             | 313.15   | 119.0        | -62.0          |
| ASB  | Austal          | Industrials            | 8.76     | 3.39         | -61.3          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 17.41        | -56.2          |
| PXA  | Pexa Group      | Real Estate            | 16.92    | 7.51         | -55.6          |

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
| Materials              | 48.65                  |
| Information Technology | 45.12                  |
| Financials             | 44.0                   |
| Energy                 | 40.02                  |
| Healthcare             | 36.92                  |
| Consumer Staples       | 33.14                  |
| Consumer Discretionary | 27.62                  |
| Communication Services | 26.5                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name      | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------- | -------------- | ------------------ | -------------------- |
| Healthcare       | 53.8           | 44.2               | 1.22                 |
| Materials        | 34.0           | 49.3               | 0.69                 |
| Industrials      | 18.6           | 36.0               | 0.52                 |
| Energy           | 8.8            | 41.6               | 0.21                 |
| Financials       | 4.4            | 30.0               | 0.15                 |
| Utilities        | 2.5            | 27.5               | 0.09                 |
| Consumer Staples | -0.7           | 28.2               | -0.03                |
| Real Estate      | -3.5           | 20.4               | -0.17                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 171.2        |
| BHP  | BHP                    | Materials              | 260.3            | 57.54        |
| WBC  | Westpac                | Financials             | 136.3            | 36.66        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 36.13        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 92.96        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 256.3        |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.69        |
| CSL  | CSL                    | Healthcare             | 67.4             | 122.61       |
