---
title: "Beyond CLIP: Calibrated (Few-Shot) Defect Detection With System One Decision Models"
description: "Cameras and vision sensors are widely used for product and process inspection in manufacturing environments."
pubDate: 2026-11-03
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.41199"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Cameras and vision sensors are widely used for product and process inspection in manufacturing environments. Traditionally, this process required thousands of images of both nominal and defective products to train such models. Recent research shows that vision transformer (ViT) models, such as CLIP, can reduce this requirement to 50-100 images per nominal and defective class. However, collecting even 50 defective images can be difficult in high-yield or low-volume manufacturing processes. In this paper, we examine the utility of two recently proposed structured decision models (Jev and Clef-Flash) in applications using as few as k=2 reference images per class at inference. In the process, we provide three main contributions: (a) a framework for k-shot learning of these models for image classification/inspection applications; (b) an agentic approach for automatically refining the text descriptions that guide image classification in these decision models; and (c) an approach to calibrate the resulting defect probabilities to improve their reliability for inspection decisions. We test these contributions in five manufacturing case studies.

[Read the original source](https://arxiv.org/abs/2610.41199) for the full context.
