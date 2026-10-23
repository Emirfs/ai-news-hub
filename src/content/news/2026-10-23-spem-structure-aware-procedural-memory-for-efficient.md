---
title: "SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents"
description: "LLM-based agents increasingly rely on reusable skills."
pubDate: 2026-10-22
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.26995"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

LLM-based agents increasingly rely on reusable skills. However, scaling skill libraries makes efficient and accurate skill use difficult. Full skill loading incurs high token and runtime overhead. In contrast, flat semantic retrieval treats skills as independent text entries, ignoring dependencies, execution order, state transitions, and data flow constraints. We propose SPEM, a lightweight structure-aware procedural memory framework for efficient skill use in LLM-based agents. SPEM maintains Atomic Skill Memory for individual skills and Skill-DAG Memory for reusable compositions derived from successful executions. For a new task, SPEM reuses high-confidence Skill-DAG templates when available. Otherwise, it retrieves atomic skills and invokes Skill-GNN for state- and structure-aware skill selection. Successful executions are written back as new Skill-DAGs, allowing procedural memory to accumulate over time. Experiments on ALFWorld and SkillsBench show that SPEM achieves the best overall effectiveness--efficiency trade-off, reaching 87.1% ALFWorld success and 38.38% SkillsBench reward while reducing token and runtime costs against strong baselines.

[Read the original source](https://arxiv.org/abs/2610.26995) for the full context.
