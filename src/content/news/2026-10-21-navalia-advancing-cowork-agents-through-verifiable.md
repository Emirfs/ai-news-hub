---
title: "Navalia: Advancing Cowork Agents through Verifiable Task Synthesis and Long-Horizon Post-Training"
description: "Large language model (LLM) agents are evolving from conversational assistants into Cowork Agents capable of autonomous planning, tool use, and complex task execution."
pubDate: 2026-10-21
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.26887"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Large language model (LLM) agents are evolving from conversational assistants into Cowork Agents capable of autonomous planning, tool use, and complex task execution. Financial analysis requires these agents to integrate cross-document evidence and perform multistep numerical reasoning, but expert task authoring is costly, while direct LLM synthesis struggles to produce challenging tasks with reliable answers. We introduce Navalia, a framework for Cowork Agents that combines verifiable task synthesis with long-horizon post-training. Using corporate financial reports as its data source, Navalia semantically selects supporting evidence from complete fact sets and constructs executable computation chains to generate analytical tasks with traceable evidence and actual data dependencies between steps. We further use independent LLM review and programmatic checks to verify evidence consistency and answer correctness. The verified tasks are then used for trajectory collection, cold-start supervised fine-tuning (SFT), and reinforcement learning (RL) to improve long-horizon task execution.

[Read the original source](https://arxiv.org/abs/2610.26887) for the full context.
