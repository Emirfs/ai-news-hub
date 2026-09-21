"""
Master autonomous pipeline orchestrator for Neural Pulse.
Supports hourly news cycle, trending and emerging repo refresh,
multi-lingual README generation, and automated Discord/Telegram broadcasting.
"""

import argparse
import sys
import json
import re
from datetime import datetime, timezone
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.ingest import collect_candidate_news, load_history, save_history, verify_live_url
from pipeline.generator import generate_article_from_item, format_markdown_file, create_slug
from pipeline.weekly_digest import generate_weekly_digest, extract_frontmatter
from pipeline.repos import refresh_all_repos, TRENDING_FILE, EMERGING_FILE
from pipeline.translate_articles import generate_multilingual_metadata
from pipeline.translate_full_articles import generate_full_translated_body
from pipeline.broadcast import broadcast_to_discord, broadcast_to_telegram, SITE_URL

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "src" / "content" / "news"
README_FILE = REPO_ROOT / "README.md"
ARCHIVE_FILE = REPO_ROOT / "ARCHIVE.md"

SUBMIT_ISSUE_URL = "https://github.com/Emirfs/ai-news-hub/issues/new?title=%5BProject+Submission%5D+Your+AI+Repo&body=%2A%2ARepository+URL%3A%2A%2A+https%3A%2F%2Fgithub.com%2F...%0A%2A%2AProject+Description%3A%2A%2A+What+does+your+AI+project+do%3F"


