"""
Fetches trending and emerging open-source AI repositories from GitHub.
Maintains:
1. src/data/trending_repos.json (Major trending AI projects)
2. src/data/emerging_repos.json (Hidden gems, indie projects with 15-500 stars, recently updated)
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "src" / "data"
TRENDING_FILE = DATA_DIR / "trending_repos.json"
EMERGING_FILE = DATA_DIR / "emerging_repos.json"

HEADERS = {
    "User-Agent": "NeuralPulseBot/1.0",
    "Accept": "application/vnd.github.v3+json"
}


def fetch_trending_repos(max_items: int = 8) -> list[dict]:
    """Fetch high-star trending AI repos."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    all_repos = []
    seen_names = set()

    queries = [
        {"query": "topic:ai-agents stars:>500", "tag": "Autonomous Agents"},
        {"query": "topic:llm stars:>1000", "tag": "Foundation Models"},
        {"query": "deepseek in:name,description stars:>500", "tag": "DeepSeek Ecosystem"},
        {"query": "coding agent in:name,description stars:>300", "tag": "Developer Tools"}
    ]

    for item in queries:
        q = item["query"]
        url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=4"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            for repo in data.get("items", []):
                full_name = repo["full_name"]
                if full_name in seen_names:
                    continue

                seen_names.add(full_name)
                desc = repo.get("description") or "Open-source artificial intelligence framework."
                all_repos.append({
                    "name": full_name,
                    "url": repo["html_url"],
                    "stars": repo.get("stargazers_count", 0),
                    "forks": repo.get("forks_count", 0),
                    "description": desc[:140] + ("..." if len(desc) > 140 else ""),
                    "language": repo.get("language") or "Python",
                    "tag": item["tag"],
                    "pushed_at": (repo.get("pushed_at") or "")[:10]
                })
        except Exception as e:
            print(f"Error fetching trending query '{q}': {e}")

    all_repos.sort(key=lambda x: x["stars"], reverse=True)
    selected = all_repos[:max_items]

    with open(TRENDING_FILE, "w", encoding="utf-8") as f:
        json.dump(selected, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved {len(selected)} trending AI repositories to {TRENDING_FILE.name}")
    return selected


def fetch_emerging_repos(max_items: int = 8) -> list[dict]:
    """
    Fetch hidden gems: actively maintained repositories with 15-500 stars,
    pushed in the last 10 days, allowing indie builders and experimental projects to be discovered.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    all_repos = []
    seen_names = set()

    # Query active projects pushed recently with 15-500 stars
    queries = [
        {"query": "ai agent stars:15..500 pushed:>2026-09-10", "tag": "Experimental Agent"},
        {"query": "llm tool stars:20..400 pushed:>2026-09-10", "tag": "Indie Tool"},
        {"query": "robotics model stars:10..350 pushed:>2026-09-10", "tag": "Embodied AI"},
        {"query": "local ai stars:15..450 pushed:>2026-09-10", "tag": "Local AI"}
    ]

    for item in queries:
        q = item["query"]
        url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}&sort=updated&order=desc&per_page=4"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            for repo in data.get("items", []):
                full_name = repo["full_name"]
                if full_name in seen_names:
                    continue

                seen_names.add(full_name)
                desc = repo.get("description") or "Independent artificial intelligence project and tool."
                all_repos.append({
                    "name": full_name,
                    "url": repo["html_url"],
                    "stars": repo.get("stargazers_count", 0),
                    "forks": repo.get("forks_count", 0),
                    "description": desc[:140] + ("..." if len(desc) > 140 else ""),
                    "language": repo.get("language") or "Python",
                    "tag": item["tag"],
                    "pushed_at": (repo.get("pushed_at") or "")[:10]
                })
        except Exception as e:
            print(f"Error fetching emerging query '{q}': {e}")

    # Sort by pushed_at descending, then stars
    all_repos.sort(key=lambda x: (x.get("pushed_at", ""), x["stars"]), reverse=True)
    selected = all_repos[:max_items]

    with open(EMERGING_FILE, "w", encoding="utf-8") as f:
        json.dump(selected, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved {len(selected)} emerging AI hidden gems to {EMERGING_FILE.name}")
    return selected


def refresh_all_repos():
    fetch_trending_repos(max_items=8)
    fetch_emerging_repos(max_items=8)


if __name__ == "__main__":
    refresh_all_repos()
