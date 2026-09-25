---
title: "Pistis Technical Report"
description: "We introduce the Pistis model family, comprising 27B- and 9B-parameter multimodal large language models built on Qwen3.6 and Qwen3.5, respectively, and developed through a general and scalable post-training framework."
pubDate: 2026-09-25
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.28554"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

We introduce the Pistis model family, comprising 27B- and 9B-parameter multimodal large language models built on Qwen3.6 and Qwen3.5, respectively, and developed through a general and scalable post-training framework. The framework first establishes a strong foundation through large-scale multimodal supervised fine-tuning (SFT). Building on this SFT foundation, we propose Interleaved Distillation and Reinforcement Learning (IDRL), a novel post-training paradigm that tightly integrates on-policy distillation and reinforcement learning within a single training loop. By alternating between the two objectives, rather than optimizing either in isolation or combining them in a static joint loss, IDRL enables more effective knowledge transfer, greater optimization stability, and more precise credit assignment for long-horizon agentic trajectories, leading to stronger performance while mitigating common capability trade-offs.

[Read the original source](https://arxiv.org/abs/2609.28554) for the full context.
