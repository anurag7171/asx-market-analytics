# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 48.05             | 122.38   | -24.05    |
| Energy           | 11        | 18.76             | 48.29    | -29.54    |
| Industrials      | 24        | 8.47              | 91.45    | -46.08    |
| Utilities        | 7         | 3.82              | 30.71    | -11.37    |
| Healthcare       | 16        | 1.43              | 174.81   | -51.27    |
| Financials       | 36        | 0.92              | 79.55    | -46.87    |
| Consumer Staples | 7         | -3.7              | 49.44    | -29.34    |
| Real Estate      | 17        | -13.99            | 8.84     | -52.49    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 174.8               |
| 2    | PLS  | PLS Group            | Materials   | 122.4               |
| 3    | RSG  | Resolute Mining      | Materials   | 113.8               |
| 4    | PDI  | Predictive Discovery | Materials   | 107.6               |
| 5    | S32  | South32              | Materials   | 100.5               |
| 6    | BGL  | Bellevue Gold        | Materials   | 94.3                |
| 7    | GGP  | Greatland Resources  | Materials   | 92.3                |
| 8    | NWH  | NRW Holdings         | Industrials | 91.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 122.7                 |
| DRO  | 254          | 104.0                 |
| EOS  | 254          | 99.5                  |
| CTD  | 254          | 85.1                  |
| ZIP  | 254          | 79.6                  |
| LTR  | 254          | 79.5                  |
| OBM  | 254          | 79.0                  |
| TUA  | 254          | 76.2                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Materials              | 36                  |
| Financials             | 17                  |
| Energy                 | 10                  |
| Healthcare             | 9                   |
| Industrials            | 7                   |
| Communication Services | 5                   |
| Utilities              | 4                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.25         | -86.0          |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.15         | -74.2          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.75         | -73.6          |
| 360  | Life360                | Information Technology | 55.44    | 20.75        | -62.6          |
| WTC  | Wisetech Global        | Information Technology | 97.44    | 37.69        | -61.3          |
| GDG  | Generation Development | Financials             | 7.56     | 3.17         | -58.1          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 7.43         | -55.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.23         | -53.6          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -86.0            |
| TUA  | Tuas                   | -76.0            |
| DRO  | Droneshield            | -74.8            |
| WTC  | Wisetech Global        | -70.5            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.7            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.58                  |
| Information Technology | 45.35                  |
| Financials             | 44.1                   |
| Energy                 | 40.74                  |
| Healthcare             | 36.62                  |
| Consumer Staples       | 32.56                  |
| Consumer Discretionary | 27.6                   |
| Communication Services | 27.44                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 48.1           | 49.1               | 0.98                 |
| Energy                 | 18.8           | 41.7               | 0.45                 |
| Industrials            | 8.5            | 35.1               | 0.24                 |
| Utilities              | 3.8            | 27.5               | 0.14                 |
| Healthcare             | 1.4            | 43.6               | 0.03                 |
| Financials             | 0.9            | 30.7               | 0.03                 |
| Consumer Staples       | -3.7           | 28.2               | -0.13                |
| Information Technology | -18.8          | 48.2               | -0.39                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 160.42       |
| BHP  | BHP                    | Materials              | 260.3            | 62.25        |
| WBC  | Westpac                | Financials             | 136.3            | 34.96        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.95        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.73        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 251.87       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.25        |
| CSL  | CSL                    | Healthcare             | 67.4             | 174.5        |
