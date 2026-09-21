"""
Master autonomous pipeline orchestrator for Neural Pulse.
Supports hourly news cycle, trending repo refresh, and weekly digest compilation.
Maintains README.md and ARCHIVE.md with the latest dispatches and trending repos.
"""

import argparse
import sys
import json
import re
from datetime import datetime, timezone
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.ingest import collect_candidate_news, load_history, save_history
from pipeline.generator import generate_article_from_item, format_markdown_file, create_slug
from pipeline.weekly_digest import generate_weekly_digest, extract_frontmatter
from pipeline.repos import fetch_trending_repos, REPOS_FILE

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "src" / "content" / "news"
README_FILE = REPO_ROOT / "README.md"
ARCHIVE_FILE = REPO_ROOT / "ARCHIVE.md"


def update_readme_and_archive():
    """
    Generates README.md and ARCHIVE.md focusing exclusively on:
    1. What Neural Pulse does (autonomous news publication).
    2. Trending AI repositories.
    3. Latest published news in direct Markdown format.
    """
    if not NEWS_DIR.exists():
        return

    articles = []
    for md_file in NEWS_DIR.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            meta, body = extract_frontmatter(content)
            slug = md_file.stem
            articles.append({
                "slug": slug,
                "file_name": md_file.name,
                "title": meta.get("title", slug),
                "description": meta.get("description", ""),
                "date": meta.get("pubDate", "Unknown"),
                "category": meta.get("category", "General"),
                "source": meta.get("sourceName", "Web"),
                "is_digest": meta.get("isWeeklyDigest", False),
            })
        except Exception as e:
            print(f"Error parsing {md_file.name}: {e}")

    # Sort descending by date, then title
    articles.sort(key=lambda a: (str(a["date"]), a["title"]), reverse=True)

    # Load trending repos
    repos = []
    if REPOS_FILE.exists():
        try:
            with open(REPOS_FILE, "r", encoding="utf-8") as f:
                repos = json.load(f)
        except Exception:
            pass

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    readme_lines = [
        "# ⚡ Neural Pulse — Autonomous AI & Tech News",
        "",
        "> **Ne İşe Yarar:** Neural Pulse, yapay zeka, makine öğrenimi, robotik ve teknoloji dünyasındaki en son gelişmeleri ve trend açık kaynak projeleri her saat başı otonom olarak araştıran, teknik sinyalleri özetleyen ve yayınlayan bağımsız bir AI haber bültenidir.",
        ">",
        f"> **Son Güncelleme:** `{now_iso}` | **Toplam Haber Sayısı:** `{len(articles)}`",
        "",
        "**Yayın Kanalları:**",
        "- 🌐 [Canlı Web Sitesi (Beyaz & Gece Modu)](https://emirfs.github.io/ai-news-hub/)",
        "- 📡 [RSS Beslemesi (XML)](https://emirfs.github.io/ai-news-hub/rss.xml)",
        "",
        "---",
        "",
        "## 🔥 Trend & İlginç Açık Kaynak AI Repoları",
        "",
        "GitHub telemetrisinden saatlik olarak derlenen en popüler ve yenilikçi yapay zeka repoları:",
        "",
        "| Repo Adı | Yıldız | Kategori | Dil | Açıklama |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]

    for r in repos[:6]:
        stars_k = f"★ {r['stars'] / 1000:.1f}k" if r['stars'] >= 1000 else f"★ {r['stars']}"
        desc = r['description'][:90] + ("..." if len(r['description']) > 90 else "")
        readme_lines.append(f"| [{r['name']}]({r['url']}) | `{stars_k}` | {r.get('tag', 'AI')} | `{r.get('language', 'Python')}` | {desc} |")

    readme_lines.extend([
        "",
        "---",
        "",
        "## 📰 En Son Çıkan Haberler (.md Formatında)",
        "",
        "Aşağıdaki listeden haberlerin Markdown kaynak dosyalarını doğrudan GitHub üzerinden okuyabilir veya web sürümüne geçebilirsiniz:",
        "",
        "| Tarih | Kategori | Haber Başlığı (.md Dosyası) | Özet | Canlı Okuma | Kaynak |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ])

    for a in articles:
        md_link = f"[{a['title']}](src/content/news/{a['file_name']})"
        web_link = f"[Web'de Oku](https://emirfs.github.io/ai-news-hub/news/{a['slug']}/)"
        badge = "📋 **[Haftalık Bülten]** " if a["is_digest"] else ""
        short_desc = a["description"].replace("|", "-")[:120] + ("..." if len(a["description"]) > 120 else "")
        readme_lines.append(f"| `{a['date']}` | {a['category']} | {badge}{md_link} | {short_desc} | {web_link} | {a['source']} |")

    readme_lines.append("")
    readme_lines.append("---")
    readme_lines.append("*Tüm haberler otonom yapay zeka ajanı tarafından saatlik olarak derlenir ve Markdown olarak saklanır.*")
    readme_lines.append("")

    full_content = "\n".join(readme_lines)
    README_FILE.write_text(full_content, encoding="utf-8")
    ARCHIVE_FILE.write_text(full_content, encoding="utf-8")
    print(f"✓ Updated README.md and ARCHIVE.md with {len(articles)} articles and {len(repos)} repos.")


def run_daily_pipeline(max_items: int = 2, dry_run: bool = False):
    """Run hourly news discovery, LLM curation, repo refresh, and markdown generation."""
    print("=" * 60)
    print("Starting Neural Pulse Autonomous News Cycle")
    print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print("=" * 60)

    # Refresh trending repos
    try:
        fetch_trending_repos(max_items=8)
    except Exception as e:
        print(f"Warning: Repo refresh error: {e}")

    NEWS_DIR.mkdir(parents=True, exist_ok=True)
    history = load_history()
    seen_urls = set(history.get("seen_urls", []))
    published = history.get("published_articles", [])

    candidates = collect_candidate_news(max_items=max_items)
    if not candidates:
        print("No new candidate articles found in this cycle.")
        update_readme_and_archive()
        return

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    generated_count = 0

    for idx, item in enumerate(candidates, 1):
        print(f"\n[{idx}/{len(candidates)}] Processing: {item['title']}")
        try:
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
                source_url=item['url'],
                source_name=item['source_name'],
                pub_date=today_str
            )

            if dry_run:
                print(f"  [DRY RUN] Would write to: {file_path.name}")
                print(f"  Title: {article['title']}")
                print(f"  Category: {article['category']}")
            else:
                file_path.write_text(md_content, encoding="utf-8")
                print(f"  ✓ Saved dispatch: {file_path.name}")
                seen_urls.add(item['url'])
                published.append({
                    "slug": file_path.stem,
                    "date": today_str,
                    "title": article['title']
                })
                generated_count += 1

        except Exception as e:
            print(f"  ✗ Error generating article for '{item['title']}': {e}")

    if not dry_run:
        if generated_count > 0:
            history["seen_urls"] = list(seen_urls)
            history["published_articles"] = published
            save_history(history)
            print(f"\n✓ Successfully published {generated_count} new dispatches and updated history.json.")
        # Always update README and ARCHIVE
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
        fetch_trending_repos(max_items=8)
        update_readme_and_archive()


if __name__ == "__main__":
    main()
