# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 34.41             | 148.0    | -32.18    |
| Energy           | 11        | 18.14             | 64.05    | -37.26    |
| Industrials      | 24        | 5.08              | 70.27    | -48.25    |
| Utilities        | 7         | 0.9               | 28.62    | -12.11    |
| Financials       | 36        | -2.66             | 63.97    | -57.32    |
| Consumer Staples | 7         | -5.58             | 42.09    | -32.05    |
| Healthcare       | 16        | -5.86             | 102.87   | -53.65    |
| Real Estate      | 16        | -19.88            | 1.32     | -57.88    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials   | 148.0               |
| 2    | 4DX  | 4DMedical            | Healthcare  | 102.9               |
| 3    | PLS  | PLS Group            | Materials   | 97.7                |
| 4    | S32  | South32              | Materials   | 96.5                |
| 5    | ALK  | Alkane Resources     | Materials   | 91.2                |
| 6    | SGM  | Sims Metal           | Materials   | 77.6                |
| 7    | SFR  | Sandfire Resources   | Materials   | 72.3                |
| 8    | GGP  | Greatland Resources  | Materials   | 71.5                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.5                 |
| DRO  | 254          | 103.6                 |
| EOS  | 254          | 99.1                  |
| CTD  | 254          | 87.5                  |
| ZIP  | 254          | 79.6                  |
| LTR  | 254          | 77.4                  |
| OBM  | 254          | 77.1                  |
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
| Materials              | 24                  |
| Financials             | 11                  |
| Healthcare             | 7                   |
| Energy                 | 7                   |
| Industrials            | 6                   |
| Communication Services | 4                   |
| Utilities              | 2                   |
| Information Technology | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.31         | -85.6          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.63         | -75.4          |
| TUA  | Tuas                   | Communication Services | 7.64     | 2.14         | -72.0          |
| WTC  | Wisetech Global        | Information Technology | 96.95    | 32.27        | -66.7          |
| 360  | Life360                | Information Technology | 55.44    | 19.4         | -65.0          |
| GDG  | Generation Development | Financials             | 7.56     | 2.92         | -61.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.02         | -61.4          |
| XRO  | Xero                   | Information Technology | 163.97   | 66.34        | -59.5          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| DRO  | Droneshield            | -75.8            |
| TUA  | Tuas                   | -73.8            |
| WTC  | Wisetech Global        | -70.4            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.6            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.76                  |
| Information Technology | 44.89                  |
| Financials             | 44.14                  |
| Energy                 | 41.09                  |
| Healthcare             | 36.43                  |
| Consumer Staples       | 32.31                  |
| Consumer Discretionary | 27.69                  |
| Communication Services | 27.35                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 34.4           | 48.8               | 0.7                  |
| Energy                 | 18.1           | 41.9               | 0.43                 |
| Industrials            | 5.1            | 35.1               | 0.14                 |
| Utilities              | 0.9            | 27.4               | 0.03                 |
| Financials             | -2.7           | 30.5               | -0.09                |
| Healthcare             | -5.9           | 42.7               | -0.14                |
| Consumer Staples       | -5.6           | 28.3               | -0.2                 |
| Information Technology | -24.3          | 48.4               | -0.5                 |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 151.54       |
| BHP  | BHP                    | Materials              | 260.3            | 60.2         |
| WBC  | Westpac                | Financials             | 136.3            | 34.43        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.01        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 72.29        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 239.82       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.02        |
| CSL  | CSL                    | Healthcare             | 67.4             | 174.41       |
