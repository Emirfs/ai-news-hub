---
title: "IneqAgent: Agentic Inequality Proving in Lean with Symbolic Computation"
description: "Formal inequality proving requires mathematical reasoning and exact computation, often connected through intermediate lemmas and goal reformulations."
pubDate: 2026-10-16
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.20681"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Formal inequality proving requires mathematical reasoning and exact computation, often connected through intermediate lemmas and goal reformulations. We introduce IneqAgent, an agentic framework combining LLM reasoning with symbolic computation for inequality proving in Lean4. Lemma-level Monte Carlo Tree Search coordinates lemma construction, goal reformulation, and symbolic backend selection. Complementary sum-of-squares, Bernstein, and successive difference-substitution backends produce exact certificates for local Lean proof generation. The agent integrates these proofs with LLM-generated steps and uses Lean feedback to construct complete proofs checked against the original theorem statements. On four benchmarks, IneqAgent with DeepSeek-V4-Flash solves 175 of 186 problems (94.09%), achieving the highest overall success rate among the evaluated methods. Across four backbones, it achieves higher success rates at low LLM inference cost thresholds than Direct Agent using the same backbone, with lower mean inference costs over each method&#x27;s successful runs.

[Read the original source](https://arxiv.org/abs/2610.20681) for the full context.
