# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 16.97             | 82.36    | -59.84    |
| Consumer Staples | 7         | 6.74              | 60.23    | -21.48    |
| Materials        | 47        | 4.9               | 70.36    | -50.92    |
| Industrials      | 23        | 1.79              | 61.5     | -68.72    |
| Utilities        | 7         | 1.13              | 35.4     | -11.83    |
| Financials       | 36        | -3.13             | 35.51    | -54.42    |
| Healthcare       | 16        | -3.23             | 113.33   | -49.84    |
| Real Estate      | 16        | -20.08            | -3.55    | -57.45    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 113.3               |
| 2    | CDA  | Codan                  | Information Technology | 82.7                |
| 3    | VEA  | Viva Energy            | Energy                 | 82.4                |
| 4    | RHC  | Ramsay Health Care     | Healthcare             | 78.6                |
| 5    | BSL  | BlueScope              | Materials              | 70.4                |
| 6    | NHC  | New Hope               | Energy                 | 68.0                |
| 7    | EOS  | Electro Optic Systems  | Industrials            | 61.5                |
| 8    | WOW  | Woolworths Group       | Consumer Staples       | 60.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 102.9                 |
| DRO  | 255          | 96.6                  |
| EOS  | 255          | 95.9                  |
| CTD  | 255          | 93.7                  |
| ZIP  | 255          | 80.2                  |
| TUA  | 255          | 79.8                  |
| LTR  | 255          | 77.1                  |
| OBM  | 255          | 76.9                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| NXT  | NextDC                 | 2026-10-20 | -41.7          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 17                  |
| Industrials            | 10                  |
| Healthcare             | 10                  |
| Consumer Discretionary | 10                  |
| Consumer Staples       | 7                   |
| Communication Services | 7                   |
| Materials              | 6                   |
| Information Technology | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.29         | -79.5          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.74         | -77.2          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.76         | -74.1          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.69         | -74.1          |
| DRO  | Droneshield            | Industrials            | 4.86     | 1.52         | -68.7          |
| NXT  | NextDC                 | Information Technology | 16.49    | 5.35         | -67.6          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.32         | -64.8          |
| 360  | Life360                | Information Technology | 51.36    | 21.06        | -59.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.8            |
| DYL  | Deep Yellow            | -74.7            |
| LTR  | Liontown Resources     | -74.2            |
| DRO  | Droneshield            | -70.8            |
| COH  | Cochlear               | -69.2            |
| NXT  | NextDC                 | -67.6            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.12                  |
| Information Technology | 45.08                  |
| Financials             | 44.27                  |
| Energy                 | 41.24                  |
| Healthcare             | 35.98                  |
| Consumer Staples       | 31.82                  |
| Consumer Discretionary | 27.83                  |
| Communication Services | 27.52                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 17.0           | 41.5               | 0.41                 |
| Consumer Staples       | 6.7            | 28.2               | 0.24                 |
| Materials              | 4.9            | 48.4               | 0.1                  |
| Industrials            | 1.8            | 36.5               | 0.05                 |
| Utilities              | 1.1            | 27.9               | 0.04                 |
| Healthcare             | -3.2           | 41.9               | -0.08                |
| Financials             | -3.1           | 30.7               | -0.1                 |
| Information Technology | -21.3          | 52.4               | -0.41                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 157.01       |
| BHP  | BHP                    | Materials              | 260.3            | 58.54        |
| WBC  | Westpac                | Financials             | 136.3            | 35.53        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.22        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 79.86        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.37       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.93        |
| CSL  | CSL                    | Healthcare             | 67.4             | 196.08       |
