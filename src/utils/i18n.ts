export type Language = 'en' | 'tr' | 'es' | 'zh' | 'it' | 'de';

export interface TranslationDict {
  // Navigation
  latestNews: string;
  trendingRepos: string;
  emergingAi: string;
  weeklyDigests: string;
  categories: string;
  about: string;
  rss: string;
  
  // Status Bar
  wireStatus: string;
  hourlyActive: string;
  monitoredProviders: string;
  totalIndexed: string;
  
  // Headlines & Sections
  topStory: string;
  readFullAnalysis: string;
  primaryWire: string;
  executiveHighlights: string;
  trendingDispatches: string;
  topSignals: string;
  openSourceRadar: string;
  trendingReposTitle: string;
  trendingReposSub: string;
  indieLaunchpadTag: string;
  indieLaunchpadTitle: string;
  indieLaunchpadSub: string;
  submitRepo: string;
  weeklyDigestTitle: string;
  viewAllWeekly: string;
  filterWire: string;
  allDispatches: string;
  wireStreamTitle: string;
  storiesIndexed: string;
  readAction: string;
  
  // Article Page
  backToDispatches: string;
  selectLanguage: string;
  readInYourLang: string;
  minRead: string;
  reportedBy: string;
  sourceDocument: string;
  openOriginalSource: string;
  coreSignals: string;
  verifyResearchTitle: string;
  verifyResearchSub: string;
  visitPrimary: string;
  filedUnder: string;
  continueReading: string;

  // Categories
  catLLM: string;
  catResearch: string;
  catRobotics: string;
  catOpenSource: string;
  catDigest: string;
  catIndustry: string;

  // Footer
  footerDesc: string;
  footerRights: string;
  footerPublished: string;
  navigationHeading: string;
  sourcesHeading: string;
}

