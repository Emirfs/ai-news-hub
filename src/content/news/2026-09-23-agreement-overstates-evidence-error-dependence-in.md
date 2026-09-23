---
title: "Agreement Overstates Evidence: Error Dependence in LLM Judge Consensus"
description: "Researchers report correlated errors among LLM judges, so agreement between judges may overstate the evidence."
pubDate: 2026-09-23
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.22512"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Consensus among LLM judges is often taken as strong evidence that a decision is correct. This assumes that judges make their errors independently. In practice, LLM judges are often trained and evaluated in similar ways, so they can make the same mistakes. We study how this dependency affects the reliability of consensus. We find substantial error correlation across both open-weight and frontier LLM judges. In our main bank of ten judges, the average pairwise correlation between judge errors is 0.21. As a result, the ten judges only provide roughly as much statistical information as 3.5 independent judges. The dependency is even stronger among the high-accuracy frontier judges we evaluate, including judges from different providers. In up to 28% of our comparisons, ignoring shared errors leads to the conclusion that one system is significantly better, while accounting for them does not. We also find that the pattern of errors matters. Errors shared by most judges and errors concentrated among a smaller group affect consensus differently and favor different voting methods. Measuring the overall amount of correlation alone is therefore insufficient.

[Read the original source](https://arxiv.org/abs/2609.22512) for the full context.
