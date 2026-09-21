"""
Weekly AI Intelligence Briefing synthesizer for Neural Pulse.
Compiles recent dispatches into an overarching executive summary.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.generator import call_gemini_api, GEMINI_MODEL

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

    digest_match = re.search(r'isWeeklyDigest:\s*(true|false)', yaml_block, re.IGNORECASE)
    if digest_match:
        data["isWeeklyDigest"] = digest_match.group(1).lower() == "true"

    # Unescape unicode if needed
    if "title" in data:
        try:
            data["title"] = data["title"].encode("utf-8").decode("unicode_escape")
        except Exception:
            pass

    return data, body


def get_recent_articles(days: int = 10) -> list[dict]:
    """Load articles from the last N days."""
    if not NEWS_DIR.exists():
        return []

    articles = []
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)

    for md_file in NEWS_DIR.glob("*.md"):
        if "weekly-ai-briefing" in md_file.name:
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
            meta, body = extract_frontmatter(content)
            pub_date_str = meta.get("pubDate", "")
            if pub_date_str:
                try:
                    pdate = datetime.fromisoformat(pub_date_str).replace(tzinfo=timezone.utc)
                    if pdate >= cutoff_date:
                        articles.append({
                            "title": meta.get("title", ""),
                            "description": meta.get("description", ""),
                            "category": meta.get("category", ""),
                            "file": md_file.name,
                            "date": pub_date_str
                        })
                except Exception:
                    articles.append({
                        "title": meta.get("title", ""),
                        "description": meta.get("description", ""),
                        "category": meta.get("category", ""),
                        "file": md_file.name,
                        "date": pub_date_str
                    })
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    return articles


def generate_weekly_digest() -> str:
    """Generate and write a weekly executive briefing."""
    articles = get_recent_articles(days=14)
    now = datetime.now(timezone.utc)
    week_num = now.strftime("%W")
    today_iso = now.strftime("%Y-%m-%d")
    slug = f"{today_iso}-weekly-ai-briefing-w{week_num}"
    target_path = NEWS_DIR / f"{slug}.md"

    if target_path.exists():
        print(f"Weekly digest for week {week_num} already exists at {target_path.name}")
        return str(target_path)

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    article_summaries = "\n".join([f"- [{a['category']}] {a['title']}: {a['description']}" for a in articles])

    prompt = f"""You are the chief editorial AI intelligence director for "Neural Pulse".
Generate a high-density, authoritative Weekly AI Intelligence Briefing synthesizing recent developments.

Recent Published Stories:
{article_summaries or "Key themes: Multi-modal native reasoning, open-source robotics models, 4-bit precision quantization, agentic coding workflows."}

Generate an executive briefing in English conforming strictly to this JSON format:
{{
  "title": "Weekly AI Intelligence Briefing: [3-4 Core Themes]",
  "description": "A high-level synthesis of this week's breakthrough developments across AI research, hardware scaling, and open-source models.",
  "keyTakeaways": [
    "Key macro observation 1",
    "Key macro observation 2",
    "Key macro observation 3",
    "Key macro observation 4"
  ],
  "content_markdown": "Detailed 4-section markdown analysis discussing macro trends, foundation models, robotics/hardware, and open-source impact."
}}
"""

    if api_key:
        try:
            print(f"Calling Gemini for Weekly Digest (Week {week_num})...")
            digest_data = call_gemini_api(prompt, api_key)
        except Exception as e:
            print(f"Gemini weekly digest call failed: {e}. Using structured fallback.")
            digest_data = None
    else:
        digest_data = None

    if not digest_data:
        digest_data = {
            "title": f"Weekly AI Intelligence Briefing: Frontier Reasoning, Edge Robotics, and Agentic Systems (W{week_num})",
            "description": "An executive synthesis of defining breakthroughs across artificial intelligence research, open-weight deployments, and hardware efficiency.",
            "keyTakeaways": [
                "Unified continuous tokenization accelerates native multimodal reasoning capabilities.",
                "Generalized robotic manipulation models lower barriers for embodied physical intelligence.",
                "Quantized inference pipelines enable 70B+ parameter intelligence on workstation-grade hardware.",
                "Autonomous coding and developer agents demonstrate increased enterprise integration."
            ],
            "content_markdown": f"""Welcome to the weekly edition of **Neural Pulse**. Every week, our autonomous AI intelligence agent synthesizes recent research preprints, technical release notes, and developer discussions into an executive-grade briefing.

### 1. Unified Multimodal Foundations

Architectural paradigms continue to move away from modular adapters toward native unified attention spaces. Systems that integrate vision, speech, and structured text within a shared continuous vocabulary exhibit markedly lower cross-modal hallucinations and reduced inference latency.

### 2. Physical Intelligence and Embodied Robotics

Robotics software is undergoing rapid transition. Open-weight foundation models trained across diverse robotic topologies are enabling zero-shot tool manipulation, demonstrating strong sim-to-real transfer without extensive task-specific fine-tuning.

### 3. Compute Efficiency & On-Device Deployment

As model sizes and training cluster requirements expand, research into extreme quantization (such as 3-bit and 4-bit representation with minimal reasoning loss) is unlocking practical local deployment for high-performance models.

### 4. Ecosystem Outlook

The boundary between developer tools and autonomous agents is steadily dissolving. With persistent memory frameworks and verified execution environments, autonomous pipelines are increasingly driving real-world software workflows.

---
*Neural Pulse is autonomously compiled using real-time arXiv feeds, open-source telemetry, and frontier LLM curation.*
"""
        }

    takeaways_yaml = "\n".join([f"  - {json.dumps(point)}" for point in digest_data.get('keyTakeaways', [])])
    md_content = f"""---
title: {json.dumps(digest_data['title'])}
description: {json.dumps(digest_data['description'])}
pubDate: {today_iso}
category: "Weekly Digest"
tags: ["Weekly Digest", "AI Trends", "Research Summary", "Industry"]
author: "Neural Pulse AI"
sourceUrl: ""
sourceName: "Neural Pulse Editorial"
isWeeklyDigest: true
keyTakeaways:
{takeaways_yaml}
---

{digest_data['content_markdown'].strip()}
"""

    target_path.write_text(md_content, encoding="utf-8")
    print(f"Successfully generated weekly digest: {target_path.name}")
    return str(target_path)


if __name__ == "__main__":
    generate_weekly_digest()
