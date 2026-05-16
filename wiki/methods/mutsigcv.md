---
name: MutSigCV
slug: mutsigcv
kind: method
canonical_source: corpus
unverified: true
tags:
  - significantly-mutated-genes
  - somatic-mutation
  - bioinformatics
  - cancer-genomics
processed_by: wiki-cli
processed_at: 2026-05-16
---

# MutSigCV

## Overview

MutSigCV is a statistical method for identifying significantly mutated genes (SMGs) in cancer cohorts. It extends the MutSig framework by correcting for covariates of local mutation rate — including gene expression level, DNA replication timing, and chromatin accessibility — that cause many apparent mutations to be background events. MutSigCV uses negative binomial regression to model these covariates and computes per-gene p-values and q-values (FDR-corrected) for the null hypothesis that a gene's mutation rate does not exceed background. It is one of the standard SMG discovery methods in TCGA and large pan-cancer analyses.

## Used by

- Applied to 106 colon cancer WXS profiles ([coad_cptac_2019](../datasets/coad_cptac_2019.md)) in the CPTAC proteogenomic study; identified 8 SMGs in the non-hypermutated group (all previously reported in TCGA) and 9 in the hypermutated/MSI-H group, including four novel SMGs ([CASP5](../genes/CASP5.md), [RNF43](../genes/RNF43.md), [LTN1](../genes/LTN1.md), [BMPR2](../genes/BMPR2.md)) mutated in >50% of MSI-H samples [PMID:31031003](../papers/31031003.md)
- Applied in the pan-Asia cHCC-ICC WES study (133 cases); identified [TP53](../genes/TP53.md) as the only significantly mutated gene at FDR < 0.1 (alongside dNdScv which identified [TP53](../genes/TP53.md), [AXIN1](../genes/AXIN1.md), [RB1](../genes/RB1.md), [PTEN](../genes/PTEN.md), [ARID2](../genes/ARID2.md), and [BRD7](../genes/BRD7.md) at q < 0.1) [PMID:31130341](../papers/31130341.md)
- Applied for significantly mutated gene (SMG) filtering across 240 WES pediatric PDX models from 37 molecular subtypes; hybrid hg19-mm10 competitive mapping first removed mouse reads before SMG analysis [PMID:31693904](../papers/31693904.md).
- MutSigCV v1.4 identified CDK12 as significantly recurrently mutated in prostate cancer (FDR<0.001) and ovarian cancer (FDR=0.056) across a 26,743-tumor pan-cancer cohort [PMID:32317181](../papers/32317181.md)

## Notes

- MutSigCV is particularly important for exome-scale cohorts where local mutation-rate variation (e.g., in late-replicating, low-expression gene regions) can produce false positives if not corrected.
- The four novel hypermutated SMGs identified in the CPTAC colon study (CASP5, RNF43, LTN1, BMPR2) were not reported in the original TCGA colorectal analysis, possibly due to the MSI-H enrichment of the CPTAC prospective cohort.
- Not in cBioPortal gene-panels ontology; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31693904](../papers/31693904.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32317181](../papers/32317181.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
