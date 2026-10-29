---
title: "Don't Pick a Winner: Knowledge Conflicts Need a Prior, Not a Rule"
description: "A retrieval-augmented language model answers from two sources, the retrieved context and its own knowledge, and the two disagree whenever the context is incomplete or wrong."
pubDate: 2026-10-28
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.36169"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

A retrieval-augmented language model answers from two sources, the retrieved context and its own knowledge, and the two disagree whenever the context is incomplete or wrong. Existing methods settle the disagreement with a rule fixed at design time: follow the context, amplify it in proportion to how far it moves the model, or trust the model&#x27;s memory. Each rule is confidently wrong in some deployment. In a decision-theoretic model of two sources, the score of any fixed rule is linear in the share of reliable contexts while the best attainable score is convex, so every fixed rule is beaten wherever it is not exactly optimal; and a symmetric divergence between the two sources, the signal adaptive decoding uses, carries no information about which one is right. Resolving a conflict therefore needs two inputs that no existing method keeps: evidence about each source separately, and a prior on how often the context is right. We test these claims on GRACE, a benchmark that intervenes on the knowledge-graph context of a fixed question, so that what the model knows, what the context says and what is true are measured separately.

[Read the original source](https://arxiv.org/abs/2610.36169) for the full context.
