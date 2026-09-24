---
title: "Are Stated Reasoning Steps Causally Load-Bearing?"
description: "Chain-of-thought (CoT) monitoring assumes that the reasoning a model writes reflects the computation that directly produces its answer."
pubDate: 2026-09-24
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.27038"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Chain-of-thought (CoT) monitoring assumes that the reasoning a model writes reflects the computation that directly produces its answer. Previous faithfulness metrics have been predominantly behavioral, as they simply edit the reasoning text and observe the resulting answer. However, our methodology aims to measure faithfulness causally at the activation level, specifically on self-generated reasoning. Unlike previous causal audits, which measure degradation, our interventions carry a known predicted target. In this way, each patch should switch the answer to a specific counterfactual entity derivable by construction. Specifically, we use synthetic multi-hop lookup tasks (2-6 hops). We patch the residual stream at the token span where the model states each intermediate step with the corresponding activations from a counterfactual run. For Qwen3-4B, 76.9% +/- 2.8% of stated steps are causally load-bearing (CLB) at the most responsive mid-network layer (random-position null: 11.3%; patching the underlying prompt fact: 83%, so stated steps carry approximately 96% of the achievable effect).

[Read the original source](https://arxiv.org/abs/2609.27038) for the full context.
