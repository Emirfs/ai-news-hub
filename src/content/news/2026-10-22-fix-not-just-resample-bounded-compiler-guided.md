---
title: "Fix, Not Just Resample: Bounded Compiler-Guided Repair in Lean 4"
description: "Automated theorem provers often rely on sampling language models, but proof assistants like Lean reject each failed step with a precise error message --- information that pure sampling discards."
pubDate: 2026-10-22
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2610.26942"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

Automated theorem provers often rely on sampling language models, but proof assistants like Lean reject each failed step with a precise error message --- information that pure sampling discards. To overcome this, we introduce a bounded, online step-level repair module. Our search samples $K$ candidate tactics at each step and repairs a failed tactic at most $R$ times. Instead of discarding failed tactics, we feed the compiler&#x27;s error message to a pretrained repair model to fix individual rejected steps in place. This approach improves the solve rate over a sampling-only baseline across all tested candidate budgets ($K \in \{1,3,5,8\}$), achieving up to a $32\%$ relative gain and solving $82$ additional theorems on a $1{,}990$-theorem subset of the LeanDojo benchmark. Repair is not free: it trades extra runtime for reachable proofs. But the trade is predictable: repair pays most when sampling is constrained; its return is front-loaded, with the first repair attempt capturing $84\text{--}96\%$ of the total gain; and the gain comes almost entirely from shallow tactic-execution failures rather than structural errors such as type mismatches.

[Read the original source](https://arxiv.org/abs/2610.26942) for the full context.
