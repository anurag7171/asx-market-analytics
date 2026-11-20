# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Utilities              | 7         | 5.65              | 28.53    | -8.35     |
| Industrials            | 23        | 5.42              | 72.9     | -44.97    |
| Consumer Staples       | 7         | 5.3               | 53.27    | -26.23    |
| Financials             | 36        | 0.32              | 39.73    | -59.62    |
| Energy                 | 11        | -3.39             | 37.28    | -63.05    |
| Healthcare             | 16        | -4.05             | 72.73    | -55.45    |
| Information Technology | 7         | -5.06             | 66.13    | -43.52    |
| Materials              | 47        | -5.85             | 60.02    | -67.94    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | REH  | Reece Group            | Industrials            | 72.9                |
| 2    | RHC  | Ramsay Health Care     | Healthcare             | 72.7                |
| 3    | CDA  | Codan                  | Information Technology | 66.1                |
| 4    | ALK  | Alkane Resources       | Materials              | 60.0                |
| 5    | WOW  | Woolworths Group       | Consumer Staples       | 53.3                |
| 6    | BSL  | BlueScope              | Materials              | 49.8                |
| 7    | 4DX  | 4DMedical              | Healthcare             | 48.5                |
| 8    | EOS  | Electro Optic Systems  | Industrials            | 44.0                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.1                 |
| CTD  | 254          | 97.3                  |
| EOS  | 254          | 94.6                  |
| ZIP  | 254          | 88.0                  |
| DRO  | 254          | 87.4                  |
| TUA  | 254          | 86.5                  |
| OBM  | 254          | 80.8                  |
| NXT  | 254          | 79.8                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| NXT  | NextDC                 | 2026-11-04 | 50.8           |
| NXT  | NextDC                 | 2026-10-20 | -41.7          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 18                  |
| Real Estate            | 14                  |
| Industrials            | 13                  |
| Healthcare             | 10                  |
| Consumer Discretionary | 8                   |
| Utilities              | 7                   |
| Communication Services | 6                   |
| Information Technology | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.39         | -81.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.56         | -79.0          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.41         | -78.8          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.63         | -78.4          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.04         | -78.1          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.74         | -73.7          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.55         | -68.6          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.16         | -68.2          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -79.0            |
| DYL  | Deep Yellow            | -78.4            |
| DRO  | Droneshield            | -78.1            |
| CIA  | Champion Iron          | -73.9            |
| 4DX  | 4DMedical              | -68.7            |
| GQG  | GQG Partners           | -68.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.64                  |
| Information Technology | 46.41                  |
| Financials             | 45.64                  |
| Energy                 | 42.25                  |
| Healthcare             | 36.16                  |
| Consumer Staples       | 32.47                  |
| Communication Services | 27.86                  |
| Consumer Discretionary | 27.81                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Utilities              | 5.7            | 28.1               | 0.2                  |
| Consumer Staples       | 5.3            | 28.7               | 0.18                 |
| Industrials            | 5.4            | 36.9               | 0.15                 |
| Financials             | 0.3            | 30.9               | 0.01                 |
| Energy                 | -3.4           | 42.4               | -0.08                |
| Information Technology | -5.1           | 55.4               | -0.09                |
| Healthcare             | -4.1           | 42.4               | -0.1                 |
| Materials              | -5.8           | 49.8               | -0.12                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 169.92       |
| BHP  | BHP                    | Materials              | 260.3            | 51.4         |
| WBC  | Westpac                | Financials             | 136.3            | 35.94        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.58        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 76.69        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 220.03       |
| NAB  | National Australia Ban | Financials             | 69.8             | 36.24        |
| CSL  | CSL                    | Healthcare             | 67.4             | 197.29       |
