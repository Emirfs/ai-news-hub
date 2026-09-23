import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const news = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/news" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    category: z.string().default('AI & Tech'),
    tags: z.array(z.string()).default([]),
    author: z.string().default('Neural Pulse AI'),
    sourceUrl: z.string().url().optional().or(z.literal('')),
    sourceName: z.string().optional().or(z.literal('')),
    isWeeklyDigest: z.boolean().default(false),
    sourcePolicy: z.literal('primary').optional(),
    keyTakeaways: z.array(z.string()).default([]),
    translations: z.record(
      z.string(),
      z.object({
        title: z.string(),
        description: z.string(),
        keyTakeaways: z.array(z.string()).default([]),
        body_html: z.string().optional(),
      })
    ).optional(),
  }),
});

export const collections = { news };
