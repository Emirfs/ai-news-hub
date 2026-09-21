"""
Backfill script for Neural Pulse.
Fetches top technical news and announcements for OpenAI, Anthropic, DeepSeek,
and Google Gemini over the past 30 days (August - September 2026).
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.ingest import clean_url, clean_html, load_history, save_history
from pipeline.generator import generate_article_from_item, format_markdown_file, create_slug
from pipeline.run_pipeline import update_readme_and_archive

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "src" / "content" / "news"

PROVIDERS = [
    {
        "provider": "OpenAI",
        "category": "LLMs & Foundation Models",
        "queries": ["OpenAI", "ChatGPT", "Sam Altman"]
    },
    {
        "provider": "Anthropic",
        "category": "AI Research",
        "queries": ["Anthropic", "Claude 3.5", "Claude Code"]
    },
    {
        "provider": "DeepSeek",
        "category": "Open Source AI",
        "queries": ["DeepSeek", "DeepSeek-v4", "DeepSeek-R1"]
    },
    {
        "provider": "Google Gemini",
        "category": "LLMs & Foundation Models",
        "queries": ["Google Gemini", "Gemini 3.8", "DeepMind"]
    }
]


def fetch_provider_month_news(provider_info: dict) -> list[dict]:
    items = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    # Approx timestamp for 30 days ago from 2026-09-21
    # 2026-08-21 00:00:00 UTC ~ 1787270400
    since_ts = 1787270400

    for query in provider_info["queries"]:
        url = (
            f"https://hn.algolia.com/api/v1/search_by_date?"
            f"query={urllib.parse.quote(query)}&tags=story&numericFilters=created_at_i>{since_ts},points>25&hitsPerPage=10"
        )
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            for hit in data.get("hits", []):
                title = hit.get("title", "")
                target_url = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
                summary = hit.get("story_text") or ""
                created_at = hit.get("created_at", "")[:10]  # YYYY-MM-DD
                points = hit.get("points", 0)

                # Filter out obvious non-technical or trivial gossip
                if any(bad in title.lower() for bad in ["porn", "epstein", "lawsuit", "s&p 500 rejects"]):
                    continue

                items.append({
                    "title": title,
                    "url": clean_url(target_url),
                    "summary": clean_html(summary)[:1200],
                    "source_name": f"{provider_info['provider']} Telemetry",
                    "default_category": provider_info["category"],
                    "pub_date": created_at,
                    "points": points
                })
            time.sleep(0.3)
        except Exception as e:
            print(f"Error querying {query}: {e}")

    # Deduplicate by URL
    unique = []
    seen = set()
    for it in sorted(items, key=lambda x: x["points"], reverse=True):
        if it["url"] not in seen:
            seen.add(it["url"])
            unique.append(it)

    return unique[:4]  # Top 4 highest signal per provider


def run_backfill():
    print("=" * 60)
    print("Starting 30-Day Historical Backfill: OpenAI, Anthropic, DeepSeek, Gemini")
    print("=" * 60)

    history = load_history()
    seen_urls = set(history.get("seen_urls", []))
    published = history.get("published_articles", [])
    NEWS_DIR.mkdir(parents=True, exist_ok=True)

    total_added = 0

    for prov in PROVIDERS:
        print(f"\nFetching past month dispatches for {prov['provider']}...")
        news_items = fetch_provider_month_news(prov)

        for it in news_items:
            url = it["url"]
            if url in seen_urls:
                continue

            print(f"  → Backfilling [{it['pub_date']}]: {it['title'][:65]}...")
            try:
                article = generate_article_from_item(it)
                slug_base = create_slug(article['title'])
                pub_date = it.get("pub_date", "2026-09-01")
                slug = f"{pub_date}-{slug_base}"
                file_path = NEWS_DIR / f"{slug}.md"

                counter = 1
                while file_path.exists():
                    file_path = NEWS_DIR / f"{slug}-{counter}.md"
                    counter += 1

                md_content = format_markdown_file(
                    article=article,
                    source_url=url,
                    source_name=it["source_name"],
                    pub_date=pub_date
                )

                file_path.write_text(md_content, encoding="utf-8")
                seen_urls.add(url)
                published.append({
                    "slug": file_path.stem,
                    "date": pub_date,
                    "title": article["title"]
                })
                total_added += 1

            except Exception as e:
                print(f"    ✗ Failed to process {it['title']}: {e}")

    if total_added > 0:
        history["seen_urls"] = list(seen_urls)
        history["published_articles"] = published
        save_history(history)
        print(f"\n✓ Successfully backfilled {total_added} historical dispatches.")
        update_readme_and_archive()
    else:
        print("\nAll provider stories already indexed or up to date.")


if __name__ == "__main__":
    run_backfill()
