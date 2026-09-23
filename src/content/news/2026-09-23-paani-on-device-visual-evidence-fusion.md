---
title: "PAANI : On Device Visual Evidence Fusion and Explainable Guidance for River Robot Simulation"
description: "Mobile river monitoring robots must interpret obstacles and water boundaries that geographic waypoints alone cannot describe."
pubDate: 2026-09-23
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.22353"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Mobile river monitoring robots must interpret obstacles and water boundaries that geographic waypoints alone cannot describe. On resource constrained platforms, converting imperfect visual predictions into timely and inspectable guidance is a distinct challenge. An object label or steering command does not explain which evidence supports a decision or when that evidence is unreliable. We present PAANI, an on-device perception to guidance architecture that combines a project trained YOLO11n detector and a custom MobileNetV3 Small semantic segmenter with timestamp aligned evidence fusion on Arduino UNO Q. Bounded tracking supplies object persistence, while an explicit corridor policy combines surface labels, accepted detections, urgency and mask uncertainty. Each final advisory exposes its contributing evidence and policy reasons. ROS 2 interfaces connect the local AI pipeline to a separate Gazebo vessel, localization and control testbed. Training uses 10,000 WaterScenes images for four-class detection and 1,127 MaSTr1325 images for segmentation, including 198 segmentation validation images. The selected FP32 ONNX models occupy 14.817 MB.

[Read the original source](https://arxiv.org/abs/2609.22353) for the full context.
