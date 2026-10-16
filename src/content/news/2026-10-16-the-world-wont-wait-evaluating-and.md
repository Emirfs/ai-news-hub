---
title: "The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock"
description: "Large language model (LLM) agents can solve complex interactive tasks, yet reasoning and tool calls take time."
pubDate: 2026-10-16
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.20665"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Large language model (LLM) agents can solve complex interactive tasks, yet reasoning and tool calls take time. In continuously changing environments, an otherwise correct action may arrive too late. We introduce RealtimeBench, with 180 tasks across six game types, to evaluate agents while games continue running during inference. Paired evaluations show that GPT-6.1-sol outperforms the faster Jev when games are paused, but falls behind when they keep running. We propose Two-Timescale Offline Recursive Self-Improvement (TORSI): a slow teacher studies failures and tests corrections in paused games between attempts, then writes reusable instructions for a fast student. The student acts without teacher calls during gameplay, and validation scores determine which updates are adopted. Two rounds raise Jev&#x27;s average test score from 13.51 to 24.19 on a 0--100 progress scale, improving all six game types. The instructions also improve average scores for three other models without retuning. These findings point toward real-time intelligence: enabling powerful LLM agents to remain effective in a continuously changing world by organizing deliberation, learning, and action across timescales.

[Read the original source](https://arxiv.org/abs/2610.20665) for the full context.
