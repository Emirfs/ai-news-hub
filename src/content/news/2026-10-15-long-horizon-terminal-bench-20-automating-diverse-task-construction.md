---
title: "Long-Horizon-Terminal-Bench 2.0: Automating Diverse Task Construction and Measuring Sustained Agent Progress"
description: "Long-horizon terminal benchmarks measure whether an agent can sustain progress through extended workflows with process rewards, not only whether its final state passes a binary check."
pubDate: 2026-10-15
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.14146"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Long-horizon terminal benchmarks measure whether an agent can sustain progress through extended workflows with process rewards, not only whether its final state passes a binary check. We present Long-Horizon-Terminal-Bench 2.0 (LHTB 2.0), an extension of Long-Horizon-Terminal-Bench that preserves its 46 original tasks while correcting task and evaluation-infrastructure defects and extending 31 tasks. LHTB 2.0 contains 77 tasks across 13 domains and eight task types. The extended tasks are produced through a systematic reconstruction-task pipeline. We start from a working scientific or engineering artifact, then use a parameterized reference implementation to generate multiple scenarios, reveal six as behavioral evidence, hold out three for evaluation, and use dense progress ladders to reward partial progress while preventing memorization of public outputs. We also extend the evaluation horizon from 90 minutes to three hours and record verifier checkpoints every 30 minutes, enabling direct measurement of sustained progress within a run.

[Read the original source](https://arxiv.org/abs/2610.14146) for the full context.
