# ASX 200 — SQL query results

### Q1. Sector performance leaderboard (1-year total return)

| sector_name      | companies | avg_1y_return_pct | best_pct | worst_pct |
| ---------------- | --------- | ----------------- | -------- | --------- |
| Materials        | 47        | 46.33             | 132.52   | -35.57    |
| Energy           | 11        | 20.33             | 59.85    | -26.12    |
| Healthcare       | 16        | 15.57             | 545.22   | -54.83    |
| Industrials      | 24        | 12.77             | 115.21   | -49.09    |
| Utilities        | 7         | 4.05              | 23.33    | -5.59     |
| Financials       | 36        | 3.01              | 73.19    | -39.73    |
| Consumer Staples | 7         | -2.4              | 27.56    | -25.47    |
| Real Estate      | 17        | -10.62            | 11.1     | -51.63    |

### Q2. Top 10 performers over the last year (RANK across the index)

| rank | code | company_name         | sector_name | one_year_return_pct |
| ---- | ---- | -------------------- | ----------- | ------------------- |
| 1    | 4DX  | 4DMedical            | Healthcare  | 545.2               |
| 2    | GGP  | Greatland Resources  | Materials   | 132.5               |
| 3    | VAU  | Vault Minerals       | Materials   | 125.0               |
| 4    | PLS  | PLS Group            | Materials   | 124.2               |
| 5    | NWH  | NRW Holdings         | Industrials | 115.2               |
| 6    | OBM  | Ora Banda Mining     | Materials   | 93.7                |
| 7    | PDI  | Predictive Discovery | Materials   | 93.2                |
| 8    | WGX  | Westgold Resources   | Materials   | 87.2                |

### Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)

| code | trading_days | annual_volatility_pct |
| ---- | ------------ | --------------------- |
| 4DX  | 253          | 138.7                 |
| DRO  | 253          | 104.2                 |
| EOS  | 253          | 99.8                  |
| OBM  | 253          | 78.8                  |
| LTR  | 253          | 78.7                  |
| ZIP  | 253          | 78.4                  |
| TUA  | 253          | 76.1                  |
| DYL  | 253          | 72.4                  |

### Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)

| code | company_name           | trade_date | day_change_pct |
| ---- | ---------------------- | ---------- | -------------- |
| TUA  | Tuas                   | 2026-05-18 | -62.8          |
| 4DX  | 4DMedical              | 2025-09-03 | 50.0           |
| 4DX  | 4DMedical              | 2025-09-08 | 49.5           |
| COH  | Cochlear               | 2026-04-22 | -40.7          |
| GDG  | Generation Development | 2026-07-23 | 37.1           |
| SDF  | Steadfast Group        | 2026-06-10 | 36.2           |
| 4DX  | 4DMedical              | 2025-09-01 | 36.0           |
| 4DX  | 4DMedical              | 2026-03-24 | 34.6           |

### Q5. Momentum — count of stocks above their 50-day moving average, by sector

| sector_name            | stocks_above_50d_ma |
| ---------------------- | ------------------- |
| Materials              | 35                  |
| Financials             | 25                  |
| Industrials            | 12                  |
| Healthcare             | 11                  |
| Real Estate            | 9                   |
| Energy                 | 9                   |
| Consumer Discretionary | 8                   |
| Information Technology | 6                   |

### Q6. 52-week high proximity — how far each stock sits below its yearly peak

| code | company_name    | sector_name            | high_52w | latest_price | pct_below_high |
| ---- | --------------- | ---------------------- | -------- | ------------ | -------------- |
| TUA  | Tuas            | Communication Services | 8.32     | 2.21         | -73.4          |
| DRO  | Droneshield     | Industrials            | 6.6      | 1.96         | -70.3          |
| WTC  | Wisetech Global | Information Technology | 115.58   | 42.27        | -63.4          |
| COH  | Cochlear        | Healthcare             | 297.81   | 131.25       | -55.9          |
| 360  | Life360         | Information Technology | 55.44    | 24.49        | -55.8          |
| PXA  | Pexa Group      | Real Estate            | 16.92    | 7.85         | -53.6          |
| XRO  | Xero            | Information Technology | 171.5    | 82.11        | -52.1          |
| ARB  | ARB Corporation | Consumer Discretionary | 39.79    | 19.09        | -52.0          |

### Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough

| code | company_name    | max_drawdown_pct |
| ---- | --------------- | ---------------- |
| TUA  | Tuas            | -76.0            |
| WTC  | Wisetech Global | -75.1            |
| DRO  | Droneshield     | -74.3            |
| ZIP  | Zip             | -70.0            |
| COH  | Cochlear        | -69.8            |
| 360  | Life360         | -67.7            |
| PME  | Pro Medicus     | -66.2            |
| CSL  | CSL             | -65.2            |

### Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg

| sector_name            | avg_daily_turnover_m_a |
| ---------------------- | ---------------------- |
| Materials              | 49.04                  |
| Information Technology | 45.67                  |
| Financials             | 44.12                  |
| Energy                 | 40.46                  |
| Healthcare             | 36.53                  |
| Consumer Staples       | 33.1                   |
| Consumer Discretionary | 27.57                  |
| Communication Services | 26.85                  |

### Q9. Risk-adjusted return by sector — return per unit of volatility

| sector_name            | avg_return_pct | avg_volatility_pct | return_per_unit_risk |
| ---------------------- | -------------- | ------------------ | -------------------- |
| Materials              | 46.3           | 49.3               | 0.94                 |
| Energy                 | 20.3           | 41.7               | 0.49                 |
| Industrials            | 12.8           | 36.2               | 0.35                 |
| Healthcare             | 15.6           | 44.2               | 0.35                 |
| Utilities              | 4.1            | 27.8               | 0.15                 |
| Financials             | 3.0            | 30.2               | 0.1                  |
| Consumer Staples       | -2.4           | 28.7               | -0.08                |
| Information Technology | -11.1          | 48.5               | -0.23                |

### Q10. Market-cap leaders and their latest traded price

| code | company_name           | sector_name            | market_cap_b_aud | latest_price |
| ---- | ---------------------- | ---------------------- | ---------------- | ------------ |
| CBA  | Commonwealth Bank      | Financials             | 289.2            | 165.0        |
| BHP  | BHP                    | Materials              | 260.3            | 62.2         |
| WBC  | Westpac                | Financials             | 136.3            | 35.07        |
| ANZ  | Australia & New Zealan | Financials             | 110.4            | 37.88        |
| WES  | Wesfarmers             | Consumer Discretionary | 83.2             | 84.84        |
| MQG  | Macquarie Group        | Financials             | 78.4             | 260.6        |
| NAB  | National Australia Ban | Financials             | 69.8             | 39.46        |
| CSL  | CSL                    | Healthcare             | 67.4             | 134.6        |
