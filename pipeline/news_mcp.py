"""Read-only MCP stdio server exposing the public Neural Pulse RSS feed.

Run: python -m pipeline.news_mcp
Set NEWS_RSS_URL to use another deployment of this site's RSS feed.
"""

import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from html import unescape

RSS_URL = os.getenv("NEWS_RSS_URL", "https://emirfs.github.io/ai-news-hub/rss.xml")
SITE_URL = RSS_URL.removesuffix("rss.xml")


def latest(limit=5, query=""):
    """Fetch current published items; never claim they were independently verified."""
    request = urllib.request.Request(RSS_URL, headers={"User-Agent": "NeuralPulseMCP/1.0"})
    with urllib.request.urlopen(request, timeout=12) as response:
        body = response.read(2_000_001)
    if len(body) > 2_000_000:
        raise ValueError("RSS feed is too large")
    root = ET.fromstring(body)
    if root.findtext("./channel/title") != "Neural Pulse | Source-linked AI news":
        raise ValueError("The deployed RSS feed has not switched to source-linked articles yet")
    items = []
    for item in root.findall("./channel/item"):
        title = unescape(item.findtext("title", "")).strip()
        description = unescape(item.findtext("description", "")).strip()
        link = (item.findtext("link", "") or "").strip()
        date = (item.findtext("pubDate", "") or "").strip()
        if not title or not link.startswith((SITE_URL, "https://emirfs.github.io/ai-news-hub/news/")):
            continue
        if query.casefold() not in (title + " " + description).casefold():
            continue
        try:
            published = parsedate_to_datetime(date).isoformat()
        except (TypeError, ValueError):
            published = date
        items.append({"title": title, "description": description, "published": published, "url": link})
        if len(items) >= limit:
            break
    return items


def reply(message):
    sys.stdout.write(json.dumps(message, ensure_ascii=False, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def dispatch(request):
    method = request.get("method")
    if "id" not in request:
        return
    rid = request["id"]
    try:
        if method == "initialize":
            result = {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}, "resources": {}}, "serverInfo": {"name": "neural-pulse-news", "version": "1.0.0"}}
        elif method == "ping":
            result = {}
        elif method == "tools/list":
            result = {"tools": [{"name": "latest_news", "description": "Get source-attributed AI news from Neural Pulse, with dates and article links. Not independently fact-checked.", "inputSchema": {"type": "object", "properties": {"limit": {"type": "integer", "minimum": 1, "maximum": 20}, "query": {"type": "string"}}}}]}
        elif method == "tools/call":
            if request.get("params", {}).get("name") != "latest_news":
                raise ValueError("Unknown tool")
            args = request.get("params", {}).get("arguments") or {}
            limit = args.get("limit", 5)
            query = args.get("query", "")
            if type(limit) is not int or not 1 <= limit <= 20 or not isinstance(query, str):
                raise ValueError("Invalid limit or query")
            result = {"content": [{"type": "text", "text": json.dumps({"notice": "Source-attributed; not independently fact-checked.", "articles": latest(limit, query)}, ensure_ascii=False)}]}
        elif method == "resources/list":
            result = {"resources": [{"uri": RSS_URL, "name": "Neural Pulse RSS", "mimeType": "application/rss+xml", "description": "Public AI news feed"}]}
        elif method == "resources/read":
            if request.get("params", {}).get("uri") != RSS_URL:
                raise ValueError("Unknown resource")
            request = urllib.request.Request(RSS_URL, headers={"User-Agent": "NeuralPulseMCP/1.0"})
            with urllib.request.urlopen(request, timeout=12) as response:
                body = response.read(2_000_001)
            if len(body) > 2_000_000:
                raise ValueError("RSS feed is too large")
            if ET.fromstring(body).findtext("./channel/title") != "Neural Pulse | Source-linked AI news":
                raise ValueError("The deployed RSS feed has not switched to source-linked articles yet")
            result = {"contents": [{"uri": RSS_URL, "mimeType": "application/rss+xml", "text": body.decode("utf-8")}]}
        else:
            reply({"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "Method not found"}})
            return
        reply({"jsonrpc": "2.0", "id": rid, "result": result})
    except Exception as exc:
        reply({"jsonrpc": "2.0", "id": rid, "error": {"code": -32000, "message": str(exc)}})


def main():
    for line in sys.stdin:
        try:
            dispatch(json.loads(line))
        except (json.JSONDecodeError, TypeError) as exc:
            reply({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(exc)}})


if __name__ == "__main__":
    main()
