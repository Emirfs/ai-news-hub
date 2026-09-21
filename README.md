# ⚡ Neural Pulse — Autonomous AI & Frontier Tech Chronicle

An autonomous, agent-operated technology newsroom and publication hosted on **GitHub Pages**, powered by **Google Gemini Flash (2.0)**, **Python**, and **Astro**.

---

## 🌐 Overview

**Neural Pulse** monitors, filters, synthesizes, and publishes daily artificial intelligence breakthroughs and weekly intelligence briefings without human intervention.

- **Zero-Cost Serverless Stack**: Runs entirely on free GitHub Actions compute, Google Gemini Flash API tier, and GitHub Pages.
- **High-Signal Data Ingestion**: Scrapes arXiv (cs.AI & cs.LG), Hugging Face Daily Papers, Hacker News AI stream, and frontier lab blogs.
- **AI Editorial Engine**: Google Gemini Flash extracts key technical takeaways, verifies context, and crafts structured Markdown articles.
- **Lightning Fast Static Delivery**: Built with Astro and Tailwind CSS for instant load times, SEO optimization, and native RSS 2.0 syndication.

---

## 🏗️ Architecture

```
   [ arXiv cs.AI / cs.LG ]     [ Hugging Face ]     [ Hacker News AI ]
             │                         │                    │
             └─────────────────────────┼────────────────────┘
                                       │
                                       ▼
                       [ pipeline/ingest.py ]
                          • URL normalization
                          • Deduplication via history.json
                          • Relevance pattern matching
                                       │
                                       ▼
                      [ pipeline/generator.py ]
                          • Gemini 2.0 Flash REST API
                          • Structured JSON schema
                          • Key technical takeaways
                                       │
                                       ▼
                        [ src/content/news/*.md ]
                          • Typed frontmatter schema
                          • Clean markdown sections
                                       │
                                       ▼
                 [ GitHub Actions Workflow Pipeline ]
      Daily News (06:00 UTC) ───► Commit & Push ───► Deploy to GitHub Pages
      Weekly Digest (Sun 18:00) ──► Commit & Push ───► Deploy to GitHub Pages
```

---

## 🚀 Quick Setup & GitHub Deployment

### 1. Push to your GitHub Repository

```bash
cd ai-news-hub
git add .
git commit -m "feat: initial autonomous ai newsroom"
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
git branch -M main
git push -u origin main
```

### 2. Configure GitHub Secret (`GEMINI_API_KEY`)

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. In your GitHub repository, navigate to **Settings** → **Secrets and variables** → **Actions**.
3. Click **New repository secret**.
4. Name: `GEMINI_API_KEY`
5. Secret: Paste your Gemini API key.

### 3. Enable GitHub Pages

1. In your GitHub repository, go to **Settings** → **Pages**.
2. Under **Build and deployment** → **Source**, select **GitHub Actions**.
3. That's it! Every commit and scheduled workflow will automatically publish to `https://<YOUR_USERNAME>.github.io/<YOUR_REPO_NAME>/`.

---

## ⏰ Autonomous Schedules

| Workflow | Schedule | Trigger | Action |
|---|---|---|---|
| **AI Daily News Curator** | Every day at `06:00 UTC` | Cron + Manual `workflow_dispatch` | Collects top 3 AI stories, generates articles, commits to `main` |
| **AI Weekly Digest** | Every Sunday at `18:00 UTC` | Cron + Manual `workflow_dispatch` | Synthesizes recent dispatches into an executive weekly briefing |
| **Deploy to GitHub Pages** | On every push / workflow completion | Automated | Builds Astro static site and publishes to GitHub Pages |

---

## 💻 Local Development

```bash
# 1. Install dependencies
npm install

# 2. Run local development server
npm run dev

# 3. Test the news crawler locally (dry run)
python pipeline/run_pipeline.py --mode daily --count 2 --dry-run

# 4. Generate real articles locally (with or without GEMINI_API_KEY)
# If GEMINI_API_KEY is not set, a structured fallback is generated for offline testing
python pipeline/run_pipeline.py --mode daily --count 1

# 5. Generate weekly digest
python pipeline/run_pipeline.py --mode weekly

# 6. Build static production site
npm run build
```

---

## 📁 Project Structure

```
ai-news-hub/
├── .github/workflows/
│   ├── ai-daily-curator.yml    # Daily cron workflow (06:00 UTC)
│   ├── ai-weekly-digest.yml    # Weekly digest cron workflow (Sundays 18:00 UTC)
│   └── deploy-pages.yml        # GitHub Pages build & deploy workflow
├── pipeline/
│   ├── ingest.py               # Multi-source RSS & Algolia crawler + deduplication
│   ├── generator.py            # Gemini Flash REST client + markdown builder
│   ├── weekly_digest.py        # Weekly briefing synthesizer
│   ├── run_pipeline.py         # Unified CLI orchestrator
│   └── history.json            # Persistent deduplication database
├── src/
│   ├── components/             # NewsCard, LeadStory, Header, Footer
│   ├── content/news/           # Markdown articles with typed frontmatter
│   ├── layouts/                # BaseLayout with SEO tags
│   ├── pages/                  # Home, /news/[...slug], /digests, /categories, /about, /rss.xml
│   ├── styles/global.css       # Tailwind v4 custom editorial styles
│   └── content.config.ts       # Astro Content Collection schema
├── astro.config.mjs            # Astro configuration
└── package.json
```
