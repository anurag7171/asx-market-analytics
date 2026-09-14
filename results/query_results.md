# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 37.1              | 147.37   | -28.81    |
| Energy           | 11        | 20.14             | 64.07    | -32.28    |
| Industrials      | 24        | 5.06              | 74.04    | -50.77    |
| Utilities        | 7         | 0.52              | 29.79    | -13.26    |
| Financials       | 36        | -1.79             | 66.2     | -55.6     |
| Consumer Staples | 7         | -5.44             | 41.58    | -32.32    |
| Healthcare       | 16        | -6.94             | 93.26    | -54.03    |
| Real Estate      | 16        | -19.36            | 1.32     | -57.07    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | PDI  | Predictive Discovery | Materials   | 147.4               |
| 2    | PLS  | PLS Group            | Materials   | 106.0               |
| 3    | S32  | South32              | Materials   | 94.1                |
| 4    | 4DX  | 4DMedical            | Healthcare  | 93.3                |
| 5    | ALK  | Alkane Resources     | Materials   | 84.5                |
| 6    | SGM  | Sims Metal           | Materials   | 78.8                |
| 7    | GGP  | Greatland Resources  | Materials   | 76.1                |
| 8    | NWH  | NRW Holdings         | Industrials | 74.0                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 106.2                 |
| DRO  | 253          | 103.9                 |
| EOS  | 253          | 99.3                  |
| CTD  | 253          | 87.6                  |
| ZIP  | 253          | 79.7                  |
| LTR  | 253          | 77.5                  |
| OBM  | 253          | 77.3                  |
| TUA  | 253          | 76.0                  |

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
| Energy                 | 7                   |
| Industrials            | 6                   |
| Healthcare             | 6                   |
| Utilities              | 3                   |
| Communication Services | 3                   |
| Consumer Discretionary | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.38         | -85.2          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.6          | -75.7          |
| TUA  | Tuas                   | Communication Services | 7.69     | 2.1          | -72.7          |
| WTC  | Wisetech Global        | Information Technology | 97.09    | 32.44        | -66.6          |
| 360  | Life360                | Information Technology | 55.44    | 19.54        | -64.8          |
| GDG  | Generation Development | Financials             | 7.56     | 3.02         | -60.0          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.07         | -59.5          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 6.86         | -59.2          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| DRO  | Droneshield            | -75.7            |
| TUA  | Tuas                   | -74.0            |
| WTC  | Wisetech Global        | -70.5            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.7            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.69                  |
| Information Technology | 44.89                  |
| Financials             | 44.14                  |
| Energy                 | 40.98                  |
| Healthcare             | 36.39                  |
| Consumer Staples       | 32.38                  |
| Consumer Discretionary | 27.65                  |
| Communication Services | 27.35                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 37.1           | 48.8               | 0.76                 |
| Energy                 | 20.1           | 42.0               | 0.48                 |
| Industrials            | 5.1            | 35.1               | 0.14                 |
| Utilities              | 0.5            | 27.4               | 0.02                 |
| Financials             | -1.8           | 30.5               | -0.06                |
| Healthcare             | -6.9           | 42.6               | -0.16                |
| Consumer Staples       | -5.4           | 28.3               | -0.19                |
| Information Technology | -26.0          | 48.3               | -0.54                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 154.97       |
| BHP  | BHP                    | Materials              | 260.3            | 60.59        |
| WBC  | Westpac                | Financials             | 136.3            | 34.53        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.54        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 72.57        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 245.04       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.72        |
| CSL  | CSL                    | Healthcare             | 67.4             | 171.57       |
