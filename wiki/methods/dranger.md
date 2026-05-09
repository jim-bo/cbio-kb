---
name: dRanger
slug: dranger
kind: method
canonical_source: corpus
unverified: false
tags:
  - structural-variation
  - rearrangement
  - whole-genome-seq
  - somatic-sv
processed_by: entity-page-writer
processed_at: 2026-05-09
---

# dRanger

## Overview

dRanger is a computational tool for detecting somatic structural variants (rearrangements) from paired-end whole-genome sequencing data. It identifies discordant read pairs spanning genomic rearrangements and applies a panel-of-normal filtering strategy to remove germline and artifact signals. dRanger was developed at the Broad Institute and is used as the primary SV discovery step in pipelines that feed into BreakPointer (for breakpoint refinement) and ChainFinder (for chromoplexy detection).

## Used by

- Applied to 57 prostate WGS tumor/normal pairs filtered against a panel of 172–176 non-cancerous genomes; identified 5,596 high-confidence somatic rearrangements, of which 113 were validated by PCR/resequencing; detected 39% of rearrangements participating in chromoplexy chains (vs 2.8% in simulated controls, p<10⁻⁴) [PMID:23622249](../papers/23622249.md)
- Used for rearrangement discovery in 16 esophageal adenocarcinoma WGS pairs, yielding 2,952 candidate rearrangements (median 172/tumor, range 77–402); 38 predicted in-frame fusions identified but no recurrent fusions found [PMID:23525077](../papers/23525077.md)

## Notes

- Panel-of-normal filtering is critical for removing recurrent mapping artifacts and germline SVs.
- Outputs are typically refined by BreakPointer for base-pair resolution and then analyzed by ChainFinder for chain detection.
- Rearrangement count and mutation count are uncorrelated in EAC (R²=0.0046), suggesting independent mutagenic processes.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-09**.*
