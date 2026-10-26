---
title: "Permission to Retry: A Study of Authorization and Recovery in AI Agent Workflows"
description: "A durable agent can resume a consequential action while its authority changes and the action's external outcome remains uncertain."
pubDate: 2026-10-26
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.31916"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

A durable agent can resume a consequential action while its authority changes and the action&#x27;s external outcome remains uncertain. We study execution-time reliability of tool-using AI agents, isolating recovery decisions from language-model behavior. Checkpoint state, permission to dispatch, evidence of an external effect and permission to reconcile are distinct obligations. We present a finite conformance study that checks these obligations through histories scored against a provider effect ledger hidden from the recovering application. A prospectively frozen campaign executes 336 histories on native LangGraph and Temporal hosts, crossing 14 schedules, three provider contracts and four matched application policies. All 168 paired host cells have identical checked outcomes. Per host, retained-ledger reconciliation passes all 42 histories: 21 checked completions, 15 denials and six unknown outcomes with reservations retained. Cached retry, revalidation before retry and stable-key retry pass 30, 36 and 31 histories respectively.

[Read the original source](https://arxiv.org/abs/2610.31916) for the full context.
