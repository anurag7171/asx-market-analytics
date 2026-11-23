# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Industrials            | 23        | 3.82              | 55.56    | -38.68    |
| Consumer Staples       | 7         | 3.8               | 52.25    | -28.55    |
| Utilities              | 7         | 2.85              | 26.51    | -12.53    |
| Energy                 | 11        | -0.34             | 35.6     | -60.32    |
| Financials             | 36        | -0.55             | 37.45    | -64.27    |
| Materials              | 47        | -1.41             | 65.91    | -67.95    |
| Information Technology | 7         | -6.04             | 67.84    | -47.31    |
| Healthcare             | 16        | -7.08             | 72.35    | -56.58    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care     | Healthcare             | 72.3                |
| 2    | CDA  | Codan                  | Information Technology | 67.8                |
| 3    | ALK  | Alkane Resources       | Materials              | 65.9                |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 55.6                |
| 5    | WOW  | Woolworths Group       | Consumer Staples       | 52.2                |
| 6    | REH  | Reece Group            | Industrials            | 51.7                |
| 7    | BSL  | BlueScope              | Materials              | 51.6                |
| 8    | JHX  | James Hardie           | Materials              | 41.6                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.0                 |
| CTD  | 254          | 97.4                  |
| EOS  | 254          | 94.7                  |
| ZIP  | 253          | 88.3                  |
| DRO  | 254          | 86.9                  |
| TUA  | 254          | 86.5                  |
| OBM  | 254          | 80.9                  |
| NXT  | 254          | 79.8                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| CTD  | Corporate Travel Manag | 2026-09-03 | -85.6          |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| NXT  | NextDC                 | 2026-11-04 | 50.8           |
| NXT  | NextDC                 | 2026-10-20 | -41.7          |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Real Estate            | 14                  |
| Financials             | 14                  |
| Industrials            | 13                  |
| Healthcare             | 9                   |
| Consumer Discretionary | 6                   |
| Utilities              | 5                   |
| Information Technology | 5                   |
| Consumer Staples       | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.36         | -82.2          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.25         | -79.8          |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.56         | -78.6          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.63         | -78.5          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.07         | -77.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.69         | -74.3          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.52         | -70.6          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.03         | -70.1          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -79.0            |
| DYL  | Deep Yellow            | -78.5            |
| DRO  | Droneshield            | -78.1            |
| CIA  | Champion Iron          | -74.3            |
| GQG  | GQG Partners           | -70.6            |
| 4DX  | 4DMedical              | -70.1            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.67                  |
| Information Technology | 46.3                   |
| Financials             | 45.7                   |
| Energy                 | 42.3                   |
| Healthcare             | 36.14                  |
| Consumer Staples       | 32.39                  |
| Communication Services | 27.91                  |
| Consumer Discretionary | 27.72                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 3.8            | 28.7               | 0.13                 |
| Utilities              | 2.8            | 28.1               | 0.1                  |
| Industrials            | 3.8            | 36.8               | 0.1                  |
| Energy                 | -0.3           | 42.2               | -0.01                |
| Financials             | -0.6           | 30.9               | -0.02                |
| Materials              | -1.4           | 49.5               | -0.03                |
| Information Technology | -6.0           | 55.2               | -0.11                |
| Healthcare             | -7.1           | 42.3               | -0.17                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 166.15       |
| BHP  | BHP                    | Materials              | 260.3            | 52.52        |
| WBC  | Westpac                | Financials             | 136.3            | 35.26        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.94        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 76.06        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 224.93       |
| NAB  | National Australia Ban | Financials             | 69.8             | 36.03        |
| CSL  | CSL                    | Healthcare             | 67.4             | 199.3        |
