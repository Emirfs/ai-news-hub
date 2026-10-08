---
title: "EPOCH: Reliable Discovery through Evidence-Governed Search"
description: "AI research agents are increasingly used to search over programs, mathematical constructions, and proofs."
pubDate: 2026-10-08
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.06986"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

AI research agents are increasingly used to search over programs, mathematical constructions, and proofs. However, existing systems typically optimize evaluator feedback without adequately governing how that feedback is interpreted, challenged, and reused. As a result, promising but fragile candidates can be promoted as discoveries, while benchmark improvements, finite certificates, and theorem-level claims are too easily conflated. We introduce EPOCH, an evidence-governed architecture designed to close this gap. EPOCH implements an evidence-governed discovery loop by combining explicit task contracts, typed memory, active falsification, admission checks, and independent replay, so that each candidate is evaluated against the strength and scope of the claim it supports. EPOCH achieves state-of-the-art aggregate performance on AlgoTune, substantially exceeding the strongest baseline in mean normalized score (0.65 vs. 0.53), and attains the highest mean score on the internal Math14 suite (0.57). It further shows favorable held-out behavior under official-test replay and leads the descriptive aggregate on AgentHPO.

[Read the original source](https://arxiv.org/abs/2610.06986) for the full context.
