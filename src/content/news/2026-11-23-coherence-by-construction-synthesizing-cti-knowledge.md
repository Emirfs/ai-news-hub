---
title: "Coherence by Construction: Synthesizing CTI Knowledge Graphs and the Formal Limits of Coherence Validation"
description: "Synthesizing relational training data such as knowledge graphs with a large language model typically emits structured objects one at a time, which keeps each object valid but leaves the relationships between them ungrounded."
pubDate: 2026-11-23
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.26717"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Synthesizing relational training data such as knowledge graphs with a large language model typically emits structured objects one at a time, which keeps each object valid but leaves the relationships between them ungrounded. We study an alternative paradigm, generation by simulation: rather than describing a relational artifact, we simulate a process that produces it and take the artifact to be its causal record. Language-model agents propose intent and a deterministic referee resolves outcomes against an explicit world model, so a relation is emitted only when the event it represents occurs, making coherence a property of construction. We instantiate the paradigm for cyber threat intelligence knowledge graphs in the STIX 2.1 standard with three engines, among them an evolutionary engine applying language-model genetic operators to structured graph genomes, sharing a deterministic compiler that makes malformed and dangling output unrepresentable. We prove referential closure, causal grounding, and identifier stability, an ablation localizes each to the referee and world model rather than the policy, and two independent LLM judges reproduce the rubric&#x27;s engine ranking.

[Read the original source](https://arxiv.org/abs/2611.26717) for the full context.
