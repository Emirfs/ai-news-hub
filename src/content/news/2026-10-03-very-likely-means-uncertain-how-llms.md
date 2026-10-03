---
title: "\"very likely\" Means \"uncertain\"? How LLMs Diverge from Humans in Linguistic Uncertainty Quantification"
description: "Humans express uncertainty verbally via markers (e.g., \"possible,\" \"likely\"), yet most LLM uncertainty quantification (UQ) relies on costing likelihood- or consistency-based signals."
pubDate: 2026-10-03
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.00083"
sourceName: "arXiv (cs.LG)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.LG). It has not been independently fact-checked by Neural Pulse.

Humans express uncertainty verbally via markers (e.g., &quot;possible,&quot; &quot;likely&quot;), yet most LLM uncertainty quantification (UQ) relies on costing likelihood- or consistency-based signals. From a cognitive perspective, accurate verbal uncertainty reflects metacognitive monitoring, representing knowledge boundaries (&quot;knowing that you don&#x27;t know&quot;) to support regulation and information seeking. In this paper, we investigate how LLMs diverge from humans in verbal uncertainty quantification and whether verbal markers can reliably quantify LLM uncertainty. We curate a corpus of human uncertainty markers from psychology and decision-science literature and benchmark LLMs against it. We observe that LLMs encode verbal uncertainty with numerical levels that differ substantially from those of humans. We then introduce METHODNAME, a novel optimization-based algorithm that learns an optimal uncertainty profile over uncertainty markers directly from LLM outputs. By fitting a marker-uncertainty mapping to best explain empirical correctness, METHODNAME discovers how much probability mass each verbal marker should convey, rather than estimating uncertainty via repeated sampling.

[Read the original source](https://arxiv.org/abs/2610.00083) for the full context.
