---
title: "Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable Agent-System Interaction"
description: "Tool-calling agents have become central to enterprise AI, yet training and evaluating them at scale remains severely constrained due to business and legal restrictions on enterprise systems, data, and database schemas."
pubDate: 2026-10-09
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.10549"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Tool-calling agents have become central to enterprise AI, yet training and evaluating them at scale remains severely constrained due to business and legal restrictions on enterprise systems, data, and database schemas. Tabular data synthesis offers a natural alternative, but its effectiveness is fundamentally limited by structural validity and schema availability, while procedure-based approaches yield the opposite weakness, typically lacking distributional fidelity without per-domain authoring. We introduce **Synthesis Through Simulation** (STS), a **schema--free** data synthesis paradigm in which an LLM agent generates data by executing operations against policy-enforcing APIs within simulated enterprise environments. Because data is generated through the same environment that defines what is valid, STS guarantees structural validity by construction while decoupling validity enforcement from distribution modeling, allowing each to be addressed independently.

[Read the original source](https://arxiv.org/abs/2610.10549) for the full context.
