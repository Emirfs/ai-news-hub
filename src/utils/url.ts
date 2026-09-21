/**
 * Helper to ensure internal links always respect Astro's base path on GitHub Pages
 * (e.g. /ai-news-hub/news/slug/ instead of /news/slug/).
 */
export function getPath(path: string): string {
  const rawBase = import.meta.env.BASE_URL || '/';
  const base = rawBase.replace(/\/$/, '');
  const cleanPath = path.startsWith('/') ? path : `/${path}`;
  return `${base}${cleanPath}`;
}
