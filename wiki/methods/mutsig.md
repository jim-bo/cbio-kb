---
name: MutSig
slug: mutsig
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [statistical-method, somatic-mutation, cancer-genomics, significance-testing]
processed_by: crosslinker
processed_at: 2026-05-09
---

# MutSig

## Overview

MutSig (Mutation Significance) is a statistical algorithm developed at the Broad Institute to identify genes mutated at rates significantly above the background mutation rate in cancer. It accounts for context-specific mutation rates (nucleotide context, gene expression, replication timing) and gene-specific variability to compute q-values for each gene. MutSig is widely used in WES-based cancer genome studies to distinguish driver genes from passenger mutations.

## Used by

- Applied to 55 DLBCL WES samples in the [dlbc_broad_2012](../datasets/dlbc_broad_2012.md) cohort; identified 58 significantly mutated genes at FDR q <= 0.1, with a 97.9% validation rate by targeted resequencing [PMID:22343534](../papers/22343534.md).
- MutSig applied to identify statistically significant driver genes ([SPOP](../genes/SPOP.md), [FOXA1](../genes/FOXA1.md), [MED12](../genes/MED12.md)) in 112 prostate adenocarcinoma WES samples [PMID:22610119](../papers/22610119.md)
- Applied to 103 breast cancer tumor WES data (Broad cohort, [brca_broad](../datasets/brca_broad.md)) to identify significantly mutated genes including [PIK3CA](../genes/PIK3CA.md), [TP53](../genes/TP53.md), and [AKT1](../genes/AKT1.md) [PMID:22722202](../papers/22722202.md)
- MutSig applied to somatic mutation data from 224 TCGA colorectal carcinoma exomes to identify 24 significantly mutated genes including novel candidates [ARID1A](../genes/ARID1A.md), [SOX9](../genes/SOX9.md), [AMER1](../genes/AMER1.md) [PMID:22810696](../papers/22810696.md)
- InVEx permutation framework (related to MutSig) applied to 121 melanoma exomes; leverages intronic mutation rates to control for high UV-induced mutation background; identified 11 significantly mutated genes [PMID:22817889](../papers/22817889.md)
- MutSig applied to 92 medulloblastoma exomes (Broad) to identify 12 significantly mutated genes (q<0.1) including novel candidates [DDX3X](../genes/DDX3X.md), [GPS2](../genes/GPS2.md), [BCOR](../genes/BCOR.md), [LDB1](../genes/LDB1.md) [PMID:22820256](../papers/22820256.md)
- Applied to TCGA [LUSC](../cancer_types/LUSC.md) cohort (178 tumors) to identify significantly mutated genes including [CDKN2A](../genes/CDKN2A.md), TP53, [KEAP1](../genes/KEAP1.md), [NFE2L2](../genes/NFE2L2.md), and MLL2 [PMID:22960745](../papers/22960745.md)
- Applied to Broad [LUAD](../cancer_types/LUAD.md) cohort (183 tumors) to identify significantly mutated genes; nominated [RBM10](../genes/RBM10.md), [U2AF1](../genes/U2AF1.md), and ARID1A as novel drivers alongside [EGFR](../genes/EGFR.md), [KRAS](../genes/KRAS.md), and [STK11](../genes/STK11.md) [PMID:22980975](../papers/22980975.md)
- MutSig applied to neuroblastoma WES data to identify significantly mutated genes; [ALK](../genes/ALK.md), [PTPN11](../genes/PTPN11.md), and [ATRX](../genes/ATRX.md) passed significance thresholds [PMID:23334666](../papers/23334666.md)
- MutSig analysis of 160 CLL exomes identified [SF3B1](../genes/SF3B1.md), [NOTCH1](../genes/NOTCH1.md), DDX3X, and [POT1](../genes/POT1.md) as significantly mutated genes beyond background rates [PMID:23415222](../papers/23415222.md)
- MutSig significance algorithm identified 26 significantly mutated genes (FDR q<0.1) in 145 esophageal adenocarcinomas, including TP53, CDKN2A, [SMAD4](../genes/SMAD4.md), PIK3CA, and novel candidates [ELMO1](../genes/ELMO1.md), [DOCK2](../genes/DOCK2.md), and [SPART](../genes/SPART.md) [PMID:23525077](../papers/23525077.md)

## Notes

- MutSig relies on a background mutation model; covariates include expression levels, replication timing, and trinucleotide context.
- At a q <= 0.1 threshold in the DLBCL study, confirmed known drivers ([MYD88](../genes/MYD88.md), [CARD11](../genes/CARD11.md), [EZH2](../genes/EZH2.md), [CREBBP](../genes/CREBBP.md), [CD79B](../genes/CD79B.md), [TP53](../genes/TP53.md)) and identified novel candidates ([MEF2B](../genes/MEF2B.md), [KMT2D](../genes/KMT2D.md), [BTG1](../genes/BTG1.md), [GNA13](../genes/GNA13.md), [ACTB](../genes/ACTB.md), [P2RY8](../genes/P2RY8.md), [TNFRSF14](../genes/TNFRSF14.md)) [PMID:22343534](../papers/22343534.md).
- A complementary rare-driver analysis using mutational clustering and evolutionary conservation identified [KRAS](../genes/KRAS.md), [BRAF](../genes/BRAF.md), [NOTCH1](../genes/NOTCH1.md), and [SYK](../genes/SYK.md) as likely drivers not captured by MutSig alone [PMID:22343534](../papers/22343534.md).
- Not a sequencing panel; lacks a cBioPortal genePanelId.

## Sources

- [PMID:22343534](../papers/22343534.md) — DLBCL WES study where MutSig identified 58 significantly mutated genes.

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22610119](../papers/22610119.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22722202](../papers/22722202.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22810696](../papers/22810696.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22817889](../papers/22817889.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22820256](../papers/22820256.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22960745](../papers/22960745.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22980975](../papers/22980975.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23334666](../papers/23334666.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23415222](../papers/23415222.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23525077](../papers/23525077.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
