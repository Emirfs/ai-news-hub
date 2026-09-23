"""Discover recent AI stories from official primary-source feeds."""

import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

from pipeline.social_discovery import discover_primary_candidates, is_official
HISTORY_FILE = Path(__file__).parent / "history.json"
FEEDS = [
    {"name": "Anthropic Newsroom", "type": "anthropic_html", "url": "https://www.anthropic.com/news", "category": "LLMs & Foundation Models"},
    {"name": "OpenAI News", "type": "rss", "url": "https://openai.com/news/rss.xml", "category": "LLMs & Foundation Models"},
    {"name": "arXiv (cs.AI)", "type": "rss", "url": "https://export.arxiv.org/rss/cs.AI", "category": "AI Research"},
    {"name": "arXiv (cs.LG)", "type": "rss", "url": "https://export.arxiv.org/rss/cs.LG", "category": "AI Research"},
    {"name": "Hugging Face Blog", "type": "atom", "url": "https://huggingface.co/blog/feed.xml", "category": "Open Source AI"},
    {"name": "NVIDIA AI Blog", "type": "rss", "url": "https://blogs.nvidia.com/feed/", "category": "Robotics & Hardware"},
]
RELEVANCE_PATTERNS = [
    r"\b(ai|artificial intelligence)\b", r"\b(llm|llms|foundation model|foundation models)\b",
    r"\b(deep learning|machine learning)\b", r"\b(neural network|transformers?|reasoning|benchmarks?)\b",
    r"\b(gpus?|chip|silicon|accelerator|robotics|embodied ai|humanoid)\b",
    r"\b(open source|weights|checkpoint|autonomous agent|agents|agentic)\b",
    r"\b(gemini|openai|chatgpt|claude|anthropic|deepmind|deepseek|mistral|llama|groq|gpt[-\s]?\d+|opus\s+\d+(?:\.\d+)?)\b",
]
COMPILED_PATTERNS = [re.compile(p, re.IGNORECASE) for p in RELEVANCE_PATTERNS]
RUMOR_RE = re.compile(r"\b(rumou?rs?|leaks?|leaked|speculation|unreleased|unconfirmed|reportedly|allegedly|expected)\b", re.I)


def clean_html(raw_html: str) -> str:
    if not raw_html:
        return ""
    import html
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw_html))).strip()

def source_excerpt(summary: str, max_chars: int = 1200) -> str:
    """Keep source text readable without ending an excerpt mid-sentence."""
    summary = re.sub(r"^arXiv:\S+\s+Announce Type:\s+\w+\s+Abstract:\s*", "", summary)
    if len(summary) <= max_chars:
        return summary
    endings = [match.start() for match in re.finditer(r"(?<=[.!?])\s+", summary[:max_chars])]
    if endings and endings[-1] >= 200:
        return summary[:endings[-1]].strip()
    return summary[:max_chars].rsplit(" ", 1)[0].strip() + "…"


def clean_url(url: str) -> str:
    if not url:
        return ""
    parsed = urllib.parse.urlparse(url)
    pairs = [(k, v) for k, v in urllib.parse.parse_qsl(parsed.query)
             if not k.startswith("utm_") and k not in ("ref", "source", "feed")]
    path = parsed.path.rstrip("/") or "/"
    return urllib.parse.urlunparse((parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.params,
                                    urllib.parse.urlencode(pairs), ""))


def load_history() -> dict:
    try:
        return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"seen_urls": [], "published_articles": []}


def save_history(history: dict):
    HISTORY_FILE.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")


def is_relevant(title: str, summary: str) -> bool:
    return any(p.search(title + " " + summary) for p in COMPILED_PATTERNS)


def parse_publication_date(value: str) -> datetime | None:
    if not value:
        return None
    try:
        date = parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError):
        try:
            date = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except (AttributeError, ValueError):
            date = None
    if date is None:
        for fmt in ("%B %d, %Y", "%b %d, %Y"):
            try:
                date = datetime.strptime(value.strip(), fmt).replace(tzinfo=timezone.utc)
                break
            except ValueError:
                pass
    if date is not None and date.tzinfo is None:
        date = date.replace(tzinfo=timezone.utc)
    return date.astimezone(timezone.utc) if date else None


def recent_date(value: str, days: int = 7) -> bool:
    published = parse_publication_date(value)
    if published is None:
        return False
    age = datetime.now(timezone.utc) - published
    return timedelta(0) <= age <= timedelta(days=days)

def verify_live_url(url: str, timeout: int = 8) -> bool:
    """Require an accessible official HTTPS page; reachability is not fact-checking."""
    if not is_official(url):
        return False
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "NeuralPulse/1.0"})
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status == 200
    except Exception:
        return False



