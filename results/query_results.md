# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 9.68              | 65.28    | -59.94    |
| Materials        | 47        | 7.5               | 65.52    | -63.88    |
| Consumer Staples | 7         | 4.21              | 44.58    | -21.69    |
| Industrials      | 23        | 2.51              | 43.26    | -66.34    |
| Utilities        | 7         | -0.19             | 31.17    | -14.39    |
| Financials       | 36        | -1.3              | 50.98    | -57.0     |
| Healthcare       | 16        | -6.0              | 78.07    | -48.54    |
| Real Estate      | 16        | -15.17            | 0.78     | -56.62    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care   | Healthcare             | 78.1                |
| 2    | ALK  | Alkane Resources     | Materials              | 65.5                |
| 3    | VEA  | Viva Energy          | Energy                 | 65.3                |
| 4    | CDA  | Codan                | Information Technology | 64.8                |
| 5    | BSL  | BlueScope            | Materials              | 59.6                |
| 6    | PDI  | Predictive Discovery | Materials              | 51.3                |
| 7    | STO  | Santos               | Energy                 | 51.2                |
| 8    | NHC  | New Hope             | Energy                 | 51.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 105.8                 |
| DRO  | 255          | 95.9                  |
| CTD  | 255          | 95.7                  |
| EOS  | 255          | 95.2                  |
| ZIP  | 255          | 86.4                  |
| TUA  | 255          | 85.7                  |
| OBM  | 255          | 78.4                  |
| LTR  | 255          | 75.5                  |

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
| Real Estate            | 15                  |
| Industrials            | 12                  |
| Healthcare             | 12                  |
| Consumer Discretionary | 10                  |
| Materials              | 7                   |
| Consumer Staples       | 6                   |
| Information Technology | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.27         | -83.3          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.56         | -77.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.62         | -76.5          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.71         | -75.4          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.37         | -71.1          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.92         | -70.9          |
| NXT  | NextDC                 | Information Technology | 16.49    | 5.87         | -64.4          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.44         | -64.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| DYL  | Deep Yellow            | -76.8            |
| LTR  | Liontown Resources     | -76.5            |
| CIA  | Champion Iron          | -71.6            |
| DRO  | Droneshield            | -71.1            |
| COH  | Cochlear               | -68.4            |
| NXT  | NextDC                 | -67.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.13                  |
| Information Technology | 45.38                  |
| Financials             | 44.56                  |
| Energy                 | 41.35                  |
| Healthcare             | 35.99                  |
| Consumer Staples       | 32.41                  |
| Consumer Discretionary | 28.09                  |
| Communication Services | 27.75                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 9.7            | 41.4               | 0.23                 |
| Materials              | 7.5            | 48.5               | 0.15                 |
| Consumer Staples       | 4.2            | 28.4               | 0.15                 |
| Industrials            | 2.5            | 36.5               | 0.07                 |
| Utilities              | -0.2           | 28.0               | -0.01                |
| Financials             | -1.3           | 30.8               | -0.04                |
| Healthcare             | -6.0           | 42.1               | -0.14                |
| Information Technology | -20.8          | 52.5               | -0.4                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 166.72       |
| BHP  | BHP                    | Materials              | 260.3            | 57.56        |
| WBC  | Westpac                | Financials             | 136.3            | 36.82        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 40.81        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 76.69        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 252.44       |
| NAB  | National Australia Ban | Financials             | 69.8             | 41.51        |
| CSL  | CSL                    | Healthcare             | 67.4             | 200.73       |
