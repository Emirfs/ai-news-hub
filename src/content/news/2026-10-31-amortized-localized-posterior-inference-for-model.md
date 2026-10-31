---
title: "Amortized Localized Posterior Inference for Model Calibration with Application to an Ocean Turbulence Closure"
description: "Model discrepancy may prevent a single calibration parameter from reproducing a physical response across the context domain."
pubDate: 2026-10-31
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.37731"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Model discrepancy may prevent a single calibration parameter from reproducing a physical response across the context domain. In addition, uncertainties in observations and contexts affect calibration and must be accounted for and quantified. We construct a family of localized posteriors by weighting observation likelihoods according to their proximity to a target context. Gaussian localization weights incorporate context uncertainty through covariance inflation, with reflection at domain boundaries and an optional correction for uneven context sampling. A conditional normalizing flow approximates the family of posteriors through amortized variational inference. Integrating the localized posteriors under a prescribed context measure gives the marginalized parameter distribution. In a twin experiment with the Branin-Hoo model, we compare global and localized inference under uniform and skewed context distributions. Localization reduces the reported aggregate predictive errors relative to the global posterior.

[Read the original source](https://arxiv.org/abs/2610.37731) for the full context.
