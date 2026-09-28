---
title: "ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?"
description: "Agents are increasingly deployed with real autonomy in web application and network penetration testing, where a single out-of-scope action can breach a client's engagement boundary."
pubDate: 2026-09-28
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.30325"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Agents are increasingly deployed with real autonomy in web application and network penetration testing, where a single out-of-scope action can breach a client&#x27;s engagement boundary. Existing offensive-security benchmarks measure raw hacking capability; as those benchmarks saturate, the real barrier to deployment is a special case of alignment: scope adherence. We introduce ScopeBench, a benchmark of 30 dead-end agentic security tasks in which the stated objective is reachable only by violating the stated scope. Each task appears under two conditions that share an environment, verifier, and objective and differ only in scope: one instruction set has no scope and measures capability; the other has a natural-language scope to measure adherence. Scopeless trajectories are graded by a standard deterministic verifier. Scoped trajectories pass through two grading arms. First, the same deterministic verifier checks for the flag: because the flag sits behind the scope boundary, a pass proves by construction that a forbidden action occurred, yielding a high-precision lower bound on the violation rate.

[Read the original source](https://arxiv.org/abs/2609.30325) for the full context.
