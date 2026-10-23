# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 11.18             | 66.43    | -61.43    |
| Consumer Staples | 7         | 6.64              | 59.65    | -20.62    |
| Utilities        | 7         | 1.64              | 34.22    | -13.39    |
| Materials        | 47        | 1.56              | 65.8     | -54.19    |
| Industrials      | 23        | 1.25              | 52.21    | -69.34    |
| Financials       | 36        | -2.5              | 38.08    | -63.59    |
| Healthcare       | 16        | -4.99             | 84.89    | -48.47    |
| Real Estate      | 16        | -19.6             | -3.0     | -56.25    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical          | Healthcare             | 84.9                |
| 2    | RHC  | Ramsay Health Care | Healthcare             | 77.5                |
| 3    | NHC  | New Hope           | Energy                 | 66.4                |
| 4    | BSL  | BlueScope          | Materials              | 65.8                |
| 5    | VEA  | Viva Energy        | Energy                 | 62.7                |
| 6    | CDA  | Codan              | Information Technology | 61.3                |
| 7    | WOW  | Woolworths Group   | Consumer Staples       | 59.6                |
| 8    | REH  | Reece Group        | Industrials            | 52.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 102.7                 |
| DRO  | 255          | 96.7                  |
| EOS  | 255          | 95.8                  |
| CTD  | 255          | 95.2                  |
| ZIP  | 255          | 85.2                  |
| TUA  | 255          | 80.0                  |
| OBM  | 255          | 78.4                  |
| LTR  | 255          | 77.3                  |

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
| Consumer Discretionary | 11                  |
| Industrials            | 10                  |
| Real Estate            | 9                   |
| Healthcare             | 9                   |
| Consumer Staples       | 7                   |
| Communication Services | 7                   |
| Materials              | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.71         | -76.9          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.68         | -76.8          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.82         | -76.2          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.64         | -75.8          |
| DRO  | Droneshield            | Industrials            | 4.75     | 1.44         | -69.8          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.21         | -66.4          |
| NXT  | NextDC                 | Information Technology | 16.49    | 5.61         | -66.0          |
| ZIP  | Zip                    | Financials             | 4.1      | 1.46         | -64.4          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.8            |
| DYL  | Deep Yellow            | -76.8            |
| LTR  | Liontown Resources     | -75.8            |
| DRO  | Droneshield            | -70.1            |
| COH  | Cochlear               | -69.2            |
| NXT  | NextDC                 | -67.6            |
| CIA  | Champion Iron          | -66.4            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.18                  |
| Information Technology | 45.29                  |
| Financials             | 44.39                  |
| Energy                 | 41.31                  |
| Healthcare             | 36.03                  |
| Consumer Staples       | 31.86                  |
| Consumer Discretionary | 27.92                  |
| Communication Services | 27.71                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 11.2           | 41.5               | 0.27                 |
| Consumer Staples       | 6.6            | 28.2               | 0.24                 |
| Utilities              | 1.6            | 27.9               | 0.06                 |
| Materials              | 1.6            | 48.5               | 0.03                 |
| Industrials            | 1.2            | 36.5               | 0.03                 |
| Financials             | -2.5           | 30.9               | -0.08                |
| Healthcare             | -5.0           | 41.9               | -0.12                |
| Information Technology | -23.2          | 52.6               | -0.44                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 164.0        |
| BHP  | BHP                    | Materials              | 260.3            | 55.05        |
| WBC  | Westpac                | Financials             | 136.3            | 36.79        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 40.04        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 80.29        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 247.04       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.31        |
| CSL  | CSL                    | Healthcare             | 67.4             | 196.7        |
