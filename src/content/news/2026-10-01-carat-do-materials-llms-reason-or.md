---
title: "CARAT: Do Materials LLMs Reason or Recite?"
description: "When a materials LLM answers a question about crystal structure, does it reason from the structure or copy an answer already printed in its input?"
pubDate: 2026-10-01
category: "AI Research"
tags: []
author: "Neural Pulse AI"
sourceUrl: "https://arxiv.org/abs/2609.38340"
sourceName: "arXiv (cs.AI)"
isWeeklyDigest: false
sourcePolicy: primary
keyTakeaways: []
---

### Source-attributed summary

This summary uses the published excerpt from arXiv (cs.AI). It has not been independently fact-checked by Neural Pulse.

When a materials LLM answers a question about crystal structure, does it reason from the structure or copy an answer already printed in its input? Accuracy cannot tell: a structural description often prints the very field it is scored against. CARAT holds question and gold answer fixed across eight matched views, names each structural relation separately in GraphSpace, and adds matched fine-tuning, answer masking, evidence injection, paired inference, and a rule that can withhold claims. First, on the benchmark&#x27;s hardest families the grounded view is worth 17.3 points over formula inputs. Second, we turn that scrutiny on ourselves. GraphSpace beats a plain periodic graph by 19.3 points, but that margin is two effects at once: where the plain rendering carries everything the question needs it is 1.96 points, and where it omits those fields entirely, 46.7 points. The headline mostly measures what the baseline lacked, not how evidence is presented. Third, we attack our own benchmark. A rule that skips the link and reads the list directly answers four of seven hardened families, so we rebuilt it until eleven such shortcuts sat near chance.

[Read the original source](https://arxiv.org/abs/2609.38340) for the full context.
