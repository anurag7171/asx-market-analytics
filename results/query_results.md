# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 13.35             | 65.15    | -49.04    |
| Materials        | 47        | 11.98             | 68.77    | -51.89    |
| Consumer Staples | 7         | 4.62              | 55.28    | -22.98    |
| Industrials      | 23        | 1.01              | 45.98    | -69.26    |
| Utilities        | 7         | -0.66             | 29.31    | -13.5     |
| Financials       | 36        | -3.18             | 43.33    | -57.44    |
| Healthcare       | 16        | -4.27             | 91.62    | -51.67    |
| Real Estate      | 16        | -20.35            | -3.0     | -58.2     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical          | Healthcare             | 91.6                |
| 2    | RHC  | Ramsay Health Care | Healthcare             | 80.1                |
| 3    | ALK  | Alkane Resources   | Materials              | 68.8                |
| 4    | CDA  | Codan              | Information Technology | 67.2                |
| 5    | VEA  | Viva Energy        | Energy                 | 65.2                |
| 6    | BSL  | BlueScope          | Materials              | 64.9                |
| 7    | NHC  | New Hope           | Energy                 | 56.7                |
| 8    | WOW  | Woolworths Group   | Consumer Staples       | 55.3                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 102.5                 |
| DRO  | 255          | 96.6                  |
| CTD  | 255          | 95.7                  |
| EOS  | 255          | 95.2                  |
| ZIP  | 255          | 86.1                  |
| TUA  | 255          | 85.6                  |
| OBM  | 255          | 78.4                  |
| LTR  | 255          | 75.8                  |

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
| Financials             | 21                  |
| Industrials            | 9                   |
| Consumer Discretionary | 9                   |
| Healthcare             | 8                   |
| Real Estate            | 7                   |
| Materials              | 6                   |
| Consumer Staples       | 6                   |
| Information Technology | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.31         | -82.8          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.57         | -77.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.7          | -73.3          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.8          | -72.5          |
| DRO  | Droneshield            | Industrials            | 4.75     | 1.46         | -69.3          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.26         | -65.7          |
| NXT  | NextDC                 | Information Technology | 16.49    | 6.29         | -61.9          |
| 360  | Life360                | Information Technology | 51.36    | 20.65        | -59.8          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.5            |
| DYL  | Deep Yellow            | -76.8            |
| LTR  | Liontown Resources     | -75.8            |
| DRO  | Droneshield            | -70.1            |
| COH  | Cochlear               | -69.2            |
| NXT  | NextDC                 | -67.6            |
| CIA  | Champion Iron          | -66.7            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.14                  |
| Information Technology | 45.42                  |
| Financials             | 44.47                  |
| Energy                 | 41.33                  |
| Healthcare             | 36.14                  |
| Consumer Staples       | 31.96                  |
| Consumer Discretionary | 28.02                  |
| Communication Services | 27.76                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 13.3           | 41.6               | 0.32                 |
| Materials              | 12.0           | 48.4               | 0.25                 |
| Consumer Staples       | 4.6            | 28.2               | 0.16                 |
| Industrials            | 1.0            | 36.6               | 0.03                 |
| Utilities              | -0.7           | 28.0               | -0.02                |
| Healthcare             | -4.3           | 41.6               | -0.1                 |
| Financials             | -3.2           | 30.9               | -0.1                 |
| Information Technology | -21.2          | 52.5               | -0.4                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 163.01       |
| BHP  | BHP                    | Materials              | 260.3            | 58.04        |
| WBC  | Westpac                | Financials             | 136.3            | 36.53        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.86        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.14        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.26       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.42        |
| CSL  | CSL                    | Healthcare             | 67.4             | 197.1        |
