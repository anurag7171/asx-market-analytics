# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name            | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------------- | --------- | ----------------- | -------- | --------- |
| Industrials            | 23        | 6.13              | 57.11    | -38.11    |
| Consumer Staples       | 7         | 5.3               | 54.58    | -29.12    |
| Utilities              | 7         | 3.67              | 26.96    | -11.78    |
| Financials             | 36        | 1.27              | 40.78    | -59.76    |
| Materials              | 47        | 0.54              | 69.15    | -67.95    |
| Energy                 | 11        | -0.21             | 34.96    | -59.05    |
| Information Technology | 7         | -3.15             | 75.66    | -47.39    |
| Healthcare             | 16        | -4.65             | 75.89    | -56.58    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | RHC  | Ramsay Health Care     | Healthcare             | 75.9                |
| 2    | CDA  | Codan                  | Information Technology | 75.7                |
| 3    | ALK  | Alkane Resources       | Materials              | 69.2                |
| 4    | EOS  | Electro Optic Systems  | Industrials            | 57.1                |
| 5    | REH  | Reece Group            | Industrials            | 56.4                |
| 6    | BSL  | BlueScope              | Materials              | 55.5                |
| 7    | WOW  | Woolworths Group       | Consumer Staples       | 54.6                |
| 8    | JHX  | James Hardie           | Materials              | 46.4                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 254          | 106.3                 |
| CTD  | 254          | 98.2                  |
| EOS  | 254          | 94.7                  |
| TUA  | 254          | 92.4                  |
| ZIP  | 253          | 88.3                  |
| DRO  | 254          | 86.9                  |
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
| Financials             | 23                  |
| Industrials            | 15                  |
| Real Estate            | 14                  |
| Consumer Discretionary | 11                  |
| Healthcare             | 10                  |
| Communication Services | 7                   |
| Utilities              | 6                   |
| Materials              | 5                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name           | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | ---------------------- | ---------------------- | -------- | ------------ | -------------- |
| LTR  | Liontown Resources     | Materials              | 2.64     | 0.58         | -78.0          |
| DYL  | Deep Yellow            | Energy                 | 2.91     | 0.65         | -77.8          |
| CTD  | Corporate Travel Manag | Consumer Discretionary | 16.07    | 3.64         | -77.3          |
| DRO  | Droneshield            | Industrials            | 4.74     | 1.08         | -77.2          |
| TUA  | Tuas                   | Communication Services | 7.64     | 1.8          | -76.4          |
| CIA  | Champion Iron          | Materials              | 6.59     | 1.69         | -74.3          |
| LLC  | Lendlease              | Real Estate            | 5.03     | 1.61         | -68.0          |
| 4DX  | 4DMedical              | Healthcare             | 6.8      | 2.2          | -67.6          |

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
| Materials              | 49.66                  |
| Information Technology | 46.33                  |
| Financials             | 45.72                  |
| Energy                 | 42.31                  |
| Healthcare             | 36.2                   |
| Consumer Staples       | 32.45                  |
| Communication Services | 27.91                  |
| Consumer Discretionary | 27.75                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Consumer Staples       | 5.3            | 28.8               | 0.18                 |
| Industrials            | 6.1            | 36.9               | 0.17                 |
| Utilities              | 3.7            | 28.1               | 0.13                 |
| Financials             | 1.3            | 31.0               | 0.04                 |
| Materials              | 0.5            | 49.6               | 0.01                 |
| Energy                 | -0.2           | 42.2               | -0.0                 |
| Information Technology | -3.1           | 55.3               | -0.06                |
| Healthcare             | -4.6           | 42.4               | -0.11                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 169.18       |
| BHP  | BHP                    | Materials              | 260.3            | 53.23        |
| WBC  | Westpac                | Financials             | 136.3            | 35.9         |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 38.67        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 78.13        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 227.64       |
| NAB  | National Australia Ban | Financials             | 69.8             | 36.64        |
| CSL  | CSL                    | Healthcare             | 67.4             | 204.43       |
