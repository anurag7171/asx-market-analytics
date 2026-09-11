# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 37.38             | 131.56   | -27.29    |
| Energy           | 11        | 20.85             | 64.03    | -28.46    |
| Industrials      | 24        | 6.68              | 76.5     | -46.7     |
| Utilities        | 7         | 0.68              | 29.65    | -12.85    |
| Financials       | 36        | -0.88             | 67.68    | -53.59    |
| Consumer Staples | 7         | -5.57             | 41.52    | -32.2     |
| Healthcare       | 16        | -7.91             | 77.78    | -54.03    |
| Real Estate      | 16        | -19.05            | 2.39     | -58.36    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name        | sector_name | one_year_return_pct |
| ---- | ---- | ------------------- | ----------- | ------------------- |
| 1    | PLS  | PLS Group           | Materials   | 131.6               |
| 2    | S32  | South32             | Materials   | 103.1               |
| 3    | SGM  | Sims Metal          | Materials   | 85.3                |
| 4    | ALK  | Alkane Resources    | Materials   | 80.7                |
| 5    | IGO  | IGO                 | Materials   | 80.3                |
| 6    | 4DX  | 4DMedical           | Healthcare  | 77.8                |
| 7    | NWH  | NRW Holdings        | Industrials | 76.5                |
| 8    | GGP  | Greatland Resources | Materials   | 74.9                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.2                 |
| DRO  | 254          | 103.7                 |
| EOS  | 254          | 99.5                  |
| CTD  | 254          | 87.4                  |
| ZIP  | 254          | 79.6                  |
| OBM  | 254          | 77.9                  |
| LTR  | 254          | 77.7                  |
| TUA  | 254          | 75.7                  |

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
| Materials              | 28                  |
| Financials             | 11                  |
| Energy                 | 8                   |
| Industrials            | 5                   |
| Healthcare             | 5                   |
| Utilities              | 3                   |
| Communication Services | 3                   |
| Consumer Discretionary | 2                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 2.46         | -84.7          |
| DRO  | Droneshield            | Industrials            | 6.6      | 1.66         | -74.8          |
| TUA  | Tuas                   | Communication Services | 7.84     | 2.03         | -74.1          |
| WTC  | Wisetech Global        | Information Technology | 97.09    | 32.69        | -66.3          |
| 360  | Life360                | Information Technology | 55.44    | 19.73        | -64.4          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 1.07         | -59.5          |
| PXA  | Pexa Group             | Real Estate            | 16.81    | 6.8          | -59.5          |
| XRO  | Xero                   | Information Technology | 163.97   | 67.05        | -59.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| DRO  | Droneshield            | -74.8            |
| TUA  | Tuas                   | -74.5            |
| WTC  | Wisetech Global        | -70.5            |
| ZIP  | Zip                    | -70.0            |
| COH  | Cochlear               | -69.7            |
| 360  | Life360                | -67.7            |
| PME  | Pro Medicus            | -66.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 50.36                  |
| Information Technology | 44.88                  |
| Financials             | 44.13                  |
| Energy                 | 40.88                  |
| Healthcare             | 36.47                  |
| Consumer Staples       | 32.38                  |
| Consumer Discretionary | 27.63                  |
| Communication Services | 27.4                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 37.4           | 48.5               | 0.77                 |
| Energy                 | 20.9           | 41.9               | 0.5                  |
| Industrials            | 6.7            | 35.1               | 0.19                 |
| Utilities              | 0.7            | 27.5               | 0.02                 |
| Financials             | -0.9           | 30.6               | -0.03                |
| Healthcare             | -7.9           | 42.6               | -0.19                |
| Consumer Staples       | -5.6           | 28.2               | -0.2                 |
| Information Technology | -25.6          | 48.2               | -0.53                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 154.19       |
| BHP  | BHP                    | Materials              | 260.3            | 60.87        |
| WBC  | Westpac                | Financials             | 136.3            | 34.22        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.27        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 72.82        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 245.25       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.72        |
| CSL  | CSL                    | Healthcare             | 67.4             | 167.1        |
