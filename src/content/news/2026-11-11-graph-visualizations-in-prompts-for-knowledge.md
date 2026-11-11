---
title: "Graph Visualizations in Prompts for Knowledge Graph Question Answering"
description: "We study when and how multimodal input improves knowledge graph question answering (KGQA) in large vision--language models."
pubDate: 2026-11-11
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.12938"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

We study when and how multimodal input improves knowledge graph question answering (KGQA) in large vision--language models. Using a controlled evaluation over 1,500 WebQSP and CWQ questions and six VLMs within a fixed KGQA pipeline, we compare text-only prompting against text-plus-graph visualization at the per-question level and analyze performance changes as a function of reasoning complexity, model size, and image layout. Adding a graph image yields an average gain of 1.85 F1 points, driven by strong precision improvements on low-complexity questions (+4.65 F1). Mixed-effects and regression analyses show that these multimodal gains do not depend strongly on model scale, but are highly sensitive to graph layout: image-only settings sharply degrade performance, hierarchical Graphviz layouts outperform less organized renderings, and decomposing large subgraphs into separated paths yields the largest improvements. Taken together, the results indicate that visual prompting primarily aids KGQA by enhancing prediction precision in low-complexity contexts, provided that visual design respects cognitive and perceptual constraints.

[Read the original source](https://arxiv.org/abs/2611.12938) for the full context.
