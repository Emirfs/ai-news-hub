"""
Fetches trending and interesting open-source AI repositories from GitHub.
Saves data to src/data/trending_repos.json for the frontend radar.
"""

import json
import urllib.request
import urllib.parse
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "src" / "data"
REPOS_FILE = DATA_DIR / "trending_repos.json"

SEARCH_QUERIES = [
    {"query": "topic:ai-agents stars:>500", "tag": "Autonomous Agents"},
    {"query": "topic:llm stars:>1000", "tag": "Foundation Models"},
    {"query": "deepseek in:name,description stars:>500", "tag": "DeepSeek Ecosystem"},
    {"query": "robotics foundation model in:name,description stars:>100", "tag": "Robotics & Hardware"},
    {"query": "coding agent in:name,description stars:>300", "tag": "Developer Tools"}
]


def fetch_trending_repos(max_items: int = 8) -> list[dict]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    all_repos = []
    seen_names = set()

    headers = {
        "User-Agent": "NeuralPulseBot/1.0",
        "Accept": "application/vnd.github.v3+json"
    }

    for item in SEARCH_QUERIES:
        q = item["query"]
        url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=4"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            for repo in data.get("items", []):
                full_name = repo["full_name"]
                if full_name in seen_names:
                    continue

                seen_names.add(full_name)
                desc = repo.get("description") or "Open-source artificial intelligence framework and research implementation."
                all_repos.append({
                    "name": full_name,
                    "url": repo["html_url"],
                    "stars": repo.get("stargazers_count", 0),
                    "forks": repo.get("forks_count", 0),
                    "description": desc[:140] + ("..." if len(desc) > 140 else ""),
                    "language": repo.get("language") or "Python",
                    "tag": item["tag"],
                    "owner_avatar": repo.get("owner", {}).get("avatar_url", "")
                })
        except Exception as e:
            print(f"Error fetching repos for query '{q}': {e}")

    # Sort by stars descending
    all_repos.sort(key=lambda x: x["stars"], reverse=True)
    selected = all_repos[:max_items]

    # Save to file
    with open(REPOS_FILE, "w", encoding="utf-8") as f:
        json.dump(selected, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved {len(selected)} trending AI repositories to {REPOS_FILE.name}")
    return selected


if __name__ == "__main__":
    fetch_trending_repos()
