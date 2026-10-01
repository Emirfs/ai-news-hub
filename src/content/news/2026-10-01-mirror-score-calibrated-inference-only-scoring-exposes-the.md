---
title: "Mirror-Score: Calibrated, Inference-only Scoring Exposes the Limits of Sequence-compatibility Ranking in D-peptide Design"
description: "D-peptides combine protease resistance with high target specificity, but computational design of D-peptide binders remains immature."
pubDate: 2026-09-30
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.36057"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

D-peptides combine protease resistance with high target specificity, but computational design of D-peptide binders remains immature. Mirror-Peptidizer introduced an in silico mirror-image screening pipeline using target reflection, backbone generation, and ProteinMPNN sequence design, but its raw ProteinMPNN negative log-likelihood (NLL) ranking was not validated against measured affinities, and only 4 of 9 tested MDM2 designs bound detectably. We introduce Mirror-Score, a calibrated, inference-only scoring framework for heterochiral D-peptide/L-protein complexes, and a public benchmark of 31 crystal complexes across four target families, including 18 with literature-verified affinities. Raw ProteinMPNN NLL is not a valid affinity ranker: its pooled Spearman correlation with affinity is 0.19, and correlations reverse between MDM2/CHIP (+0.62) and gp41 (-0.70). We therefore evaluate Boltz-2 mirror-space cofolding confidence.

[Read the original source](https://arxiv.org/abs/2609.36057) for the full context.
