---
title: "The Harness as the Only Mutable Surface: Compliance-Bounded Self-Evolution of LLM Agents in Credit Pipelines, with a Measured Admission Gate"
description: "Self-improving LLM agents can adapt a credit pipeline to a changed rule, but an agent that rewrites itself destroys the artefact a supervisor reviews: a named change, a recorded test, an approval."
pubDate: 2026-10-09
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.10629"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Self-improving LLM agents can adapt a credit pipeline to a changed rule, but an agent that rewrites itself destroys the artefact a supervisor reviews: a named change, a recorded test, an approval. We argue that self-evolution is reviewable only if it is confined to the runtime harness (instruction text, tool-call logic and primitive composition) while model weights stay fixed, so that every adaptation is a diff with a cause and a test attached. We give a dual-loop engine built on that bound, with one admission gate that writes a hash-chained record before deployment, and we measure the gate in simulation, with a simulated agent and a seeded-search proposer rather than language models. Across three families of supervisory re-interpretation at three severities, 10 seeds each, the gated loop admitted 144 of 7,449 candidate changes, none of which worsened error on held-out history, and restored the false-positive rate to the oracle level without raising missed flags in every low- and mid-severity cell.

[Read the original source](https://arxiv.org/abs/2610.10629) for the full context.
