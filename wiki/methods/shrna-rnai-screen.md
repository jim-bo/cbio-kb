---
name: shRNA RNAi Screen
slug: shrna-rnai-screen
kind: method
canonical_source: corpus
unverified: true
tags: [functional-genomics, rnai, loss-of-function-screen]
processed_by: crosslinker
processed_at: 2026-05-04
---

# shRNA RNAi Screen

## Overview

Short hairpin RNA (shRNA) RNAi screening is a pooled or arrayed loss-of-function genetic screen that uses RNA interference to knock down gene expression and assess the proliferative or viability impact of each knockdown across a panel of cell lines. Results identify gene dependencies specific to tumor subtypes or genotypes.

## Used by

- Used to functionally validate copy-number dependencies in dedifferentiated liposarcoma ([DDLS](../cancer_types/DDLS.md)): 385 genes screened with 2,007 shRNAs (median 5 shRNAs per gene) in three DDLS cell lines (LPS141, DDLS8817, FU-DDLS-1); 99 genes with significant anti-proliferative effects in ≥1 line confirmed [PMID:20601955](../papers/20601955.md).

## Notes

- [CDK4](../genes/CDK4.md) was the most overexpressed amplified hit; sustained CDK4 shRNA knockdown (>10 days) inhibited proliferation in LPS141 and DDLS8817 [PMID:20601955](../papers/20601955.md).
- [MDM2](../genes/MDM2.md) knockdown required sustained depletion (>1 week) to impair proliferation; [YEATS4](../genes/YEATS4.md) knockdown phenocopied the MDM2 screen result in DDLS [PMID:20601955](../papers/20601955.md).
- Only 1 of 58 overlapping genes (PSMB4) was a common essential in a 12-cell-line pan-cancer reference screen, supporting DDLS-specific dependencies [PMID:20601955](../papers/20601955.md).

## Sources

- [PMID:20601955](../papers/20601955.md)

*This page was processed by **crosslinker** on **2026-05-04**.*
