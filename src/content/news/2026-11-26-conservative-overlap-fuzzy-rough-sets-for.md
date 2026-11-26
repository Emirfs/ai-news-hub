---
title: "Conservative Overlap Fuzzy Rough Sets for Incomplete Data"
description: "Attribute reduction in incomplete information systems is difficult because missing values break the equivalence-class structure of rough set theory."
pubDate: 2026-11-26
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.31329"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Attribute reduction in incomplete information systems is difficult because missing values break the equivalence-class structure of rough set theory. We propose the Conservative Overlap Fuzzy Rough Set (COFRS) model. Each object is described by its set of present attributes. The similarity of two objects is a weighted overlap on the attributes present in both, divided by the fixed number of attributes |A| instead of the size of their union, so missing values are penalised globally and are not matched as wildcards. From this similarity we define a soft dependency degree based on weighted granule consistency, and we search for reducts by greedy backward elimination in O(|U|^2 |A|^2) time. We show that the relation is symmetric and non-reflexive, that the dependency degree is not monotone, and we give a sufficient condition under which monotonicity holds. On 11 UCI benchmarks with missing rates from 0.15% to 20.46%, COFRS gives the smallest reducts on average (4.1 attributes, against 5.0-11.2 for Tolerance-RS, a range-threshold variant Tol-RS_tau, Zhou-RS and the min-aggregation variant COFRS-min).

[Read the original source](https://arxiv.org/abs/2611.31329) for the full context.
