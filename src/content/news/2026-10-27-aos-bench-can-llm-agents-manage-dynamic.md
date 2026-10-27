---
title: "AOS-Bench: Can LLM Agents Manage Dynamic Workloads?"
description: "Coding agents are moving from handling one request at a time to serving as persistent assistants to which users hand a stream of work: a build, a data-processing job and a bug fix may all be pending on the same machine at once."
pubDate: 2026-10-27
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.33178"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Coding agents are moving from handling one request at a time to serving as persistent assistants to which users hand a stream of work: a build, a data-processing job and a bug fix may all be pending on the same machine at once. Such an agent must decide when to take on new tasks, how to delegate and overlap them, and how to stay within the machine&#x27;s CPU and memory. Existing benchmarks cannot measure this, because they evaluate each task in isolation. We introduce \benchname{}, which evaluates an agent system as a workload manager: verified tasks arrive over time and must be delivered under shared CPU and memory limits, and the same tasks run one at a time serve as a per-system reference. Across five model--harness pairs, isolated task success does not carry over evenly. On heavy workloads every system loses 13 to 23 points. On medium workloads, systems span 11 points in isolated success but 26 points in stream success, and two systems 0.6 points apart in isolation deliver 54\% and 68\% of the same tasks. Execution-policy interventions trace much of this gap to task intake: serial dispatch leaves 73\% of heavy-workload tasks unclaimed.

[Read the original source](https://arxiv.org/abs/2610.33178) for the full context.
