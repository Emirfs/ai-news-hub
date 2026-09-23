import type { ExtensionAPI } from '@oh-my-pi/pi-coding-agent';

const feedUrl = 'https://emirfs.github.io/ai-news-hub/rss.xml';
const intervalMs = 15 * 60 * 1000;

type Story = { title: string; url: string };

function decodeXml(text: string): string {
  return text.replace(/&(?:amp|lt|gt|quot|apos|#\d+);/g, (entity) => {
    const named: Record<string, string> = { '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&apos;': "'" };
    return named[entity] ?? String.fromCodePoint(Number(entity.slice(2, -1)));
  });
}

async function stories(): Promise<Story[]> {
  const response = await fetch(feedUrl, { signal: AbortSignal.timeout(12_000) });
  if (!response.ok) throw new Error(`RSS HTTP ${response.status}`);
  const xml = await response.text();
  if (!xml.includes('<title>Neural Pulse | Source-linked AI news</title>')) {
    throw new Error('The deployed feed has not switched to source-linked articles yet');
  }
  return [...xml.matchAll(/<item\b[^>]*>([\s\S]*?)<\/item>/g)].slice(0, 10).flatMap((match) => {
    const title = match[1].match(/<title>([\s\S]*?)<\/title>/)?.[1];
    const link = match[1].match(/<link>([\s\S]*?)<\/link>/)?.[1];
    if (!title || !link) return [];
    const url = decodeXml(link.trim());
    if (!url.startsWith('https://emirfs.github.io/ai-news-hub/news/')) return [];
    return [{ title: decodeXml(title.trim().replace(/^<!\[CDATA\[|\]\]>$/g, '')), url }];
  });
}

export default function (pi: ExtensionAPI) {
  pi.setLabel('Neural Pulse news alerts');
  let seen: Set<string> | undefined;
  let latest: Story[] = [];

  pi.on('session_start', async (_event, ctx) => {
    const refresh = async () => {
      try {
        const current = await stories();
        if (seen) {
          for (const story of current.slice().reverse()) {
            if (!seen.has(story.url) && ctx.hasUI) {
              ctx.ui.notify(`New AI news: ${story.title}\nRead: ${story.url}\n/news for headlines`, 'info');
            }
          }
        }
        seen = new Set(current.map((story) => story.url));
        latest = current;
      } catch (error) {
        pi.logger.warn(`Neural Pulse feed unavailable: ${String(error)}`);
      }
    };
    await refresh();
    ctx.setInterval(refresh, intervalMs);
  });

  pi.registerCommand('news', {
    description: 'Show recent Neural Pulse headlines and links',
    handler: async (_args, ctx) => {
      if (!latest.length) {
        try { latest = await stories(); } catch (error) { ctx.ui.notify(`News feed unavailable: ${String(error)}`, 'warning'); return; }
      }
      ctx.ui.notify(latest.slice(0, 5).map((story) => `${story.title}\n${story.url}`).join('\n\n') || 'No news yet.', 'info');
    },
  });
}
