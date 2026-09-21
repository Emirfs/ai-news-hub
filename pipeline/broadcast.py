"""
Automated broadcaster for Neural Pulse.
Broadcasts newly published dispatches to Discord webhooks, Telegram channels,
and provides 1-click submission links for Hacker News, Reddit, and X.
"""

import json
import os
import urllib.request
import urllib.parse
from pathlib import Path

SITE_URL = "https://emirfs.github.io/ai-news-hub"
REPO_URL = "https://github.com/Emirfs/ai-news-hub"


def broadcast_to_discord(article: dict, article_url: str):
    """Broadcasts article to Discord webhook if DISCORD_WEBHOOK_URL is configured."""
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook_url:
        return

    payload = {
        "username": "Neural Pulse Wire",
        "avatar_url": "https://raw.githubusercontent.com/Emirfs/ai-news-hub/main/public/favicon.svg",
        "embeds": [
            {
                "title": f"⚡ {article['title']}",
                "url": article_url,
                "description": article['description'],
                "color": 12196636,  # Dark red / amber
                "fields": [
                    {
                        "name": "Category",
                        "value": article.get("category", "AI & Tech"),
                        "inline": True
                    },
                    {
                        "name": "Primary Source",
                        "value": f"[{article.get('sourceName', 'Original Source')}]({article.get('sourceUrl', SITE_URL)})",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "Neural Pulse • Autonomous AI Newsroom"
                }
            }
        ]
    }

    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "NeuralPulseBot/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print("✓ Broadcasted dispatch to Discord.")
    except Exception as e:
        print(f"Discord broadcast note: {e}")


def broadcast_to_telegram(article: dict, article_url: str):
    """Broadcasts article to Telegram channel if TELEGRAM_BOT_TOKEN is configured."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not bot_token or not chat_id:
        return

    text = (
        f"⚡ <b>{article['title']}</b>\n\n"
        f"{article['description']}\n\n"
        f"🏷 <i>{article.get('category', 'AI & Tech')}</i>\n"
        f"🔗 <a href='{article_url}'>Full Analysis</a> | "
        f"<a href='{article.get('sourceUrl', SITE_URL)}'>Primary Source</a>\n"
        f"#AI #NeuralPulse"
    )

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print("✓ Broadcasted dispatch to Telegram.")
    except Exception as e:
        print(f"Telegram broadcast note: {e}")


def get_social_share_links() -> dict:
    """Returns pre-filled 1-click submission URLs for major developer platforms."""
    hn_title = "Show HN: Neural Pulse – Autonomous AI & tech newsroom on GitHub Pages"
    hn_url = f"https://news.ycombinator.com/submitlink?u={urllib.parse.quote(SITE_URL)}&t={urllib.parse.quote(hn_title)}"

    reddit_title = "I built an autonomous, zero-cost AI newsroom running on GitHub Actions and Gemini"
    reddit_url = f"https://www.reddit.com/r/SideProject/submit?title={urllib.parse.quote(reddit_title)}&url={urllib.parse.quote(SITE_URL)}"

    x_text = f"Announcing Neural Pulse: The autonomous AI & frontier tech newsroom running on GitHub Actions & Gemini Flash.\n\n🌐 {SITE_URL}\n📡 {REPO_URL}\n\n#AI #OpenSource"
    x_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(x_text)}"

    return {
        "hacker_news": hn_url,
        "reddit": reddit_url,
        "x": x_url
    }


if __name__ == "__main__":
    links = get_social_share_links()
    print("Pre-filled promotional launch links:")
    print("Hacker News:", links["hacker_news"])
    print("Reddit:", links["reddit"])
    print("X:", links["x"])
