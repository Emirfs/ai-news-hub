---
title: "Goal-driven Variant Categorization"
description: "Process discovery rarely yields a single coherent process structure."
pubDate: 2026-09-23
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.22475"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Process discovery rarely yields a single coherent process structure. For analysis, a common step is to cluster process variants based on structural similarity and then assign business meaning to the resulting groups. Since these partitions are not derived from the organization&#x27;s goals, analysts must manually interpret and consolidate variants into business-meaningful categories. This judgment-intensive step becomes increasingly difficult as the number and complexity of variants grow. In this paper, we propose a goal-driven approach to variant categorization that reverses this workflow. We first author an organization&#x27;s goal model that predefines the categorization axis. Each variant is transformed into a textual narrative describing its behavior, and a Large Language Model (LLM) interprets it in the context of the goal model and assigns the variant to the most appropriate category. LLM-based semantic reasoning connects low-level process behavior with analyst-defined business goals. We instantiate this approach end-to-end and evaluate it on three public logs differing substantially in scale and behavioral diversity.

[Read the original source](https://arxiv.org/abs/2609.22475) for the full context.
