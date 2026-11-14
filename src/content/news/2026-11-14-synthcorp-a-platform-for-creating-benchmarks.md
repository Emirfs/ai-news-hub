---
title: "SynthCorp: A Platform for Creating Benchmarks for Data Agents"
description: "Current benchmarks for LLM-driven data agents saturate quickly and cannot target specific capabilities."
pubDate: 2026-11-14
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.14765"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Current benchmarks for LLM-driven data agents saturate quickly and cannot target specific capabilities. We present SynthCorp, a platform that creates customizable data estates and benchmarks by simulating how business events produce and modify corporate data over time. Each data estate combines relational databases, a document store, and a data catalog, paired with evaluation tasks and executable gold programs. First, given a scenario and target complexity dimensions, SynthCorp synthesizes reusable event types and compiles each into a program over predefined simulation primitives. Second, SynthCorp schedules event instances on a virtual calendar, interleaving routine and disruption events so that tables, documents, and catalog entries remain consistent. Third, SynthCorp executes the calendar to materialize the data estate and records every operation in a simulation log. Fourth, SynthCorp generates analytical tasks and derives verified gold programs from the log. We use SynthCorp to generate initial evaluation benchmarks comprising seven data estates (up to 1K operational tables) and 256 tasks across five domains.

[Read the original source](https://arxiv.org/abs/2611.14765) for the full context.
