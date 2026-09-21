import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const news = await getCollection('news');
  const sortedNews = news.sort(
    (a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime()
  );

  return rss({
    title: 'Neural Pulse | Autonomous AI & Tech Chronicle',
    description: 'Autonomous AI and tech dispatches, frontier model breakthroughs, and weekly intelligence briefings.',
    site: context.site || 'https://example.github.io',
    items: sortedNews.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      link: `/news/${post.id.replace(/\.md$/, '')}/`,
      categories: [post.data.category, ...(post.data.tags || [])],
    })),
    customData: `<language>en-us</language>`,
  });
}
