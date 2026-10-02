# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Materials              | 47        | 18.29             | 129.21   | -34.86    |
| Energy                 | 11        | 17.18             | 86.35    | -46.15    |
| Industrials            | 23        | 2.77              | 77.28    | -64.77    |
| Consumer Staples       | 7         | -0.47             | 48.03    | -21.94    |
| Utilities              | 7         | -0.92             | 25.98    | -12.04    |
| Financials             | 36        | -2.98             | 69.16    | -60.98    |
| Healthcare             | 16        | -5.76             | 105.69   | -54.46    |
| Information Technology | 7         | -15.24            | 124.59   | -63.43    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name            | one_year_return_pct |
| ---- | ---- | -------------------- | ---------------------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials              | 129.2               |
| 2    | CDA  | Codan                | Information Technology | 124.6               |
| 3    | 4DX  | 4DMedical            | Healthcare             | 105.7               |
| 4    | VEA  | Viva Energy          | Energy                 | 86.3                |
| 5    | S32  | South32              | Materials              | 82.9                |
| 6    | SGM  | Sims Metal           | Materials              | 79.5                |
| 7    | NWH  | NRW Holdings         | Industrials            | 77.3                |
| 8    | RHC  | Ramsay Health Care   | Healthcare             | 75.8                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 104.3                 |
| DRO  | 254          | 98.9                  |
| EOS  | 254          | 96.9                  |
| CTD  | 254          | 89.7                  |
| ZIP  | 254          | 80.3                  |
| TUA  | 254          | 79.5                  |
| LTR  | 254          | 77.9                  |
| OBM  | 254          | 76.9                  |

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
| Materials              | 13                  |
| Industrials            | 9                   |
| Financials             | 7                   |
| Healthcare             | 6                   |
| Energy                 | 4                   |
| Consumer Discretionary | 3                   |
| Communication Services | 3                   |
| Utilities              | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.41         | -85.0          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.72         | -77.5          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.82         | -72.3          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.8          | -69.9          |
| XRO  | Xero                   | Information Technology | 160.95   | 57.85        | -64.1          |
| GDG  | Generation Development | Financials             | 7.56     | 2.72         | -64.0          |
| 360  | Life360                | Information Technology | 55.44    | 20.4         | -63.2          |
| WTC  | Wisetech Global        | Information Technology | 89.75    | 33.43        | -62.8          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -78.1            |
| DRO  | Droneshield            | -76.1            |
| LTR  | Liontown Resources     | -70.1            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.2            |
| WTC  | Wisetech Global        | -68.1            |
| 360  | Life360                | -67.7            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.47                  |
| Information Technology | 44.97                  |
| Financials             | 44.2                   |
| Energy                 | 40.78                  |
| Healthcare             | 35.95                  |
| Consumer Staples       | 32.2                   |
| Consumer Discretionary | 27.78                  |
| Communication Services | 27.34                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Energy                 | 17.2           | 41.5               | 0.41                 |
| Materials              | 18.3           | 48.7               | 0.38                 |
| Industrials            | 2.8            | 36.3               | 0.08                 |
| Consumer Staples       | -0.5           | 28.4               | -0.02                |
| Utilities              | -0.9           | 27.7               | -0.03                |
| Financials             | -3.0           | 30.9               | -0.1                 |
| Healthcare             | -5.8           | 42.1               | -0.14                |
| Information Technology | -15.2          | 49.5               | -0.31                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 151.45       |
| BHP  | BHP                    | Materials              | 260.3            | 61.21        |
| WBC  | Westpac                | Financials             | 136.3            | 34.32        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.37        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 76.22        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 245.63       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.5         |
| CSL  | CSL                    | Healthcare             | 67.4             | 175.35       |
