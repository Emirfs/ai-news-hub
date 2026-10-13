---
title: "CLEAT: Learning Value-Guided Clarification for Interactive Agents"
description: "LLM agents can execute increasingly complex tasks, but effective assistance also requires aligning their actions with goals and constraints that users may leave unstated."
pubDate: 2026-10-13
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.12655"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

LLM agents can execute increasingly complex tasks, but effective assistance also requires aligning their actions with goals and constraints that users may leave unstated. We study this problem as interactive intent alignment through clarification. Yet clarification is useful only when the agent can turn the answer into better decisions. As training changes how the agent handles incomplete information and uses additional answers, the same clarification can become more or less useful. We introduce CLEAT (CLarification through valuE-guided Agent co-Training), a framework that co-trains a clarification-value controller and the task policy from shared interaction outcomes. We formulate residual query value to measure the task utility gained by asking rather than proceeding under the current policy, and estimate it through paired rollouts from the same interaction history. These paired returns train the controller to predict clarification value and the task policy to select useful questions and act on the answers.

[Read the original source](https://arxiv.org/abs/2610.12655) for the full context.
