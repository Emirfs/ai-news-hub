---
title: "Frozen in Time: How a Physics Foundation Model Forgets Under Sim-to-Real Adaptation"
description: "Scientific foundation models (SciFMs) have achieved remarkable performance on a wide range of PDEs, including the ability to efficiently adapt to unseen data distributions with additional finetuning."
pubDate: 2026-11-02
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.40857"
sourceName: "arXiv (cs.LG)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.LG). It has not been independently fact-checked by Neural Pulse.

Scientific foundation models (SciFMs) have achieved remarkable performance on a wide range of PDEs, including the ability to efficiently adapt to unseen data distributions with additional finetuning. As with all neural architectures, finetuning such models comes with the risk of catastrophic forgetting, whereby adapting to new tasks degrades prior knowledge of the model. We study catastrophic forgetting in Walrus-1.3B, a SciFM for continuum dynamics, over the course of a two-stage sim-to-real adaptation: first finetuning on simulated flow around a cylinder and then adapting to experimental data of the same system. We find that finetuning on the simulations rapidly degrades rollout performance on the original pretraining datasets, with one-step errors increasing up to 35x after just 20 epochs. Subsequent adaptation to real data further erodes performance on the simulated task. We characterize the potential drivers of forgetting, such as dataset dependence and task representation similarity.

[Read the original source](https://arxiv.org/abs/2610.40857) for the full context.
