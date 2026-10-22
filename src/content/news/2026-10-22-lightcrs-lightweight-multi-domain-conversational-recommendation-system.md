---
title: "LightCRS: Lightweight Multi-Domain Conversational Recommendation System"
description: "Conversational recommender systems have recently adopted vision-language models to match user dialogue intents with multimodal product information."
pubDate: 2026-10-22
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.26948"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Conversational recommender systems have recently adopted vision-language models to match user dialogue intents with multimodal product information. However, extending these methods to many product domains faces a dilemma: deploying a separately adapted VLM per domain scales cost linearly with the number of domains and requires routing each dialogue to the right model, while naively merging all domains into a single VLM degrades accuracy because product characteristics vary widely across categories. We propose LightCRS, a lightweight, query-conditioned framework for unified multi-domain multimodal conversational recommendation. LightCRS precomputes multimodal product representations once offline with frozen encoders. Online, a compact 5.3M-parameter module fuses this evidence for each dialogue via query-conditioned cross-attention, whose parameters are shared across all domains, and compares candidates jointly with an inter-candidate Transformer. To enable rigorous evaluation, we construct MM-R2A-25, a 25-domain benchmark pairing natural Reddit recommendation-seeking conversations with Amazon product listings.

[Read the original source](https://arxiv.org/abs/2610.26948) for the full context.
