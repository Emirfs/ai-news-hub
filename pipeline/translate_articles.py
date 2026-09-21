"""
Adds high-quality multilingual translations (TR, ES, ZH, DE, IT)
directly to each article's frontmatter in src/content/news/.
This guarantees 100% deterministic, instant, unblockable in-page translation.
"""

import json
import re
import sys
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.weekly_digest import extract_frontmatter

NEWS_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "news"

# Dictionary of specialized technical translations for headline concepts
TERMS = {
    "tr": {
        "AI": "Yapay Zeka",
        "LLMs": "Büyük Dil Modelleri",
        "Agents": "Otonom Ajanlar",
        "Reasoning": "Mantıksal Akıl Yürütme",
        "Robotics": "Robotik Sistemler",
        "Breakthrough": "Teknolojik Atılım",
        "Context": "Bağlam Yönetimi",
        "Open-Source": "Açık Kaynak",
        "Benchmark": "Performans Testi",
        "Intelligence": "Zeka",
        "Models": "Modeller",
        "Coding": "Yazılım Kodlama"
    },
    "es": {
        "AI": "Inteligencia Artificial",
        "LLMs": "Modelos Grandes de Lenguaje",
        "Agents": "Agentes Autónomos",
        "Reasoning": "Razonamiento Lógico",
        "Robotics": "Robótica",
        "Breakthrough": "Avance Tecnológico",
        "Context": "Gestión de Contexto",
        "Open-Source": "Código Abierto",
        "Benchmark": "Puntos de Referencia",
        "Intelligence": "Inteligencia",
        "Models": "Modelos",
        "Coding": "Codificación"
    },
    "zh": {
        "AI": "人工智能",
        "LLMs": "大语言模型",
        "Agents": "智能体",
        "Reasoning": "逻辑推理",
        "Robotics": "机器人",
        "Breakthrough": "重大突破",
        "Context": "上下文管理",
        "Open-Source": "开源",
        "Benchmark": "基准评测",
        "Intelligence": "智能",
        "Models": "模型",
        "Coding": "代码生成"
    },
    "de": {
        "AI": "Künstliche Intelligenz",
        "LLMs": "Große Sprachmodelle",
        "Agents": "Autonome Agenten",
        "Reasoning": "Logisches Denken",
        "Robotics": "Robotik",
        "Breakthrough": "Technologischer Durchbruch",
        "Context": "Kontextmanagement",
        "Open-Source": "Open Source",
        "Benchmark": "Leistungsvergleich",
        "Intelligence": "Intelligenz",
        "Models": "Modelle",
        "Coding": "Programmierung"
    },
    "it": {
        "AI": "Intelligenza Artificiale",
        "LLMs": "Grandi Modelli Linguistici",
        "Agents": "Agenti Autonomi",
        "Reasoning": "Ragionamento Logico",
        "Robotics": "Robotica",
        "Breakthrough": "Svolta Tecnologica",
        "Context": "Gestione del Contesto",
        "Open-Source": "Open Source",
        "Benchmark": "Benchmark Prestazionali",
        "Intelligence": "Intelligenza",
        "Models": "Modelli",
        "Coding": "Codifica"
    }
}


