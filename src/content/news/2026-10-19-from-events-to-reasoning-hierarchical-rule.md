---
title: "From Events to Reasoning: Hierarchical Rule Composition over Explicit States"
description: "What a reasoning system emits is a conclusion; what it owes is a justification."
pubDate: 2026-10-19
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.22403"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

What a reasoning system emits is a conclusion; what it owes is a justification. Producing one requires every operation to be admissible on the facts actually available, the dependencies of intermediate results to survive to the end of the path, and the path to be revised when a premise changes. We present the Event Reasoning System (ERS), in which the reasoning state is an explicit event graph. Semantic features nominate candidate objects and rule bindings, and declared rule and task conditions decide which may execute, so candidates that violate the represented period, unit, or evidence constraints cannot enter an accepted reasoning path. Low-level rules provide reusable local transformations, and recursively composable high-level control rules organize subgoals and legal paths under the current goal, information gaps, and budget; a finite library is thereby rebound into paths never stored as complete solutions. We formalize admissible transitions, task-dependent control, compositional expressivity, dependency-preserving revision, and the gap between reachable solutions and those a budgeted controller finds.

[Read the original source](https://arxiv.org/abs/2610.22403) for the full context.
