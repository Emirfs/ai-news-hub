---
title: "Pretrained ASR Pseudo-labeling for Noisy Police Audio"
description: "Pretrained ASR systems perform poorly on noisy Broadcast Police Communication (BPC), hindering efforts to understand police decision-making."
pubDate: 2026-09-28
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.30469"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Pretrained ASR systems perform poorly on noisy Broadcast Police Communication (BPC), hindering efforts to understand police decision-making. Pseudo-labeling offers an unsupervised path to improve ASR without expensive human labels, but the efficacy of this approach on very noisy domains is not known. In this work, we systematically assess the opportunities and limits of pseudo-labeling to adapt foundation ASR models (Whisper and Qwen3-ASR) to noisy BPC domain corpora from Baltimore and Chicago. We demonstrate that existing internal confidence metrics (log-probabilities and STAR scores) fail to distinguish between high and low quality BPC pseudo-labels, and we introduce an external LLM-as-a-judge filtering paradigm that leverages parametric knowledge to discard contextually implausible transcripts. Our LLM-judging filters more aggressively than internal metrics and significantly reduces WER of the pseudo-labeled training sets across the Baltimore and Chicago BPC corpora, though a substantial gap remains relative to an oracle filter.

[Read the original source](https://arxiv.org/abs/2609.30469) for the full context.
