---
title: "Fast Polynomial Transcendentals for LLMs"
description: "Graphics processing unit (GPU) generations scale matrix, special-function, and memory pipelines at different rates, so kernel bottlenecks move as hardware evolves."
pubDate: 2026-10-03
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.00049"
sourceName: "arXiv (cs.LG)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.LG). It has not been independently fact-checked by Neural Pulse.

Graphics processing unit (GPU) generations scale matrix, special-function, and memory pipelines at different rates, so kernel bottlenecks move as hardware evolves. FlashAttention-4 exposed this imbalance inside attention on NVIDIA Blackwell. We test whether short polynomial programs can accelerate other special-function-unit (SFU) operations in large language models (LLMs). We first compare native PyTorch evaluation with packed fused multiply--add (FMA) programs in an isolated IEEE binary16 (FP16) sweep spanning L2-resident and high-bandwidth-memory (HBM)-resident working sets. We then replace native sigmoid, tanh, and sigmoid linear unit (SiLU) with degree-3 or degree-4 bfloat16 (BF16) programs in four GB200 integration tasks: dense SiLU, tanh-softcapped attention, sigmoid attention, and routed-expert Swish-gated linear unit (SwiGLU). The programs combine analytical symmetry, target-format rounding, and packed arithmetic inside consuming kernels. The isolated paths improve by 1.19--2.19x in L2 and 1.00--1.70x in HBM. The dense-SiLU, tanh-softcapped-attention, and routed-expert substitutions improve complete training-step throughput by 2.7\%, 2.9\%, and 8.0\%, respectively.

[Read the original source](https://arxiv.org/abs/2610.00049) for the full context.
