-- ============================================================================
-- ASX 200 Market Analytics — analytical SQL
-- Demonstrates: multi-table JOINs, CTEs, and window functions
--               (LAG, RANK, FIRST_VALUE, moving averages, running max).
-- Returns/risk use adj_close (split and dividend adjusted). Turnover uses raw close.
-- Engine: SQLite 3.25+
-- ============================================================================

-- Q1. Sector performance leaderboard (1-year total return)
WITH bounds AS (
    SELECT code,
           FIRST_VALUE(adj_close) OVER w AS first_px,
           LAST_VALUE(adj_close)  OVER w AS last_px
    FROM daily_prices
    WINDOW w AS (PARTITION BY code ORDER BY trade_date
                 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
),
company_return AS (
    SELECT DISTINCT code, 100.0 * (last_px - first_px) / first_px AS pct_return
    FROM bounds
)
SELECT s.sector_name,
       COUNT(*)                       AS companies,
       ROUND(AVG(cr.pct_return), 2)   AS avg_1y_return_pct,
       ROUND(MAX(cr.pct_return), 2)   AS best_pct,
       ROUND(MIN(cr.pct_return), 2)   AS worst_pct
FROM company_return cr
JOIN companies c ON c.code = cr.code
JOIN sectors   s ON s.sector_id = c.sector_id
GROUP BY s.sector_name
ORDER BY avg_1y_return_pct DESC;

-- Q2. Top 10 performers over the last year (RANK across the index)
WITH bounds AS (
    SELECT code,
           FIRST_VALUE(adj_close) OVER w AS first_px,
           LAST_VALUE(adj_close)  OVER w AS last_px
    FROM daily_prices
    WINDOW w AS (PARTITION BY code ORDER BY trade_date
                 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
),
ret AS (
    SELECT DISTINCT code, 100.0 * (last_px - first_px) / first_px AS pct_return
    FROM bounds
)
SELECT RANK() OVER (ORDER BY r.pct_return DESC) AS rank,
       r.code, c.company_name, s.sector_name,
       ROUND(r.pct_return, 1) AS one_year_return_pct
FROM ret r
JOIN companies c ON c.code = r.code
JOIN sectors   s ON s.sector_id = c.sector_id
ORDER BY r.pct_return DESC
LIMIT 10;

-- Q3. Most volatile stocks — annualised volatility from daily returns (LAG + CTE)
WITH daily AS (
    SELECT code, adj_close,
           LAG(adj_close) OVER (PARTITION BY code ORDER BY trade_date) AS prev_px
    FROM daily_prices
),
returns AS (
    SELECT code, (adj_close - prev_px) / prev_px AS r
    FROM daily WHERE prev_px IS NOT NULL
)
SELECT code,
       COUNT(*) AS trading_days,
       ROUND(100.0 * SQRT(AVG(r*r) - AVG(r)*AVG(r)) * SQRT(252), 1) AS annual_volatility_pct
FROM returns
GROUP BY code
ORDER BY annual_volatility_pct DESC
LIMIT 10;

-- Q4. Biggest single-day moves using LAG (adjusted, so splits don't show up)
WITH chg AS (
    SELECT code, trade_date, adj_close,
           LAG(adj_close) OVER (PARTITION BY code ORDER BY trade_date) AS prev_px
    FROM daily_prices
)
SELECT c.code, co.company_name, c.trade_date,
       ROUND(100.0 * (c.adj_close - c.prev_px) / c.prev_px, 1) AS day_change_pct
FROM chg c
JOIN companies co ON co.code = c.code
WHERE c.prev_px IS NOT NULL
ORDER BY ABS((c.adj_close - c.prev_px) / c.prev_px) DESC
LIMIT 10;

-- Q5. Momentum — count of stocks above their 50-day moving average, by sector
WITH ma AS (
    SELECT code, adj_close,
           AVG(adj_close) OVER (PARTITION BY code ORDER BY trade_date
                                ROWS BETWEEN 49 PRECEDING AND CURRENT ROW) AS ma50,
           ROW_NUMBER() OVER (PARTITION BY code ORDER BY trade_date DESC) AS rn
    FROM daily_prices
)
SELECT s.sector_name, COUNT(*) AS stocks_above_50d_ma
FROM ma
JOIN companies c ON c.code = ma.code
JOIN sectors   s ON s.sector_id = c.sector_id
WHERE ma.rn = 1 AND ma.adj_close > ma.ma50
GROUP BY s.sector_name
ORDER BY stocks_above_50d_ma DESC;

-- Q6. 52-week high proximity — how far each stock sits below its yearly peak
WITH stats AS (
    SELECT code,
           MAX(adj_close) AS high_52w,
           (SELECT adj_close FROM daily_prices p2
             WHERE p2.code = p.code ORDER BY trade_date DESC LIMIT 1) AS latest_px
    FROM daily_prices p
    GROUP BY code
)
SELECT st.code, c.company_name, s.sector_name,
       ROUND(st.high_52w, 2)  AS high_52w,
       ROUND(st.latest_px, 2) AS latest_price,
       ROUND(100.0 * (st.latest_px - st.high_52w) / st.high_52w, 1) AS pct_below_high
FROM stats st
JOIN companies c ON c.code = st.code
JOIN sectors   s ON s.sector_id = c.sector_id
ORDER BY pct_below_high ASC
LIMIT 10;

-- Q7. Maximum drawdown per stock — running peak (window MAX) then deepest trough
WITH running AS (
    SELECT code, adj_close,
           MAX(adj_close) OVER (PARTITION BY code ORDER BY trade_date
                                ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS peak
    FROM daily_prices
)
SELECT r.code, c.company_name,
       ROUND(MIN(100.0 * (r.adj_close - r.peak) / r.peak), 1) AS max_drawdown_pct
FROM running r
JOIN companies c ON c.code = r.code
GROUP BY r.code
ORDER BY max_drawdown_pct ASC
LIMIT 10;

-- Q8. Average daily traded value by sector (liquidity, in actual A$) — JOIN + agg
SELECT s.sector_name,
       ROUND(AVG(p.close * p.volume) / 1e6, 2) AS avg_daily_turnover_m_aud
FROM daily_prices p
JOIN companies c ON c.code = p.code
JOIN sectors   s ON s.sector_id = c.sector_id
WHERE p.volume IS NOT NULL
GROUP BY s.sector_name
ORDER BY avg_daily_turnover_m_aud DESC;

-- Q9. Risk-adjusted return by sector — return per unit of volatility
WITH daily AS (
    SELECT code, trade_date, adj_close,
           LAG(adj_close) OVER (PARTITION BY code ORDER BY trade_date) AS prev
    FROM daily_prices
),
seqd AS (
    SELECT code, adj_close,
           ROW_NUMBER() OVER (PARTITION BY code ORDER BY trade_date) AS seq,
           COUNT(*)     OVER (PARTITION BY code) AS mx
    FROM daily_prices
),
per_co AS (
    SELECT seqd.code,
           (MAX(CASE WHEN seq = mx THEN adj_close END)
              - MAX(CASE WHEN seq = 1 THEN adj_close END))
              / MAX(CASE WHEN seq = 1 THEN adj_close END)      AS ret,
           (SELECT SQRT(AVG(r2*r2) - AVG(r2)*AVG(r2)) * SQRT(252)
              FROM (SELECT (adj_close - prev)/prev AS r2 FROM daily d
                     WHERE d.code = seqd.code AND prev IS NOT NULL)) AS vol
    FROM seqd
    GROUP BY seqd.code
)
SELECT s.sector_name,
       ROUND(AVG(pc.ret) * 100, 1) AS avg_return_pct,
       ROUND(AVG(pc.vol) * 100, 1) AS avg_volatility_pct,
       ROUND(AVG(pc.ret) / NULLIF(AVG(pc.vol), 0), 2) AS return_per_unit_risk
FROM per_co pc
JOIN companies c ON c.code = pc.code
JOIN sectors   s ON s.sector_id = c.sector_id
GROUP BY s.sector_name
ORDER BY return_per_unit_risk DESC;

-- Q10. Market-cap leaders and their latest traded price
SELECT c.code, c.company_name, s.sector_name,
       ROUND(c.market_cap / 1e9, 1) AS market_cap_b_aud,
       (SELECT ROUND(close, 2) FROM daily_prices p
         WHERE p.code = c.code ORDER BY trade_date DESC LIMIT 1) AS latest_price
FROM companies c
JOIN sectors s ON s.sector_id = c.sector_id
WHERE c.market_cap IS NOT NULL
ORDER BY c.market_cap DESC
LIMIT 10;
