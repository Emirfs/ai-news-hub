# Neural Pulse — English

[Website](https://emirfs.github.io/ai-news-hub/) · [RSS](https://emirfs.github.io/ai-news-hub/rss.xml) · [Türkçe](README.tr.md) · [Español](README.es.md) · [中文](README.zh.md) · [Italiano](README.it.md) · [Deutsch](README.de.md)

Neural Pulse collects recent AI stories from official sources. Scheduled GitHub Actions runs at minutes 17 and 47 each hour; GitHub may delay or skip scheduled runs. The website updates only after a successful commit and Pages deployment. Your PC does not need to stay on.

## Sources and accuracy

Official Anthropic and OpenAI announcements, arXiv, Hugging Face Blog, and NVIDIA feeds supply dated items. Reddit RSS, Hugging Face daily papers, and optional X API searches discover additional links. Community posts are **not** published as verified news: only dated official linked pages qualify. Some sites may block requests or omit publication dates; those stories are skipped. A reachable source does not prove its factual claims. Older archive entries were produced under different rules; read their primary sources critically.

Gemini may extract sentences from a source excerpt when `GEMINI_API_KEY` is set. Otherwise the excerpt is retained. Never treat generated summaries as independent fact-checking. The pipeline runs locally with `python -m pipeline.run_pipeline --mode daily --count 2 --dry-run`; omit `--dry-run` to write articles. Configure `X_BEARER_TOKEN` as a GitHub Actions secret to enable X discovery; Reddit may return HTTP 429. No local credentials are required for public feeds.

## Terminal access

The read-only MCP server exposes `latest_news` with `limit` and `query`, and the public RSS resource. Run `python -m pipeline.news_mcp`. In OMP opened from this repository, `.omp/mcp.json` registers the server. Other MCP clients can configure a stdio command `python -m pipeline.news_mcp` with `cwd` set to this repository's absolute path. This server fetches the public RSS URL; it cannot publish stories.

The project-local OMP extension `.omp/extensions/news.ts` polls RSS every 15 minutes while an OMP session is active. It shows new headlines with article links and provides `/news`. Notifications do not appear while OMP is closed, and terminal URL clicking depends on the terminal. Restart OMP after enabling the extension. No global profile settings are changed.
