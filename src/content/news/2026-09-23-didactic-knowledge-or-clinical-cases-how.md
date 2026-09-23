---
title: "Didactic knowledge or Clinical Cases? How Data Types Shape Medical Large Language Models"
description: "Medical large language models are commonly trained on mixtures of didactic data (e.g., textbooks) and clinical data (e.g., patient records), yet how these data types differentially shape model capabilities remains unclear."
pubDate: 2026-09-23
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.22161"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Medical large language models are commonly trained on mixtures of didactic data (e.g., textbooks) and clinical data (e.g., patient records), yet how these data types differentially shape model capabilities remains unclear. We address this issue with token-matched experiments that vary the didactic-to-clinical ratio and analyze how data composition affects performance, capability profiles, and error patterns across knowledge-intensive and clinic-oriented tasks. We uncover an asymmetric transfer across task types: clinical data improves clinic-oriented tasks while remaining competitive on knowledge-intensive ones, whereas didactic data mainly improves knowledge-intensive tasks. Error analysis suggests a knowing-doing gap, where improvements in knowledge recall do not reliably generalize to clinical reasoning. We further observe that modest amounts of clinical data yield most of the gains on EHR-grounded tasks, while the optimal mixture ratio varies with the knowledge and clinical reasoning demands of downstream tasks.

[Read the original source](https://arxiv.org/abs/2609.22161) for the full context.
