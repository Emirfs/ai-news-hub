---
title: "Constant-Memory Recall: Learned Associations in a Fixed Matrix State"
description: "Fixed-size recurrent memory limits storage growth during inference, but successful recall depends on the task and training."
pubDate: 2026-10-03
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.00232"
sourceName: "arXiv (cs.LG)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.LG). It has not been independently fact-checked by Neural Pulse.

Fixed-size recurrent memory limits storage growth during inference, but successful recall depends on the task and training. We study a small DeltaNet variant with fixed token-specific key biases, trained to remember 32 new key-value pairings per sequence. With 32 KiB of recurrent matrix state, it achieves 99.95% mean accuracy across three training seeds when choosing among the sequence&#x27;s values. Recall remains near perfect when filler extends the pre-query context to 1,798 tokens without adding pairings. Zeroing the first memory block removes this recall. An exploratory 48-pair test remains near chance after one quarter of the primary training budget and does not locate a capacity limit. Parameter-matched vector and Transformer baselines remain near chance, including the Transformer after additional training searches. This unresolved baseline failure prevents a memory-efficiency comparison.

[Read the original source](https://arxiv.org/abs/2610.00232) for the full context.
