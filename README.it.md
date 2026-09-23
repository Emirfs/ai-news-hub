# Neural Pulse — Italiano

[Sito](https://emirfs.github.io/ai-news-hub/) · [RSS](https://emirfs.github.io/ai-news-hub/rss.xml) · [English](README.en.md) · [Türkçe](README.tr.md) · [Español](README.es.md) · [中文](README.zh.md) · [Deutsch](README.de.md)

Neural Pulse raccoglie notizie sull'intelligenza artificiale da fonti ufficiali. GitHub Actions tenta un aggiornamento ai minuti 17 e 47 di ogni ora. GitHub può ritardare o saltare un'esecuzione. Il sito cambia solo dopo un commit e una distribuzione Pages riusciti. Il computer personale può restare spento.

## Fonti e attendibilità

Anthropic, OpenAI, arXiv, Hugging Face Blog e NVIDIA forniscono notizie datate. Reddit RSS, Hugging Face Daily Papers e l'API X opzionale aiutano a scoprire collegamenti. I post della comunità non vengono pubblicati come notizie verificate: serve una pagina ufficiale con data. Una fonte raggiungibile non equivale a una verifica indipendente. Controlla gli articoli precedenti nelle fonti originali.

Con `GEMINI_API_KEY`, Gemini può selezionare frasi già presenti nell'estratto della fonte. Senza chiave, l'estratto resta invariato. Prova `python -m pipeline.run_pipeline --mode daily --count 2 --dry-run`. Per X aggiungi il segreto GitHub Actions `X_BEARER_TOKEN`. Reddit può rispondere HTTP 429.

## Terminali

Il server MCP in sola lettura espone `latest_news` e la risorsa RSS. Esegui `python -m pipeline.news_mcp`. OMP usa `.omp/mcp.json` in questo progetto. Negli altri client MCP configura lo stesso comando e la directory di lavoro con il percorso assoluto del repository.

L'estensione `.omp/extensions/news.ts` controlla RSS ogni 15 minuti durante una sessione OMP attiva. Mostra titoli e collegamenti per le nuove notizie; `/news` elenca le ultime notizie. A OMP chiuso non invia notifiche. La possibilità di aprire i collegamenti dipende dal terminale. Riavvia OMP per caricare l'estensione.
