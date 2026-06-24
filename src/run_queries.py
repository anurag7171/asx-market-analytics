"""
Execute every query in sql/queries.sql against asx.db, print a tidy preview of
each result, and write the previews to results/query_results.md for the README.

Run:  python3 src/run_queries.py
"""

import os
import re
import sqlite3

HERE = os.path.dirname(__file__)
DB = os.path.join(HERE, "..", "asx.db")
SQL = os.path.join(HERE, "..", "sql", "queries.sql")
OUT = os.path.join(HERE, "..", "results", "query_results.md")


def split_queries(text: str):
    """Return (title, sql) per query. Strip comments first (they may contain ';')."""
    titles = re.findall(r"--\s*(Q\d+\..*)", text)
    no_comments = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("--"))
    stmts = [s.strip() + ";" for s in no_comments.split(";") if "SELECT" in s.upper()]
    return list(zip(titles, stmts))


def fmt_table(cols, rows, maxw=22):
    rows = rows[:8]
    widths = [min(maxw, max(len(str(c)), *([len(str(r[i])) for r in rows] or [0]))) for i, c in enumerate(cols)]
    def line(vals):
        return "| " + " | ".join(str(v)[:maxw].ljust(w) for v, w in zip(vals, widths)) + " |"
    sep = "| " + " | ".join("-" * w for w in widths) + " |"
    return "\n".join([line(cols), sep] + [line(r) for r in rows])


def main():
    con = sqlite3.connect(DB)
    con.execute("PRAGMA foreign_keys = ON;")
    queries = split_queries(open(SQL, encoding="utf-8").read())
    md = ["# ASX 200 — SQL query results\n"]
    for title, q in queries:
        cur = con.execute(q)
        cols = [d[0] for d in cur.description]
        rows = cur.fetchall()
        print(f"\n### {title}  ({len(rows)} rows)")
        table = fmt_table(cols, rows)
        print(table)
        md += [f"### {title}", "", table, ""]
    con.close()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write("\n".join(md))
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
