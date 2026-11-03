---
title: "ANGLER: Verifier-Grounded Benchmarking with an Adaptive Attacker for Web Agents"
description: "Web agents are increasingly deployed to complete tasks autonomously on real websites, where adversarially injected content can induce them to perform unauthorized actions."
pubDate: 2026-11-03
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.41272"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Web agents are increasingly deployed to complete tasks autonomously on real websites, where adversarially injected content can induce them to perform unauthorized actions. Existing evaluations primarily use fixed attacks or focus on a single attack type, and evaluate attacks at the text level rather than through real state changes, thus underestimating how vulnerable agents are to diverse attacks. To address the gap, we introduce REEF, a benchmark of red-teaming executable environments with faithful verification for measuring the security vulnerabilities of web agents. REEF covers 9 verifier-grounded websites spanning travel, commerce, productivity, media, and communication, and pairs every authentic benign task with a malicious objective delivered through 5 attack types at both the user and the environment level. REEF&#x27;s state-based verifiers provide the execution feedback that drives ANGLER, an adaptive near-miss-guided lure evolution framework for red-teaming. Rather than evaluating a fixed attack set, ANGLER uses outcomes from prior rollouts to guide LLM-based attack mutation and candidate selection, prioritizing near-miss seeds during refinement.

[Read the original source](https://arxiv.org/abs/2610.41272) for the full context.
