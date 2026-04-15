---
name: TCIA NSCLC-Radiomics-Genomics Lung3
studyId: tcia-nsclc-radiomics-genomics-lung3
institution: MAASTRO Clinic, Maastricht, Netherlands
size: 89
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - ct-imaging
  - gene-expression-microarray
panels: []
tags:
  - nsclc
  - radiomics
  - radiogenomics
  - tcia
  - ct
  - lung
  - gene-expression
  - validation-cohort
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# TCIA NSCLC-Radiomics-Genomics Lung3

## Overview

The Lung3 collection is a radiogenomics cohort of 89 NSCLC patients at MAASTRO Clinic (Maastricht, Netherlands) with matched pretreatment CT imaging and whole-genome Affymetrix gene expression profiling (HuRSTA_2a520709 array, 21,766 genes). It was used by Aerts et al. 2014 to link radiomic features to gene sets via GSEA, demonstrating that intratumour-heterogeneity radiomic features correlate with cell-cycling / proliferation pathways. Publicly available on TCIA as NSCLC-Radiomics-Genomics. [PMID:24892406](../papers/24892406.md)

## Composition

- **Cancer type**: [NSCLC](../cancer_types/NSCLC.md), n=89.
- **Modality**: CT (pretreatment) + Affymetrix HuRSTA_2a520709 gene expression microarray (21,766 genes).
- **Annotations**: manual tumour delineations; gene-set enrichment analysis (GSEA) against MSigDB C5/GO collection at FDR ≤20%.
- **Role in Aerts 2014**: radiogenomics arm; the only cohort used for molecular correlations. [PMID:24892406](../papers/24892406.md)

## Assays / panels (linked)

- [CT radiomics](../methods/ct-radiomics.md) — 440-feature library.
- Gene expression microarray (Affymetrix HuRSTA_2a520709).

## Papers using this cohort

- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*: Lung3 used for GSEA-based radiogenomics; all four signature features show enriched gene sets; heterogeneity features (III and IV) correlate with cell-cycling pathways.

## Notable findings derived from this cohort

- All four features of the locked radiomic signature showed significant GSEA enrichment against the MSigDB C5 GO gene-set collection (FDR ≤20%) in Lung3. [PMID:24892406](../papers/24892406.md)
- The two intratumour-heterogeneity features (Grey Level Nonuniformity and wavelet Grey Level Nonuniformity HLH) correlated with cell-cycling / proliferation pathways, suggesting that more heterogeneous CT phenotypes reflect higher tumour proliferation. [PMID:24892406](../papers/24892406.md)

## Sources

- TCIA collection: NSCLC-Radiomics-Genomics — https://www.cancerimagingarchive.net/collection/nsclc-radiomics-genomics/
- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*, DOI 10.1038/ncomms5006.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
