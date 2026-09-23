# Neural Pulse — Türkçe

[Site](https://emirfs.github.io/ai-news-hub/) · [RSS](https://emirfs.github.io/ai-news-hub/rss.xml) · [English](README.en.md) · [Español](README.es.md) · [中文](README.zh.md) · [Italiano](README.it.md) · [Deutsch](README.de.md)

Neural Pulse, yapay zekâ haberlerini resmî kaynaklardan toplar. GitHub Actions her saatin 17. ve 47. dakikasında çalışmayı dener. GitHub zamanlanmış işleri geciktirebilir veya atlayabilir. Site ancak başarılı kayıt ve Pages dağıtımından sonra güncellenir. Bilgisayarınızın açık kalması gerekmez.

## Kaynaklar ve doğruluk

Anthropic, OpenAI, arXiv, Hugging Face Blog ve NVIDIA kaynakları tarihli haber sağlar. Reddit RSS, Hugging Face günlük makaleleri ve isteğe bağlı X API bağlantıları keşfeder. Topluluk gönderileri doğrudan haber olmaz. Yalnızca tarihi bulunan resmî kaynak sayfaları yayına uygundur. Erişilebilen kaynak, içindeki iddiaların bağımsız doğrulandığını göstermez. Eski arşiv farklı kurallarla üretildi; iddiaları asıl kaynaktan inceleyin.

`GEMINI_API_KEY` ayarlanırsa Gemini, kaynak alıntısından mevcut cümleleri seçebilir. Aksi halde kaynak alıntısı korunur. Deneme: `python -m pipeline.run_pipeline --mode daily --count 2 --dry-run`. `--dry-run` seçeneğini kaldırırsanız dosyalar yazılır. X keşfi için GitHub Actions gizli değişkeni `X_BEARER_TOKEN` gerekir. Reddit bazen HTTP 429 döndürür.

## Terminal bağlantısı

Salt okunur MCP sunucusu, `latest_news` aracını ve RSS kaynağını sağlar. Komut: `python -m pipeline.news_mcp`. Proje kökündeki OMP oturumları `.omp/mcp.json` yapılandırmasını kullanır. Başka MCP istemcilerinde aynı komutu tanımlayın; çalışma dizinini bu deponun mutlak yolu yapın.

`.omp/extensions/news.ts` uzantısı, açık OMP oturumunda RSS'yi 15 dakikada bir kontrol eder. Yeni başlıkları bağlantılarıyla bildirir; `/news` son başlıkları gösterir. OMP kapalıyken bildirim gelmez. Bağlantının tıklanması terminalin desteğine bağlıdır. Uzantı için OMP'yi yeniden başlatın. Genel profil ayarları değişmez.
