---
title: "AREX-2: Advancing Self-Improving Agents through Long-Horizon Reflective Tasks"
description: "We present AREX-2, an effort to advance the self-improving capability of LLM agents, which we define as the ability to iteratively refine a solution at test time."
pubDate: 2026-10-01
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.38288"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

We present AREX-2, an effort to advance the self-improving capability of LLM agents, which we define as the ability to iteratively refine a solution at test time. This ability rests on two complementary capabilities: reflection, which produces a solution better than the current one, and long-horizon execution, which keeps the iteration effective over many rounds. We hypothesize that both capabilities are domain-agnostic, and can therefore be learned in scenarios that are well suited for supervision. Accordingly, we synthesize long-horizon improvement trajectories from machine learning and algorithmic programming tasks, two domains that offer verifiable feedback and reward sustained iteration. Trained on this data, our agent, built on Qwen3.8-27B, achieves strong results on MLE-bench Lite (81.8) and Frontier-CS (70.7), transfers to deep research with 84.0 on BrowseComp, 52.6 on HLE, 92.2 on GAIA, and 93.8 on DeepSearchQA, and keeps improving as its budget of rounds grows. These results show that long-horizon reflective data is an effective route toward self-improving agents.

[Read the original source](https://arxiv.org/abs/2609.38288) for the full context.
