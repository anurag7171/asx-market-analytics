# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 13.01             | 85.07    | -66.18    |
| Consumer Staples | 7         | 7.46              | 62.7     | -22.07    |
| Materials        | 47        | 3.67              | 63.32    | -50.05    |
| Utilities        | 7         | 2.86              | 31.39    | -7.84     |
| Industrials      | 23        | 0.23              | 45.6     | -72.16    |
| Financials       | 36        | -3.91             | 40.23    | -58.45    |
| Healthcare       | 16        | -4.43             | 121.74   | -53.25    |
| Real Estate      | 16        | -18.18            | -1.11    | -59.26    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name          | sector_name            | one_year_return_pct |
| ---- | ---- | --------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical             | Healthcare             | 121.7               |
| 2    | VEA  | Viva Energy           | Energy                 | 85.1                |
| 3    | CDA  | Codan                 | Information Technology | 80.7                |
| 4    | RHC  | Ramsay Health Care    | Healthcare             | 74.3                |
| 5    | BSL  | BlueScope             | Materials              | 63.3                |
| 6    | WOW  | Woolworths Group      | Consumer Staples       | 62.7                |
| 7    | WDS  | Woodside Energy Group | Energy                 | 56.6                |
| 8    | NHC  | New Hope              | Energy                 | 53.8                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 103.2                 |
| DRO  | 255          | 96.8                  |
| EOS  | 255          | 96.0                  |
| CTD  | 255          | 90.4                  |
| ZIP  | 255          | 80.7                  |
| TUA  | 255          | 79.4                  |
| LTR  | 255          | 77.0                  |
| OBM  | 255          | 76.7                  |

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
| Industrials            | 8                   |
| Healthcare             | 7                   |
| Consumer Discretionary | 7                   |
| Consumer Staples       | 6                   |
| Energy                 | 5                   |
| Utilities              | 4                   |
| Communication Services | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.49         | -84.5          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.54         | -79.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.68         | -74.2          |
| DRO  | Droneshield            | Industrials            | 5.1      | 1.42         | -72.2          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.81         | -72.0          |
| XRO  | Xero                   | Information Technology | 157.07   | 57.72        | -63.3          |
| 360  | Life360                | Information Technology | 51.36    | 18.93        | -63.1          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.43         | -63.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.8            |
| LTR  | Liontown Resources     | -74.2            |
| DRO  | Droneshield            | -72.2            |
| DYL  | Deep Yellow            | -72.0            |
| COH  | Cochlear               | -69.2            |
| ZIP  | Zip                    | -68.9            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.33                  |
| Information Technology | 44.91                  |
| Financials             | 44.41                  |
| Energy                 | 41.13                  |
| Healthcare             | 35.86                  |
| Consumer Staples       | 31.98                  |
| Consumer Discretionary | 27.88                  |
| Communication Services | 27.46                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 13.0           | 41.6               | 0.31                 |
| Consumer Staples       | 7.5            | 28.2               | 0.26                 |
| Utilities              | 2.9            | 27.9               | 0.1                  |
| Materials              | 3.7            | 48.5               | 0.08                 |
| Industrials            | 0.2            | 36.2               | 0.01                 |
| Healthcare             | -4.4           | 41.8               | -0.11                |
| Financials             | -3.9           | 30.8               | -0.13                |
| Information Technology | -21.9          | 49.8               | -0.44                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 156.15       |
| BHP  | BHP                    | Materials              | 260.3            | 58.0         |
| WBC  | Westpac                | Financials             | 136.3            | 35.71        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.01        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.5         |
| MQG  | Macquarie Group        | Financials             | 78.4             | 246.68       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.71        |
| CSL  | CSL                    | Healthcare             | 67.4             | 186.9        |
