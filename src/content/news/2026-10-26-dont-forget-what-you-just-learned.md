---
title: "Don't Forget What You Just Learned: Self-Directed Repair Turns Agent Mistakes Into Lasting Lessons"
description: "Intelligent agents should learn from their mistakes so that experience leads to continuous improvement."
pubDate: 2026-10-26
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.31846"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Intelligent agents should learn from their mistakes so that experience leads to continuous improvement. Yet today&#x27;s agents recover from a mistake only temporarily: in-context reflections are easily forgotten across sessions and compete for limited context, while full-parameter fine-tuning is expensive and can interfere with existing capabilities. We introduce Self-Direction, a mechanism for agents to learn from mistakes that combines the benefits of temporary in-context retries and policy updates. When an agent fails a task, it reflects on its own trajectory in order to extract a lesson and immediately distills it into a lightweight low-rank adapter. By keeping the original weights frozen, Self-Direction prevents adapter training from overwriting base-model parameters while training additional parameters equivalent to ~0.02% of the base model&#x27;s parameter count for each adapter. The agent then saves these adapters in a persistent library of lessons, automatically routing them to solve related problems later.

[Read the original source](https://arxiv.org/abs/2610.31846) for the full context.