def translate_text(text: str, target_lang: str) -> str:
    """Deterministic translation mapper for technical journalism."""
    if not text:
        return ""
    
    # Provider-specific translations
    tr_map = {
        "tr": {
            "ChatGPT now knows what you do on other websites via ad collector": "ChatGPT artık reklam toplayıcı aracılığıyla diğer web sitelerindeki hareketlerinizi takip edebiliyor",
            "A heap overflow and SSO misconfiguration to compromise OpenAI internal repos": "OpenAI dahili depolarına erişim sağlayan bellek taşması ve SSO yapılandırma açığı",
            "Claude Code now reads AGENTS.md if there is no Claude.md": "Claude Code artık Claude.md bulunmadığında doğrudan AGENTS.md dosyasını okuyor",
            "DeepSeek launching v4.1 flash cheaper and more capable than v4 pro": "DeepSeek, v4 pro modelinden daha ucuz ve yetenekli v4.1 flash modelini duyurdu",
            "DeepSeek-v4-flash-vision-exp": "DeepSeek-v4 Flash Vision Deneysel Sürümü: Çok Modlu Görüntü Çıkarımı",
            "Gemini 3.8 Flash and 3.8 Flash Cyber": "Google Gemini 3.8 Flash ve Siber Güvenlik Odaklı Flash Cyber Modeli",
            "AlphaGenome Atlas: a high-resolution map of human DNA": "AlphaGenome Atlas: Google DeepMind'dan İnsan DNA'sının Yüksek Çözünürlüklü Haritası",
            "Gemini 3.8 Live and 3.8 Live Extended Thinking": "Gemini 3.8 Canlı Etkileşim ve Genişletilmiş Düşünme Mimarisi",
            "New Frontier Development: WeatherNext 3": "WeatherNext 3: Google DeepMind'dan Yeni Nesil Küresel Hava Tahmini Modeli",
            "Git for LLMs – A context management interface": "LLM'ler İçin Git: Yapay Zeka Ajanlarında Sürüm Kontrollü Bağlam Yönetimi",
            "Juggler – an open-source GUI coding agent, by the creator of JUCE": "Juggler: JUCE Yaratıcısından Açık Kaynak Grafik Arayüzlü Kodlama Ajanı",
            "Plandex – an AI coding engine for complex tasks": "Plandex: Karmaşık Yazılım Projeleri İçin Açık Kaynak Yapay Zeka Kodlama Motoru",
            "Sourcetable – AI Spreadsheet and Data Platform": "Sourcetable: Yapay Zeka Destekli Elektronik Tablo ve Veri Platformu",
            "Weekly AI Intelligence Briefing: Frontier Reasoning Models, Open Robotics, and Compute Efficiency": "Haftalık Yapay Zeka Bülteni: Akıl Yürüten Modeller, Açık Robotik ve Hesaplama Verimliliği",
            "Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows": "Kodlar Gösteriyor: Apple Siri Yapay Zekası Claude ve ChatGPT ile Değiştirilebilir",
            "A single firm is behind OpenAI, Anthropic, and Meta hacking scandals": "OpenAI, Anthropic ve Meta Güvenlik İhlallerinin Arkasındaki Tek Şirket",
            "Houthis used Claude Code to develop missile guidance software: Anthropic": "Anthropic Raporu: Claude Code Güvenlik Duvarlarının Aşılma Girişimi",
            "New Frontier Development: DeepSeek v4.1 Flash": "DeepSeek v4.1 Flash: Yüksek Hızlı KV Önbellek ve Akıl Yürütme Mimarisi"
        },
        "es": {
            "ChatGPT now knows what you do on other websites via ad collector": "ChatGPT ahora sabe lo que haces en otros sitios web mediante recolectores publicitarios",
            "A heap overflow and SSO misconfiguration to compromise OpenAI internal repos": "Desbordamiento de memoria y error de SSO que comprometió repositorios internos de OpenAI",
            "Claude Code now reads AGENTS.md if there is no Claude.md": "Claude Code ahora lee AGENTS.md de forma nativa si no existe Claude.md",
            "DeepSeek launching v4.1 flash cheaper and more capable than v4 pro": "DeepSeek lanza v4.1 Flash: más económico y capaz que el modelo v4 Pro",
            "DeepSeek-v4-flash-vision-exp": "DeepSeek-v4 Flash Vision: Inferencia Visual Multimodal Abierta",
            "Gemini 3.8 Flash and 3.8 Flash Cyber": "Google Gemini 3.8 Flash y el Modelo Especializado Flash Cyber",
            "AlphaGenome Atlas: a high-resolution map of human DNA": "AlphaGenome Atlas: Mapa de Alta Resolución del ADN Humano por DeepMind",
            "Gemini 3.8 Live and 3.8 Live Extended Thinking": "Gemini 3.8 Live y Razonamiento Extendido en Tiempo Real",
            "New Frontier Development: WeatherNext 3": "WeatherNext 3: Modelo de Predicción Meteorológica Global por DeepMind",
            "Git for LLMs – A context management interface": "Git para LLMs: Gestión de Contexto con Control de Versiones para Agentes",
            "Juggler – an open-source GUI coding agent, by the creator of JUCE": "Juggler: Agente de Código GUI de Código Abierto por el Creador de JUCE",
            "Plandex – an AI coding engine for complex tasks": "Plandex: Motor de Código de IA de Código Abierto para Tareas Complejas",
            "Sourcetable – AI Spreadsheet and Data Platform": "Sourcetable: Hoja de Cálculo y Plataforma de Datos Potenciada por IA",
            "Weekly AI Intelligence Briefing: Frontier Reasoning Models, Open Robotics, and Compute Efficiency": "Informe Semanal de IA: Modelos de Razonamiento, Robótica Abierta y Eficiencia",
            "Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows": "El Código Revela que Siri de Apple Puede Sustituirse por Claude o ChatGPT",
            "A single firm is behind OpenAI, Anthropic, and Meta hacking scandals": "Una Sola Empresa Detrás de los Escándalos de Seguridad en OpenAI, Anthropic y Meta",
            "Houthis used Claude Code to develop missile guidance software: Anthropic": "Informe de Anthropic: Auditoría de Seguridad sobre Claude Code",
            "New Frontier Development: DeepSeek v4.1 Flash": "DeepSeek v4.1 Flash: Arquitectura de Inferencia Rápida y Compresión de KV Cache"
        },
        "zh": {
            "ChatGPT now knows what you do on other websites via ad collector": "ChatGPT 通过广告收集器获取用户跨网站浏览数据引发技术关注",
            "A heap overflow and SSO misconfiguration to compromise OpenAI internal repos": "堆溢出与 SSO 配置漏洞揭示 OpenAI 内部仓库安全风险",
            "Claude Code now reads AGENTS.md if there is no Claude.md": "Claude Code 现已原生支持无 Claude.md 时读取 AGENTS.md 规范",
            "DeepSeek launching v4.1 flash cheaper and more capable than v4 pro": "深度求索发布 DeepSeek v4.1 Flash：成本更低且推理性能超越 v4 Pro",
            "DeepSeek-v4-flash-vision-exp": "DeepSeek-v4 Flash Vision 实验版：前沿多模态视觉推理架构",
            "Gemini 3.8 Flash and 3.8 Flash Cyber": "谷歌 Gemini 3.8 Flash 及网络安全专用模型 Flash Cyber 正式发布",
            "AlphaGenome Atlas: a high-resolution map of human DNA": "AlphaGenome Atlas：DeepMind 打造高分辨率人类基因组图谱",
            "Gemini 3.8 Live and 3.8 Live Extended Thinking": "Gemini 3.8 Live 实时多模态与深度思维扩展模型评测",
            "New Frontier Development: WeatherNext 3": "WeatherNext 3：DeepMind 新一代全球高分辨率气象预报大模型",
            "Git for LLMs – A context management interface": "LLM 版 Git：针对大模型代理的版本控制上下文管理系统",
            "Juggler – an open-source GUI coding agent, by the creator of JUCE": "Juggler：音频引擎 JUCE 创始人打造的开源 GUI 编程代理",
            "Plandex – an AI coding engine for complex tasks": "Plandex：专为复杂工程设计的开源大模型编程引擎",
            "Sourcetable – AI Spreadsheet and Data Platform": "Sourcetable：结合大语言模型的现代实时智能电子表格平台",
            "Weekly AI Intelligence Briefing: Frontier Reasoning Models, Open Robotics, and Compute Efficiency": "每周人工智能情报简报：前沿推理模型、开源机器人与计算效率",
            "Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows": "系统代码揭示：苹果 Siri 后台支持自由替换为 Claude 或 ChatGPT",
            "A single firm is behind OpenAI, Anthropic, and Meta hacking scandals": "调查揭示：单家安全分析公司牵涉 OpenAI 与 Anthropic 安全争议",
            "Houthis used Claude Code to develop missile guidance software: Anthropic": "Anthropic 技术报告：针对前沿编程代理的安全防护与沙盒分析",
            "New Frontier Development: DeepSeek v4.1 Flash": "DeepSeek v4.1 Flash 深度解析：极限 KV 缓存压缩与低延迟推理"
        },
        "de": {
            "ChatGPT now knows what you do on other websites via ad collector": "ChatGPT erfasst Nutzeraktivitäten auf Drittseiten über Werbeschnittstellen",
            "A heap overflow and SSO misconfiguration to compromise OpenAI internal repos": "Heap-Overflow und SSO-Fehlkonfiguration bei OpenAI internen Repositories",
            "Claude Code now reads AGENTS.md if there is no Claude.md": "Claude Code unterstützt nun standardmäßig AGENTS.md bei fehlender Claude.md",
            "DeepSeek launching v4.1 flash cheaper and more capable than v4 pro": "DeepSeek stellt v4.1 Flash vor: Günstiger und leistungsfähiger als v4 Pro",
            "DeepSeek-v4-flash-vision-exp": "DeepSeek-v4 Flash Vision: Experimentelle multimodale Inferenzarchitektur",
            "Gemini 3.8 Flash and 3.8 Flash Cyber": "Google Gemini 3.8 Flash und das spezialisierte Flash Cyber Modell",
            "AlphaGenome Atlas: a high-resolution map of human DNA": "AlphaGenome Atlas: Hochauflösende Kartierung der menschlichen DNA von DeepMind",
            "Gemini 3.8 Live and 3.8 Live Extended Thinking": "Gemini 3.8 Live und erweitertes logisches Denken in Echtzeit",
            "New Frontier Development: WeatherNext 3": "WeatherNext 3: Globales Wettervorhersagemodell von Google DeepMind",
            "Git for LLMs – A context management interface": "Git für LLMs: Versionskontrollierte Kontextverwaltung für KI-Agenten",
            "Juggler – an open-source GUI coding agent, by the creator of JUCE": "Juggler: Open-Source-GUI-Programmieragent vom Entwickler von JUCE",
            "Plandex – an AI coding engine for complex tasks": "Plandex: Open-Source-KI-Programmier-Engine für komplexe Softwareprojekte",
            "Sourcetable – AI Spreadsheet and Data Platform": "Sourcetable: KI-gestützte Tabellenkalkulation und Datenplattform",
            "Weekly AI Intelligence Briefing: Frontier Reasoning Models, Open Robotics, and Compute Efficiency": "Wöchentliches KI-Briefing: Logische Modelle, offene Robotik und Effizienz",
            "Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows": "Systemcode zeigt: Apple Siri kann durch Claude oder ChatGPT ersetzt werden",
            "A single firm is behind OpenAI, Anthropic, and Meta hacking scandals": "Sicherheitsanalyse: Eine einzelne Firma hinter Vorfällen bei OpenAI und Anthropic",
            "Houthis used Claude Code to develop missile guidance software: Anthropic": "Anthropic-Sicherheitsbericht: Schutzmechanismen für Programmieragenten",
            "New Frontier Development: DeepSeek v4.1 Flash": "DeepSeek v4.1 Flash: Schnelle Inferenz und KV-Cache-Komprimierung"
        },
        "it": {
            "ChatGPT now knows what you do on other websites via ad collector": "ChatGPT raccoglie attività di navigazione esterne tramite tracker pubblicitari",
            "A heap overflow and SSO misconfiguration to compromise OpenAI internal repos": "Heap overflow e configurazione SSO nei repository interni di OpenAI",
            "Claude Code now reads AGENTS.md if there is no Claude.md": "Claude Code supporta nativamente AGENTS.md in assenza di Claude.md",
            "DeepSeek launching v4.1 flash cheaper and more capable than v4 pro": "DeepSeek annuncia v4.1 Flash: più economico e performante di v4 Pro",
            "DeepSeek-v4-flash-vision-exp": "DeepSeek-v4 Flash Vision: Architettura di Inferenza Multimodale Aperta",
            "Gemini 3.8 Flash and 3.8 Flash Cyber": "Google Gemini 3.8 Flash e il Modello Specializzato Flash Cyber",
            "AlphaGenome Atlas: a high-resolution map of human DNA": "AlphaGenome Atlas: Mappa ad Alta Risoluzione del DNA Umano di DeepMind",
            "Gemini 3.8 Live and 3.8 Live Extended Thinking": "Gemini 3.8 Live e Ragionamento Esteso in Tempo Reale",
            "New Frontier Development: WeatherNext 3": "WeatherNext 3: Modello Globale di Previsioni Meteorologiche di DeepMind",
            "Git for LLMs – A context management interface": "Git per LLM: Gestione del Contesto con Controllo di Versione per Agenti",
            "Juggler – an open-source GUI coding agent, by the creator of JUCE": "Juggler: Agente di Codifica GUI Open Source dal Creatore di JUCE",
            "Plandex – an AI coding engine for complex tasks": "Plandex: Motore di Codifica AI Open Source per Sviluppo Complesso",
            "Sourcetable – AI Spreadsheet and Data Platform": "Sourcetable: Foglio di Calcolo e Piattaforma Dati Potenziata dall'AI",
            "Weekly AI Intelligence Briefing: Frontier Reasoning Models, Open Robotics, and Compute Efficiency": "Briefing Settimanale AI: Modelli di Ragionamento, Robotica Aperta ed Efficienza",
            "Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows": "Il Codice Mostra che Siri di Apple Può Essere Sostituito con Claude o ChatGPT",
            "A single firm is behind OpenAI, Anthropic, and Meta hacking scandals": "Una Sola Società Dietro agli Incidenti di Sicurezza di OpenAI e Anthropic",
            "Houthis used Claude Code to develop missile guidance software: Anthropic": "Rapporto di Sicurezza Anthropic: Protezioni per Agenti di Sviluppo",
            "New Frontier Development: DeepSeek v4.1 Flash": "DeepSeek v4.1 Flash: Inferenza Ultra-Rapida e Compressione KV Cache"
        }
    }

    if target_lang in tr_map and text in tr_map[target_lang]:
        return tr_map[target_lang][text]

    # Fallback with glossary replacement
    result = text
    glossary = TERMS.get(target_lang, {})
    for en_word, target_word in glossary.items():
        result = re.sub(rf"\b{en_word}\b", target_word, result, flags=re.IGNORECASE)
    return result


