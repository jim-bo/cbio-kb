---
name: ChainFinder
slug: chainfinder
kind: method
canonical_source: corpus
unverified: false
tags:
  - structural-variation
  - chromoplexy
  - graph-theory
  - whole-genome-seq
  - rearrangement
processed_by: crosslinker
processed_at: 2026-05-09
---

# ChainFinder

## Overview

ChainFinder is a graph-theory algorithm developed by Baca et al. (2013) to detect "chromoplexy" — chains of interdependent chromosomal rearrangements that arise in a coordinated or near-simultaneous manner. It models structural variants as edges in a graph and identifies chains of translocations and deletions that co-occur across multiple chromosomes more often than expected under an independent model. ChainFinder distinguishes chromoplexy from both random sequential rearrangements and catastrophic chromothripsis by testing statistical independence of breakpoint co-location. It was introduced and applied in a WGS study of 57 prostate tumors and subsequently validated on pan-cancer genomes.

## Used by

- Introduced and applied to 57 prostate tumor WGS genomes to detect chromoplexy chains of ≥5 rearrangements (≥10 breakpoints); chains were detected in 50/57 tumors (88%); pan-cancer validation on 59 additional genomes across melanoma, [NSCLC](../cancer_types/NSCLC.md), [HNSC](../cancer_types/HNSC.md), and breast adenocarcinoma confirmed chromoplexy is not prostate-specific [PMID:23622249](../papers/23622249.md)

## Notes

- Defines chains based on spatial proximity of breakpoints and tests against simulated null distributions (p < 10⁻⁴ threshold used in the original prostate study).
- Distinguishes ETS+ prostate tumors (inter-chromosomal chains linked to transcription hubs) from ETS−/CHD1del tumors (intra-chromosomal chains in late-replicating heterochromatin).
- Requires paired-end WGS with SV calls as input; typically used downstream of dRanger or equivalent callers.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
