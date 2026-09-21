"""
Autonomous news ingest engine for Neural Pulse.
Fetches high-signal AI and tech news from RSS feeds and Hacker News Algolia.
Deduplicates using history.json.
"""

import json
import re
import urllib.request
import urllib.parse
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
from pathlib import Path

HISTORY_FILE = Path(__file__).parent / "history.json"

FEEDS = [
    {
        "name": "arXiv (cs.AI)",
        "type": "rss",
        "url": "http://export.arxiv.org/rss/cs.AI",
        "category": "AI Research"
    },
    {
        "name": "arXiv (cs.LG Machine Learning)",
        "type": "rss",
        "url": "http://export.arxiv.org/rss/cs.LG",
        "category": "AI Research"
    },
    {
        "name": "Hugging Face Daily",
        "type": "atom",
        "url": "https://huggingface.co/blog/feed.xml",
        "category": "Open Source AI"
    },
    {
        "name": "NVIDIA AI Blog",
        "type": "rss",
        "url": "https://blogs.nvidia.com/feed/",
        "category": "Robotics & Hardware"
    },
    {
        "name": "Hacker News AI Top",
        "type": "hn_algolia",
        "url": "https://hn.algolia.com/api/v1/search?query=AI+OR+LLM+OR+GPT+OR+Claude+OR+Gemini&tags=story&numericFilters=points>35&hitsPerPage=25",
        "category": "LLMs & Foundation Models"
    }
]

RELEVANCE_PATTERNS = [
    r"\b(ai|artificial intelligence)\b",
    r"\b(llm|llms|foundation model|foundation models)\b",
    r"\b(deep learning|machine learning)\b",
    r"\b(neural network|transformers|transformer)\b",
    r"\b(reasoning|benchmark|benchmarks)\b",
    r"\b(gpu|gpus|chip|silicon|accelerator)\b",
    r"\b(robotics|embodied ai|humanoid)\b",
    r"\b(open source|weights|checkpoint)\b",
    r"\b(autonomous agent|agents|agentic)\b",
    r"\b(gemini|openai|chatgpt|claude|anthropic|deepmind|mistral|llama|groq)\b"
]
COMPILED_PATTERNS = [re.compile(p, re.IGNORECASE) for p in RELEVANCE_PATTERNS]


def clean_html(raw_html: str) -> str:
    """Strip HTML tags and unescape entities."""
    if not raw_html:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw_html)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_url(url: str) -> str:
    """Normalize URL by stripping tracking query params."""
    if not url:
        return ""
    parsed = urllib.parse.urlparse(url)
    q_pairs = urllib.parse.parse_qsl(parsed.query)
    clean_pairs = [(k, v) for k, v in q_pairs if not k.startswith("utm_") and k not in ("ref", "source", "feed")]
    new_query = urllib.parse.urlencode(clean_pairs)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, ""))


def load_history() -> dict:
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"seen_urls": [], "published_articles": []}


def save_history(history: dict):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def is_relevant(title: str, summary: str) -> bool:
    combined = f"{title} {summary}"
    return any(pattern.search(combined) is not None for pattern in COMPILED_PATTERNS)


def fetch_feed_data(feed: dict) -> list[dict]:
    items = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        req = urllib.request.Request(feed["url"], headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            content = response.read()

        if feed["type"] == "hn_algolia":
            data = json.loads(content.decode("utf-8"))
            for hit in data.get("hits", []):
                title = hit.get("title", "")
                url = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
                summary = hit.get("story_text") or ""
                items.append({
                    "title": title,
                    "url": clean_url(url),
                    "summary": clean_html(summary),
                    "source_name": feed["name"],
                    "default_category": feed["category"],
                    "score": hit.get("points", 0)
                })

        elif feed["type"] == "atom":
            root = ET.fromstring(content)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            entries = root.findall("atom:entry", ns)
            if not entries:
                entries = root.findall("entry")
            for entry in entries:
                title_elem = entry.find("atom:title", ns)
                if title_elem is None:
                    title_elem = entry.find("title")
                title = title_elem.text if title_elem is not None and title_elem.text else ""

                link_elem = entry.find("atom:link", ns)
                if link_elem is None:
                    link_elem = entry.find("link")
                url = ""
                if link_elem is not None:
                    url = link_elem.get("href") or link_elem.text or ""

                summary_elem = entry.find("atom:summary", ns)
                if summary_elem is None:
                    summary_elem = entry.find("summary")
                summary = summary_elem.text if summary_elem is not None and summary_elem.text else ""

                items.append({
                    "title": clean_html(title),
                    "url": clean_url(url),
                    "summary": clean_html(summary)[:1000],
                    "source_name": feed["name"],
                    "default_category": feed["category"],
                    "score": 50
                })

        elif feed["type"] == "rss":
            root = ET.fromstring(content)
            channel = root.find("channel")
            if channel is None:
                channel = root
            for item in channel.findall("item"):
                title_elem = item.find("title")
                title = title_elem.text if title_elem is not None and title_elem.text else ""

                link_elem = item.find("link")
                url = link_elem.text if link_elem is not None and link_elem.text else ""

                desc_elem = item.find("description")
                summary = desc_elem.text if desc_elem is not None and desc_elem.text else ""

                items.append({
                    "title": clean_html(title),
                    "url": clean_url(url),
                    "summary": clean_html(summary)[:1000],
                    "source_name": feed["name"],
                    "default_category": feed["category"],
                    "score": 40
                })

    except Exception as e:
        print(f"Feed fetch note: {feed['name']} ({e})")

    return items


def collect_candidate_news(max_items: int = 5) -> list[dict]:
    """Collect, deduplicate, and rank top candidate news items."""
    history = load_history()
    seen_urls = set(history.get("seen_urls", []))

    candidates = []
    for feed in FEEDS:
        items = fetch_feed_data(feed)
        for it in items:
            url = it["url"]
            title = it["title"]
            summary = it["summary"]

            if not url or not title:
                continue
            if url in seen_urls:
                continue
            if not is_relevant(title, summary):
                continue

            candidates.append(it)

    unique_candidates = []
    seen_batch = set()
    for item in candidates:
        if item["url"] not in seen_batch:
            seen_batch.add(item["url"])
            unique_candidates.append(item)

    unique_candidates.sort(key=lambda x: x.get("score", 0), reverse=True)
    return unique_candidates[:max_items]


if __name__ == "__main__":
    candidates = collect_candidate_news(max_items=3)
    print(f"Top {len(candidates)} high-signal AI candidates:")
    for idx, c in enumerate(candidates, 1):
        print(f"[{idx}] {c['title']} ({c['source_name']}) -> {c['url']}")
