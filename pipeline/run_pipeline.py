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
import os

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pipeline.ingest import collect_candidate_news, load_history, save_history, parse_publication_date
from pipeline.generator import generate_article_from_item, format_markdown_file, create_slug
from pipeline.weekly_digest import generate_weekly_digest, extract_frontmatter
from pipeline.repos import refresh_all_repos, TRENDING_FILE, EMERGING_FILE

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
            if not meta.get("sourcePolicy") or not meta.get("sourceUrl"):
                continue
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
        "**Guides:** [English](README.en.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [中文](README.zh.md) · [Italiano](README.it.md) · [Deutsch](README.de.md)",
        "",
        "---",
        "",
        "## 🇬🇧 English",
        "",
        "> **What Neural Pulse Does:** Scheduled automation discovers AI news from official sources and publishes source-attributed excerpts.",
        "> Publication dates appear on each story. Source availability is not independent fact-checking.",
        f"> **Index generated:** `{now_iso}` | **Source-linked stories:** `{len(articles)}`",
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
        "### 📰 Source-linked AI stories (direct Markdown)",
        "",
        "| Date | Category | Headline (.md Source) | Source excerpt | Live Web View | Original source |",
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
        "> **Ne İşe Yarar:** Neural Pulse resmî kaynaklardan yapay zekâ haberlerini düzenli tarar ve kaynak bağlantısıyla yayımlar.",
        "> Kaynağa ulaşılması, iddiaların bağımsız doğrulandığı anlamına gelmez.",
        f"> **Dizin oluşturma:** `{now_iso}` | **Yayımlanan haber:** `{len(articles)}`",
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
        "> Neural Pulse consulta fuentes originales y publica resúmenes con enlaces. Las afirmaciones no se verifican de forma independiente.",
        "> Consulte las fechas y fuentes en el [sitio web](https://emirfs.github.io/ai-news-hub/).",
        "",
        "---",
        "",
        "## 🇨🇳 中文",
        "",
        "> Neural Pulse 定期收集原始来源的人工智能新闻，并附上来源链接。内容未经独立事实核查。",
        "> 请在[网站](https://emirfs.github.io/ai-news-hub/)查看每篇报道的发布日期。",
        "",
        "---",
        "",
        "## 🇮🇹 Italiano",
        "",
        "> Neural Pulse raccoglie notizie dalle fonti originali e pubblica estratti attribuiti. Le affermazioni non sono verificate in modo indipendente.",
        "> Controlla date e fonti sul [sito](https://emirfs.github.io/ai-news-hub/).",
        "",
        "---",
        "",
        "## 🇩🇪 Deutsch",
        "",
        "> Neural Pulse sammelt KI-Nachrichten aus Originalquellen und veröffentlicht Auszüge mit Quellenangabe. Die Angaben werden nicht unabhängig geprüft.",
        "> Datum und Quellen stehen auf der [Website](https://emirfs.github.io/ai-news-hub/).",
        "",
        "---",
        "*Stories link to their original sources; source availability does not constitute independent verification.*",
        ""
    ])

    full_content = "\n".join(lines)
    README_FILE.write_text(full_content, encoding="utf-8")
    ARCHIVE_FILE.write_text(full_content, encoding="utf-8")
    print(f"✓ Updated multi-language README.md and ARCHIVE.md with {len(articles)} source-attributed stories.")


def run_daily_pipeline(max_items: int = 2, dry_run: bool = False):
    """Run hourly news discovery, LLM curation, repo refresh, broadcasting, and markdown generation."""
    print("=" * 60)
    print("Starting Neural Pulse Autonomous News Cycle")
    print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print("=" * 60)

    if not dry_run:
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
        print("No new eligible official-source stories found in this cycle.")
        if not dry_run:
            update_readme_and_archive()
        return

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    generated_count = 0

    for idx, item in enumerate(candidates, 1):
        print(f"\n[{idx}/{len(candidates)}] Processing: {item['title']}")
        

        try:
            item["key"] = os.environ.get("GEMINI_API_KEY", "")
            item["model"] = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
            article = generate_article_from_item(item)
            slug_base = create_slug(article['title'])
            slug = f"{today_str}-{slug_base}"
            file_path = NEWS_DIR / f"{slug}.md"

            counter = 1
            while file_path.exists():
                file_path = NEWS_DIR / f"{slug}-{counter}.md"
                counter += 1

            md_content = format_markdown_file(
                article=article,
                pub_date=parse_publication_date(item["published"]).strftime("%Y-%m-%d"),
                source_url=item["url"],
                source_name=item["source_name"],
            )

            if dry_run:
                print(f"  [DRY RUN] Would write to: {file_path.name}")
                print(f"  Title: {article['title']}")
            else:
                file_path.write_text(md_content, encoding="utf-8")
                print(f"  ✓ Saved source-attributed story: {file_path.name}")
                seen_urls.add(item['url'])
                published.append({"slug": file_path.stem, "date": today_str, "title": article['title']})
                generated_count += 1
        except Exception as e:
            print(f"  ✗ Error generating article for '{item['title']}': {e}")

    if not dry_run:
        if generated_count > 0:
            history["seen_urls"] = list(seen_urls)
            history["published_articles"] = published
            save_history(history)
            print(f"\n✓ Published {generated_count} source-attributed stories and updated history.json.")
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
