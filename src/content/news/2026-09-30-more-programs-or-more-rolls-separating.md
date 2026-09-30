---
title: "More Programs or More Rolls? Separating Coverage from Specialization in LLM Harnesses"
description: "Automated generation of LLM harnesses promises to improve inference through task specialization."
pubDate: 2026-09-30
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.35873"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Automated generation of LLM harnesses promises to improve inference through task specialization. Yet additional answer coverage can arise from repeated execution of the same program, making specialization difficult to identify. We introduce a controlled evaluation that separates answer coverage, repeatable task advantages, and gains from pre-execution selection. On 386 MATH-500 tasks, we compare eight generated harnesses plus a baseline with nine byte-identical baseline copies, using three executions per member. Identical programs yield 2.16 percentage points of repeat-averaged oracle headroom. Generated programs exhibit substantially more repeatable score patterns, but these chiefly reveal persistent weaknesses: losses relative to the baseline persist across all three repeats on 100 tasks, while persistent wins occur on only one task and are sensitive to answer extraction. The frozen selector gains 0.00 percentage points, and both populations reach 98.70% oracle coverage at 27 harness executions. Stable complementarity remains unresolved at three repeats. Supporting BIRD traces locate failures in mechanism implementation, activation, and output validity.

[Read the original source](https://arxiv.org/abs/2609.35873) for the full context.