class _AnthropicNewsParser(HTMLParser):
    """Parse dated visible links from the official newsroom listing."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items, self.current, self.stack = [], None, []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href", "").startswith("/"):
            self._finish()
            self.current = {"url": urllib.parse.urljoin("https://www.anthropic.com", attrs["href"]),
                            "title": "", "summary": "", "published": ""}
        if self.current is None:
            return
        self.stack.append(tag)
        if tag == "time":
            self.current["published"] = attrs.get("datetime", "")

    def handle_data(self, data):
        if self.current is None:
            return
        text = data.strip()
        if not text:
            return
        if "time" in self.stack and not self.current["published"]:
            self.current["published"] = text
        elif any(t in self.stack for t in ("h1", "h2", "h3")):
            self.current["title"] += " " + text
        elif "p" in self.stack:
            self.current["summary"] += " " + text

    def handle_endtag(self, tag):
        if self.current is None:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == tag:
                self.stack = self.stack[:i]
                break
        if tag == "a":
            self._finish()

    def _finish(self):
        if self.current:
            for field in ("title", "summary", "published"):
                self.current[field] = self.current[field].strip()
            if self.current["title"] and self.current["summary"] and self.current["published"]:
                self.items.append(self.current)
        self.current, self.stack = None, []


def fetch_feed_data(feed: dict) -> list[dict]:
    try:
        request = urllib.request.Request(
            feed["url"],
            headers={"User-Agent": "NeuralPulse/1.0 (+https://github.com/Emirfs/ai-news-hub)"},
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            content = response.read()
        if feed["type"] == "anthropic_html":
            parser = _AnthropicNewsParser()
            parser.feed(content.decode("utf-8", errors="replace"))
            entries = parser.items
        else:
            root = ET.fromstring(content)
            ns = {"atom": "http://www.w3.org/2005/Atom", "dc": "http://purl.org/dc/elements/1.1/", "content": "http://purl.org/rss/1.0/modules/content/"}
            raw_entries = root.findall(".//item") if feed["type"] == "rss" else root.findall(".//atom:entry", ns)
            entries = []
            for entry in raw_entries:
                def text(*names):
                    for name in names:
                        elem = entry.find(name, ns)
                        if elem is not None and elem.text:
                            return elem.text.strip()
                    return ""
                link = entry.find("link", ns)
                url = (link.get("href") or link.text or "").strip() if link is not None else ""
                cat = entry.find("category")
                category = "AI Research" if feed["name"] == "OpenAI News" and cat is not None and (cat.text or "").lower() == "research" else feed["category"]
                entries.append({"title": text("title"), "summary": text("description", "summary", "content:encoded"),
                                "url": url, "published": text("pubDate", "published", "updated", "dc:date"),
                                "category": category})
        items = []
        for entry in entries:
            title, summary = clean_html(entry.get("title", "")), clean_html(entry.get("summary", ""))
            url = clean_url(entry.get("url", ""))
            if title and summary and url:
                items.append({"title": title, "url": url, "summary": source_excerpt(summary),
                              "source_name": feed["name"], "default_category": entry.get("category", feed["category"]),
                              "published": entry.get("published", ""),
                              "score": 60 if feed["name"] == "Anthropic Newsroom" else 55 if feed["name"] == "OpenAI News" else 40,
                              "is_primary_source": True})
        return items
    except Exception as exc:
        print(f"ERROR: Feed fetch failed: {feed['name']} ({feed['url']}): {exc}")
        return []

def _published_source_urls() -> set[str]:
    urls = set()
    news_dir = Path(__file__).resolve().parent.parent / "src" / "content" / "news"
    if not news_dir.exists():
        return urls
    for article in news_dir.glob("*.md"):
        try:
            content = article.read_text(encoding="utf-8")
            match = re.search(r'^sourceUrl:\s*["\']?([^"\'\n]+)', content, re.M)
            if match:
                urls.add(clean_url(match.group(1).strip()))
        except OSError as exc:
            print(f"WARNING: Could not inspect {article.name}: {exc}")
    return urls


def collect_candidate_news(max_items: int = 5) -> list[dict]:
    """Select recent, sourced stories from official feeds and community discovery."""
    seen_urls = {clean_url(url) for url in load_history().get("seen_urls", [])}
    seen_urls.update(_published_source_urls())
    unique = {}
    sources = [item for feed in FEEDS for item in fetch_feed_data(feed)]
    sources.extend(discover_primary_candidates())
    for item in sources:
        url = clean_url(item.get("url", ""))
        title = item.get("title", "").strip()
        summary = item.get("summary", "").strip()
        if not url or not title or not summary or url in seen_urls:
            continue
        if not recent_date(item.get("published", "")) or not is_relevant(title, summary):
            continue
        if RUMOR_RE.search(title) or RUMOR_RE.search(summary):
            continue
        item.update(url=url, title=title, summary=summary)
        if url not in unique or item["score"] > unique[url]["score"]:
            unique[url] = item
    ranked = sorted(unique.values(), key=lambda story: (story["score"], parse_publication_date(story["published"])), reverse=True)
    eligible = []
    for item in ranked:
        if verify_live_url(item["url"]):
            eligible.append(item)
            if len(eligible) >= max_items:
                break
    return eligible


if __name__ == "__main__":
    for idx, candidate in enumerate(collect_candidate_news(max_items=3), 1):
        print(f"[{idx}] {candidate['title']} ({candidate['source_name']}) -> {candidate['url']}")
