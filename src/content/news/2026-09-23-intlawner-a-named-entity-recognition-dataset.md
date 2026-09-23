---
title: "IntLawNER: A Named Entity Recognition Dataset and Benchmark in International Law"
description: "International law provides the normative framework through which states coordinate action, regulate armed conflict, and protect human rights, yet its texts remain without token-level named entity recognition (NER) resources."
pubDate: 2026-09-23
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.22529"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

International law provides the normative framework through which states coordinate action, regulate armed conflict, and protect human rights, yet its texts remain without token-level named entity recognition (NER) resources. We introduce IntLawNER, a NER dataset and benchmark for codified sources of international law, covering 2,987 gold-annotated sentences and 8,094 entity spans from International Court of Justice (ICJ) decisions, UN Security Council resolutions, and European Court of Human Rights (ECtHR) judgments, annotated with seven institution-specific entity types. We construct IntLawNER with a cost-effective hybrid algorithmic-agentic pipeline that reduces 468k source sentences to a compact annotation set through candidate retrieval, LLM-based vetting, and human review, with 89.6% of gold spans accepted unchanged from the silver layer. However, the silver-to-gold analysis reveals that human-machine aggregate agreement metrics can be misleading in domain-specific NER: Cohen&#x27;s kappa=0.964 on boundary-matched spans masks a macro-F1 of 0.753 when missing entities, boundary errors, and label corrections are included.

[Read the original source](https://arxiv.org/abs/2609.22529) for the full context.
