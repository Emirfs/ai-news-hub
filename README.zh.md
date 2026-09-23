# Neural Pulse — 中文

[网站](https://emirfs.github.io/ai-news-hub/) · [RSS](https://emirfs.github.io/ai-news-hub/rss.xml) · [English](README.en.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Deutsch](README.de.md)

Neural Pulse 从官方来源收集人工智能新闻。GitHub Actions 每小时在第 17 和 47 分钟尝试运行。GitHub 可能延迟或跳过定时任务。只有成功提交并完成 Pages 部署后，网站才会更新。你的电脑无需保持开机。

## 来源与准确性

Anthropic、OpenAI、arXiv、Hugging Face Blog 和 NVIDIA 提供带日期的内容。Reddit RSS、Hugging Face 每日论文及可选的 X API 用于发现链接。社区帖子不会直接作为已核实新闻发布；候选内容必须有注明日期的官方页面。链接可访问并不等于独立事实核查。旧文章按照不同规则生成，请查看原始来源。

设置 `GEMINI_API_KEY` 后，Gemini 可从来源摘要中选择原有句子；否则保留来源摘要。使用 `python -m pipeline.run_pipeline --mode daily --count 2 --dry-run` 试运行。启用 X 发现需要 GitHub Actions 密钥 `X_BEARER_TOKEN`。Reddit 可能返回 HTTP 429。

## 终端接入

只读 MCP 服务提供 `latest_news` 工具和 RSS 资源。运行 `python -m pipeline.news_mcp`。在本项目中启动 OMP 时，`.omp/mcp.json` 会注册服务。其他 MCP 客户端需使用相同命令，并将工作目录设为仓库的绝对路径。

OMP 扩展 `.omp/extensions/news.ts` 在会话运行期间每 15 分钟查询 RSS。出现新文章时，它显示标题和链接；`/news` 显示最近的新闻。关闭 OMP 后不会通知。能否点击链接取决于终端。重启 OMP 以加载扩展。