def update_readme_and_archive():
    """
    Generates multi-lingual README.md with English prominently FIRST,
    followed by Turkish, Spanish, Chinese, Italian, and German options.
    """
    if not NEWS_DIR.exists():
        return

    articles = []
    for md_file in NEWS_DIR.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            meta, body = extract_frontmatter(content)
            slug = md_file.stem
            
            trans_match = re.search(r"translations:\s*(\{.*?\})\n---", content, re.DOTALL)
            translations = {}
            if trans_match:
                try:
                    translations = json.loads(trans_match.group(1))
                except Exception:
                    pass

            articles.append({
                "slug": slug,
                "file_name": md_file.name,
                "title": meta.get("title", slug),
                "description": meta.get("description", ""),
                "date": meta.get("pubDate", "Unknown"),
                "category": meta.get("category", "General"),
                "source": meta.get("sourceName", "Primary Wire"),
                "source_url": meta.get("sourceUrl", ""),
                "is_digest": meta.get("isWeeklyDigest", False),
                "translations": translations
            })
        except Exception as e:
            print(f"Error parsing {md_file.name}: {e}")

    articles.sort(key=lambda a: (str(a["date"]), a["title"]), reverse=True)

    trending_repos = []
    if TRENDING_FILE.exists():
        try:
            with open(TRENDING_FILE, "r", encoding="utf-8") as f:
                trending_repos = json.load(f)
        except Exception:
            pass

    emerging_repos = []
    if EMERGING_FILE.exists():
        try:
            with open(EMERGING_FILE, "r", encoding="utf-8") as f:
                emerging_repos = json.load(f)
        except Exception:
            pass

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# ⚡ Neural Pulse — Autonomous AI & Tech News",
        "",
        "**Languages / Diller / Idiomas / 语言:** [ 🇬🇧 English (Default)](#-english) • [ 🇹🇷 Türkçe](#-türkçe) • [ 🇪🇸 Español](#-español) • [ 🇨🇳 中文](#-中文) • [ 🇮🇹 Italiano](#-italiano) • [ 🇩🇪 Deutsch](#-deutsch)",
        "",
        "---",
        "",
        "## 🇬🇧 English",
        "",
        "> **What Neural Pulse Does:** Neural Pulse is an autonomous technology journal monitoring, verifying, and publishing breaking developments across artificial intelligence, foundation models, robotics, and open-source software every hour.",
        ">",
        f"> **Last Synced:** `{now_iso}` | **Total Verified Dispatches:** `{len(articles)}`",
        "",
        "**Publication Outlets:**",
        "- 🌐 [Live Web Publication (White Mode & Dark Mode)](https://emirfs.github.io/ai-news-hub/)",
        "- 📡 [RSS 2.0 Syndication Feed](https://emirfs.github.io/ai-news-hub/rss.xml)",
        "",
        "### 🔥 Trending & Novel Open-Source AI Repositories",
        "",
        "Curated hourly from GitHub telemetry across agents, foundation models, and developer tools:",
        "",
        "| Repository | Stars | Category | Language | Description |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]

    for r in trending_repos[:5]:
        stars_k = f"★ {r['stars'] / 1000:.1f}k" if r['stars'] >= 1000 else f"★ {r['stars']}"
        desc = r['description'][:90] + ("..." if len(r['description']) > 90 else "")
        lines.append(f"| [{r['name']}]({r['url']}) | `{stars_k}` | {r.get('tag', 'AI')} | `{r.get('language', 'Python')}` | {desc} |")

    lines.extend([
        "",
        "### 🚀 Emerging AI & Community Launchpad (<500 Stars)",
        "",
        f"> 💡 **Submit your independent AI project:** [Open a submission issue on GitHub]({SUBMIT_ISSUE_URL}).",
        "",
        "| Repository | Stars | Last Commit | Category | Language | Description |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ])

    for r in emerging_repos[:5]:
        desc = r['description'][:85] + ("..." if len(r['description']) > 85 else "")
        lines.append(f"| [{r['name']}]({r['url']}) | `★ {r['stars']}` | `{r.get('pushed_at', 'Recent')}` | {r.get('tag', 'Indie')} | `{r.get('language', 'Python')}` | {desc} |")

    lines.extend([
        "",
        "### 📰 Latest AI News Dispatches (Direct Markdown)",
        "",
        "| Date | Category | Headline (.md Source) | Executive Briefing | Live Web View | Primary Source |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ])

    for a in articles:
        md_link = f"[{a['title']}](src/content/news/{a['file_name']})"
        web_link = f"[Read Online](https://emirfs.github.io/ai-news-hub/news/{a['slug']}/)"
        badge = "📋 **[Digest]** " if a["is_digest"] else ""
        short_desc = a["description"].replace("|", "-")[:115] + ("..." if len(a["description"]) > 115 else "")
        lines.append(f"| `{a['date']}` | {a['category']} | {badge}{md_link} | {short_desc} | {web_link} | [{a['source']}]({a['source_url']}) |")

    # TURKISH SECTION
    lines.extend([
        "",
        "---",
        "",
        "## 🇹🇷 Türkçe",
        "",
        "> **Ne İşe Yarar:** Neural Pulse, yapay zeka, makine öğrenimi, robotik ve teknoloji dünyasındaki en son gelişmeleri ve bağımsız açık kaynak projeleri her saat başı otonom olarak araştıran, teknik sinyalleri özetleyen ve yayınlayan bağımsız bir AI haber bültenidir.",
        ">",
        f"> **Son Güncelleme:** `{now_iso}` | **Doğrulanmış Haber Sayısı:** `{len(articles)}`",
        "",
        "**Yayın Kanalları:**",
        "- 🌐 [Canlı Web Sitesi (Beyaz Mod & Gece Modu)](https://emirfs.github.io/ai-news-hub/)",
        "- 📡 [RSS Beslemesi (XML)](https://emirfs.github.io/ai-news-hub/rss.xml)",
        "",
        "### 📰 En Son Çıkan Haberler (.md Formatında)",
        "",
        "| Tarih | Kategori | Haber Başlığı (.md Dosyası) | Özet | Canlı Okuma | Orijinal Kaynak |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ])

    for a in articles:
        tr_title = a["title"]
        tr_desc = a["description"]
        if a.get("translations") and a["translations"].get("tr"):
            tr_title = a["translations"]["tr"].get("title", tr_title)
            tr_desc = a["translations"]["tr"].get("description", tr_desc)

        md_link = f"[{tr_title}](src/content/news/{a['file_name']})"
        web_link = f"[Web'de Oku](https://emirfs.github.io/ai-news-hub/news/{a['slug']}/)"
        badge = "📋 **[Haftalık Bülten]** " if a["is_digest"] else ""
        short_desc = tr_desc.replace("|", "-")[:115] + ("..." if len(tr_desc) > 115 else "")
        lines.append(f"| `{a['date']}` | {a['category']} | {badge}{md_link} | {short_desc} | {web_link} | [{a['source']}]({a['source_url']}) |")

    lines.extend([
        "",
        "---",
        "",
        "## 🇪🇸 Español",
        "",
        "> **Propósito:** Neural Pulse es una publicación tecnológica autónoma que monitorea, verifica y publica avances de última hora en inteligencia artificial y modelos abiertos cada hora.",
        "> Consulta el [sitio web en vivo](https://emirfs.github.io/ai-news-hub/) para leer despachos traducidos al español con un solo clic.",
        "",
        "---",
        "",
        "## 🇨🇳 中文",
        "",
        "> **关于我们：** Neural Pulse 是一个每小时自主运行的人工智能前沿快讯平台，实时跟踪大语言模型、开源智能体与具身智能突破。",
        "> 访问 [在线新闻网站](https://emirfs.github.io/ai-news-hub/) 可一键切换中文阅读模式并查阅所有原始技术文档。",
        "",
        "---",
        "",
        "## 🇮🇹 Italiano",
        "",
        "> **Scopo:** Neural Pulse è una pubblicazione tecnologica autonoma che monitora e riporta ogni ora le ultime novità sull'intelligenza artificiale e sulla robotica open source.",
        "> Visita il [sito web online](https://emirfs.github.io/ai-news-hub/) per leggere le analisi in italiano.",
        "",
        "---",
        "",
        "## 🇩🇪 Deutsch",
        "",
        "> **Überblick:** Neural Pulse ist ein autonomes Technologie-Journal, das stündlich die neuesten Entwicklungen in künstlicher Intelligenz, Robotik und Open-Source-Modellen zusammenfasst.",
        "> Besuchen Sie die [Live-Website](https://emirfs.github.io/ai-news-hub/) für tiefe Analysen und Direktquellen.",
        "",
        "---",
        "*All news stories are autonomously compiled and backed by verified HTTP 200 source URLs.*",
        ""
    ])

    full_content = "\n".join(lines)
    README_FILE.write_text(full_content, encoding="utf-8")
    ARCHIVE_FILE.write_text(full_content, encoding="utf-8")
    print(f"✓ Updated multi-language README.md and ARCHIVE.md with {len(articles)} verified dispatches.")


def run_daily_pipeline(max_items: int = 2, dry_run: bool = False):
    """Run hourly news discovery, LLM curation, repo refresh, broadcasting, and markdown generation."""
    print("=" * 60)
    print("Starting Neural Pulse Autonomous News Cycle")
    print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print("=" * 60)

    try:
        refresh_all_repos()
    except Exception as e:
        print(f"Warning: Repo refresh error: {e}")

    NEWS_DIR.mkdir(parents=True, exist_ok=True)
    history = load_history()
    seen_urls = set(history.get("seen_urls", []))
    published = history.get("published_articles", [])

    candidates = collect_candidate_news(max_items=max_items)
    if not candidates:
        print("No new verified candidate articles found in this cycle.")
        update_readme_and_archive()
        return

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    generated_count = 0

    for idx, item in enumerate(candidates, 1):
        print(f"\n[{idx}/{len(candidates)}] Processing: {item['title']}")
        
        if not verify_live_url(item['url']):
            print(f"  ✗ Rejecting item with dead URL: {item['url']}")
            continue

        try:
            article = generate_article_from_item(item)
            slug_base = create_slug(article['title'])
            slug = f"{today_str}-{slug_base}"
            file_path = NEWS_DIR / f"{slug}.md"

            counter = 1
            while file_path.exists():
                file_path = NEWS_DIR / f"{slug}-{counter}.md"
                counter += 1

            # Generate multi-language metadata and full-body translations
            multi_trans = generate_multilingual_metadata(article)
            for lang in ["tr", "es", "zh", "de", "it"]:
                if lang in multi_trans:
                    multi_trans[lang]["body_html"] = generate_full_translated_body(article["title"], item["source_name"], lang)
            article["translations"] = multi_trans

            md_content = format_markdown_file(
                article=article,
                source_url=item['url'],
                source_name=item['source_name'],
                pub_date=today_str
            )

            # Append translations to frontmatter
            trans_yaml = json.dumps(multi_trans, ensure_ascii=False, indent=2)
            md_content = re.sub(
                r"(---\s*\n)(.*?)(\n---)",
                r"\1\2" + f"\ntranslations: {trans_yaml}" + r"\3",
                md_content,
                flags=re.DOTALL
            )

            if dry_run:
                print(f"  [DRY RUN] Would write to: {file_path.name}")
                print(f"  Title: {article['title']}")
            else:
                file_path.write_text(md_content, encoding="utf-8")
                print(f"  ✓ Saved verified dispatch: {file_path.name}")
                seen_urls.add(item['url'])
                published.append({
                    "slug": file_path.stem,
                    "date": today_str,
                    "title": article['title']
                })
                generated_count += 1

                # Broadcast to external channels if configured
                article_public_url = f"{SITE_URL}/news/{file_path.stem}/"
                broadcast_to_discord(article, article_public_url)
                broadcast_to_telegram(article, article_public_url)

        except Exception as e:
            print(f"  ✗ Error generating article for '{item['title']}': {e}")

    if not dry_run:
        if generated_count > 0:
            history["seen_urls"] = list(seen_urls)
            history["published_articles"] = published
            save_history(history)
            print(f"\n✓ Successfully published {generated_count} new dispatches and updated history.json.")
        update_readme_and_archive()


def main():
    parser = argparse.ArgumentParser(description="Neural Pulse AI Newsroom Pipeline")
    parser.add_argument("--mode", choices=["daily", "weekly", "archive", "repos"], default="daily", help="Pipeline execution mode")
    parser.add_argument("--count", type=int, default=2, help="Max articles to generate in daily mode")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without writing files")

    args = parser.parse_args()

    if args.mode == "daily":
        run_daily_pipeline(max_items=args.count, dry_run=args.dry_run)
    elif args.mode == "weekly":
        generate_weekly_digest()
        update_readme_and_archive()
    elif args.mode == "archive":
        update_readme_and_archive()
    elif args.mode == "repos":
        refresh_all_repos()
        update_readme_and_archive()


if __name__ == "__main__":
    main()
