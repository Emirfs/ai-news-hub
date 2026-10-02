---
title: "Heavy-Tailed Memory Traces in Long-Horizon Language Agents"
description: "Long-horizon language agents increasingly rely on external memory as a frozen world model, yet current memory systems are usually judged only by task success or token cost."
pubDate: 2026-10-02
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.00010"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Long-horizon language agents increasingly rely on external memory as a frozen world model, yet current memory systems are usually judged only by task success or token cost. We argue that the missing object is the shape of memory use: under finite context and repeated retrieval, agent memory can concentrate on a small core while leaving rare states in a long tail where prediction errors accumulate. We study this effect through a conservative tail audit and find that concentration is reproducible but policy-dependent. Random-walk agents produce log-normal-compatible retrieval artifacts, whereas semantic LLM policies yield the strongest truncated-power-law-compatible core--tail traces. Motivated by this audit, we propose Core--Tail World Model (CTWM), a rank-based memory controller that allocates prompt budget with a single exponent $\tau$ while retaining a summarized tail. On Synthetic Graph World, CTWM preserves full state and transition coverage, reduces prompt tokens by 5.9%, and lowers bottom-half tail prediction error by 13.6% relative to a graph-memory baseline.

[Read the original source](https://arxiv.org/abs/2610.00010) for the full context.
