# Neural Pulse — Deutsch

[Website](https://emirfs.github.io/ai-news-hub/) · [RSS](https://emirfs.github.io/ai-news-hub/rss.xml) · [English](README.en.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [中文](README.zh.md) · [Italiano](README.it.md)

Neural Pulse sammelt KI-Nachrichten aus offiziellen Quellen. GitHub Actions versucht die Veröffentlichung stündlich um Minute 17 und 47. GitHub kann geplante Läufe verzögern oder auslassen. Die Website wird erst nach erfolgreichem Commit und Pages-Deployment aktualisiert. Der eigene Rechner muss nicht eingeschaltet bleiben.

## Quellen und Genauigkeit

Anthropic, OpenAI, arXiv, Hugging Face Blog und NVIDIA liefern datierte Beiträge. Reddit-RSS, Hugging-Face-Tagesartikel und die optionale X-API helfen bei der Entdeckung weiterer Links. Beiträge aus der Community werden nicht direkt als bestätigte Nachrichten veröffentlicht: Es wird eine datierte offizielle Seite benötigt. Erreichbarkeit ist keine unabhängige Faktenprüfung. Prüfe ältere Artikel anhand der Originalquellen.

Mit `GEMINI_API_KEY` kann Gemini vorhandene Sätze aus einem Quellauszug auswählen. Sonst bleibt der Quellauszug bestehen. Testlauf: `python -m pipeline.run_pipeline --mode daily --count 2 --dry-run`. Für X ist das GitHub-Actions-Secret `X_BEARER_TOKEN` nötig. Reddit kann HTTP 429 zurückgeben.

## Terminalzugriff

Der schreibgeschützte MCP-Server bietet `latest_news` und die RSS-Ressource. Starte `python -m pipeline.news_mcp`. OMP lädt `.omp/mcp.json` in diesem Projekt. Für andere MCP-Clients richte denselben Befehl mit dem absoluten Repository-Pfad als Arbeitsverzeichnis ein.

Die Erweiterung `.omp/extensions/news.ts` prüft RSS während aktiver OMP-Sitzungen alle 15 Minuten. Neue Titel erscheinen mit Links; `/news` zeigt aktuelle Einträge. Bei geschlossenem OMP gibt es keine Meldungen. Ob Links anklickbar sind, hängt vom Terminal ab. Starte OMP neu, um die Erweiterung zu laden.
