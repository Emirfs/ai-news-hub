---
title: "Where the Tokens Go: Heat, Entropy and Error in Agentic Coding"
description: "Coding agents are billed by the token, yet software engineering says nothing about what a token actually buys."
pubDate: 2026-11-20
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2611.23375"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Coding agents are billed by the token, yet software engineering says nothing about what a token actually buys. Here we introduce a theory of software thermodynamics. The theory draws analogues from classical and stochastic thermodynamics, extends them, and applies them to modern agentic coding. We count the tokens an agent generates as its cost and divide that cost into work and heat. The test suite acts as a software Maxwell&#x27;s daemon that judges every coding change. We test the theory with an analogue of the experiments in which a single molecule is pulled open and let fold again: an agent makes a change to a repository (coding) and then undoes it (uncoding), many times over, and we count the tokens of every model call. The cycle returns the requested edits to where they began, with each direction started from a stored reference tree, and the spread of its cost over repeated cycles defines a software temperature, which rose with the sampling temperature of the model. About 80 per cent of the tokens of a successful run are generated in model calls that leave the requested change where it was, and we call these tokens heat.

[Read the original source](https://arxiv.org/abs/2611.23375) for the full context.
