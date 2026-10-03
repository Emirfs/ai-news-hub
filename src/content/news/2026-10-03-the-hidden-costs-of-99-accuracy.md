---
title: "The Hidden Costs of 99% Accuracy: A Trustworthiness Audit of the Telco Customer Churn Benchmark"
description: "Customer churn prediction on the IBM Telco Customer Churn benchmark (n = 7,043) routinely reports test accuracies above 95%, with the most cited published study reporting 99.01%."
pubDate: 2026-10-03
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.00118"
sourceName: "arXiv (cs.LG)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.LG). It has not been independently fact-checked by Neural Pulse.

Customer churn prediction on the IBM Telco Customer Churn benchmark (n = 7,043) routinely reports test accuracies above 95%, with the most cited published study reporting 99.01%. We audit this benchmark for four trustworthiness failures invisible to the accuracy- and F1-centred reporting that dominates the literature. First, pre-split SMOTE inflates churn-class F1 by 13.1 percentage points across ten classifiers and fifteen seeds (Wilcoxon p 0.95 pre-modelling diagnostic. Third, in a 15-seed calibration audit, isotonic regression is the strongest default; temperature scaling fails on class-weighted tree ensembles whose predicted-probability distribution is bimodal. Fourth, the cost-optimal decision threshold (under a 50 USD retention offer and 24-month CLV proxy) is approximately 5-10 times lower than the F1-optimal threshold, saving approximately 77,000 USD per 1,000 customers. We replicate F1 and F2 on Iranian Telecom Churn (within domain) and Bank Customer Churn (across domain): F1 generalises; F2 generalises only within telecom.

[Read the original source](https://arxiv.org/abs/2610.00118) for the full context.
