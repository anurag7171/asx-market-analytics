# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 12.27             | 65.83    | -53.69    |
| Materials        | 47        | 9.93              | 62.49    | -61.24    |
| Consumer Staples | 7         | 4.05              | 46.65    | -22.72    |
| Industrials      | 23        | 1.75              | 39.84    | -65.23    |
| Utilities        | 7         | -0.32             | 28.91    | -14.43    |
| Financials       | 36        | -1.35             | 46.24    | -57.6     |
| Healthcare       | 16        | -3.47             | 79.23    | -49.82    |
| Real Estate      | 16        | -18.06            | -0.45    | -56.23    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare             | 79.2                |
| 2    | RHC  | Ramsay Health Care   | Healthcare             | 78.0                |
| 3    | VEA  | Viva Energy          | Energy                 | 65.8                |
| 4    | CDA  | Codan                | Information Technology | 65.1                |
| 5    | ALK  | Alkane Resources     | Materials              | 62.5                |
| 6    | NHC  | New Hope             | Energy                 | 59.4                |
| 7    | BSL  | BlueScope            | Materials              | 58.3                |
| 8    | PDI  | Predictive Discovery | Materials              | 54.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 102.6                 |
| DRO  | 255          | 95.8                  |
| CTD  | 255          | 95.7                  |
| EOS  | 255          | 95.0                  |
| ZIP  | 255          | 86.3                  |
| TUA  | 255          | 85.7                  |
| OBM  | 255          | 78.4                  |
| LTR  | 255          | 75.9                  |

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
| Financials             | 23                  |
| Real Estate            | 12                  |
| Healthcare             | 10                  |
| Industrials            | 8                   |
| Consumer Staples       | 7                   |
| Materials              | 6                   |
| Consumer Discretionary | 6                   |
| Utilities              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.25         | -83.6          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.52         | -78.1          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.67         | -74.6          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.79         | -73.0          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.87         | -71.6          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.45         | -69.4          |
| NXT  | NextDC                 | Information Technology | 16.49    | 6.17         | -62.6          |
| 360  | Life360                | Information Technology | 51.36    | 20.83        | -59.4          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| DYL  | Deep Yellow            | -76.8            |
| LTR  | Liontown Resources     | -75.8            |
| CIA  | Champion Iron          | -71.6            |
| DRO  | Droneshield            | -70.0            |
| COH  | Cochlear               | -68.5            |
| NXT  | NextDC                 | -67.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.04                  |
| Information Technology | 45.3                   |
| Financials             | 44.46                  |
| Energy                 | 41.32                  |
| Healthcare             | 35.99                  |
| Consumer Staples       | 31.91                  |
| Consumer Discretionary | 28.08                  |
| Communication Services | 27.69                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 12.3           | 41.4               | 0.3                  |
| Materials              | 9.9            | 48.5               | 0.2                  |
| Consumer Staples       | 4.1            | 28.2               | 0.14                 |
| Industrials            | 1.8            | 36.5               | 0.05                 |
| Utilities              | -0.3           | 28.0               | -0.01                |
| Financials             | -1.3           | 30.9               | -0.04                |
| Healthcare             | -3.5           | 41.9               | -0.08                |
| Information Technology | -20.9          | 52.5               | -0.4                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 166.39       |
| BHP  | BHP                    | Materials              | 260.3            | 57.52        |
| WBC  | Westpac                | Financials             | 136.3            | 37.21        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 40.72        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 74.02        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 252.38       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.36        |
| CSL  | CSL                    | Healthcare             | 67.4             | 197.5        |
