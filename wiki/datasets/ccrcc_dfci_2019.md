---
name: DFCI ccRCC Immunotherapy Response Cohort (2019)
studyId: ccrcc_dfci_2019
institution: Dana-Farber Cancer Institute
size: 35
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
panels: []
tags:
  - immune-checkpoint-blockade
  - anti-pd-1
  - anti-pd-l1
  - swi-snf-complex
  - pbaf-complex
  - chromatin-remodeling
  - biomarker
  - clear-cell-rcc
processed_by: crosslinker
processed_at: 2026-05-15
---

# DFCI ccRCC Immunotherapy Response Cohort (2019)

## Overview

Prospective discovery cohort of 35 patients with metastatic clear cell renal cell carcinoma ([CCRCC](../cancer_types/CCRCC.md)) enrolled on a [nivolumab](../drugs/nivolumab.md) (anti-PD-1) trial at Dana-Farber Cancer Institute. Pre-treatment paired tumor/normal whole-exome sequencing (mean coverage 128x tumor / 91x normal) was performed to identify genomic correlates of response to immune checkpoint blockade. A separate validation cohort of 63 ccRCC patients treated with anti-PD-(L)1 ± anti-CTLA-4 was also analyzed. The study is deposited in cBioPortal as `ccrcc_dfci_2019`. [PMID:29301960](../papers/29301960.md)

## Composition

- **Discovery cohort:** 35 metastatic [CCRCC](../cancer_types/CCRCC.md) patients on a prospective [nivolumab](../drugs/nivolumab.md) trial; pre-treatment tumor/normal pairs sequenced by [whole-exome sequencing](../methods/whole-exome-seq.md). [PMID:29301960](../papers/29301960.md)
- **Validation cohort (not in cBioPortal study):** 63 metastatic [CCRCC](../cancer_types/CCRCC.md) patients treated with anti-PD-1 ([nivolumab](../drugs/nivolumab.md)) or anti-PD-L1 ([atezolizumab](../drugs/atezolizumab.md)) alone or combined with anti-CTLA-4 ([ipilimumab](../drugs/ipilimumab.md)); [PBRM1](../genes/PBRM1.md) status from WES (n=49) or panel sequencing (n=14). [PMID:29301960](../papers/29301960.md)
- **Clinical endpoint:** Composite response — clinical benefit (CB) = CR/PR by RECIST 1.1 or SD with any objective tumor reduction lasting ≥6 months; no clinical benefit (NCB) = PD by RECIST 1.1 with discontinuation within 3 months; intermediate benefit (IB) = remainder. [PMID:29301960](../papers/29301960.md)
- **Reference expression data:** TCGA KIRC ccRCC and the Sato (Kyoto University) untreated ccRCC cohort used for RNA-seq comparisons. [PMID:29301960](../papers/29301960.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — paired tumor/normal, mean 128x (tumor) / 91x (normal) coverage
- [rna-seq](../methods/rna-seq.md) — on-study tumor transcriptomics for pathway enrichment analysis ([GSEA](../methods/gsea.md))

## Papers using this cohort

- [PMID:29301960](../papers/29301960.md) — Miao et al. 2018, *Science* — "Genomic correlates of response to immune checkpoint therapies in clear cell renal cell carcinoma"

## Notable findings derived from this cohort

- [PBRM1](../genes/PBRM1.md) was the only recurrently mutated gene (by [MutSig2CV](../methods/mutsig.md)) in which truncating/LOF mutations were enriched in CB vs. NCB tumors: 9/11 vs. 3/13 (Fisher's exact p=0.012, q=0.086). [PMID:29301960](../papers/29301960.md)
- All discovery-cohort truncating PBRM1 alterations co-occurred with deletion of the non-mutated allele on chromosome 3p, producing complete biallelic LOF; most mutations were predicted to be clonal by [ABSOLUTE](../methods/absolute.md). [PMID:29301960](../papers/29301960.md)
- Patients with biallelic [PBRM1](../genes/PBRM1.md) loss had significantly prolonged [OS](../cancer_types/OS.md) (log-rank p=0.0074) and PFS (p=0.029) vs. PBRM1-intact patients on anti-PD-1. [PMID:29301960](../papers/29301960.md)
- Median nonsynonymous tumor mutation burden was modest (82/exome) and did not differ between CB and NCB groups; PD-L1 IHC was also not predictive in this cohort. [PMID:29301960](../papers/29301960.md)
- GSEA of PBRM1-LOF tumors (n=18 vs. n=14 intact) confirmed up-regulation of hypoxia and IL6/JAK-STAT3 hallmark gene sets. [PMID:29301960](../papers/29301960.md)
- [VHL](../genes/VHL.md) LOF — the most commonly mutated ccRCC gene — did not correlate with immune-related gene expression, indicating the signal is PBRM1-specific. [PMID:29301960](../papers/29301960.md)
- PFS benefit from [PBRM1](../genes/PBRM1.md) LOF was more pronounced in previously-treated (VEGF-inhibitor pre-exposed) patients than in treatment-naive patients (p=0.009). [PMID:29301960](../papers/29301960.md)

## Sources

- cBioPortal study: `ccrcc_dfci_2019`
- DOI: [10.1126/science.aan5951](https://doi.org/10.1126/science.aan5951)

*This page was processed by **crosslinker** on **2026-05-15**.*
