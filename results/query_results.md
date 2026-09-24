# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 28.76             | 127.29   | -29.19    |
| Energy           | 11        | 19.92             | 82.05    | -36.59    |
| Industrials      | 23        | 5.86              | 81.08    | -56.91    |
| Healthcare       | 16        | -0.07             | 167.1    | -49.52    |
| Utilities        | 7         | -0.38             | 27.47    | -11.92    |
| Financials       | 36        | -0.39             | 78.07    | -58.48    |
| Consumer Staples | 7         | -2.68             | 45.47    | -25.99    |
| Real Estate      | 16        | -19.45            | 0.22     | -58.01    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 167.1               |
| 2    | PDI  | Predictive Discovery | Materials   | 127.3               |
| 3    | S32  | South32              | Materials   | 96.4                |
| 4    | SGM  | Sims Metal           | Materials   | 88.5                |
| 5    | VEA  | Viva Energy          | Energy      | 82.0                |
| 6    | NWH  | NRW Holdings         | Industrials | 81.1                |
| 7    | SFR  | Sandfire Resources   | Materials   | 81.0                |
| 8    | L1G  | L1 Group             | Financials  | 78.1                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.5                 |
| DRO  | 254          | 103.4                 |
| EOS  | 254          | 99.0                  |
| CTD  | 254          | 89.1                  |
| ZIP  | 254          | 80.3                  |
| TUA  | 254          | 79.3                  |
| LTR  | 254          | 77.5                  |
| OBM  | 254          | 77.2                  |

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
| Materials              | 20                  |
| Industrials            | 10                  |
| Financials             | 10                  |
| Healthcare             | 7                   |
| Energy                 | 4                   |
| Information Technology | 2                   |
| Consumer Staples       | 2                   |
| Consumer Discretionary | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.43         | -84.9          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.79         | -76.6          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.62         | -75.5          |
| WTC  | Wisetech Global        | Information Technology | 94.14    | 32.05        | -66.0          |
| 360  | Life360                | Information Technology | 55.44    | 19.31        | -65.2          |
| XRO  | Xero                   | Information Technology | 161.41   | 59.02        | -63.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.97         | -63.1          |
| GDG  | Generation Development | Financials             | 7.56     | 2.87         | -62.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -76.6            |
| DRO  | Droneshield            | -75.8            |
| ZIP  | Zip                    | -70.0            |
| WTC  | Wisetech Global        | -69.6            |
| COH  | Cochlear               | -69.2            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -65.6            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.68                  |
| Information Technology | 44.91                  |
| Financials             | 44.12                  |
| Energy                 | 40.83                  |
| Healthcare             | 36.18                  |
| Consumer Staples       | 32.27                  |
| Consumer Discretionary | 27.71                  |
| Communication Services | 27.34                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 28.8           | 48.8               | 0.59                 |
| Energy                 | 19.9           | 41.4               | 0.48                 |
| Industrials            | 5.9            | 36.4               | 0.16                 |
| Healthcare             | -0.1           | 42.3               | -0.0                 |
| Utilities              | -0.4           | 27.6               | -0.01                |
| Financials             | -0.4           | 30.7               | -0.01                |
| Consumer Staples       | -2.7           | 28.4               | -0.09                |
| Information Technology | -22.2          | 48.5               | -0.46                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 149.98       |
| BHP  | BHP                    | Materials              | 260.3            | 61.02        |
| WBC  | Westpac                | Financials             | 136.3            | 34.13        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.43        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 73.87        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 242.55       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.15        |
| CSL  | CSL                    | Healthcare             | 67.4             | 179.12       |
