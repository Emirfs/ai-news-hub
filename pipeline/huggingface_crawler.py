"""
Hugging Face Crawler for Neural Pulse.
Monitors:
1. Trending AI models (trendingScore)
2. Most downloaded newly popular models (downloads)
3. Hugging Face Daily Papers (top community-curated arXiv papers)
"""

import json
import urllib.request
from pathlib import Path

HEADERS = {
    "User-Agent": "NeuralPulseBot/1.0 (+https://github.com/Emirfs/ai-news-hub)"
}


def fetch_hf_trending_models(limit: int = 6) -> list[dict]:
    """Fetch top trending AI models on Hugging Face."""
    url = f"https://huggingface.co/api/models?sort=trendingScore&direction=-1&limit={limit}"
    candidates = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as resp:
            models = json.loads(resp.read().decode("utf-8"))

        for m in models:
            model_id = m.get("id", "")
            if not model_id:
                continue

            downloads = m.get("downloads", 0)
            likes = m.get("likes", 0)
            pipeline = m.get("pipeline_tag") or "machine-learning"

            # Filter high-interest models
            if likes < 20 and downloads < 500:
                continue

            title = f"Hugging Face Trending Release: {model_id} ({pipeline})"
            summary = (
                f"Model {model_id} has gained rapid community traction on Hugging Face with "
                f"{likes:,} likes and {downloads:,} downloads. Task architecture: {pipeline}."
            )
            target_url = f"https://huggingface.co/{model_id}"

            candidates.append({
                "title": title,
                "url": target_url,
                "summary": summary,
                "source_name": "Hugging Face Model Hub",
                "default_category": "Open Source AI",
                "score": likes + min(50, downloads // 1000)
            })
    except Exception as e:
        print(f"HF Trending Models fetch note: {e}")

    return candidates


def fetch_hf_daily_papers(limit: int = 6) -> list[dict]:
    """Fetch top community-curated research papers from Hugging Face Daily Papers."""
    url = "https://huggingface.co/api/daily_papers"
    candidates = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as resp:
            papers = json.loads(resp.read().decode("utf-8"))

        for item in papers[:limit]:
            paper = item.get("paper", {})
            title = paper.get("title", "")
            arxiv_id = paper.get("id", "")
            summary = paper.get("summary", "") or f"High-signal AI preprint published on arXiv ({arxiv_id})."
            upvotes = item.get("upvotes", 0)

            if not title or not arxiv_id:
                continue

            target_url = f"https://arxiv.org/abs/{arxiv_id}"

            candidates.append({
                "title": f"Hugging Face Daily Research: {title}",
                "url": target_url,
                "summary": summary[:1200],
                "source_name": "Hugging Face Daily Papers",
                "default_category": "AI Research",
                "score": upvotes + 30
            })
    except Exception as e:
        print(f"HF Daily Papers fetch note: {e}")

    return candidates


def get_all_huggingface_candidates(max_items: int = 6) -> list[dict]:
    """Aggregates trending models and curated papers from Hugging Face."""
    models = fetch_hf_trending_models(limit=6)
    papers = fetch_hf_daily_papers(limit=6)
    combined = models + papers
    combined.sort(key=lambda x: x.get("score", 0), reverse=True)
    return combined[:max_items]


if __name__ == "__main__":
    candidates = get_all_huggingface_candidates()
    print(f"Collected {len(candidates)} Hugging Face candidates:")
    for c in candidates:
        print(f"- {c['title']} -> {c['url']}")
