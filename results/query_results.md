# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Healthcare       | 16        | 90.55             | 1716.67  | -56.63    |
| Materials        | 47        | 55.18             | 254.48   | -26.53    |
| Industrials      | 24        | 30.0              | 279.69   | -31.29    |
| Energy           | 11        | 11.17             | 39.26    | -32.93    |
| Financials       | 36        | 5.42              | 80.5     | -32.99    |
| Utilities        | 7         | -0.66             | 24.73    | -13.65    |
| Consumer Staples | 7         | -4.25             | 28.78    | -43.66    |
| Real Estate      | 17        | -5.57             | 19.9     | -41.52    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name           | sector_name            | one_year_return_pct |
| ---- | ---- | ---------------------- | ---------------------- | ------------------- |
| 1    | 4DX  | 4DMedical              | Healthcare             | 1716.7              |
| 2    | EOS  | Electro Optic Systems  | Industrials            | 279.7               |
| 3    | PLS  | PLS Group              | Materials              | 254.5               |
| 4    | MIN  | Mineral Resources      | Materials              | 163.9               |
| 5    | NWH  | NRW Holdings           | Industrials            | 141.9               |
| 6    | LTR  | Liontown Resources     | Materials              | 131.5               |
| 7    | CDA  | Codan                  | Information Technology | 127.2               |
| 8    | LYC  | Lynas Rare Earths      | Materials              | 121.9               |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 142.8                 |
| EOS  | 253          | 108.8                 |
| DRO  | 253          | 107.1                 |
| TUA  | 253          | 81.7                  |
| LTR  | 253          | 81.5                  |
| OBM  | 253          | 79.6                  |
| ZIP  | 253          | 76.8                  |
| CYL  | 253          | 72.4                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| EOS  | Electro Optic Systems  | 2025-08-05 | 43.4           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |
| MSB  | Mesoblast              | 2025-07-18 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Financials             | 28                  |
| Industrials            | 17                  |
| Materials              | 16                  |
| Real Estate            | 14                  |
| Healthcare             | 14                  |
| Consumer Discretionary | 10                  |
| Consumer Staples       | 6                   |
| Information Technology | 4                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.28         | -72.6          |
| WTC  | Wisetech Global | Information Technology | 120.11   | 35.37        | -70.6          |
| DRO  | Droneshield     | Industrials            | 6.6      | 2.52         | -61.8          |
| XRO  | Xero            | Information Technology | 181.0    | 73.56        | -59.4          |
| COH  | Cochlear        | Healthcare             | 313.15   | 127.86       | -59.2          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 18.15        | -54.4          |
| SEK  | Seek            | Communication Services | 28.65    | 13.17        | -54.0          |
| ASB  | Austal          | Industrials            | 8.76     | 4.04         | -53.9          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name          | max_drawdown_pct |
| ---- | --------------------- | ---------------- |
| WTC  | Wisetech Global       | -76.1            |
| TUA  | Tuas                  | -76.0            |
| DRO  | Droneshield           | -74.0            |
| COH  | Cochlear              | -71.3            |
| ZIP  | Zip                   | -70.0            |
| 360  | Life360               | -67.7            |
| PME  | Pro Medicus           | -67.2            |
| TLX  | Telix Pharmaceuticals | -66.0            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 48.53                  |
| Information Technology | 45.16                  |
| Financials             | 44.05                  |
| Energy                 | 39.5                   |
| Healthcare             | 36.98                  |
| Consumer Staples       | 33.13                  |
| Consumer Discretionary | 27.6                   |
| Communication Services | 26.34                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Healthcare             | 90.6           | 44.6               | 2.03                 |
| Materials              | 55.2           | 49.3               | 1.12                 |
| Industrials            | 30.0           | 36.0               | 0.83                 |
| Energy                 | 11.2           | 41.2               | 0.27                 |
| Financials             | 5.4            | 30.0               | 0.18                 |
| Utilities              | -0.7           | 27.4               | -0.02                |
| Information Technology | -6.3           | 46.6               | -0.14                |
| Consumer Staples       | -4.3           | 28.2               | -0.15                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 164.66       |
| BHP  | BHP                    | Materials              | 260.3            | 60.02        |
| WBC  | Westpac                | Financials             | 136.3            | 35.29        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 35.0         |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 89.04        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 250.73       |
| NAB  | National Australia Ban | Financials             | 69.8             | 38.65        |
| CSL  | CSL                    | Healthcare             | 67.4             | 124.23       |
