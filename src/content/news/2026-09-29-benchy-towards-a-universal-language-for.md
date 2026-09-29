---
title: "Benchy: towards a universal language for task-oriented AI benchmarks"
description: "Benchy is a semantic language and execution engine for benchmarking AI programs."
pubDate: 2026-09-29
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.30550"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Benchy is a semantic language and execution engine for benchmarking AI programs. A benchmark is completely specified by a program, a scoring function, and a dataset, B=(P,S,D), and is separate from the AI-system taking it; a run binds the two, R=(B,AI). Benchmarks are authored as canonical YAML in which each semantic concept has one valid syntax, classified by a shared task/domain/language ontology, and deterministically compiled into a canonical JSON intermediate representation that the engine executes. Compilation changes representation, not meaning: it does not repair invalid definitions or inject hidden defaults. Programs use fixed schemas of named input and output fields, the leaf output fields are the scoring dimensions, and the engine exposes one universal runtime contract --- a named-field input object in, a named-field output object out --- to which external AI-systems adapt at the boundary, so integration mechanics never propagate into benchmark semantics. This paper gives the semantic object model, the ontology and task-to-program validation rule, the scoring and failure semantics, the compilation and execution architecture, and the scope of the current language.

[Read the original source](https://arxiv.org/abs/2609.30550) for the full context.
