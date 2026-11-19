---
title: "Language Models Can Rewrite Their Own Weights"
description: "Language models are trained once, frozen and deployed: improving one again takes another training run, and a prompt, a scaffold or extra computation at inference is gone once the task ends."
pubDate: 2026-11-18
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.21885"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Language models are trained once, frozen and deployed: improving one again takes another training run, and a prompt, a scaffold or extra computation at inference is gone once the task ends. A frontier model has been shown to edit the weights of a much smaller one. We ask whether a model can rewrite its own weights to make itself better, and find that it can, by its own reasoning, with no gradients and no training; we call this self-rewriting. Given its weights, graded answers and the ability to run itself, a 27B model diagnoses its failure and edits the weights behind it. It surpasses itself: its own edit makes it 6.6 points more accurate on 490 problems it never saw, in a test fixed in advance, and another session&#x27;s edit also makes it significantly better. It keeps getting better: it submits an edit only when its own tests support it, each edit replacing the last, and over its first eight such sessions its accuracy only rises. Unlike test-time scaling, the gain persists in its weights and adds no cost per answer; unlike training, it needs no pre- or post-training infrastructure, only an open model and hours on one GPU.

[Read the original source](https://arxiv.org/abs/2611.21885) for the full context.
