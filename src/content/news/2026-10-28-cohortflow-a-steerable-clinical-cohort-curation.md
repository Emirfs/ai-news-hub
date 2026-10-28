---
title: "CohortFlow: A Steerable Clinical Cohort Curation Agent with Localized Semantic Correction"
description: "Language model agents for clinical cohort curation should accommodate evolving eligibility criteria without repeatedly processing unchanged requirements."
pubDate: 2026-10-28
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.36100"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Language model agents for clinical cohort curation should accommodate evolving eligibility criteria without repeatedly processing unchanged requirements. We introduce CohortFlow, a steerable agent that represents natural language corrections as localized updates to a structured cohort specification and reconciles them with a persistent execution graph. Explicitly recorded semantic dependencies enable affected computations to be selectively invalidated while preserving valid prior results. On 100 scenarios derived from clinical-trial eligibility criteria, comprising 126 correction turns, localized steering achieves 77.0% requirement micro-F1 versus 76.4% for full regeneration using the same 8B model, a small numerical advantage that is not statistically significant ($p=0.493$). It reduces mean correction latency by 64.8% after completion and 44.3% during execution, with 38.1% fewer model calls. In a separate proof-of-concept evaluation over MIMIC, all 13 cohort states execute successfully, while correction trajectories demonstrate selective preservation of unaffected computations and recomputation of changed or dependent nodes.

[Read the original source](https://arxiv.org/abs/2610.36100) for the full context.
