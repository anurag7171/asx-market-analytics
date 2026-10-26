# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 11.6              | 71.4     | -56.21    |
| Consumer Staples | 7         | 5.99              | 56.32    | -17.53    |
| Materials        | 47        | 3.58              | 64.69    | -54.14    |
| Utilities        | 7         | 1.15              | 32.88    | -12.48    |
| Industrials      | 23        | 0.78              | 45.07    | -68.26    |
| Financials       | 36        | -2.45             | 40.75    | -60.39    |
| Healthcare       | 16        | -4.52             | 92.19    | -49.75    |
| Real Estate      | 16        | -18.92            | -1.77    | -55.65    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical          | Healthcare             | 92.2                |
| 2    | RHC  | Ramsay Health Care | Healthcare             | 75.5                |
| 3    | VEA  | Viva Energy        | Energy                 | 71.4                |
| 4    | BSL  | BlueScope          | Materials              | 64.7                |
| 5    | NHC  | New Hope           | Energy                 | 60.7                |
| 6    | WOW  | Woolworths Group   | Consumer Staples       | 56.3                |
| 7    | CDA  | Codan              | Information Technology | 56.0                |
| 8    | STO  | Santos             | Energy                 | 47.8                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 102.8                 |
| DRO  | 254          | 96.8                  |
| CTD  | 254          | 95.8                  |
| EOS  | 254          | 95.4                  |
| ZIP  | 254          | 86.1                  |
| TUA  | 254          | 85.6                  |
| OBM  | 254          | 78.9                  |
| LTR  | 254          | 77.0                  |

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
| Real Estate            | 11                  |
| Consumer Discretionary | 11                  |
| Industrials            | 9                   |
| Healthcare             | 9                   |
| Consumer Staples       | 7                   |
| Communication Services | 7                   |
| Materials              | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.26         | -83.4          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.38         | -79.0          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.7          | -75.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.68         | -74.2          |
| DRO  | Droneshield            | Industrials            | 4.75     | 1.46         | -69.3          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.19         | -66.7          |
| NXT  | NextDC                 | Information Technology | 16.49    | 5.54         | -66.4          |
| ZIP  | Zip                    | Financials             | 4.1      | 1.62         | -60.5          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.4            |
| DYL  | Deep Yellow            | -76.8            |
| LTR  | Liontown Resources     | -75.8            |
| DRO  | Droneshield            | -70.1            |
| COH  | Cochlear               | -69.2            |
| NXT  | NextDC                 | -67.6            |
| CIA  | Champion Iron          | -66.7            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.1                   |
| Information Technology | 45.29                  |
| Financials             | 44.4                   |
| Energy                 | 41.28                  |
| Healthcare             | 36.01                  |
| Consumer Staples       | 31.89                  |
| Consumer Discretionary | 27.95                  |
| Communication Services | 27.72                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 11.6           | 41.6               | 0.28                 |
| Consumer Staples       | 6.0            | 28.2               | 0.21                 |
| Materials              | 3.6            | 48.6               | 0.07                 |
| Utilities              | 1.1            | 27.9               | 0.04                 |
| Industrials            | 0.8            | 36.5               | 0.02                 |
| Financials             | -2.5           | 30.9               | -0.08                |
| Healthcare             | -4.5           | 41.9               | -0.11                |
| Information Technology | -24.1          | 52.7               | -0.46                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 163.2        |
| BHP  | BHP                    | Materials              | 260.3            | 55.62        |
| WBC  | Westpac                | Financials             | 136.3            | 36.53        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.9         |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 79.03        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 246.56       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.0         |
| CSL  | CSL                    | Healthcare             | 67.4             | 195.14       |
