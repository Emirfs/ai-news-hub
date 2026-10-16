---
title: "ARIA: Runtime Inspection and Amendment for Multi-Agent Systems"
description: "In LLM-based multi-agent systems (MAS), a local mistake can propagate as other agents build on it, turning a correctable error into a failed task."
pubDate: 2026-10-16
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.20780"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

In LLM-based multi-agent systems (MAS), a local mistake can propagate as other agents build on it, turning a correctable error into a failed task. Diagnosing completed runs or repeatedly re-executing them to search for corrections does not provide a learned policy for intervening while execution is still in progress. We present Agent Runtime Inspection and Amendment (ARIA), a framework for learning when and how to repair ongoing multi-agent executions. Our key intuition is to turn execution-verified repairs into reusable supervision, moving repair search into data construction and training so that a learned model can intervene at runtime without repeatedly testing alternatives. First, we collect over 24{,}000 successful and failed trajectories across four multi-agent frameworks, six benchmarks, and eight host models. From these trajectories, we construct the ARIA dataset, to our knowledge the first large-scale dataset pairing failed multi-agent trajectories with execution-verified repairs. It contains 3{,}953 verified repair pairs, each specifying what went wrong, where to intervene, and how execution should continue.

[Read the original source](https://arxiv.org/abs/2610.20780) for the full context.
