export type Language = 'en' | 'tr' | 'es' | 'zh' | 'it' | 'de';

export interface TranslationDict {
  latestNews: string;
  weeklyDigests: string;
  categories: string;
  about: string;
  trendingRepos: string;
  indieLaunchpad: string;
  readAnalysis: string;
  readFullReport: string;
  keyTakeaways: string;
  originalSource: string;
  openOriginal: string;
  allDispatches: string;
  filterWire: string;
  newsDesk: string;
  hourlyActive: string;
  readingTime: string;
  backToNews: string;
  filedUnder: string;
  relatedStories: string;
  submitRepo: string;
  languageName: string;
}

export const translations: Record<Language, TranslationDict> = {
  en: {
    latestNews: 'Latest News',
    weeklyDigests: 'Weekly Briefings',
    categories: 'Categories',
    about: 'About',
    trendingRepos: 'Trending Repos',
    indieLaunchpad: 'Indie AI Launchpad',
    readAnalysis: 'Read Analysis',
    readFullReport: 'Read Full Analysis',
    keyTakeaways: 'Executive Summary & Key Signals',
    originalSource: 'Primary Technical Wire',
    openOriginal: 'Open Original Source Document',
    allDispatches: 'All Dispatches',
    filterWire: 'Filter Wire:',
    newsDesk: 'News Desk:',
    hourlyActive: 'Hourly Autonomous Wire Active',
    readingTime: 'min read',
    backToNews: 'Back to Dispatches',
    filedUnder: 'Filed under:',
    relatedStories: 'Continue Reading Frontier News',
    submitRepo: '+ Submit Your Repo',
    languageName: 'English'
  },
  tr: {
    latestNews: 'Son Haberler',
    weeklyDigests: 'Haftalık Bültenler',
    categories: 'Kategoriler',
    about: 'Hakkında',
    trendingRepos: 'Trend Repolar',
    indieLaunchpad: 'Yükselen Bağımsız AI',
    readAnalysis: 'Analizi Oku',
    readFullReport: 'Detaylı Haberi Oku',
    keyTakeaways: 'Yönetici Özeti ve Önemli Çıkarımlar',
    originalSource: 'Orijinal Birincil Kaynak',
    openOriginal: 'Orijinal Kaynak Habere Git',
    allDispatches: 'Tüm Haberler',
    filterWire: 'Akış Filtrele:',
    newsDesk: 'Haber Masası:',
    hourlyActive: 'Saatlik Otonom Akış Aktif',
    readingTime: 'dk okuma',
    backToNews: 'Haber Akışına Dön',
    filedUnder: 'Kategori:',
    relatedStories: 'Gündemdeki Diğer Gelişmeler',
    submitRepo: '+ Projenizi Gönderin',
    languageName: 'Türkçe'
  },
  es: {
    latestNews: 'Últimas Noticias',
    weeklyDigests: 'Resúmenes Semanales',
    categories: 'Categorías',
    about: 'Acerca de',
    trendingRepos: 'Repos Populares',
    indieLaunchpad: 'Lanzadera de IA Independiente',
    readAnalysis: 'Leer Análisis',
    readFullReport: 'Leer Análisis Completo',
    keyTakeaways: 'Resumen Ejecutivo y Puntos Clave',
    originalSource: 'Fuente Técnica Primaria',
    openOriginal: 'Abrir Documento Fuente Original',
    allDispatches: 'Todos los Despachos',
    filterWire: 'Filtrar Flujo:',
    newsDesk: 'Mesa de Noticias:',
    hourlyActive: 'Flujo Autónomo Horario Activo',
    readingTime: 'min de lectura',
    backToNews: 'Volver a los Despachos',
    filedUnder: 'Archivado en:',
    relatedStories: 'Continuar Leyendo Noticias de Vanguardia',
    submitRepo: '+ Enviar Repositorio',
    languageName: 'Español'
  },
  zh: {
    latestNews: '最新新闻',
    weeklyDigests: '每周简报',
    categories: '分类目录',
    about: '关于本站',
    trendingRepos: '热门开源仓库',
    indieLaunchpad: '独立 AI 项目发射台',
    readAnalysis: '阅读分析',
    readFullReport: '阅读完整深度分析',
    keyTakeaways: '核心要点与执行摘要',
    originalSource: '原始技术来源',
    openOriginal: '前往原始来源文档',
    allDispatches: '所有快讯',
    filterWire: '筛选频道：',
    newsDesk: '新闻台：',
    hourlyActive: '每小时自主更新中',
    readingTime: '分钟阅读',
    backToNews: '返回快讯列表',
    filedUnder: '分类于：',
    relatedStories: '继续阅读前沿科技报道',
    submitRepo: '+ 提交开源项目',
    languageName: '中文'
  },
  it: {
    latestNews: 'Ultime Notizie',
    weeklyDigests: 'Briefing Settimanali',
    categories: 'Categorie',
    about: 'Informazioni',
    trendingRepos: 'Repo di Tendenza',
    indieLaunchpad: 'Vetrina AI Indipendente',
    readAnalysis: 'Leggi Analisi',
    readFullReport: 'Leggi Analisi Completa',
    keyTakeaways: 'Sintesi Esecutiva e Punti Chiave',
    originalSource: 'Fonte Tecnica Primaria',
    openOriginal: 'Apri Documento Fonte Originale',
    allDispatches: 'Tutte le Notizie',
    filterWire: 'Filtra Notizie:',
    newsDesk: 'Desk Notizie:',
    hourlyActive: 'Flusso Autonomo Orario Attivo',
    readingTime: 'min di lettura',
    backToNews: 'Torna alle Notizie',
    filedUnder: 'Archiviato in:',
    relatedStories: 'Continua a Leggere Notizie di Frontiera',
    submitRepo: '+ Invia Repository',
    languageName: 'Italiano'
  },
  de: {
    latestNews: 'Neueste Nachrichten',
    weeklyDigests: 'Wöchentliche Briefings',
    categories: 'Kategorien',
    about: 'Über uns',
    trendingRepos: 'Trend-Repositories',
    indieLaunchpad: 'Unabhängige AI-Startrampe',
    readAnalysis: 'Analyse Lesen',
    readFullReport: 'Vollständige Analyse Lesen',
    keyTakeaways: 'Wesentliche Erkenntnisse & Zusammenfassung',
    originalSource: 'Primäre Technische Quelle',
    openOriginal: 'Originalquelle Öffnen',
    allDispatches: 'Alle Meldungen',
    filterWire: 'Ticker Filtern:',
    newsDesk: 'Nachrichtenredaktion:',
    hourlyActive: 'Stündlicher Autonomer Ticker Aktiv',
    readingTime: 'Min. Lesezeit',
    backToNews: 'Zurück zur Übersicht',
    filedUnder: 'Kategorie:',
    relatedStories: 'Weitere Spitzenforschung Lesen',
    submitRepo: '+ Repo Einreichen',
    languageName: 'Deutsch'
  }
};
