# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 33.77             | 133.07   | -31.66    |
| Energy           | 11        | 18.09             | 61.67    | -31.59    |
| Industrials      | 24        | 6.37              | 73.89    | -45.78    |
| Utilities        | 7         | 0.96              | 28.57    | -9.18     |
| Financials       | 36        | -1.92             | 63.23    | -57.75    |
| Consumer Staples | 7         | -4.32             | 42.42    | -29.65    |
| Healthcare       | 16        | -4.83             | 102.13   | -53.01    |
| Real Estate      | 16        | -18.12            | 3.0      | -58.38    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials   | 133.1               |
| 2    | 4DX  | 4DMedical            | Healthcare  | 102.1               |
| 3    | S32  | South32              | Materials   | 92.0                |
| 4    | PLS  | PLS Group            | Materials   | 88.4                |
| 5    | ALK  | Alkane Resources     | Materials   | 88.3                |
| 6    | SGM  | Sims Metal           | Materials   | 77.1                |
| 7    | NWH  | NRW Holdings         | Industrials | 73.9                |
| 8    | SFR  | Sandfire Resources   | Materials   | 72.9                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.4                 |
| DRO  | 254          | 103.8                 |
| EOS  | 254          | 99.2                  |
| CTD  | 254          | 88.4                  |
| ZIP  | 254          | 79.6                  |
| LTR  | 254          | 77.3                  |
| OBM  | 254          | 77.1                  |
| TUA  | 254          | 76.0                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |
| ZIP  | Zip                    | 2026-02-18 | -34.4          |
| TPG  | TPG Telecom            | 2025-11-13 | -32.1          |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Materials              | 22                  |
| Financials             | 14                  |
| Industrials            | 9                   |
| Healthcare             | 8                   |
| Energy                 | 7                   |
| Communication Services | 5                   |
| Utilities              | 3                   |
| Information Technology | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.6          | -83.8          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.74         | -73.7          |
| TUA  | Tuas                   | Communication Services | 7.64     | 2.24         | -70.7          |
| WTC  | Wisetech Global        | Information Technology | 96.95    | 31.89        | -67.1          |
| 360  | Life360                | Information Technology | 55.44    | 19.12        | -65.5          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.01         | -61.7          |
| GDG  | Generation Development | Financials             | 7.56     | 2.92         | -61.4          |
| XRO  | Xero                   | Information Technology | 163.97   | 65.45        | -60.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| DRO  | Droneshield            | -75.8            |
| TUA  | Tuas                   | -73.8            |
| WTC  | Wisetech Global        | -70.4            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.84                  |
| Information Technology | 44.96                  |
| Financials             | 44.26                  |
| Energy                 | 41.17                  |
| Healthcare             | 36.48                  |
| Consumer Staples       | 32.36                  |
| Consumer Discretionary | 27.73                  |
| Communication Services | 27.38                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 33.8           | 48.9               | 0.69                 |
| Energy                 | 18.1           | 41.7               | 0.43                 |
| Industrials            | 6.4            | 35.1               | 0.18                 |
| Utilities              | 1.0            | 27.4               | 0.04                 |
| Financials             | -1.9           | 30.6               | -0.06                |
| Healthcare             | -4.8           | 42.7               | -0.11                |
| Consumer Staples       | -4.3           | 28.3               | -0.15                |
| Information Technology | -24.8          | 48.4               | -0.51                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 154.01       |
| BHP  | BHP                    | Materials              | 260.3            | 60.21        |
| WBC  | Westpac                | Financials             | 136.3            | 34.83        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.78        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 72.86        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 239.64       |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.22        |
| CSL  | CSL                    | Healthcare             | 67.4             | 177.56       |
