---
title: "Constraint-Aware Test-Time Scoring for LLM and VLM Candidate Selection"
description: "When an LLM or VLM produces several candidate answers, picking the best one usually relies on the model's own confidence, a learned judge model, or a domain check."
pubDate: 2026-11-27
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.33161"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

When an LLM or VLM produces several candidate answers, picking the best one usually relies on the model&#x27;s own confidence, a learned judge model, or a domain check. Each has a known weakness: an answer can be fluent but insecure, mathematically plausible but physically infeasible, or rated highly by a judge while quietly breaking a task requirement. We propose a scoring framework that combines a small set of hard checks every answer must pass with a wider set of softer checks whose scores are blended into one number per candidate. This adaptive scoring framework consists of three components: a drafting model that produces the candidates, a configuring model that selects and weights the checks for each task, and scoring models that rate properties no grounded tool can compute. We apply our proposed method to four tasks: writing code that is both correct and secure (CWEval), generating robot manipulation plans (LIBERO with added safety variants), passing competitive-programming hidden tests (LiveCodeBench), and answering questions from retrieved documents (HotpotQA).

[Read the original source](https://arxiv.org/abs/2611.33161) for the full context.
