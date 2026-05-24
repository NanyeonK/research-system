#!/usr/bin/env python3
"""Small OpenAlex scanner for research-system v2 literature layer.

This script intentionally uses only Python standard library modules. It writes
structured metadata for gate packets and literature maps. It does not verify
that a paper supports a manuscript claim.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPENALEX = "https://api.openalex.org/works"


def request_json(url: str, params: dict[str, str]) -> dict[str, Any]:
    query = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{query}", headers={"User-Agent": "research-system-v2-literature-layer"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def simplify_work(work: dict[str, Any]) -> dict[str, Any]:
    authors = []
    for item in work.get("authorships", [])[:8]:
        author = item.get("author") or {}
        name = author.get("display_name")
        if name:
            authors.append(name)
    primary = work.get("primary_location") or {}
    source = (primary.get("source") or {}).get("display_name")
    return {
        "openalex_id": work.get("id"),
        "doi": work.get("doi"),
        "title": work.get("title"),
        "publication_year": work.get("publication_year"),
        "authors": authors,
        "source": source,
        "type": work.get("type"),
        "cited_by_count": work.get("cited_by_count"),
        "landing_page_url": primary.get("landing_page_url"),
        "pdf_url": primary.get("pdf_url"),
        "open_access": work.get("open_access"),
        "abstract_inverted_index_present": bool(work.get("abstract_inverted_index")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run an OpenAlex literature scan and save structured results.")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--email", default="", help="Optional email for OpenAlex polite pool")
    parser.add_argument("--from-year", default="", help="Optional lower publication year, for example 2020")
    parser.add_argument("--to-year", default="", help="Optional upper publication year, for example 2026")
    parser.add_argument("--limit", type=int, default=25, help="Maximum results, capped at 200")
    parser.add_argument("--sort", default="relevance_score:desc", help="OpenAlex sort string")
    args = parser.parse_args()

    limit = max(1, min(args.limit, 200))
    filters = []
    if args.from_year and args.to_year:
        filters.append(f"publication_year:{args.from_year}-{args.to_year}")
    elif args.from_year:
        filters.append(f"publication_year:>{int(args.from_year) - 1}")
    elif args.to_year:
        filters.append(f"publication_year:<{int(args.to_year) + 1}")

    params = {
        "search": args.query,
        "per-page": str(limit),
        "sort": args.sort,
        "select": "id,doi,title,publication_year,authorships,primary_location,type,cited_by_count,open_access,abstract_inverted_index",
    }
    if filters:
        params["filter"] = ",".join(filters)
    if args.email and args.email != "<optional_contact_email>":
        params["mailto"] = args.email
    else:
        print("Warning: OpenAlex email not configured. Use --email for polite-pool requests.", file=sys.stderr)

    time.sleep(0.1)
    data = request_json(OPENALEX, params)
    results = [simplify_work(w) for w in data.get("results", [])]
    payload = {
        "source": "OpenAlex",
        "queried_at": datetime.now(timezone.utc).isoformat(),
        "query": args.query,
        "filters": filters,
        "sort": args.sort,
        "count": len(results),
        "results": results,
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(results)} OpenAlex results to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
