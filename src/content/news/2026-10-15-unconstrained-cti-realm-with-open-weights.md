---
title: "Unconstrained CTI-REALM with Open-Weights"
description: "Organisations that want language-model agents for security work face a choice between open-weight models, which they can run and audit themselves, and far more expensive closed frontier models."
pubDate: 2026-10-15
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.14180"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Organisations that want language-model agents for security work face a choice between open-weight models, which they can run and audit themselves, and far more expensive closed frontier models. We study that choice on CTI-REALM (arXiv:2603.13517), a benchmark in which an agent turns a threat-intelligence report into a working detection by querying a live telemetry store. We evaluate twenty-six models, nineteen open-weight and seven closed, under a common harness, scorer and panel of LLM judges. Our main finding is that an open-weight model can match the strongest closed models at less than a tenth of their cost, provided it is given enough turns. The benchmark&#x27;s published limit on agent messages is a confound: a task that exhausts the limit scores zero on every checkpoint, including those it had already passed, so results at that limit partly measure which models finish in time. At the published limit the leading open-weight and closed models cannot be distinguished. With the limit relaxed, the models it was truncating recover, and the highest rewards belong to open-weight models.

[Read the original source](https://arxiv.org/abs/2610.14180) for the full context.
