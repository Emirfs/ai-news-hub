---
title: "Replication Without Persistence in Hosted LLMs: Measurement Sensitivity in Action-Time Belief Evaluation"
description: "Behavioural evaluations of hosted language models can vary because the evaluated service, the measurement instrument, or both differ across runs."
pubDate: 2026-09-23
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.22478"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Behavioural evaluations of hosted language models can vary because the evaluated service, the measurement instrument, or both differ across runs. We separate three validation questions: whether a prior finding recurs on fresh data under its historical configuration (replication), whether the endpoint changes when the evaluation-and-inference configuration is rebuilt under the same identifier (measurement sensitivity), and whether the finding persists across subsequently tested identifiers under one common instrument (persistence). We study these questions in Regent Chess, a sequential environment in which a hidden, mutable state is recorded exactly, allowing stated beliefs to be scored against ground truth at action time; positive endpoint values mean worse performance than a matched-uniform comparator. The previously reported Gemini 3.1 Flash-Lite deficit recurs on fresh games under its historical configuration (+0.0530, 95% CI [+0.0329,+0.0714]).

[Read the original source](https://arxiv.org/abs/2609.22478) for the full context.
