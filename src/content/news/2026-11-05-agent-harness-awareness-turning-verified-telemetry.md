---
title: "Agent Harness Awareness: Turning Verified Telemetry into Operational Control for Tool-Using Agents"
description: "Tool descriptions tell an agent what an action can do, but they do not necessarily reveal whether that action is healthy or suitable at the moment of use."
pubDate: 2026-11-05
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.05391"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Tool descriptions tell an agent what an action can do, but they do not necessarily reveal whether that action is healthy or suitable at the moment of use. Execution harnesses often possess this information through monitors, traces, and recent failures while the model choosing the next action does not. We call this gap operational blindness. We introduce Agent Harness Awareness, a trust-separated design in which the host supplies a small, fresh, verified state snapshot before a consequential action while retaining measurement, enforcement, evaluation, and final dispatch authority. We test its tools-and-network instance with ToolRoute, a controlled isolation benchmark that holds the task and candidate semantics constant and varies the operational information available to the model. In a 216-decision ablation across GPT-5.6 Sol, Claude Sonnet 5, and Gemini 3.7 Flash, verified tool-health state reduced mean observable policy regret by 96.9% against a same-shape neutral control (4,252 ms to 131 ms) and raised single-dispatch completion from 69.4% to 95.8%.

[Read the original source](https://arxiv.org/abs/2611.05391) for the full context.
