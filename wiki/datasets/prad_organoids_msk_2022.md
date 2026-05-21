---
name: Prostate Cancer (MSK, Science 2022)
studyId: prad_organoids_msk_2022
institution: Memorial Sloan Kettering Cancer Center
size: 40
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [atac-seq, rna-seq, msk-impact, chip-seq]
panels: [IMPACT468]
tags: [prostate-cancer, prad, crpc, organoids, pdx, chromatin, subtype, msk]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Prostate Cancer (MSK, Science 2022)

## Overview

Biobank of 40 metastatic castration-resistant prostate cancer (mCRPC) models profiled by ATAC-seq and RNA-seq at Memorial Sloan Kettering, comprising 22 patient-derived organoids (15 newly derived MSKPCa8–MSKPCa24 plus 7 prior), 6 patient-derived xenografts (PDXs), and 12 cell lines. Primary purpose was to define chromatin-based molecular subtypes of CRPC. Released on cBioPortal as study `prad_organoids_msk_2022`. [PMID:35617398](../papers/35617398.md)

## Composition

- **40 mCRPC models** (22 organoids, 6 PDXs, 12 cell lines); cancer type: [PRAD](../cancer_types/PRAD.md).
- 10/15 newly derived organoids had matched tumor biopsies for mutational/CNV profiling by [MSK-IMPACT](../methods/msk-impact-panel.md).
- Patient RNA-seq classification cohort: 366 CRPC patients (266 from the published [prad_su2c_2019](../datasets/prad_su2c_2019.md) cohort + 100 from Weill Cornell Medicine). [PMID:35617398](../papers/35617398.md)

## Assays / panels (linked)

- [ATAC-seq](../methods/atac-seq.md): 35 newly profiled models + 5 published NEPC models; 861,195 reproducible peaks; mostly distal intergenic/intronic (enhancer-enriched).
- [RNA-seq](../methods/rna-seq.md): polyA-enriched, applied to all models and 366 CRPC patients for subtype classification.
- [MSK-IMPACT](../methods/msk-impact-panel.md) (468-gene): somatic mutation and CNV profiling of organoids and matched biopsies.
- [ChIP-seq](../methods/chip-seq.md): for [FOSL1](../genes/FOSL1.md), TEAD, YAP, TAZ in MSKPCa3 and DU145 cell lines.
- Functional: CRISPR sgRNA cell-competition assays; [siRNA knockdown](../methods/sirna-knockdown.md) of YAP/TAZ; exogenous FOSL1 overexpression in LNCaP. [PMID:35617398](../papers/35617398.md)

## Papers using this cohort

- [PMID:35617398](../papers/35617398.md) — Tang et al., *Science* 2022: four chromatin-defined CRPC subtypes (CRPC-AR, CRPC-NE, CRPC-WNT, CRPC-SCL); primary discovery study for this dataset.

## Notable findings derived from this cohort

- Four chromatin-defined CRPC subtypes identified by consensus k-means clustering of ATAC-seq peaks: CRPC-AR (AR/FOXA1-driven), CRPC-NE (NEUROD1/ASCL1-driven), CRPC-WNT (TCF7L2-driven; [CTNNB1](../genes/CTNNB1.md) hotspot mutations in 3/4 models), and the newly described CRPC-SCL (stem cell-like; AP-1/FOSL1/YAP-TAZ/TEAD-driven). [PMID:35617398](../papers/35617398.md)
- [TP53](../genes/TP53.md) driver mutations or deep deletions in 23/35 (66%) models; [PTEN](../genes/PTEN.md) bi-allelic loss in 43%; [RB1](../genes/RB1.md) bi-allelic loss in 20% genomically but 14/24 (58%) AR-negative/low samples — significantly enriched over CRPC-AR (2/12, p=0.0200). [PMID:35617398](../papers/35617398.md)
- CRPC-SCL is the second-most-common subtype (~28%) in 366 CRPC patients (SU2C + WCM) and associated with significantly shorter time on next-generation ARSIs (enzalutamide/abiraterone). [PMID:35617398](../papers/35617398.md)
- [FOSL1](../genes/FOSL1.md) acts as a pioneer factor whose overexpression in AR-high LNCaP cells reprograms chromatin toward CRPC-SCL accessible sites and upregulates CRPC-SCL signature genes (FDR<1e-5). [PMID:35617398](../papers/35617398.md)
- [Verteporfin](../drugs/verteporfin.md) (YAP/TAZ inhibitor) and T-5224 (AP-1/c-Fos inhibitor) selectively inhibit proliferation of CRPC-SCL models MSKPCa3 and DU145 versus CRPC-AR models. [PMID:35617398](../papers/35617398.md)

## Sources

- cBioPortal study `prad_organoids_msk_2022`; reference genome hg19. [PMID:35617398](../papers/35617398.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
