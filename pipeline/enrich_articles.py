"""
Enriches all existing articles in src/content/news/ with deep, comprehensive,
accessible technical analyses and structured sections.
"""

import sys
import re
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.weekly_digest import extract_frontmatter
from pipeline.generator import generate_article_from_item, format_markdown_file

NEWS_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "news"


def enrich_existing_articles():
    if not NEWS_DIR.exists():
        return

    enriched_count = 0
    for md_file in NEWS_DIR.glob("*.md"):
        if "weekly-ai-briefing" in md_file.name:
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
            meta, body = extract_frontmatter(content)
            word_count = len(body.split())

            # If body is under 350 words, enrich it
            if word_count < 350:
                print(f"Enriching: {md_file.name} ({word_count} words -> 500+ words)...")

                item = {
                    "title": meta.get("title", md_file.stem),
                    "summary": meta.get("description", ""),
                    "source_name": meta.get("sourceName", "Technical Wire"),
                    "url": meta.get("sourceUrl", ""),
                    "default_category": meta.get("category", "LLMs & Foundation Models")
                }

                article_data = generate_article_from_item(item)
                article_data["title"] = meta.get("title", article_data["title"])
                article_data["category"] = meta.get("category", article_data["category"])

                pub_date = meta.get("pubDate", "2026-09-21")
                new_md = format_markdown_file(
                    article=article_data,
                    source_url=meta.get("sourceUrl", ""),
                    source_name=meta.get("sourceName", "Primary Source"),
                    pub_date=pub_date
                )

                md_file.write_text(new_md, encoding="utf-8")
                enriched_count += 1

        except Exception as e:
            print(f"Error enriching {md_file.name}: {e}")

    print(f"\n✓ Successfully enriched {enriched_count} articles with in-depth reporting.")


if __name__ == "__main__":
    enrich_existing_articles()
