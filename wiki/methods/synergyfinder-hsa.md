---
name: SynergyFinder HSA
slug: synergyfinder-hsa
kind: method
canonical_source: corpus
unverified: true
tags: []
processed_by: crosslinker
processed_at: 2026-05-14
---

# SynergyFinder HSA

## Overview

SynergyFinder is a web application and R package for quantifying drug combination synergy from dose-response matrices. The Highest Single Agent (HSA) model defines synergy as a combined drug effect that exceeds the response of the stronger single agent at equivalent concentrations. An HSA synergy score >10 is conventionally interpreted as synergistic. SynergyFinder also supports Bliss independence, Loewe additivity, and ZIP reference models.

## Used by

- SynergyFinder HSA scoring used to quantify synergy between [olaparib](../drugs/olaparib.md) and [spautin-1](../drugs/spautin-1.md) ([USP10](../genes/USP10.md) inhibitor) in 22Rv1 and C4-2 prostate cancer cell lines; combined treatment produced HSA synergy scores >10, with the strongest synergy at olaparib 0.4–0.8 µM combined with spautin-1 2–4 µM [PMID:28068672](../papers/28068672.md).

## Notes

- HSA synergy score >10 is the threshold used to define synergistic interactions in standard SynergyFinder outputs.
- Synergy was confirmed in BRCA2-WT-overexpressing 22Rv1 cells, ruling out dependence on the line's monoallelic [BRCA2](../genes/BRCA2.md) deficiency.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
