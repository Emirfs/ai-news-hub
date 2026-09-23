import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { getPath } from '../utils/url';

export async function GET(context: APIContext) {
  const news = await getCollection('news');
  const sortedNews = news
    .filter((post) => post.data.sourcePolicy === 'primary')
    .sort((a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime());

  return rss({
    title: 'Neural Pulse | Source-linked AI news',
    description: 'Dated AI stories linked to official sources. Claims are not independently verified.',
    site: context.site || 'https://example.github.io',
    items: sortedNews.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      link: getPath(`/news/${post.id.replace(/\.md$/, '')}/`),
      categories: [post.data.category, ...(post.data.tags || [])],
    })),
    customData: `<language>en-us</language>`,
  });
}