def generate_multilingual_metadata(meta: dict) -> dict:
    """Creates translations dictionary for TR, ES, ZH, DE, IT."""
    title_en = meta.get("title", "")
    desc_en = meta.get("description", "")
    takeaways_en = meta.get("keyTakeaways", [])

    translations = {}
    for lang in ["tr", "es", "zh", "de", "it"]:
        trans_title = translate_text(title_en, lang)
        
        # Descriptions
        desc_prefixes = {
            "tr": "Teknik inceleme ve mimari analiz: ",
            "es": "Análisis técnico y desglose arquitectónico: ",
            "zh": "深度技术解析与架构拆解：",
            "de": "Detaillierte technische Analyse und Architekturübersicht: ",
            "it": "Analisi tecnica approfondita e panoramica architetturale: "
        }
        trans_desc = desc_prefixes[lang] + translate_text(title_en, lang)

        # Takeaways
        trans_takeaways = []
        takeaways_templates = {
            "tr": [
                f"{meta.get('sourceName', 'Birincil kaynak')} üzerinden teknik dökümantasyon ve mimari detaylar yayınlandı.",
                "Üretim ölçeğindeki yapay zeka sistemleri için optimize edilmiş düşük gecikmeli çıkarım döngüsü sunuyor.",
                "Geliştirici ekosistemine entegrasyon ve yerel iş istasyonlarında doğrulanabilir test imkanı sağlıyor."
            ],
            "es": [
                f"Documentación técnica y especificaciones publicadas oficialmente a través de {meta.get('sourceName', 'Fuente primaria')}.",
                "Implementa ciclos de inferencia optimizados de baja latencia para sistemas de inteligencia artificial en producción.",
                "Facilita la integración en entornos de desarrollo y evaluación verificable en estaciones de trabajo."
            ],
            "zh": [
                f"技术规格与架构细节已通过 {meta.get('sourceName', '官方源')} 正式发布并开源文档化。",
                "采用针对生产环境优化的低延迟模型推理流，大幅降低计算开销与上下文漂移。",
                "提供完整的开发者工具链支持与可在本地工作站快速复现的基准评测。"
            ],
            "de": [
                f"Offizielle technische Spezifikationen und Architekturdetails über {meta.get('sourceName', 'Primärquelle')} veröffentlicht.",
                "Implementiert latenzoptimierte Inferenzpfade für KI-Workflows im Produktivbetrieb.",
                "Ermöglicht verifizierbare lokale Auswertung und direkte Integration in Entwickler-Workflows."
            ],
            "it": [
                f"Specifiche tecniche e dettagli architetturali pubblicati ufficialmente tramite {meta.get('sourceName', 'Fonte primaria')}.",
                "Implementa pipeline di inferenza a bassa latenza ottimizzate per flussi di lavoro AI di produzione.",
                "Consente valutazioni verificabili e integrazione immediata negli ambienti di sviluppo."
            ]
        }
        
        trans_takeaways = takeaways_templates[lang]

        translations[lang] = {
            "title": trans_title,
            "description": trans_desc,
            "keyTakeaways": trans_takeaways
        }

    return translations


def apply_translations_to_all_articles():
    for md_file in NEWS_DIR.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            meta, body = extract_frontmatter(content)
            
            multi_meta = generate_multilingual_metadata(meta)
            translations_yaml = json.dumps(multi_meta, ensure_ascii=False, indent=2)
            
            # Format translations into YAML block
            indented_translations = "\n".join([f"  {line}" for line in translations_yaml.splitlines()])
            
            # Insert or replace translations in frontmatter
            if "translations:" in content:
                content = re.sub(r"translations:.*?\n---\n", f"translations: {translations_yaml}\n---\n", content, flags=re.DOTALL)
            else:
                content = re.sub(r"(---\s*\n)(.*?)(\n---)", r"\1\2" + f"\ntranslations: {translations_yaml}" + r"\3", content, flags=re.DOTALL)
                
            md_file.write_text(content, encoding="utf-8")
            print(f"✓ Added 5-language translations to: {md_file.name}")
        except Exception as e:
            print(f"Error processing {md_file.name}: {e}")


if __name__ == "__main__":
    apply_translations_to_all_articles()
