"""Discover links from Reddit, Hugging Face, and opt-in X; publish only dated primary pages."""

import json
import os
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html import unescape
from html.parser import HTMLParser

USER_AGENT = "NeuralPulse/1.0 (+https://github.com/Emirfs/ai-news-hub)"
OFFICIAL_HOSTS = {
    "anthropic.com", "www.anthropic.com", "openai.com", "www.openai.com",
    "developers.openai.com", "huggingface.co", "arxiv.org", "export.arxiv.org",
    "blogs.nvidia.com", "deepmind.google", "blog.google",
}
REDDIT_FEEDS = ["https://www.reddit.com/r/MachineLearning/new/.rss", "https://www.reddit.com/r/LocalLLaMA/new/.rss"]


def fetch(url, headers=None):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(request, timeout=12) as response:
        return response.read(1_000_001)


def is_official(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in OFFICIAL_HOSTS:
        return False
    if parsed.hostname == "huggingface.co":
        return parsed.path.startswith("/blog/")
    if parsed.hostname in ("arxiv.org", "export.arxiv.org"):
        return parsed.path.startswith("/abs/")
    return True


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = self.description = self.published = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            key = attrs.get("property", attrs.get("name", "")).lower()
            value = attrs.get("content", "")
            if key in ("og:title", "twitter:title") and not self.title:
                self.title = value
            elif key in ("og:description", "description") and not self.description:
                self.description = value
            elif key in ("article:published_time", "datepublished", "pubdate", "citation_date") and not self.published:
                self.published = value
        elif tag == "time" and attrs.get("datetime") and not self.published:
            self.published = attrs["datetime"]


def primary_item(url):
    """Do not publish a community post, an undated document, or an unknown host."""
    if not is_official(url):
        return None
    try:
        parser = Metadata()
        parser.feed(fetch(url).decode("utf-8", errors="replace"))
        if not (parser.title and parser.description and parser.published):
            return None
        host = urllib.parse.urlparse(url).hostname
        return {"title": parser.title, "summary": parser.description, "url": url,
                "published": parser.published, "source_name": host,
                "default_category": "AI Research", "score": 45, "is_primary_source": True}
    except Exception as exc:
        print(f"Discovery source unavailable: {url}: {exc}")
        return None


def discover_links():
    links = set()
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for url in REDDIT_FEEDS:
        try:
            root = ET.fromstring(fetch(url))
            for entry in root.findall("atom:entry", ns)[:20]:
                content = unescape(unescape(ET.tostring(entry, encoding="unicode")))
                for candidate in re.findall(r'https://[^\s"<>]+', content):
                    decoded = urllib.parse.unquote(candidate).rstrip("&;.,)")
                    if is_official(decoded):
                        links.add(decoded)
        except Exception as exc:
            print(f"Discovery feed unavailable: {url}: {exc}")
    try:
        papers = json.loads(fetch("https://huggingface.co/api/daily_papers"))
        for entry in papers[:15]:
            identifier = entry.get("paper", {}).get("id", "")
            if re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", identifier):
                links.add(f"https://arxiv.org/abs/{identifier}")
    except Exception as exc:
        print(f"Hugging Face discovery unavailable: {exc}")
    token = os.getenv("X_BEARER_TOKEN", "").strip()
    if token:
        url = ("https://api.x.com/2/tweets/search/recent?query="
               + urllib.parse.quote("(from:AnthropicAI OR from:OpenAI OR from:OpenAIDevs) has:links -is:retweet")
               + "&tweet.fields=entities&max_results=20")
        try:
            payload = json.loads(fetch(url, {"Authorization": f"Bearer {token}"}))
            for tweet in payload.get("data", []):
                for link in tweet.get("entities", {}).get("urls", []):
                    expanded = link.get("expanded_url", "")
                    if is_official(expanded):
                        links.add(expanded)
        except Exception as exc:
            print(f"X discovery unavailable: {exc}")
    return list(links)


def discover_primary_candidates():
    results = []
    for url in discover_links()[:30]:
        item = primary_item(url)
        if item:
            results.append(item)
    return results
