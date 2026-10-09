---
title: "An Explainable Header-Centric Framework for Large-Scale Semantic Table Interpretation and Data Quality Assessment"
description: "Knowledge Graph (KG) quality depends not only on downstream graph validation, but also on the quality of tabular metadata used before integration."
pubDate: 2026-10-09
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.10541"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Knowledge Graph (KG) quality depends not only on downstream graph validation, but also on the quality of tabular metadata used before integration. In metadata-only Semantic Table Interpretation (STI), where cell values are unavailable, noisy, or unsuitable, column headers become a critical source of semantic evidence for traceable KG preparation. We present an explainable, header-centric framework for metadata-only Column Type Annotation (CTA) and Data Quality Assessment (DQA). The framework maps headers to 39 interpretable FinalFormat types using curated lexical resources and preserves token-level traceability through SourceKeywords. Each assigned type activates validation rules based on a taxonomy of Data Quality Issues (DQIs), producing detections such as missing data, duplicates, domain violations, wrong data type, and temporal mismatch. These detections are aggregated into HeadersIQ, a lightweight, unweighted data source-level quality metric. The framework was evaluated across heterogeneous benchmarks, including UCI, Prague, Kaggle, VizNet/Sato, SOTAB, T2Dv2, and the SemTab 2024 Metadata-to-KG track, comprising around 120,000 header columns.

[Read the original source](https://arxiv.org/abs/2610.10541) for the full context.
