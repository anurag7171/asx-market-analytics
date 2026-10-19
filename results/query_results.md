# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Energy                 | 11        | 18.18             | 86.09    | -59.15    |
| Materials              | 47        | 8.07              | 71.46    | -48.69    |
| Consumer Staples       | 7         | 5.33              | 57.57    | -20.47    |
| Industrials            | 23        | 3.01              | 64.3     | -65.66    |
| Utilities              | 7         | 1.36              | 31.92    | -10.39    |
| Healthcare             | 16        | -2.64             | 124.35   | -52.79    |
| Financials             | 36        | -2.84             | 41.11    | -56.92    |
| Information Technology | 7         | -18.25            | 89.03    | -60.98    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 124.3               |
| 2    | CDA  | Codan                  | Information Technology | 89.0                |
| 3    | VEA  | Viva Energy            | Energy                 | 86.1                |
| 4    | RHC  | Ramsay Health Care     | Healthcare             | 78.4                |
| 5    | BSL  | BlueScope              | Materials              | 71.5                |
| 6    | NHC  | New Hope               | Energy                 | 66.1                |
| 7    | ALK  | Alkane Resources       | Materials              | 64.7                |
| 8    | EOS  | Electro Optic Systems  | Industrials            | 64.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 103.1                 |
| DRO  | 254          | 97.1                  |
| EOS  | 254          | 96.0                  |
| CTD  | 254          | 90.6                  |
| ZIP  | 254          | 80.7                  |
| TUA  | 254          | 80.0                  |
| LTR  | 254          | 77.2                  |
| OBM  | 254          | 77.0                  |

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
| Financials             | 16                  |
| Industrials            | 11                  |
| Materials              | 8                   |
| Healthcare             | 8                   |
| Consumer Discretionary | 8                   |
| Consumer Staples       | 7                   |
| Energy                 | 6                   |
| Utilities              | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.48         | -84.6          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.73         | -77.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.69         | -74.1          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.77         | -73.5          |
| DRO  | Droneshield            | Industrials            | 4.86     | 1.53         | -68.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.35         | -64.3          |
| 360  | Life360                | Information Technology | 51.36    | 19.74        | -61.6          |
| XRO  | Xero                   | Information Technology | 154.59   | 60.32        | -61.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.8            |
| LTR  | Liontown Resources     | -74.2            |
| DYL  | Deep Yellow            | -73.5            |
| DRO  | Droneshield            | -70.8            |
| COH  | Cochlear               | -69.2            |
| ZIP  | Zip                    | -68.7            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.19                  |
| Information Technology | 44.85                  |
| Financials             | 44.24                  |
| Energy                 | 41.21                  |
| Healthcare             | 35.82                  |
| Consumer Staples       | 31.82                  |
| Consumer Discretionary | 27.85                  |
| Communication Services | 27.48                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 18.2           | 41.5               | 0.44                 |
| Consumer Staples       | 5.3            | 28.2               | 0.19                 |
| Materials              | 8.1            | 48.5               | 0.17                 |
| Industrials            | 3.0            | 36.6               | 0.08                 |
| Utilities              | 1.4            | 27.9               | 0.05                 |
| Healthcare             | -2.6           | 41.9               | -0.06                |
| Financials             | -2.8           | 30.8               | -0.09                |
| Information Technology | -18.3          | 50.1               | -0.36                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 155.39       |
| BHP  | BHP                    | Materials              | 260.3            | 60.46        |
| WBC  | Westpac                | Financials             | 136.3            | 35.41        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.29        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.95        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.31       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.9         |
| CSL  | CSL                    | Healthcare             | 67.4             | 194.05       |
