---
title: "FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving"
description: "Prefill-decode disaggregation is becoming a common architecture for LLM serving because it separates two phases with distinct execution patterns and SLO objectives."
pubDate: 2026-10-07
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.06917"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Prefill-decode disaggregation is becoming a common architecture for LLM serving because it separates two phases with distinct execution patterns and SLO objectives. Existing systems typically combine a fixed prefill/decode worker ratio with request routing across workers. However, real-world workloads exhibit both short bursts and sustained shifts in the prefill-to-decode demand ratio. As a result, a configuration that is well provisioned at one time may quickly become mismatched, causing latency SLO violations even when idle capacity exists elsewhere. Existing autoscaling mechanisms can add capacity, but they react slowly, require spare GPUs, and do not directly address short-timescale phase imbalance. We present FluidPD, a P/D-disaggregated serving system that provides SLO-aware in-place elasticity. FluidPD introduces two complementary mechanisms. FluidToken handles transient imbalance by offloading a bounded portion of prefill computation to decode workers when decode-side slack is available. FluidRole handles sustained imbalance by reassigning running workers between prefill and decode roles in place, avoiding model reload and engine restart.

[Read the original source](https://arxiv.org/abs/2610.06917) for the full context.
