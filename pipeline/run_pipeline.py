"""
Master autonomous pipeline orchestrator for Neural Pulse.
Supports daily news cycle and weekly digest compilation.
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.ingest import collect_candidate_news, load_history, save_history
from pipeline.generator import generate_article_from_item, format_markdown_file, create_slug
from pipeline.weekly_digest import generate_weekly_digest

NEWS_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "news"


def run_daily_pipeline(max_items: int = 3, dry_run: bool = False):
    """Run daily news discovery, LLM curation, and markdown generation."""
    print("=" * 60)
    print("Starting Neural Pulse Autonomous News Cycle")
    print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print("=" * 60)

    NEWS_DIR.mkdir(parents=True, exist_ok=True)
    history = load_history()
    seen_urls = set(history.get("seen_urls", []))
    published = history.get("published_articles", [])

    candidates = collect_candidate_news(max_items=max_items)
    if not candidates:
        print("No new candidate articles found in this cycle.")
        return

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    generated_count = 0

    for idx, item in enumerate(candidates, 1):
        print(f"\n[{idx}/{len(candidates)}] Processing: {item['title']}")
        try:
            article = generate_article_from_item(item)
            slug_base = create_slug(article['title'])
            slug = f"{today_str}-{slug_base}"
            file_path = NEWS_DIR / f"{slug}.md"

            counter = 1
            while file_path.exists():
                file_path = NEWS_DIR / f"{slug}-{counter}.md"
                counter += 1

            md_content = format_markdown_file(
                article=article,
                source_url=item['url'],
                source_name=item['source_name'],
                pub_date=today_str
            )

            if dry_run:
                print(f"  [DRY RUN] Would write to: {file_path.name}")
                print(f"  Title: {article['title']}")
                print(f"  Category: {article['category']}")
            else:
                file_path.write_text(md_content, encoding="utf-8")
                print(f"  ✓ Saved dispatch: {file_path.name}")
                seen_urls.add(item['url'])
                published.append({
                    "slug": file_path.stem,
                    "date": today_str,
                    "title": article['title']
                })
                generated_count += 1

        except Exception as e:
            print(f"  ✗ Error generating article for '{item['title']}': {e}")

    if not dry_run and generated_count > 0:
        history["seen_urls"] = list(seen_urls)
        history["published_articles"] = published
        save_history(history)
        print(f"\n✓ Successfully published {generated_count} new dispatches and updated history.json.")


def main():
    parser = argparse.ArgumentParser(description="Neural Pulse AI Newsroom Pipeline")
    parser.add_argument("--mode", choices=["daily", "weekly"], default="daily", help="Pipeline execution mode")
    parser.add_argument("--count", type=int, default=3, help="Max articles to generate in daily mode")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without writing files")

    args = parser.parse_args()

    if args.mode == "daily":
        run_daily_pipeline(max_items=args.count, dry_run=args.dry_run)
    elif args.mode == "weekly":
        generate_weekly_digest()


if __name__ == "__main__":
    main()
