# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 14.83             | 73.87    | -60.5     |
| Consumer Staples | 7         | 7.79              | 59.91    | -18.78    |
| Materials        | 47        | 7.72              | 65.03    | -50.51    |
| Industrials      | 23        | 2.94              | 61.35    | -68.48    |
| Utilities        | 7         | 1.55              | 34.94    | -15.18    |
| Financials       | 36        | -2.46             | 38.55    | -56.1     |
| Healthcare       | 16        | -3.51             | 103.78   | -50.15    |
| Real Estate      | 16        | -19.45            | -3.11    | -56.8     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 103.8               |
| 2    | RHC  | Ramsay Health Care     | Healthcare             | 80.7                |
| 3    | VEA  | Viva Energy            | Energy                 | 73.9                |
| 4    | CDA  | Codan                  | Information Technology | 66.8                |
| 5    | BSL  | BlueScope              | Materials              | 65.0                |
| 6    | NHC  | New Hope               | Energy                 | 64.4                |
| 7    | EOS  | Electro Optic Systems  | Industrials            | 61.3                |
| 8    | WOW  | Woolworths Group       | Consumer Staples       | 59.9                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 102.9                 |
| DRO  | 255          | 96.6                  |
| EOS  | 255          | 95.9                  |
| CTD  | 255          | 95.1                  |
| ZIP  | 255          | 80.1                  |
| TUA  | 255          | 80.0                  |
| LTR  | 255          | 77.1                  |
| OBM  | 255          | 76.7                  |

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
| Financials             | 18                  |
| Industrials            | 10                  |
| Consumer Discretionary | 10                  |
| Healthcare             | 9                   |
| Consumer Staples       | 7                   |
| Communication Services | 7                   |
| Real Estate            | 6                   |
| Utilities              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.82         | -76.2          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.85         | -75.8          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.71         | -75.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.69         | -73.9          |
| DRO  | Droneshield            | Industrials            | 4.79     | 1.51         | -68.5          |
| NXT  | NextDC                 | Information Technology | 16.49    | 5.75         | -65.1          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.32         | -64.8          |
| XRO  | Xero                   | Information Technology | 154.38   | 63.7         | -58.7          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.8            |
| DYL  | Deep Yellow            | -75.4            |
| LTR  | Liontown Resources     | -74.2            |
| DRO  | Droneshield            | -70.4            |
| COH  | Cochlear               | -69.2            |
| NXT  | NextDC                 | -67.6            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.1                   |
| Information Technology | 45.26                  |
| Financials             | 44.21                  |
| Energy                 | 41.26                  |
| Healthcare             | 35.98                  |
| Consumer Staples       | 31.81                  |
| Consumer Discretionary | 27.9                   |
| Communication Services | 27.53                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 14.8           | 41.5               | 0.36                 |
| Consumer Staples       | 7.8            | 28.2               | 0.28                 |
| Materials              | 7.7            | 48.2               | 0.16                 |
| Industrials            | 2.9            | 36.5               | 0.08                 |
| Utilities              | 1.5            | 27.9               | 0.06                 |
| Healthcare             | -3.5           | 41.9               | -0.08                |
| Financials             | -2.5           | 30.7               | -0.08                |
| Information Technology | -22.8          | 52.6               | -0.43                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 157.17       |
| BHP  | BHP                    | Materials              | 260.3            | 57.13        |
| WBC  | Westpac                | Financials             | 136.3            | 35.68        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.69        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.38        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.04       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.01        |
| CSL  | CSL                    | Healthcare             | 67.4             | 196.14       |
