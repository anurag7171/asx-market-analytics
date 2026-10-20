# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Energy                 | 11        | 16.04             | 82.51    | -61.01    |
| Materials              | 47        | 6.96              | 73.2     | -49.13    |
| Consumer Staples       | 7         | 5.91              | 59.29    | -20.47    |
| Industrials            | 23        | 2.51              | 60.04    | -66.67    |
| Utilities              | 7         | 2.12              | 33.67    | -8.71     |
| Healthcare             | 16        | -2.91             | 116.23   | -50.35    |
| Financials             | 36        | -3.03             | 37.68    | -55.51    |
| Information Technology | 7         | -18.09            | 88.27    | -60.32    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 116.2               |
| 2    | CDA  | Codan                  | Information Technology | 88.3                |
| 3    | VEA  | Viva Energy            | Energy                 | 82.5                |
| 4    | RHC  | Ramsay Health Care     | Healthcare             | 75.5                |
| 5    | BSL  | BlueScope              | Materials              | 73.2                |
| 6    | NHC  | New Hope               | Energy                 | 61.5                |
| 7    | EOS  | Electro Optic Systems  | Industrials            | 60.0                |
| 8    | WDS  | Woodside Energy Group  | Energy                 | 60.0                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 102.9                 |
| DRO  | 255          | 97.0                  |
| EOS  | 255          | 95.8                  |
| CTD  | 255          | 93.4                  |
| ZIP  | 255          | 80.6                  |
| TUA  | 255          | 79.8                  |
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
| Industrials            | 11                  |
| Consumer Discretionary | 10                  |
| Healthcare             | 8                   |
| Materials              | 7                   |
| Consumer Staples       | 7                   |
| Energy                 | 5                   |
| Utilities              | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.06         | -81.0          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.75         | -77.2          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.73         | -74.7          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.69         | -73.7          |
| DRO  | Droneshield            | Industrials            | 4.86     | 1.49         | -69.3          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.33         | -64.6          |
| 360  | Life360                | Information Technology | 51.36    | 20.09        | -60.9          |
| XRO  | Xero                   | Information Technology | 154.59   | 61.34        | -60.3          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.8            |
| DYL  | Deep Yellow            | -74.7            |
| LTR  | Liontown Resources     | -74.2            |
| DRO  | Droneshield            | -70.8            |
| COH  | Cochlear               | -69.2            |
| ZIP  | Zip                    | -68.7            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.15                  |
| Information Technology | 44.81                  |
| Financials             | 44.25                  |
| Energy                 | 41.18                  |
| Healthcare             | 35.85                  |
| Consumer Staples       | 31.82                  |
| Consumer Discretionary | 27.84                  |
| Communication Services | 27.47                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 16.0           | 41.5               | 0.39                 |
| Consumer Staples       | 5.9            | 28.2               | 0.21                 |
| Materials              | 7.0            | 48.5               | 0.14                 |
| Utilities              | 2.1            | 27.9               | 0.08                 |
| Industrials            | 2.5            | 36.5               | 0.07                 |
| Healthcare             | -2.9           | 41.9               | -0.07                |
| Financials             | -3.0           | 30.8               | -0.1                 |
| Information Technology | -18.1          | 50.0               | -0.36                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 155.6        |
| BHP  | BHP                    | Materials              | 260.3            | 59.5         |
| WBC  | Westpac                | Financials             | 136.3            | 35.13        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.98        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 79.58        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.15       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.2         |
| CSL  | CSL                    | Healthcare             | 67.4             | 196.3        |
