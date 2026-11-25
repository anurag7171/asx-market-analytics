# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Industrials            | 23        | 5.24              | 57.46    | -46.25    |
| Consumer Staples       | 7         | 5.0               | 56.64    | -29.46    |
| Utilities              | 7         | 4.87              | 28.55    | -13.47    |
| Financials             | 36        | 2.08              | 44.25    | -60.34    |
| Energy                 | 11        | -1.54             | 35.44    | -60.82    |
| Materials              | 47        | -4.22             | 53.61    | -70.32    |
| Information Technology | 7         | -5.66             | 67.18    | -52.63    |
| Healthcare             | 16        | -5.97             | 55.03    | -56.58    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | CDA  | Codan                  | Information Technology | 67.2                |
| 2    | REH  | Reece Group            | Industrials            | 57.5                |
| 3    | WOW  | Woolworths Group       | Consumer Staples       | 56.6                |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 56.6                |
| 5    | RHC  | Ramsay Health Care     | Healthcare             | 55.0                |
| 6    | ALK  | Alkane Resources       | Materials              | 53.6                |
| 7    | BSL  | BlueScope              | Materials              | 49.2                |
| 8    | JHX  | James Hardie           | Materials              | 45.9                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.3                 |
| CTD  | 254          | 98.3                  |
| EOS  | 254          | 94.7                  |
| TUA  | 254          | 92.8                  |
| ZIP  | 253          | 88.6                  |
| DRO  | 254          | 85.7                  |
| OBM  | 254          | 80.6                  |
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
| Financials             | 22                  |
| Industrials            | 16                  |
| Real Estate            | 14                  |
| Healthcare             | 9                   |
| Consumer Discretionary | 9                   |
| Communication Services | 8                   |
| Utilities              | 7                   |
| Materials              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.53         | -79.9          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.63         | -78.7          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.63         | -78.5          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.07         | -77.3          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.85         | -76.0          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.63         | -75.2          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.15         | -68.4          |
| GQG  | GQG Partners           | Financials             | 1.75     | 0.57         | -67.2          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name           | max_drawdown_pct |
| ---- | ---------------------- | ---------------- |
| CTD  | Corporate Travel Manag | -87.6            |
| TUA  | Tuas                   | -83.6            |
| LTR  | Liontown Resources     | -79.9            |
| DYL  | Deep Yellow            | -78.5            |
| DRO  | Droneshield            | -78.1            |
| CIA  | Champion Iron          | -75.2            |
| GQG  | GQG Partners           | -70.6            |
| 4DX  | 4DMedical              | -70.1            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.15                  |
| Information Technology | 46.19                  |
| Financials             | 45.54                  |
| Energy                 | 42.26                  |
| Healthcare             | 36.13                  |
| Consumer Staples       | 32.4                   |
| Communication Services | 27.82                  |
| Consumer Discretionary | 27.6                   |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Utilities              | 4.9            | 28.1               | 0.17                 |
| Consumer Staples       | 5.0            | 28.8               | 0.17                 |
| Industrials            | 5.2            | 36.9               | 0.14                 |
| Financials             | 2.1            | 31.0               | 0.07                 |
| Energy                 | -1.5           | 42.2               | -0.04                |
| Materials              | -4.2           | 49.6               | -0.09                |
| Information Technology | -5.7           | 55.3               | -0.1                 |
| Healthcare             | -6.0           | 42.2               | -0.14                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 169.66       |
| BHP  | BHP                    | Materials              | 260.3            | 52.22        |
| WBC  | Westpac                | Financials             | 136.3            | 35.6         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.57        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.06        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 224.95       |
| NAB  | National Australia Ban | Financials             | 69.8             | 36.38        |
| CSL  | CSL                    | Healthcare             | 67.4             | 208.0        |
