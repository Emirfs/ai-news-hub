"""Source-attributed news excerpts for Neural Pulse."""

import json
import re
from html import escape

ALLOWED_CATEGORIES = [
    "LLMs & Foundation Models",
    "AI Research",
    "Robotics & Hardware",
    "Open Source AI",
    "Industry & Startups",
]


def create_slug(title: str, max_words: int = 6) -> str:
    """Generate a clean URL slug from a headline."""
    words = re.sub(r"[^\w\s-]", "", title.lower()).split()[:max_words]
    return "-".join(words)


def generate_article_from_item(item: dict) -> dict:
    """Generate a concise source-attributed article; never add unsupported facts."""
    title = item["title"].strip()
    source_excerpt = item.get("summary", "").strip()
    if not title or not source_excerpt:
        raise ValueError("A source headline and excerpt are required")
    if item.get("is_primary_source") is not True:
        raise ValueError("Only official primary-source items can be published")
    excerpt = source_excerpt
    category = item.get("default_category", "AI Research")
    if category not in ALLOWED_CATEGORIES:
        raise ValueError("Unconfirmed stories cannot be published automatically")
    key = item.get("key", "")
    if key and len(source_excerpt) >= 80:
        try:
            import urllib.request
            payload = json.dumps({
                "contents": [{"parts": [{"text":
                    "Summarize this official source excerpt in 2 concise factual sentences. "
                    "Use only information explicitly stated. Do not add facts, evaluations, "
                    "predictions, claims about benchmarks, or context not in the excerpt. "
                    "If it cannot be summarized safely, repeat its central factual statement. "
                    f"\n\nHeadline: {title}\nExcerpt: {source_excerpt}"}]}],
                "generationConfig": {"temperature": 0, "maxOutputTokens": 120},
            }).encode("utf-8")
            req = urllib.request.Request(
                f"https://generativelanguage.googleapis.com/v1beta/models/"
                f"{item.get('model', 'gemini-2.5-flash')}:generateContent?key={key}",
                data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=15) as response:
                result = json.loads(response.read().decode("utf-8"))
            generated = result["candidates"][0]["content"]["parts"][0]["text"].strip()
            if (generated and len(generated) <= 700
                    and all(sentence.strip() in source_excerpt
                            for sentence in re.split(r"(?<=[.!?])\s+", generated)
                            if sentence.strip())):
                excerpt = generated
        except Exception as exc:
            print(f"Summary generation unavailable; retaining source excerpt ({exc}).")
    source = item["source_name"]
    return {
        "title": title,
        "description": excerpt[:300],
        "category": category,
        "tags": [],
        "keyTakeaways": [],
        "content_markdown": (
            "### Source-attributed summary\n\n"
            f"This summary is based only on {escape(source)}'s published excerpt. "
            "It has not been independently fact-checked by Neural Pulse.\n\n"
            f"{escape(excerpt)}\n\n"
            f"[Read the original source]({item['url']}) for the full context."
        ),
    }


def format_markdown_file(article: dict, source_url: str, source_name: str, pub_date: str) -> str:
    """Format article into Astro Markdown with typed frontmatter."""
    escaped_title = json.dumps(article['title'], ensure_ascii=False)
    escaped_desc = json.dumps(article['description'], ensure_ascii=False)
    escaped_category = json.dumps(article['category'], ensure_ascii=False)
    tags_yaml = json.dumps(article.get('tags', []), ensure_ascii=False)
    takeaways = article.get('keyTakeaways', [])
    takeaways_yaml = "keyTakeaways: []" if not takeaways else "keyTakeaways:\n" + "\n".join(
        f"  - {json.dumps(point, ensure_ascii=False)}" for point in takeaways
    )

    return f"""---
title: {escaped_title}
description: {escaped_desc}
pubDate: {pub_date}
category: {escaped_category}
tags: {tags_yaml}
author: "Neural Pulse AI"
sourceUrl: {json.dumps(source_url, ensure_ascii=False)}
sourceName: {json.dumps(source_name, ensure_ascii=False)}
isWeeklyDigest: false
sourcePolicy: primary
{takeaways_yaml}
---

{article['content_markdown'].strip()}
"""
