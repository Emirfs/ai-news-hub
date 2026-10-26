---
title: "TACS-RF: Tool-driven Agentic Circuit Synthesis of RF and mmWave Modules"
description: "We present the framework of TACS-RF - a Tool-driven Agentic Circuit Synthesis of RF and mmWave modules."
pubDate: 2026-10-26
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.31882"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

We present the framework of TACS-RF - a Tool-driven Agentic Circuit Synthesis of RF and mmWave modules. In this framework, a large-language-model (LLM) coding agent (Claude Opus 4.8) directly drives industry-standard electronic-design-automation (EDA) tools such as Cadence Virtuoso/Spectre, Calibre, Cadence EMX, and Ansys HFSS to design RF and mmWave modules. We validate the framework through the agentic design of a 240-251 GHz sub-THz transmitter in a 90 nm SiGe BiCMOS process. The agent semi-autonomously designed the sub-blocks including a 60 GHz push-push Colpitts VCO with second-harmonic extraction, multistage differential cascode power drivers, a push-push frequency doubler, a differential bowtie antenna, and all the interstage matching networks. The transmitter chain with parasitic-extracted devices and EM-verified passives delivers +5.1 to +6.3 dBm across an 11 GHz varactor-only tuning range, phase noise of -80 to -88 dBc/Hz at 1 MHz offset while consuming a DC power of 361 mW. We describe the agent-driven design flow and the resulting division of labor between human and agent, taking a step toward a &quot;text-to-ASIC&quot; future for designing RF/mmWave hardware.

[Read the original source](https://arxiv.org/abs/2610.31882) for the full context.
