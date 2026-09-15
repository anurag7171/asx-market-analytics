# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 34.03             | 142.63   | -29.95    |
| Energy           | 11        | 19.41             | 62.48    | -32.02    |
| Industrials      | 24        | 4.91              | 71.54    | -50.92    |
| Utilities        | 7         | -0.25             | 29.07    | -14.75    |
| Financials       | 36        | -2.14             | 64.71    | -56.63    |
| Consumer Staples | 7         | -4.63             | 42.42    | -31.66    |
| Healthcare       | 16        | -5.42             | 110.11   | -54.03    |
| Real Estate      | 16        | -19.65            | 1.04     | -56.57    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials   | 142.6               |
| 2    | 4DX  | 4DMedical            | Healthcare  | 110.1               |
| 3    | PLS  | PLS Group            | Materials   | 99.0                |
| 4    | S32  | South32              | Materials   | 91.4                |
| 5    | ALK  | Alkane Resources     | Materials   | 79.6                |
| 6    | SGM  | Sims Metal           | Materials   | 77.0                |
| 7    | GGP  | Greatland Resources  | Materials   | 71.6                |
| 8    | NWH  | NRW Holdings         | Industrials | 71.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.3                 |
| DRO  | 254          | 103.7                 |
| EOS  | 254          | 99.1                  |
| CTD  | 254          | 87.4                  |
| ZIP  | 254          | 79.6                  |
| LTR  | 254          | 77.4                  |
| OBM  | 254          | 77.3                  |
| TUA  | 254          | 75.8                  |

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
| Financials             | 13                  |
| Healthcare             | 8                   |
| Industrials            | 7                   |
| Energy                 | 7                   |
| Communication Services | 4                   |
| Utilities              | 3                   |
| Information Technology | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.4          | -85.1          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.6          | -75.8          |
| TUA  | Tuas                   | Communication Services | 7.69     | 2.13         | -72.3          |
| WTC  | Wisetech Global        | Information Technology | 97.09    | 33.05        | -66.0          |
| 360  | Life360                | Information Technology | 55.44    | 20.52        | -63.0          |
| GDG  | Generation Development | Financials             | 7.56     | 2.95         | -61.0          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.04         | -60.6          |
| XRO  | Xero                   | Information Technology | 163.97   | 67.44        | -58.9          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| DRO  | Droneshield            | -75.8            |
| TUA  | Tuas                   | -74.0            |
| WTC  | Wisetech Global        | -70.5            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.7            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.67                  |
| Information Technology | 44.89                  |
| Financials             | 44.13                  |
| Energy                 | 40.99                  |
| Healthcare             | 36.41                  |
| Consumer Staples       | 32.34                  |
| Consumer Discretionary | 27.67                  |
| Communication Services | 27.36                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 34.0           | 48.8               | 0.7                  |
| Energy                 | 19.4           | 42.0               | 0.46                 |
| Industrials            | 4.9            | 35.0               | 0.14                 |
| Utilities              | -0.2           | 27.4               | -0.01                |
| Financials             | -2.1           | 30.5               | -0.07                |
| Healthcare             | -5.4           | 42.6               | -0.13                |
| Consumer Staples       | -4.6           | 28.3               | -0.16                |
| Information Technology | -25.4          | 48.3               | -0.53                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 152.5        |
| BHP  | BHP                    | Materials              | 260.3            | 59.25        |
| WBC  | Westpac                | Financials             | 136.3            | 34.35        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.12        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 72.83        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 239.03       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.22        |
| CSL  | CSL                    | Healthcare             | 67.4             | 174.26       |
