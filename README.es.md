# Neural Pulse — Español

[Sitio](https://emirfs.github.io/ai-news-hub/) · [RSS](https://emirfs.github.io/ai-news-hub/rss.xml) · [English](README.en.md) · [Türkçe](README.tr.md) · [中文](README.zh.md) · [Italiano](README.it.md) · [Deutsch](README.de.md)

Neural Pulse recoge noticias de inteligencia artificial de fuentes oficiales. GitHub Actions intenta ejecutar la publicación a los minutos 17 y 47 de cada hora. GitHub puede retrasar u omitir ejecuciones. El sitio cambia después de una confirmación correcta y el despliegue de Pages. Tu ordenador no necesita permanecer encendido.

## Fuentes y precisión

Anthropic, OpenAI, arXiv, Hugging Face Blog y NVIDIA proporcionan noticias fechadas. Reddit RSS, los artículos diarios de Hugging Face y la API opcional de X ayudan a descubrir enlaces. No publicamos mensajes comunitarios como noticias verificadas: exigimos una página oficial fechada. Que una fuente sea accesible no equivale a una verificación independiente. Comprueba también los artículos antiguos en sus fuentes originales.

Gemini puede seleccionar frases del extracto original si configuras `GEMINI_API_KEY`; de lo contrario, se conserva el extracto. Prueba la automatización con `python -m pipeline.run_pipeline --mode daily --count 2 --dry-run`. Para activar X, configura el secreto `X_BEARER_TOKEN` en GitHub Actions. Reddit puede responder HTTP 429.

## Terminales

El servidor MCP de solo lectura ofrece `latest_news` y el recurso RSS. Ejecútalo con `python -m pipeline.news_mcp`. OMP carga `.omp/mcp.json` desde este proyecto. Para otros clientes MCP, configura el mismo comando y usa la ruta absoluta del repositorio como directorio de trabajo.

La extensión `.omp/extensions/news.ts` consulta el RSS cada 15 minutos durante una sesión OMP activa. Muestra titulares nuevos y enlaces; `/news` enseña los últimos artículos. No hay avisos si OMP está cerrado. La apertura de enlaces depende del terminal. Reinicia OMP para cargar la extensión.
