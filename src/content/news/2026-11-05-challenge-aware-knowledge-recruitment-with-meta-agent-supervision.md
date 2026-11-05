---
title: "Challenge-Aware Knowledge Recruitment with Meta-Agent Supervision for Medical Multi-Agent Reasoning"
description: "Large language models perform strongly on standard medical QA but degrade on harder reasoning tasks, where multi-agent debate often fails to beat strong single-model prompting."
pubDate: 2026-11-05
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.05393"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Large language models perform strongly on standard medical QA but degrade on harder reasoning tasks, where multi-agent debate often fails to beat strong single-model prompting. We argue that a key limitation is that existing systems select experts and retrieve knowledge from the question alone, rather than from gaps that emerge during reasoning. We propose challenge-aware adaptive recruitment: an external CHALLENGER inspects the evolving reasoning trace and identifies specific factual or expertise gaps. These signals trigger targeted knowledge retrieval or mid-discussion specialist recruitment. On the MEDAGENTSBENCH hard subset (862 questions across nine biomedical datasets), upfront retrieval provides little benefit, while challenge-aware in-between retrieval performs better; on a multi-specialist backbone it improves accuracy on 8 of 9 datasets and adds 6 percentage points over Challenger Only. Ablations indicate benefits from both retrieval timing and gap-specific query signals, and a live web-search experiment shows that the timing advantage persists across retrieval backends.

[Read the original source](https://arxiv.org/abs/2611.05393) for the full context.
