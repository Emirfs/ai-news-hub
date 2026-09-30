---
title: "CRC-Router: Risk-Constrained Routing for Medical Agentic AI Systems"
description: "Agentic AI systems are increasingly being explored in medical imaging to improve throughput and reduce clinician workload; however, safe deployment remains challenging because autonomous errors may propagate into downstream clinical decisions."
pubDate: 2026-09-29
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.30714"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Agentic AI systems are increasingly being explored in medical imaging to improve throughput and reduce clinician workload; however, safe deployment remains challenging because autonomous errors may propagate into downstream clinical decisions. A central requirement is therefore not only strong predictive performance, but also a reliable routing mechanism that determines when the system should proceed autonomously and when a case should be escalated for further review. To address this gap, we propose CRC-Router, a risk-constrained, uncertainty-aware routing module that is applicable to both conventional medical prediction models and agentic medical AI systems. CRC-Router combines multiple complementary uncertainty signals with the predictive score to construct a per-finding routing feature vector, maps this vector to an estimated wrong-accept risk using a lightweight per-finding risk model, and then applies Conformal Risk Control (CRC) to calibrate acceptance thresholds under a user-specified risk target.

[Read the original source](https://arxiv.org/abs/2609.30714) for the full context.