export const translations: Record<Language, TranslationDict> = {
  en: {
    latestNews: 'Latest News',
    trendingRepos: 'Trending Repos',
    emergingAi: 'Emerging AI',
    weeklyDigests: 'Weekly Digests',
    categories: 'Categories',
    about: 'About',
    rss: 'RSS',
    wireStatus: 'News Desk:',
    hourlyActive: 'Hourly Autonomous Wire Active',
    monitoredProviders: 'Providers Monitored:',
    totalIndexed: 'Total Indexed Dispatches:',
    topStory: '★ Top Story',
    readFullAnalysis: 'Read Full Analysis',
    primaryWire: 'Primary Wire:',
    executiveHighlights: 'Executive Highlights',
    trendingDispatches: 'Trending Dispatches',
    topSignals: 'Top Signals',
    openSourceRadar: 'Open-Source Radar',
    trendingReposTitle: 'Trending & Novel AI Repositories',
    trendingReposSub: 'Curated directly from GitHub telemetry • Updated hourly',
    indieLaunchpadTag: 'Indie AI Launchpad & Hidden Gems',
    indieLaunchpadTitle: 'Emerging & Actively Maintained Repositories',
    indieLaunchpadSub: 'Curated independent AI tools and experimental research under 500 stars with active commits.',
    submitRepo: '+ Submit Your Repo',
    weeklyDigestTitle: 'Latest Executive Briefing',
    viewAllWeekly: 'View All Weekly Briefings →',
    filterWire: 'Filter Wire:',
    allDispatches: 'All Dispatches',
    wireStreamTitle: 'Continuous Wire Stream',
    storiesIndexed: 'Stories Indexed',
    readAction: 'Read',
    backToDispatches: 'Back to Dispatches',
    selectLanguage: 'Select Language:',
    readInYourLang: 'Read in your language:',
    minRead: 'min in-depth read',
    reportedBy: 'Curated & Verified by',
    sourceDocument: 'Primary Source Document (Direct Link)',
    openOriginalSource: 'Open Original Source',
    coreSignals: 'Executive Summary & Core Signals',
    verifyResearchTitle: 'Need to inspect the original primary publication?',
    verifyResearchSub: 'Neural Pulse provides objective synthesis and architectural reporting. You can read the complete paper or release notes on the primary source platform:',
    visitPrimary: 'Visit Primary Document',
    filedUnder: 'Filed under:',
    continueReading: 'Continue Reading Frontier News',
    catLLM: 'LLMs & Foundation Models',
    catResearch: 'AI Research',
    catRobotics: 'Robotics & Hardware',
    catOpenSource: 'Open Source AI',
    catDigest: 'Weekly Digest',
    catIndustry: 'Industry & Startups',
    footerDesc: 'The autonomous artificial intelligence journal. Monitoring frontier AI research, open-source model releases, and hardware scaling hourly. Distilled and published without human intervention.',
    footerRights: 'Neural Pulse. Autonomous news synthesis. All sources cited directly.',
    footerPublished: 'Published via GitHub Pages',
    navigationHeading: 'Navigation',
    sourcesHeading: 'Sourced Feeds'
  },
  tr: {
    latestNews: 'Son Haberler',
    trendingRepos: 'Trend Repolar',
    emergingAi: 'Yükselen AI',
    weeklyDigests: 'Haftalık Bültenler',
    categories: 'Kategoriler',
    about: 'Hakkında',
    rss: 'RSS',
    wireStatus: 'Haber Masası:',
    hourlyActive: 'Saatlik Otonom Akış Aktif',
    monitoredProviders: 'Takip Edilen Kaynaklar:',
    totalIndexed: 'Toplam Taranan Haber:',
    topStory: '★ Manşet Haber',
    readFullAnalysis: 'Detaylı Analizi Oku',
    primaryWire: 'Birincil Kaynak:',
    executiveHighlights: 'Öne Çıkan Başlıklar',
    trendingDispatches: 'Gündemdeki Haberler',
    topSignals: 'Önemli Sinyaller',
    openSourceRadar: 'Açık Kaynak Radarı',
    trendingReposTitle: 'Trend ve Yenilikçi Yapay Zeka Repoları',
    trendingReposSub: 'GitHub telemetrisinden saatlik olarak derlenir',
    indieLaunchpadTag: 'Bağımsız AI Fırlatma Rampası ve Keşifler',
    indieLaunchpadTitle: 'Yükselen ve Aktif Güncellenen Repolar',
    indieLaunchpadSub: '500 yıldız altı, düzenli commit alan bağımsız geliştirici araçları.',
    submitRepo: '+ Projenizi Gönderin',
    weeklyDigestTitle: 'Haftalık Yönetici Bülteni',
    viewAllWeekly: 'Tüm Haftalık Bültenleri Gör →',
    filterWire: 'Akışı Filtrele:',
    allDispatches: 'Tüm Haberler',
    wireStreamTitle: 'Kesintisiz Haber Telgrafı',
    storiesIndexed: 'Haber Listelendi',
    readAction: 'Oku',
    backToDispatches: 'Haber Akışına Dön',
    selectLanguage: 'Dil Seçin:',
    readInYourLang: 'Kendi dilinizde okuyun:',
    minRead: 'dakika detaylı okuma',
    reportedBy: 'Derleyen ve Doğrulayan',
    sourceDocument: 'Birincil Kaynak Belge (Doğrudan Bağlantı)',
    openOriginalSource: 'Orijinal Kaynak Habere Git',
    coreSignals: 'Yönetici Özeti ve Temel Sinyaller',
    verifyResearchTitle: 'Orijinal yayını ve dökümanları incelemek ister misiniz?',
    verifyResearchSub: 'Neural Pulse nesnel sentez ve teknik mimari analizi sunar. Tam makaleyi veya sürüm notlarını orijinal platformda okuyabilirsiniz:',
    visitPrimary: 'Birincil Kaynağı Ziyaret Et',
    filedUnder: 'Kategori:',
    relatedStories: 'Gündemdeki Diğer Gelişmeler',
    catLLM: 'Büyük Dil Modelleri',
    catResearch: 'Yapay Zeka Araştırmaları',
    catRobotics: 'Robotik ve Donanım',
    catOpenSource: 'Açık Kaynak Yapay Zeka',
    catDigest: 'Haftalık Bülten',
    catIndustry: 'Sektör ve Girişimler',
    footerDesc: 'Otonom yapay zeka gazetesi. Frontier AI araştırmalarını, açık kaynak model sürümlerini ve donanım gelişmelerini saatlik takip eder.',
    footerRights: 'Neural Pulse. Otonom haber sentezi. Tüm kaynaklara doğrudan atıf yapılır.',
    footerPublished: 'GitHub Pages ile Yayınlanmaktadır',
    navigationHeading: 'Navigasyon',
    sourcesHeading: 'Taranan Kaynaklar'
  },
  es: {
    latestNews: 'Últimas Noticias',
    trendingRepos: 'Repos Populares',
    emergingAi: 'IA Emergente',
    weeklyDigests: 'Resúmenes Semanales',
    categories: 'Categorías',
    about: 'Acerca de',
    rss: 'RSS',
    wireStatus: 'Mesa de Noticias:',
    hourlyActive: 'Flujo Autónomo Horario Activo',
    monitoredProviders: 'Proveedores Monitoreados:',
    totalIndexed: 'Total de Despachos Indexados:',
    topStory: '★ Historia Principal',
    readFullAnalysis: 'Leer Análisis Completo',
    primaryWire: 'Cable Primario:',
    executiveHighlights: 'Aspectos Destacados',
    trendingDispatches: 'Despachos Populares',
    topSignals: 'Señales Clave',
    openSourceRadar: 'Radar de Código Abierto',
    trendingReposTitle: 'Repositorios de IA Populares y Novedosos',
    trendingReposSub: 'Curados directamente de la telemetría de GitHub • Actualización horaria',
    indieLaunchpadTag: 'Lanzadera de IA Independiente y Joyas Ocultas',
    indieLaunchpadTitle: 'Repositorios Emergentes con Mantenimiento Activo',
    indieLaunchpadSub: 'Herramientas de IA independientes e investigación experimental con menos de 500 estrellas y commits activos.',
    submitRepo: '+ Enviar Repositorio',
    weeklyDigestTitle: 'Último Resumen Ejecutivo',
    viewAllWeekly: 'Ver Todos los Resúmenes Semanales →',
    filterWire: 'Filtrar Flujo:',
    allDispatches: 'Todos los Despachos',
    wireStreamTitle: 'Flujo Continuo de Noticias',
    storiesIndexed: 'Historias Indexadas',
    readAction: 'Leer',
    backToDispatches: 'Volver a los Despachos',
    selectLanguage: 'Seleccionar Idioma:',
    readInYourLang: 'Lee en tu idioma:',
    minRead: 'minutos de lectura profunda',
    reportedBy: 'Curado y Verificado por',
    sourceDocument: 'Documento Fuente Primario (Enlace Directo)',
    openOriginalSource: 'Abrir Fuente Original',
    coreSignals: 'Resumen Ejecutivo y Señales Clave',
    verifyResearchTitle: '¿Desea consultar la publicación original?',
    verifyResearchSub: 'Neural Pulse ofrece síntesis objetiva y análisis arquitectónico. Puede leer el artículo completo en la plataforma fuente original:',
    visitPrimary: 'Visitar Documento Primario',
    filedUnder: 'Archivado en:',
    relatedStories: 'Continuar Leyendo Noticias de Vanguardia',
    catLLM: 'Modelos Grandes de Lenguaje',
    catResearch: 'Investigación en IA',
    catRobotics: 'Robótica y Hardware',
    catOpenSource: 'IA de Código Abierto',
    catDigest: 'Resumen Semanal',
    catIndustry: 'Industria y Startups',
    footerDesc: 'El diario autónomo de inteligencia artificial. Monitoreo de investigación en IA de vanguardia y modelos abiertos cada hora.',
    footerRights: 'Neural Pulse. Síntesis autónoma de noticias. Todas las fuentes citadas directamente.',
    footerPublished: 'Publicado a través de GitHub Pages',
    navigationHeading: 'Navegación',
    sourcesHeading: 'Fuentes Rastreadas'
  },
  zh: {
    latestNews: '最新快讯',
    trendingRepos: '热门开源仓库',
    emergingAi: '新锐 AI 项目',
    weeklyDigests: '每周简报',
    categories: '分类目录',
    about: '关于我们',
    rss: 'RSS 订阅',
    wireStatus: '新闻台：',
    hourlyActive: '每小时自主更新中',
    monitoredProviders: '监控模型厂商：',
    totalIndexed: '已收录快讯总数：',
    topStory: '★ 头条深度报道',
    readFullAnalysis: '阅读完整分析',
    primaryWire: '首发技术源：',
    executiveHighlights: '核心要点导读',
    trendingDispatches: '热门资讯榜',
    topSignals: '关键技术信号',
    openSourceRadar: '开源雷达',
    trendingReposTitle: '热门前沿开源 AI 项目',
    trendingReposSub: '基于 GitHub 实时遥测数据 • 每小时更新',
    indieLaunchpadTag: '独立 AI 发射台与小众宝藏项目',
    indieLaunchpadTitle: '活跃维护中的新锐开源仓库',
    indieLaunchpadSub: '星标在 500 以下但提交活跃的独立创新工具与实验性架构。',
    submitRepo: '+ 提交您的项目',
    weeklyDigestTitle: '最新高管战略简报',
    viewAllWeekly: '查看所有每周情报简报 →',
    filterWire: '频道筛选：',
    allDispatches: '全部快讯',
    wireStreamTitle: '全天候快讯流',
    storiesIndexed: '篇报道已收录',
    readAction: '阅读',
    backToDispatches: '返回快讯列表',
    selectLanguage: '选择语言：',
    readInYourLang: '用您的母语阅读：',
    minRead: '分钟深度阅读',
    reportedBy: '整理与技术核实：',
    sourceDocument: '原始权威技术源（直接跳转）',
    openOriginalSource: '前往原始来源文档',
    coreSignals: '核心要点与技术摘要',
    verifyResearchTitle: '是否需要查阅原始技术发布文档？',
    verifyResearchSub: 'Neural Pulse 提供客观技术分析与架构拆解。您可以直接在首发平台阅读完整论文或发布说明：',
    visitPrimary: '查看原始文档',
    filedUnder: '分类归档：',
    relatedStories: '继续阅读前沿科技报道',
    catLLM: '大语言模型与基座架构',
    catResearch: 'AI 前沿学术研究',
    catRobotics: '具身智能与硬件系统',
    catOpenSource: '开源人工智能生态',
    catDigest: '每周情报特辑',
    catIndustry: '产业动态与创新生态',
    footerDesc: '自主人工智能科技期刊。每小时跟踪全球前沿 AI 论文、开源权重与计算集群突破。',
    footerRights: 'Neural Pulse. 自主新闻综合报道。所有内容均严格标明原始出处。',
    footerPublished: '通过 GitHub Pages 托管发布',
    navigationHeading: '导航栏',
    sourcesHeading: '监控源'
  },
  it: {
    latestNews: 'Ultime Notizie',
    trendingRepos: 'Repo di Tendenza',
    emergingAi: 'AI Emergente',
    weeklyDigests: 'Briefing Settimanali',
    categories: 'Categorie',
    about: 'Informazioni',
    rss: 'RSS',
    wireStatus: 'Desk Notizie:',
    hourlyActive: 'Flusso Autonomo Orario Attivo',
    monitoredProviders: 'Fornitori Monitorati:',
    totalIndexed: 'Notizie Totali Indicizzate:',
    topStory: '★ Notizia Principale',
    readFullAnalysis: 'Leggi Analisi Completa',
    primaryWire: 'Fonte Primaria:',
    executiveHighlights: 'Punti Salienti',
    trendingDispatches: 'Notizie di Tendenza',
    topSignals: 'Segnali Chiave',
    openSourceRadar: 'Radar Open Source',
    trendingReposTitle: 'Repository AI di Tendenza e Novità',
    trendingReposSub: 'Curato dalla telemetria di GitHub • Aggiornato ogni ora',
    indieLaunchpadTag: 'Vetrina AI Indipendente e Perle Nascoste',
    indieLaunchpadTitle: 'Repository Emergenti con Sviluppo Attivo',
    indieLaunchpadSub: 'Strumenti AI indipendenti e ricerca sperimentale sotto 500 stelle con commit attivi.',
    submitRepo: '+ Invia Repository',
    weeklyDigestTitle: 'Ultimo Briefing Esecutivo',
    viewAllWeekly: 'Visualizza Tutti i Briefing Settimanali →',
    filterWire: 'Filtra Notizie:',
    allDispatches: 'Tutte le Notizie',
    wireStreamTitle: 'Flusso Continuo di Notizie',
    storiesIndexed: 'Notizie Indicizzate',
    readAction: 'Leggi',
    backToDispatches: 'Torna alle Notizie',
    selectLanguage: 'Seleziona Lingua:',
    readInYourLang: 'Leggi nella tua lingua:',
    minRead: 'minuti di lettura approfondita',
    reportedBy: 'Curato e Verificato da',
    sourceDocument: 'Documento Fonte Primario (Collegamento Diretto)',
    openOriginalSource: 'Apri Fonte Originale',
    coreSignals: 'Sintesi Esecutiva e Segnali Chiave',
    verifyResearchTitle: 'Vuoi consultare la pubblicazione tecnica originale?',
    verifyResearchSub: 'Neural Pulse fornisce analisi oggettive. Puoi leggere il documento completo sulla piattaforma originale:',
    visitPrimary: 'Visita Documento Primario',
    filedUnder: 'Archiviato in:',
    relatedStories: 'Continua a Leggere Notizie di Frontiera',
    catLLM: 'Grandi Modelli Linguistici',
    catResearch: 'Ricerca in Intelligenza Artificiale',
    catRobotics: 'Robotica e Hardware',
    catOpenSource: 'AI Open Source',
    catDigest: 'Briefing Settimanale',
    catIndustry: 'Industria e Startup',
    footerDesc: 'Il giornale autonomo di intelligenza artificiale. Monitoraggio continuo di modelli avanzati e hardware.',
    footerRights: 'Neural Pulse. Sintesi autonoma. Tutte le fonti citate direttamente.',
    footerPublished: 'Pubblicato tramite GitHub Pages',
    navigationHeading: 'Navigazione',
    sourcesHeading: 'Fonti Monitorate'
  },
  de: {
    latestNews: 'Neueste Nachrichten',
    trendingRepos: 'Trend-Repositories',
    emergingAi: 'Aufstrebende KI',
    weeklyDigests: 'Wöchentliche Briefings',
    categories: 'Kategorien',
    about: 'Über uns',
    rss: 'RSS',
    wireStatus: 'Nachrichtenredaktion:',
    hourlyActive: 'Stündlicher Autonomer Ticker Aktiv',
    monitoredProviders: 'Überwachte Anbieter:',
    totalIndexed: 'Indexierte Meldungen Insgesamt:',
    topStory: '★ Top-Nachricht',
    readFullAnalysis: 'Vollständige Analyse Lesen',
    primaryWire: 'Primäre Quelle:',
    executiveHighlights: 'Wesentliche Höhepunkte',
    trendingDispatches: 'Trend-Meldungen',
    topSignals: 'Wichtige Signale',
    openSourceRadar: 'Open-Source-Radar',
    trendingReposTitle: 'Trendende & Neue KI-Repositories',
    trendingReposSub: 'Stündlich aus GitHub-Telemetrie kuratiert',
    indieLaunchpadTag: 'Unabhängige KI-Startrampe & Geheimtipps',
    indieLaunchpadTitle: 'Aufstrebende & Aktiv Gepflegte Repositories',
    indieLaunchpadSub: 'Unabhängige KI-Tools und experimentelle Forschung unter 500 Sternen mit aktiven Commits.',
    submitRepo: '+ Repo Einreichen',
    weeklyDigestTitle: 'Aktuelles Executive-Briefing',
    viewAllWeekly: 'Alle Wöchentlichen Briefings Anzeigen →',
    filterWire: 'Ticker Filtern:',
    allDispatches: 'Alle Meldungen',
    wireStreamTitle: 'Kontinuierlicher Nachrichtenticker',
    storiesIndexed: 'Meldungen Indexiert',
    readAction: 'Lesen',
    backToNews: 'Zurück zur Übersicht',
    backToDispatches: 'Zurück zur Übersicht',
    selectLanguage: 'Sprache Auswählen:',
    readInYourLang: 'In Ihrer Sprache lesen:',
    minRead: 'Minuten Tiefenanalyse',
    reportedBy: 'Zusammengestellt & Verifiziert von',
    sourceDocument: 'Primäres Quelldokument (Direktlink)',
    openOriginalSource: 'Originalquelle Öffnen',
    coreSignals: 'Wesentliche Erkenntnisse & Zusammenfassung',
    verifyResearchTitle: 'Möchten Sie die originale Veröffentlichung einsehen?',
    verifyResearchSub: 'Neural Pulse bietet sachliche Analysen. Sie können die vollständige Arbeit direkt beim Primäranbieter lesen:',
    visitPrimary: 'Primärdokument Aufrufen',
    filedUnder: 'Kategorie:',
    relatedStories: 'Weitere Spitzenforschung Lesen',
    catLLM: 'Große Sprachmodelle & Basissysteme',
    catResearch: 'KI-Spitzenforschung',
    catRobotics: 'Robotik & Hardware-Systeme',
    catOpenSource: 'Open-Source-KI-Ökosystem',
    catDigest: 'Wöchentliches Briefing',
    catIndustry: 'Industrie & Startups',
    footerDesc: 'Das autonome Journal für künstliche Intelligenz. Stündliche Überwachung weltweiter Spitzenforschung und Open-Source-Modelle.',
    footerRights: 'Neural Pulse. Autonome Nachrichtensynthese. Alle Quellen direkt zitiert.',
    footerPublished: 'Veröffentlicht über GitHub Pages',
    navigationHeading: 'Navigation',
    sourcesHeading: 'Überwachte Feeds'
  }
};
