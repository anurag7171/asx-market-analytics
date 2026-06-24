"""
Pull ~1 year of daily prices for every scraped ASX 200 company from Yahoo
Finance's public chart endpoint.

Input:  data/companies.csv
Output: data/prices.csv  (code, date, open, high, low, close, volume)
"""

import csv
import os
import time
from datetime import datetime, timezone

import requests

HERE = os.path.dirname(__file__)
COMPANIES = os.path.join(HERE, "..", "data", "companies.csv")
OUT = os.path.join(HERE, "..", "data", "prices.csv")
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{sym}.AX?range=1y&interval=1d"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}


def fetch_one(code: str, session: requests.Session) -> list[dict]:
    r = session.get(URL.format(sym=code), headers=HEADERS, timeout=30)
    if r.status_code != 200:
        return []
    res = r.json().get("chart", {}).get("result")
    if not res:
        return []
    res = res[0]
    ts = res.get("timestamp") or []
    q = (res.get("indicators", {}).get("quote") or [{}])[0]
    adj = (res.get("indicators", {}).get("adjclose") or [{}])[0].get("adjclose", [None] * len(ts))
    out = []

    def rnd(v):
        return round(v, 4) if isinstance(v, (int, float)) else None

    for i, t in enumerate(ts):
        close = q.get("close", [None] * len(ts))[i]
        if close is None:
            continue
        d = datetime.fromtimestamp(t, tz=timezone.utc).strftime("%Y-%m-%d")
        vol = q["volume"][i]
        out.append({
            "code": code, "date": d,
            "open": rnd(q["open"][i]), "high": rnd(q["high"][i]),
            "low": rnd(q["low"][i]), "close": rnd(close),
            "adj_close": rnd(adj[i]) if adj[i] is not None else rnd(close),
            "volume": int(vol) if vol is not None else None,
        })
    return out


def main(limit: int | None = None, delay: float = 0.25):
    with open(COMPANIES, encoding="utf-8") as f:
        codes = [r["code"] for r in csv.DictReader(f)]
    if limit:
        codes = codes[:limit]

    session = requests.Session()
    all_rows, ok, fail = [], 0, []
    for i, code in enumerate(codes, 1):
        try:
            rows = fetch_one(code, session)
            if rows:
                all_rows.extend(rows); ok += 1
            else:
                fail.append(code)
        except Exception:
            fail.append(code)
        if i % 25 == 0:
            print(f"  {i}/{len(codes)} done ({ok} ok)")
        time.sleep(delay)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code", "date", "open", "high", "low", "close", "adj_close", "volume"])
        w.writeheader()
        w.writerows(all_rows)
    print(f"\nPrices: {len(all_rows):,} rows for {ok}/{len(codes)} companies -> {OUT}")
    if fail:
        print(f"No data for {len(fail)}: {', '.join(fail[:15])}{' ...' if len(fail) > 15 else ''}")


if __name__ == "__main__":
    main()
