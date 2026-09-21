"""
Gemini Flash editorial generator for Neural Pulse.
Transforms raw technical news, abstracts, and release notes into
professional, high-density AI dispatches.
"""

import json
import os
import re
import urllib.request
import urllib.error
from datetime import datetime, timezone

# Candidate models to try in order
DEFAULT_MODELS = [
    os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
    "gemini-1.5-flash",
    "gemini-2.0-flash-exp",
    "gemini-1.5-pro",
]
GEMINI_MODEL = DEFAULT_MODELS[0]

ALLOWED_CATEGORIES = [
    "LLMs & Foundation Models",
    "AI Research",
    "Robotics & Hardware",
    "Open Source AI",
    "Industry & Startups"
]


def create_slug(title: str, max_words: int = 6) -> str:
    """Generate clean URL slug from title."""
    clean = re.sub(r"[^\w\s-]", "", title.lower())
    words = clean.split()[:max_words]
    return "-".join(words)


def call_gemini_api(prompt: str, api_key: str) -> dict:
    """Call Google Gemini REST API with model fallback."""
    last_error = None

    # Deduplicate candidate models while preserving order
    models_to_try = []
    for m in DEFAULT_MODELS:
        if m and m not in models_to_try:
            models_to_try.append(m)

    for model_name in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.3,
                "topP": 0.9,
                "responseMimeType": "application/json"
            }
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))

            candidates = res_data.get("candidates", [])
            if not candidates:
                raise ValueError(f"No candidates returned from Gemini API ({model_name})")

            content_parts = candidates[0].get("content", {}).get("parts", [])
            if not content_parts:
                raise ValueError(f"Empty content returned from Gemini API ({model_name})")

            raw_text = content_parts[0].get("text", "")
            print(f"  ✓ Successfully generated dispatch via model: {model_name}")
            return json.loads(raw_text)

        except urllib.error.HTTPError as e:
            last_error = e
            print(f"  Model {model_name} HTTP {e.code}: {e.reason}. Trying next model...")
            continue
        except Exception as e:
            last_error = e
            print(f"  Model {model_name} failed: {e}. Trying next model...")
            continue

    raise RuntimeError(f"All Gemini models failed. Last error: {last_error}")


def generate_article_from_item(item: dict) -> dict:
    """
    Takes an ingested news candidate and returns a structured article dict.
    Uses Gemini API if GEMINI_API_KEY is available; otherwise uses deterministic fallback.
    """
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    prompt = f"""You are the senior editorial AI agent at "Neural Pulse", a premier technology newsroom covering frontier artificial intelligence, machine learning research, robotics, and hardware.

Analyze the following incoming technical story and produce a rigorous, high-density, analytical news article in English.

Input Data:
Title: {item['title']}
Source: {item['source_name']}
URL: {item['url']}
Summary/Context: {item['summary']}

Requirements:
1. Title: Journalistic, clear, informative headline (maximum 14 words). Avoid clickbait.
2. Description: 1-2 sentence executive briefing explaining the core technical accomplishment and why it matters.
3. Category: Must be exactly one of: {json.dumps(ALLOWED_CATEGORIES)}.
4. Tags: 3 to 5 relevant technical tags (e.g., ["transformer", "open-source", "quantization"]).
5. Key Takeaways: Exactly 3 bullet points with concrete technical insights, benchmark metrics, or architectural mechanisms.
6. Content Markdown: 3 to 4 analytical sections in valid Markdown (use ### for section headers):
   - ### Background & Strategic Context
   - ### Technical Architecture & Key Innovations
   - ### Ecosystem Impact & Developer Implications
   (Do not include the main h1 title in the markdown body).

Output must strictly conform to this JSON schema:
{{
  "title": "...",
  "description": "...",
  "category": "...",
  "tags": ["..."],
  "keyTakeaways": ["...", "...", "..."],
  "content_markdown": "..."
}}
"""

    if api_key:
        try:
            print(f"Calling Gemini API for: {item['title'][:60]}...")
            article_data = call_gemini_api(prompt, api_key)
            if article_data.get("category") not in ALLOWED_CATEGORIES:
                article_data["category"] = item.get("default_category", ALLOWED_CATEGORIES[0])
            return article_data
        except Exception as e:
            print(f"Gemini API call failed: {e}. Falling back to structured synthesis.")

    # Fallback synthesizer (for local testing / offline mode)
    clean_title = item['title'].replace('Show HN: ', '').strip()
    return {
        "title": clean_title if len(clean_title) > 20 else f"New Frontier Development: {clean_title}",
        "description": f"New advancement released via {item['source_name']}, providing enhanced capabilities in artificial intelligence tooling and research.",
        "category": item.get("default_category", "LLMs & Foundation Models"),
        "tags": ["ai-systems", "open-source", "developer-tools", "machine-learning"],
        "keyTakeaways": [
            f"Published and distributed via {item['source_name']}.",
            "Introduces targeted architectural improvements and practical implementation workflows.",
            "Accessible for community integration and reproducible evaluation."
        ],
        "content_markdown": f"""### Background & Strategic Context

The rapid acceleration of frontier artificial intelligence systems continues to reshape software engineering and computational research. The recent release of **{clean_title}** highlights the persistent transition toward modular, autonomous intelligence workflows.

### Technical Architecture & Key Innovations

According to technical specifications published by the team:

- **Integration Pipeline**: Designed for seamless interfacing with modern machine learning stacks.
- **Efficiency Focus**: Optimized resource utilization minimizing compute overhead during inference and deployment.
- **Extensible Framework**: Modular components allowing custom evaluation criteria and developer extensions.

### Ecosystem Impact & Developer Implications

As open-source ecosystems and proprietary model providers compete on capabilities, projects that bridge the gap between foundation models and practical deployment become crucial infrastructure.

Developers and engineering teams can evaluate the full implementation and benchmarks directly from the primary project source linked above.
"""
    }


def format_markdown_file(article: dict, source_url: str, source_name: str, pub_date: str) -> str:
    """Format article into Astro Markdown with typed frontmatter."""
    escaped_title = json.dumps(article['title'], ensure_ascii=False)
    escaped_desc = json.dumps(article['description'], ensure_ascii=False)
    escaped_category = json.dumps(article['category'], ensure_ascii=False)
    tags_yaml = json.dumps(article.get('tags', []), ensure_ascii=False)
    takeaways_yaml = "\n".join([f"  - {json.dumps(point, ensure_ascii=False)}" for point in article.get('keyTakeaways', [])])

    return f"""---
title: {escaped_title}
description: {escaped_desc}
pubDate: {pub_date}
category: {escaped_category}
tags: {tags_yaml}
author: "Neural Pulse AI"
sourceUrl: "{source_url}"
sourceName: "{source_name}"
isWeeklyDigest: false
keyTakeaways:
{takeaways_yaml}
---

{article['content_markdown'].strip()}
"""
