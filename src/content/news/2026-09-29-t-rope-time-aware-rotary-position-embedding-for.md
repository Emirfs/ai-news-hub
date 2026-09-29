---
title: "T-RoPE: Time-Aware Rotary Position Embedding for Sequential Recommendation"
description: "Large-scale recommenders increasingly adopt the sequential generative recipe behind large language models, bringing the Transformer into recommendation along with design choices made for text, including Rotary Position Embedding (RoPE)."
pubDate: 2026-09-29
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.30576"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Large-scale recommenders increasingly adopt the sequential generative recipe behind large language models, bringing the Transformer into recommendation along with design choices made for text, including Rotary Position Embedding (RoPE). In language models, RoPE encodes token indices for relative position reasoning, but in recommendation, an interaction index records only event order, saying nothing about elapsed time, behavioral cycles across scales, or calendar phase. We revisit this choice and propose T-RoPE, a time-aware RoPE for sequential generative recommendation that replaces index-only rotation with timestamp-based angles, learnable temporal coefficients, multiscale frequency banks, shifted query alignment, and non-stationary key rotation. We prove that standard RoPE, even on timestamps, remains time-translation invariant and cannot distinguish seasonal contexts, and that T-RoPE breaks this invariance while preserving the RoPE interface. Across five public benchmarks, T-RoPE achieves the best result on every metric on every dataset, improving over the strongest baseline by 78--130\% in HR@10 on the sparse PixelRec data and 8--12\% across metrics on Amazon Books.

[Read the original source](https://arxiv.org/abs/2609.30576) for the full context.
