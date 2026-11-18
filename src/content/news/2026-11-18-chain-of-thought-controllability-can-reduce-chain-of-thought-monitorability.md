---
title: "Chain-of-Thought Controllability Can Reduce Chain-of-Thought Monitorability"
description: "Chain-of-thought (CoT) monitoring is a promising tool for detecting hidden goals, off-task behavior, and other failures in AI agents."
pubDate: 2026-11-18
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.21799"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Chain-of-thought (CoT) monitoring is a promising tool for detecting hidden goals, off-task behavior, and other failures in AI agents. One risk is that models could deliberately shape their reasoning to make it opaque to monitors. We stress-test this risk through persona-control training: supervised fine-tuning on mathematical reasoning traces rewritten in the voices of diverse personas. This induces a broader ability to control CoT, even though training contains no monitor-evasion examples. In covert side-task evaluations, traces in which a gpt-oss-20b model organism completes the hidden side task contain less monitorable evidence than the base model&#x27;s. Averaged across evaluations and CoT lengths, weighted by side-task-success counts, the CoT monitorability metric g-mean$^2$ falls from 0.94 for the base model to 0.68 for the model organism without a hiding instruction, and to 0.22 when explicitly instructed to hide. In intervention evaluations, explicit hiding often drives monitorability near zero.

[Read the original source](https://arxiv.org/abs/2611.21799) for the full context.
