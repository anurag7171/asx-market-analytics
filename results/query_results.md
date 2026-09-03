# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 46.34             | 130.17   | -25.53    |
| Energy           | 11        | 20.52             | 48.18    | -30.0     |
| Industrials      | 24        | 9.09              | 97.42    | -46.46    |
| Utilities        | 7         | 5.24              | 32.81    | -12.41    |
| Healthcare       | 16        | 2.46              | 197.84   | -51.43    |
| Financials       | 36        | 1.47              | 80.29    | -48.32    |
| Consumer Staples | 7         | -3.28             | 51.1     | -30.83    |
| Real Estate      | 17        | -13.64            | 10.08    | -52.82    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 197.8               |
| 2    | PLS  | PLS Group            | Materials   | 130.2               |
| 3    | RSG  | Resolute Mining      | Materials   | 106.4               |
| 4    | S32  | South32              | Materials   | 103.6               |
| 5    | NWH  | NRW Holdings         | Industrials | 97.4                |
| 6    | GGP  | Greatland Resources  | Materials   | 85.9                |
| 7    | VAU  | Vault Minerals       | Materials   | 85.6                |
| 8    | PDI  | Predictive Discovery | Materials   | 84.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 123.3                 |
| DRO  | 254          | 103.9                 |
| EOS  | 254          | 99.7                  |
| CTD  | 254          | 85.1                  |
| ZIP  | 254          | 79.6                  |
| LTR  | 254          | 79.4                  |
| OBM  | 254          | 78.9                  |
| TUA  | 254          | 76.1                  |

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
| Materials              | 37                  |
| Financials             | 15                  |
| Energy                 | 10                  |
| Healthcare             | 9                   |
| Industrials            | 7                   |
| Utilities              | 5                   |
| Communication Services | 5                   |
| Consumer Staples       | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.32         | -85.6          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.67         | -74.8          |
| TUA  | Tuas                   | Communication Services | 8.32     | 2.12         | -74.5          |
| 360  | Life360                | Information Technology | 55.44    | 19.93        | -64.1          |
| WTC  | Wisetech Global        | Information Technology | 97.44    | 36.76        | -62.3          |
| GDG  | Generation Development | Financials             | 7.58     | 3.14         | -58.6          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 7.37         | -56.2          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.19         | -54.9          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -85.6            |
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
| Materials              | 49.56                  |
| Information Technology | 45.51                  |
| Financials             | 44.13                  |
| Energy                 | 40.73                  |
| Healthcare             | 36.63                  |
| Consumer Staples       | 32.63                  |
| Consumer Discretionary | 27.6                   |
| Communication Services | 27.44                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 46.3           | 49.1               | 0.94                 |
| Energy                 | 20.5           | 41.7               | 0.49                 |
| Industrials            | 9.1            | 35.2               | 0.26                 |
| Utilities              | 5.2            | 27.5               | 0.19                 |
| Healthcare             | 2.5            | 43.6               | 0.06                 |
| Financials             | 1.5            | 30.7               | 0.05                 |
| Consumer Staples       | -3.3           | 28.2               | -0.12                |
| Information Technology | -18.4          | 48.2               | -0.38                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 160.58       |
| BHP  | BHP                    | Materials              | 260.3            | 63.78        |
| WBC  | Westpac                | Financials             | 136.3            | 34.91        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.01        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 76.91        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 249.52       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.27        |
| CSL  | CSL                    | Healthcare             | 67.4             | 175.5        |
