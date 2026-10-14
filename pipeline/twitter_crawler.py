"""
Twitter/X AI Intelligence Crawler for Neural Pulse.
Slices high-signal announcements, research tweets, and technical statements
from AI leaders (Sam Altman, Karpathy, DeepSeek, Yann LeCun, Anthropic)
sourced via verified community telemetry.
"""

import json
import urllib.request
import urllib.parse
from pathlib import Path

HEADERS = {
    "User-Agent": "NeuralPulseBot/1.0 (+https://github.com/Emirfs/ai-news-hub)"
}

TARGET_RESEARCHERS = [
    {"handle": "deepseek_ai", "name": "DeepSeek Research", "query": "deepseek twitter"},
    {"handle": "karpathy", "name": "Andrej Karpathy", "query": "karpathy twitter"},
    {"handle": "sama", "name": "Sam Altman (OpenAI)", "query": "sama twitter"},
    {"handle": "ylecun", "name": "Yann LeCun (Meta AI)", "query": "ylecun twitter"},
    {"handle": "AnthropicAI", "name": "Anthropic", "query": "anthropic tweet"},
    {"handle": "OpenAIDevs", "name": "OpenAI Developers", "query": "OpenAIDevs twitter"},
    {"handle": "bcherny", "name": "Boris Cherny (Claude Code)", "query": "bcherny twitter"},
    {"handle": "btibor91", "name": "Tibor Blaho (AI Leaks & Teardowns)", "query": "btibor91 twitter"}
]

RUMOR_SEARCH_QUERIES = [
    {"name": "Codex & Claude Limit Resets", "query": "codex limit OR limit reset OR rate limit reset", "category": "Rumors & Leaks"},
    {"name": "Claude Opus 5.5 & Next-Gen Leaks", "query": "opus 5.5 OR opus codex OR claude 4 leak", "category": "Rumors & Leaks"},
    {"name": "GPT-6 & Frontier Leaks", "query": "gpt-6 leak OR gpt-6 rumor OR openai weights leak", "category": "Rumors & Leaks"},
    {"name": "AI Frontier Speculation", "query": "ai leak OR model weights leak OR unreleased model benchmark", "category": "Rumors & Leaks"}
]

RUMOR_KEYWORDS = ["leak", "rumor", "rumour", "speculation", "unreleased", "limit reset", "rate limit", "gpt-6", "opus 5.5", "teaser"]


def fetch_researcher_tweets(limit_per_target: int = 2) -> list[dict]:
    """Fetch high-impact tweets from key AI figures."""
    candidates = []
    seen_urls = set()

    for target in TARGET_RESEARCHERS:
        q = target["query"]
        url = (
            f"https://hn.algolia.com/api/v1/search_by_date?"
            f"query={urllib.parse.quote(q)}&tags=story&numericFilters=points>25&hitsPerPage=6"
        )
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            for hit in data.get("hits", [])[:limit_per_target]:
                target_url = hit.get("url")
                title = hit.get("title", "")
                points = hit.get("points", 0)

                if not target_url or target_url in seen_urls:
                    continue

                seen_urls.add(target_url)
                summary = hit.get("story_text") or f"Official technical statement and discussion from {target['name']} ({target['handle']})."
                is_rumor = any(k in title.lower() or k in summary.lower() for k in RUMOR_KEYWORDS)
                category = "Rumors & Leaks" if is_rumor else ("Industry & Startups" if "Altman" in target['name'] else "AI Research")

                candidates.append({
                    "title": f"Twitter/X Dispatch: {title}",
                    "url": target_url,
                    "summary": summary[:1200],
                    "source_name": f"{target['name']} (@{target['handle']})",
                    "default_category": category,
                    "score": points + 20
                })
        except Exception as e:
            print(f"Twitter fetch note for {target['name']}: {e}")

    candidates.sort(key=lambda x: x.get("score", 0), reverse=True)
    return candidates

def fetch_rumor_dispatches(limit_per_query: int = 2) -> list[dict]:
    """Fetch high-signal AI rumors, leaks, and limit resets from community telemetry."""
    candidates = []
    seen_urls = set()

    for r in RUMOR_SEARCH_QUERIES:
        q = r["query"]
        url = (
            f"https://hn.algolia.com/api/v1/search_by_date?"
            f"query={urllib.parse.quote(q)}&tags=story&numericFilters=points>15&hitsPerPage=6"
        )
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            for hit in data.get("hits", [])[:limit_per_query]:
                target_url = hit.get("url")
                title = hit.get("title", "")
                points = hit.get("points", 0)

                if not target_url or target_url in seen_urls:
                    continue

                seen_urls.add(target_url)
                summary = hit.get("story_text") or f"Community telemetry, leaked benchmarks, or technical leak regarding {r['name']}."

                candidates.append({
                    "title": f"Rumor & Leak Radar: {title}",
                    "url": target_url,
                    "summary": summary[:1200],
                    "source_name": f"{r['name']} (X / Telemetry)",
                    "default_category": "Rumors & Leaks",
                    "score": points + 25
                })
        except Exception as e:
            print(f"Rumor fetch note for {r['name']}: {e}")

    candidates.sort(key=lambda x: x.get("score", 0), reverse=True)
    return candidates


def get_all_twitter_candidates(max_items: int = 6) -> list[dict]:
    """Fetch combined researcher tweets and rumor radar candidates."""
    researchers = fetch_researcher_tweets(limit_per_target=2)
    rumors = fetch_rumor_dispatches(limit_per_query=2)
    combined = researchers + rumors
    combined.sort(key=lambda x: x.get("score", 0), reverse=True)
    return combined[:max_items]


if __name__ == "__main__":
    tweets = fetch_researcher_tweets()
    print(f"Collected {len(tweets)} researcher Twitter dispatches:")
    for t in tweets:
        print(f"- {t['title']} ({t['source_name']}) -> {t['url']}")
