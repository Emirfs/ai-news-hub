---
title: "Speaking the Navigator's Language: Trajectory-Grounded Instruction Translation for Frozen Aerial VLN Agents"
description: "Aerial vision-and-language navigation (VLN) agents are typically trained on detail-rich, trajectory-aligned commands, whereas users issue short, intent-driven instructions; on a frozen OpenFly navigator, this \\emph{instruction gap} drops success rate (SR) from $31.03\\%$ to $11.33\\%$."
pubDate: 2026-10-09
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.10635"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Aerial vision-and-language navigation (VLN) agents are typically trained on detail-rich, trajectory-aligned commands, whereas users issue short, intent-driven instructions; on a frozen OpenFly navigator, this \emph{instruction gap} drops success rate (SR) from $31.03\%$ to $11.33\%$. To scale translator training, we prompt a language model with human-written style examples to convert original commands into paired, intent-centered Weak commands, which yield $15.27\%$ SR. We introduce the \textbf{Trajectory-Grounded Instruction Translator (TGIT)}, a front-end that keeps the navigator frozen and translates Weak inputs into agent-executable commands by learning from its trajectory outcomes. The resulting Weak-trained translator raises Weak-input SR to $37.93\%$ and transfers zero-shot to real human instructions ($11.33\%{\rightarrow}32.51\%$); it also improves held-out OpenFly ($4.95\%{\rightarrow}20.79\%$) and yields recovery on CityNav and AirVLN.

[Read the original source](https://arxiv.org/abs/2610.10635) for the full context.
