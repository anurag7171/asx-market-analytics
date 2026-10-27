# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Energy           | 11        | 13.19             | 72.59    | -53.73    |
| Consumer Staples | 7         | 5.7               | 56.82    | -19.77    |
| Materials        | 47        | 5.37              | 64.39    | -53.3     |
| Utilities        | 7         | 1.61              | 32.76    | -11.21    |
| Industrials      | 23        | 1.23              | 46.49    | -68.04    |
| Financials       | 36        | -2.47             | 40.75    | -58.84    |
| Healthcare       | 16        | -5.1              | 88.02    | -50.46    |
| Real Estate      | 16        | -19.33            | -1.77    | -56.2     |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical          | Healthcare             | 88.0                |
| 2    | RHC  | Ramsay Health Care | Healthcare             | 77.4                |
| 3    | VEA  | Viva Energy        | Energy                 | 72.6                |
| 4    | BSL  | BlueScope          | Materials              | 64.4                |
| 5    | NHC  | New Hope           | Energy                 | 61.5                |
| 6    | CDA  | Codan              | Information Technology | 60.1                |
| 7    | WOW  | Woolworths Group   | Consumer Staples       | 56.8                |
| 8    | ALK  | Alkane Resources   | Materials              | 52.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 255          | 102.6                 |
| DRO  | 255          | 96.6                  |
| CTD  | 255          | 95.6                  |
| EOS  | 255          | 95.3                  |
| ZIP  | 255          | 86.0                  |
| TUA  | 255          | 85.4                  |
| OBM  | 255          | 78.8                  |
| LTR  | 255          | 76.8                  |

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
| Financials             | 20                  |
| Real Estate            | 12                  |
| Industrials            | 11                  |
| Healthcare             | 9                   |
| Consumer Discretionary | 9                   |
| Materials              | 7                   |
| Consumer Staples       | 7                   |
| Utilities              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.26         | -83.5          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.4          | -78.8          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.74         | -74.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.69         | -73.9          |
| DRO  | Droneshield            | Industrials            | 4.75     | 1.47         | -69.1          |
| CIA  | Champion Iron          | Materials              | 6.59     | 2.23         | -66.1          |
| NXT  | NextDC                 | Information Technology | 16.49    | 5.75         | -65.1          |
| 360  | Life360                | Information Technology | 51.36    | 20.43        | -60.2          |

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
| Information Technology | 45.39                  |
| Financials             | 44.45                  |
| Energy                 | 41.29                  |
| Healthcare             | 36.07                  |
| Consumer Staples       | 31.92                  |
| Consumer Discretionary | 27.94                  |
| Communication Services | 27.7                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 13.2           | 41.6               | 0.32                 |
| Consumer Staples       | 5.7            | 28.2               | 0.2                  |
| Materials              | 5.4            | 48.5               | 0.11                 |
| Utilities              | 1.6            | 27.9               | 0.06                 |
| Industrials            | 1.2            | 36.5               | 0.03                 |
| Financials             | -2.5           | 30.9               | -0.08                |
| Healthcare             | -5.1           | 41.9               | -0.12                |
| Information Technology | -24.1          | 52.6               | -0.46                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 162.02       |
| BHP  | BHP                    | Materials              | 260.3            | 57.99        |
| WBC  | Westpac                | Financials             | 136.3            | 36.18        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 39.86        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.83        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 248.51       |
| NAB  | National Australia Ban | Financials             | 69.8             | 40.29        |
| CSL  | CSL                    | Healthcare             | 67.4             | 196.78       |
