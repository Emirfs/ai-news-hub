---
title: "Improving OCR Faithfulness via Gated and Attenuated On-Policy Distillation"
description: "Vision-language models may rewrite anomalous text in images into linguistically plausible expressions, compromising OCR transcription faithfulness."
pubDate: 2026-10-01
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.38282"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Vision-language models may rewrite anomalous text in images into linguistically plausible expressions, compromising OCR transcription faithfulness. Sequence-level task rewards and local teacher guidance are complementary, but guidance from the same teacher may not remain equally effective as the student improves. Offline analysis shows that supervision from a fixed teacher becomes progressively less favorable as the student improves, both across training checkpoints and across response groups with different task rewards. Motivated by this observation, we introduce GAD-RL, which adaptively regulates teacher supervision during joint post-training according to the student&#x27;s current task performance and local distributions. A frozen teacher conditions on reference transcriptions and student-generated prefixes. GAD-RL disables distillation for response groups containing an output with task reward at least 0.95 and continuously attenuates distillation strength as group-mean reward increases. It also weights forward KL by the student&#x27;s probability of the teacher&#x27;s Top-1 token, moderating local auxiliary updates when student support for that candidate is low.

[Read the original source](https://arxiv.org/abs/2609.38282) for the full context.
