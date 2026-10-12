# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Energy                 | 11        | 19.09             | 91.31    | -54.59    |
| Materials              | 47        | 14.07             | 69.54    | -40.67    |
| Consumer Staples       | 7         | 4.45              | 54.17    | -22.29    |
| Industrials            | 23        | 1.89              | 60.53    | -74.63    |
| Utilities              | 7         | 0.89              | 29.2     | -9.85     |
| Financials             | 36        | -2.95             | 51.52    | -62.38    |
| Healthcare             | 16        | -3.78             | 107.88   | -52.27    |
| Information Technology | 7         | -15.86            | 108.23   | -61.28    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name       | sector_name            | one_year_return_pct |
| ---- | ---- | ------------------ | ---------------------- | ------------------- |
| 1    | CDA  | Codan              | Information Technology | 108.2               |
| 2    | 4DX  | 4DMedical          | Healthcare             | 107.9               |
| 3    | VEA  | Viva Energy        | Energy                 | 91.3                |
| 4    | RHC  | Ramsay Health Care | Healthcare             | 72.6                |
| 5    | SGM  | Sims Metal         | Materials              | 69.5                |
| 6    | S32  | South32            | Materials              | 68.3                |
| 7    | BSL  | BlueScope          | Materials              | 65.5                |
| 8    | NHC  | New Hope           | Energy                 | 64.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 103.4                 |
| DRO  | 253          | 97.7                  |
| EOS  | 253          | 96.9                  |
| CTD  | 253          | 90.2                  |
| ZIP  | 253          | 80.5                  |
| TUA  | 253          | 79.5                  |
| LTR  | 253          | 77.9                  |
| OBM  | 253          | 77.0                  |

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
| Materials              | 12                  |
| Financials             | 12                  |
| Industrials            | 10                  |
| Healthcare             | 8                   |
| Energy                 | 5                   |
| Consumer Staples       | 5                   |
| Consumer Discretionary | 4                   |
| Utilities              | 3                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.35         | -85.4          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.59         | -79.2          |
| DRO  | Droneshield            | Industrials            | 6.03     | 1.53         | -74.6          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.75         | -71.6          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.94         | -67.7          |
| GDG  | Generation Development | Financials             | 7.56     | 2.72         | -64.0          |
| 360  | Life360                | Information Technology | 52.99    | 20.52        | -61.3          |
| XRO  | Xero                   | Information Technology | 157.07   | 61.49        | -60.9          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -79.2            |
| DRO  | Droneshield            | -74.6            |
| LTR  | Liontown Resources     | -71.6            |
| COH  | Cochlear               | -69.2            |
| ZIP  | Zip                    | -68.9            |
| DYL  | Deep Yellow            | -67.7            |
| WTC  | Wisetech Global        | -66.3            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.27                  |
| Information Technology | 44.75                  |
| Financials             | 44.17                  |
| Energy                 | 40.94                  |
| Healthcare             | 35.84                  |
| Consumer Staples       | 31.96                  |
| Consumer Discretionary | 27.79                  |
| Communication Services | 27.36                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 19.1           | 41.7               | 0.46                 |
| Materials              | 14.1           | 48.5               | 0.29                 |
| Consumer Staples       | 4.4            | 28.2               | 0.16                 |
| Industrials            | 1.9            | 36.3               | 0.05                 |
| Utilities              | 0.9            | 27.9               | 0.03                 |
| Healthcare             | -3.8           | 42.0               | -0.09                |
| Financials             | -3.0           | 30.7               | -0.1                 |
| Information Technology | -15.9          | 49.6               | -0.32                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 151.0        |
| BHP  | BHP                    | Materials              | 260.3            | 62.43        |
| WBC  | Westpac                | Financials             | 136.3            | 34.63        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.91        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 77.38        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 253.46       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.53        |
| CSL  | CSL                    | Healthcare             | 67.4             | 184.81       |
