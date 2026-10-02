---
title: "Measuring the Microtask Eligibility Gap: When Is an Off-the-Shelf SLM Enough for an Agent Harness?"
description: "Agent harnesses increasingly want to run small language models (SLMs) on the microtasks around a frontier large language model (LLM) planner: auto-approving shell commands, writing memory, selecting tools, ranking past turns."
pubDate: 2026-10-02
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.00025"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Agent harnesses increasingly want to run small language models (SLMs) on the microtasks around a frontier large language model (LLM) planner: auto-approving shell commands, writing memory, selecting tools, ranking past turns. We ask whether off-the-shelf SLMs meet practitioner-defined thresholds and, when they fail, why, and whether quantization changes the answer. We build a benchmark of 4 such microtasks with fixed prompts and automatic metrics, each with a pre-specified threshold $\tau$ anchored to a cheap non-LLM baseline and a CI-aware eligibility rule (a configuration passes only if its confidence bound clears $\tau$). Sweeping Qwen3 0.6/1.7/4/8B at their best (FP16, greedy, one frozen prompt, no tuning), we find an eligibility gap: 0 of 16 (4 tasks $\times$ 4 models) configurations pass (verified by checking the raw outputs and parser behavior). A logprob decision-threshold diagnostic (T1/T3/T4; T2 via a context-length/cascade probe) separates the failures into capability deficits and failures that can be addressed by changing the decoding threshold (4 regimes).

[Read the original source](https://arxiv.org/abs/2610.00025) for the full context.
