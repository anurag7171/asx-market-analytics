# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Energy                 | 11        | 12.88             | 80.27    | -66.67    |
| Materials              | 47        | 6.45              | 69.66    | -49.85    |
| Consumer Staples       | 7         | 6.0               | 59.39    | -23.55    |
| Utilities              | 7         | 2.66              | 31.13    | -7.91     |
| Industrials            | 23        | 1.54              | 57.98    | -68.74    |
| Healthcare             | 16        | -3.87             | 111.92   | -53.22    |
| Financials             | 36        | -5.12             | 28.14    | -59.09    |
| Information Technology | 7         | -18.34            | 90.17    | -60.08    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 111.9               |
| 2    | CDA  | Codan                  | Information Technology | 90.2                |
| 3    | VEA  | Viva Energy            | Energy                 | 80.3                |
| 4    | RHC  | Ramsay Health Care     | Healthcare             | 77.1                |
| 5    | BSL  | BlueScope              | Materials              | 69.7                |
| 6    | WOW  | Woolworths Group       | Consumer Staples       | 59.4                |
| 7    | EOS  | Electro Optic Systems  | Industrials            | 58.0                |
| 8    | ALK  | Alkane Resources       | Materials              | 57.8                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 103.1                 |
| DRO  | 255          | 97.3                  |
| EOS  | 255          | 96.4                  |
| CTD  | 255          | 90.4                  |
| ZIP  | 255          | 80.7                  |
| TUA  | 255          | 79.7                  |
| LTR  | 255          | 77.1                  |
| OBM  | 255          | 76.9                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |
| TPG  | TPG Telecom            | 2025-11-13 | -32.1          |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 15                  |
| Industrials            | 10                  |
| Healthcare             | 8                   |
| Consumer Discretionary | 8                   |
| Materials              | 7                   |
| Energy                 | 6                   |
| Consumer Staples       | 6                   |
| Utilities              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.51         | -84.4          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.64         | -78.5          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.71         | -73.1          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.82         | -71.8          |
| DRO  | Droneshield            | Industrials            | 4.99     | 1.56         | -68.7          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.38         | -63.9          |
| 360  | Life360                | Information Technology | 51.36    | 20.38        | -60.3          |
| XRO  | Xero                   | Information Technology | 154.79   | 61.79        | -60.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.8            |
| LTR  | Liontown Resources     | -74.2            |
| DYL  | Deep Yellow            | -72.0            |
| DRO  | Droneshield            | -71.5            |
| COH  | Cochlear               | -69.2            |
| ZIP  | Zip                    | -68.7            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.41                  |
| Information Technology | 44.93                  |
| Financials             | 44.44                  |
| Energy                 | 41.15                  |
| Healthcare             | 35.95                  |
| Consumer Staples       | 31.96                  |
| Consumer Discretionary | 27.87                  |
| Communication Services | 27.51                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 12.9           | 41.6               | 0.31                 |
| Consumer Staples       | 6.0            | 28.2               | 0.21                 |
| Materials              | 6.5            | 48.5               | 0.13                 |
| Utilities              | 2.7            | 27.9               | 0.1                  |
| Industrials            | 1.5            | 36.3               | 0.04                 |
| Healthcare             | -3.9           | 41.8               | -0.09                |
| Financials             | -5.1           | 30.7               | -0.17                |
| Information Technology | -18.3          | 50.0               | -0.37                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 154.38       |
| BHP  | BHP                    | Materials              | 260.3            | 60.03        |
| WBC  | Westpac                | Financials             | 136.3            | 35.15        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.89        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 79.31        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.35       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.32        |
| CSL  | CSL                    | Healthcare             | 67.4             | 192.2        |
