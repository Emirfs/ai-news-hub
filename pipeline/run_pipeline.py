"""
Master autonomous pipeline orchestrator for Neural Pulse.
Supports daily/hourly news cycle and weekly digest compilation.
Automatically updates root ARCHIVE.md for direct GitHub reading.
"""

import argparse
import sys
import re
from datetime import datetime, timezone
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.ingest import collect_candidate_news, load_history, save_history
from pipeline.generator import generate_article_from_item, format_markdown_file, create_slug
from pipeline.weekly_digest import generate_weekly_digest, extract_frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "src" / "content" / "news"
ARCHIVE_FILE = REPO_ROOT / "ARCHIVE.md"


def update_archive_markdown():
    """Generates a root ARCHIVE.md table linking to both .md files and live site."""
    if not NEWS_DIR.exists():
        return

    articles = []
    for md_file in NEWS_DIR.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            meta, body = extract_frontmatter(content)
            slug = md_file.stem
            articles.append({
                "slug": slug,
                "file_name": md_file.name,
                "title": meta.get("title", slug),
                "date": meta.get("pubDate", "Unknown"),
                "category": meta.get("category", "General"),
                "source": meta.get("sourceName", "Web"),
                "is_digest": meta.get("isWeeklyDigest", False),
            })
        except Exception as e:
            print(f"Error parsing {md_file.name} for archive: {e}")

    # Sort descending by date, then title
    articles.sort(key=lambda a: (str(a["date"]), a["title"]), reverse=True)

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# 📰 Neural Pulse — AI Dispatches Archive",
        "",
        "> Autonomous archive of frontier artificial intelligence dispatches and weekly briefings.",
        f"> **Last Synced:** `{now_iso}` | **Total Dispatches:** `{len(articles)}`",
        "",
        "**Online Readers:**",
        "- 🌐 [Live Web Publication (GitHub Pages)](https://emirfs.github.io/ai-news-hub/)",
        "- 📡 [RSS 2.0 Feed](https://emirfs.github.io/ai-news-hub/rss.xml)",
        "",
        "---",
        "",
        "## 📚 Dispatches Directory (Direct Markdown & Web Links)",
        "",
        "| Date | Category | Title & Markdown Source | Live Web View | Primary Source |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]

    for a in articles:
        md_link = f"[{a['title']}](src/content/news/{a['file_name']})"
        web_link = f"[Read Online](https://emirfs.github.io/ai-news-hub/news/{a['slug']}/)"
        badge = "📋 **[Digest]** " if a["is_digest"] else ""
        lines.append(f"| `{a['date']}` | {a['category']} | {badge}{md_link} | {web_link} | {a['source']} |")

    lines.append("")
    lines.append("---")
    lines.append("*All articles are autonomously curated and preserved in Markdown format.*")
    lines.append("")

    ARCHIVE_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ Updated root {ARCHIVE_FILE.name} with {len(articles)} entries.")


def run_daily_pipeline(max_items: int = 2, dry_run: bool = False):
    """Run hourly/daily news discovery, LLM curation, and markdown generation."""
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
        update_archive_markdown()
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

    if not dry_run:
        if generated_count > 0:
            history["seen_urls"] = list(seen_urls)
            history["published_articles"] = published
            save_history(history)
            print(f"\n✓ Successfully published {generated_count} new dispatches and updated history.json.")
        # Always keep ARCHIVE.md fresh
        update_archive_markdown()


def main():
    parser = argparse.ArgumentParser(description="Neural Pulse AI Newsroom Pipeline")
    parser.add_argument("--mode", choices=["daily", "weekly", "archive"], default="daily", help="Pipeline execution mode")
    parser.add_argument("--count", type=int, default=2, help="Max articles to generate in daily mode")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without writing files")

    args = parser.parse_args()

    if args.mode == "daily":
        run_daily_pipeline(max_items=args.count, dry_run=args.dry_run)
    elif args.mode == "weekly":
        generate_weekly_digest()
        update_archive_markdown()
    elif args.mode == "archive":
        update_archive_markdown()


if __name__ == "__main__":
    main()
