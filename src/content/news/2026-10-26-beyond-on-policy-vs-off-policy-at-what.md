---
title: "Beyond On-Policy vs. Off-Policy: At What Level Should LLM Agent Distillation Follow the Student?"
description: "Distilling interactive LLM agents requires choosing between teacher-generated demonstrations and student-generated experience, corresponding broadly to off-policy and on-policy distillation."
pubDate: 2026-10-26
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.31918"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Distilling interactive LLM agents requires choosing between teacher-generated demonstrations and student-generated experience, corresponding broadly to off-policy and on-policy distillation. While both have proven effective, we argue that this distinction is inherently hierarchical: the policy that induces an interaction history need not be the same as the policy that generates the token prefix of the current action. We introduce a hierarchical agent distillation framework that formalizes these two levels of on-policiness and enables explicit control over their pairing, mixture proportions, and training schedule. We study this problem through self-distillation, where a frozen teacher has access to task guidance unavailable to the student, and conduct a three-stage controlled study across three models and four interactive environments. We find that student-induced histories paired with teacher-generated action prefixes generally provide the strongest standalone training signal, whereas following the student at both levels generally performs worst. Nevertheless, fully on-policy data becomes beneficial when incorporated into a mixture with other configurations.

[Read the original source](https://arxiv.org/abs/2610.31918) for the full context.
