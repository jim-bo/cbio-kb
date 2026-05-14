---
name: InVEx (Integrated Variant Explorer)
slug: invex
kind: BIOINFORMATICS
canonical_source: corpus
unverified: true
tags: [significantly-mutated-genes, mutation-significance, bioinformatics, statistical-method]
processed_by: crosslinker
processed_at: 2026-05-14
---

# InVEx (Integrated Variant Explorer)

## Overview

InVEx (Integrated Variant Explorer) is a statistical framework for identifying significantly mutated genes in cancer exome sequencing studies. It evaluates the enrichment of non-synonymous mutations relative to synonymous mutations within individual genes, accounting for gene-specific background mutation rates and trinucleotide context. InVEx complements MutSig by using an within-gene ratio-based test, making it particularly effective for detecting genes under positive selection in cancer cohorts.

## Used by

- Used together with MutSig in the TCGA [GBM](../cancer_types/GBM.md) 2013 study to identify 71 significantly mutated genes from 291 exomes; jointly identified established drivers ([PTEN](../genes/PTEN.md), [TP53](../genes/TP53.md), [EGFR](../genes/EGFR.md), [PIK3CA](../genes/PIK3CA.md), [PIK3R1](../genes/PIK3R1.md), [NF1](../genes/NF1.md), [RB1](../genes/RB1.md), [IDH1](../genes/IDH1.md), [PDGFRA](../genes/PDGFRA.md)) and the novel [GBM](../cancer_types/GBM.md) driver [LZTR1](../genes/LZTR1.md) (mutated in 10 samples; hemizygous deletion at 22q in 5/6 with copy number data) [PMID:24120142](../papers/24120142.md)
- InVEx (Bonferroni p < 0.05 or Q < 0.1) used alongside MutSig to identify 13 significantly mutated genes in 318 melanoma WES cases, including [RAC1](../genes/RAC1.md) UV hot-spot (6.9%) and [NF1](../genes/NF1.md) loss-of-function enrichment (LoF p = 1.8e–11). [PMID:26091043](../papers/26091043.md)

## Notes

- InVEx evaluates non-synonymous to synonymous mutation ratios within genes, complementing the MutSig approach which uses a background mutation rate model.
- The combined use of MutSig and InVEx increases sensitivity for detecting genes under selection with diverse mutation profiles.
- InVEx was developed at the Broad Institute as part of the TCGA [GBM](../cancer_types/GBM.md) analysis pipeline.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
