---
title: "BlockLock: Reproducible LLM Inference with Fixed Batch Geometry"
description: "Reproducible LLM inference requires that a request produces the same output regardless of the other requests in the batch."
pubDate: 2026-11-06
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.06977"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Reproducible LLM inference requires that a request produces the same output regardless of the other requests in the batch. Existing solutions pay for this in different ways: batch-invariant kernels constrain every operator, and isolating prefill with fixed-shape decode ({our CoRun-style baseline}) gives up shared prefill compute and pads decode. We present BlockLock, which keeps shared batched prefill and pins only the numerical path of the protected request: it fixes the geometry that the request sees, with {two modes: BlockLock-Rows uses fixed-width rows and retains batched decode of all requests; BlockLock-Pack uses terminal-anchored packing with an isolated dummy segment, then extracts the protected request&#x27;s KV state for target-only decode. Under a stated per-deployment contract, both modes preserve the target&#x27;s output bitwise when its companions change.} Across five {dense} models (Qwen3-8B/14B, Llama-3.1-8B-Instruct, and Gemma-3-4B/12B-IT) and three single-GPU deployments (NVIDIA A6000, A100, and H100), we evaluate our approach on both tinyBenchmarks and BFCL{; we also include initial tensor-parallel experiments on two NVIDIA A6000 GPUs.

[Read the original source](https://arxiv.org/abs/2611.06977) for the full context.
