"""Compile a dated weekly index of articles with primary-source attribution."""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


NEWS_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "news"


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown content."""
    match = re.search(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content

    yaml_block, body = match.groups()
    data = {}

    title_match = re.search(r'title:\s*["\']?(.*?)["\']?$', yaml_block, re.MULTILINE)
    if title_match:
        data["title"] = title_match.group(1).strip('"\'')

    desc_match = re.search(r'description:\s*["\']?(.*?)["\']?$', yaml_block, re.MULTILINE)
    if desc_match:
        data["description"] = desc_match.group(1).strip('"\'')

    date_match = re.search(r'pubDate:\s*["\']?(.*?)["\']?$', yaml_block, re.MULTILINE)
    if date_match:
        data["pubDate"] = date_match.group(1).strip('"\'')

    cat_match = re.search(r'category:\s*["\']?(.*?)["\']?$', yaml_block, re.MULTILINE)
    if cat_match:
        data["category"] = cat_match.group(1).strip('"\'')

    source_match = re.search(r'sourceName:\s*["\']?(.*?)["\']?$', yaml_block, re.MULTILINE)
    if source_match:
        data["sourceName"] = source_match.group(1).strip('"\'')
    url_match = re.search(r'sourceUrl:\s*["\']?(.*?)["\']?$', yaml_block, re.MULTILINE)
    if url_match:
        data["sourceUrl"] = url_match.group(1).strip('"\'')
    data["sourcePolicy"] = bool(re.search(r"^sourcePolicy:\s*primary\s*$", yaml_block, re.MULTILINE))

    digest_match = re.search(r'isWeeklyDigest:\s*(true|false)', yaml_block, re.IGNORECASE)
    if digest_match:
        data["isWeeklyDigest"] = digest_match.group(1).lower() == "true"


    return data, body


def get_recent_articles(days: int = 10) -> list[dict]:
    """Load only recently published primary-source articles."""
    articles = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    for file in NEWS_DIR.glob("*.md"):
        try:
            meta, _ = extract_frontmatter(file.read_text(encoding="utf-8"))
            if not meta.get("sourcePolicy") or not meta.get("sourceUrl"):
                continue
            published = datetime.fromisoformat(meta["pubDate"])
            if published.tzinfo is None:
                published = published.replace(tzinfo=timezone.utc)
            if published < cutoff:
                continue
            articles.append({"title": meta["title"], "description": meta["description"],
                             "sourceUrl": meta["sourceUrl"], "date": meta["pubDate"]})
        except (OSError, KeyError, ValueError) as exc:
            print(f"Skipping invalid weekly source {file.name}: {exc}")
    return articles


def generate_weekly_digest() -> str:
    """List only dated source-backed articles; do not generate new factual claims."""
    articles = get_recent_articles(days=7)
    if not articles:
        print("No source-backed stories for this week's digest.")
        return ""
    articles.sort(key=lambda story: story["date"], reverse=True)
    now = datetime.now(timezone.utc)
    today_iso = now.strftime("%Y-%m-%d")
    week_num = now.strftime("%W")
    target_path = NEWS_DIR / f"{today_iso}-weekly-ai-briefing-w{week_num}.md"
    if target_path.exists():
        return str(target_path)
    lines = ["Stories published this week, linked to their original sources.",
             "The underlying claims have not been independently verified.", ""]
    for story in articles:
        lines.extend([f"### {story['title']}", "",
                      f"{story['description']}", "",
                      f"[Original source]({story['sourceUrl']})", ""])
    title = f"AI news this week: {len(articles)} source-linked stories"
    description = f"A dated list of {len(articles)} AI stories with links to their original sources."
    content = f"""---
title: {json.dumps(title, ensure_ascii=False)}
description: {json.dumps(description, ensure_ascii=False)}
pubDate: {today_iso}
category: "Weekly Digest"
tags: ["Weekly Digest"]
author: "Neural Pulse"
sourceUrl: ""
sourceName: "Neural Pulse"
isWeeklyDigest: true
keyTakeaways: []
---

{chr(10).join(lines)}
"""
    target_path.write_text(content, encoding="utf-8")
    print(f"Generated source-linked weekly list: {target_path.name}")
    return str(target_path)


if __name__ == "__main__":
    generate_weekly_digest()
