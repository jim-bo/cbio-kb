---
name: DFCI HR+/HER2- Metastatic Breast Cancer CDK4/6i Resistance Cohort
studyId: brca_dfci_2020
institution: Dana-Farber Cancer Institute (DF/HCC)
size: 58
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - hr-positive-breast-cancer
  - cdk4-6-inhibitor-resistance
  - metastatic-breast-cancer
  - intrinsic-resistance
  - acquired-resistance
processed_by: crosslinker
processed_at: 2026-05-16
---

# DFCI HR+/HER2- Metastatic Breast Cancer CDK4/6i Resistance Cohort

## Overview

The brca_dfci_2020 cohort was assembled at Dana-Farber Cancer Institute / Harvard Cancer Center (DF/HCC tissue protocol 05-246) to map the genomic landscape of intrinsic and acquired resistance to CDK4/6 inhibitors in HR+/HER2- metastatic breast cancer. Whole-exome sequencing of 59 metastatic biopsies from 58 patients — paired with matched germline (PBMC) DNA — identified eight resistance-associated alteration categories covering 65.9% of resistant tumors, including previously uncharacterized CDK4/6i resistance mechanisms ([AKT1](../genes/AKT1.md), RAS-pathway, [AURKA](../genes/AURKA.md)). [PMID:32404308](../papers/32404308.md)

## Composition

- **58 patients** with HR+/HER2- metastatic breast cancer ([BRCA](../cancer_types/BRCA.md)), 59 metastatic biopsies total.
- Biopsy categories: 18 sensitive (baseline or subsequent clinical benefit), 28 intrinsic resistance (progression at first restaging or SD <6 months), 13 acquired resistance (biopsy at/after progression following initial benefit).
- 49/58 patients (84.5%) received [palbociclib](../drugs/palbociclib.md); 55/58 (94.8%) received CDK4/6i combined with an aromatase inhibitor or [fulvestrant](../drugs/fulvestrant.md). Mean treatment duration 316 days (range 43–1052). [PMID:32404308](../papers/32404308.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — tumor + matched germline (PBMC) DNA, aligned to hg19; somatic SNV calling with [MuTect](../methods/mutect.md), structural variants with [SvABA](../methods/svaba.md), cancer-cell fractions with [ABSOLUTE](../methods/absolute.md), clonal reconstruction with [PyClone](../methods/pyclone.md). [PMID:32404308](../papers/32404308.md)
- ER expression by [immunohistochemistry](../methods/immunohistochemistry.md). [PMID:32404308](../papers/32404308.md)

## Papers using this cohort

- [PMID:32404308](../papers/32404308.md) — Wander et al. (2020), *Cancer Discovery*: Genomic landscape of CDK4/6i resistance in HR+/HER2- metastatic breast cancer.

## Notable findings derived from this cohort

- Eight alteration categories — biallelic [RB1](../genes/RB1.md) disruption, [AKT1](../genes/AKT1.md) activation, [KRAS](../genes/KRAS.md)/[HRAS](../genes/HRAS.md)/[NRAS](../genes/NRAS.md) activation, [FGFR2](../genes/FGFR2.md) alterations, [ERBB2](../genes/ERBB2.md) mutations, [AURKA](../genes/AURKA.md) amplification, [CCNE2](../genes/CCNE2.md) amplification, and ER loss — together account for 27/41 (65.9%) resistant biopsies vs. 3/18 (16.7%) sensitive biopsies (p<0.05). [PMID:32404308](../papers/32404308.md)
- [AURKA](../genes/AURKA.md) amplification was the most enriched novel resistance driver: 11/41 (26.8%) resistant vs. 0/18 sensitive biopsies (p=0.0081); first demonstration of AURKA as a CDK4/6i resistance mechanism in patients. [PMID:32404308](../papers/32404308.md)
- [PIK3CA](../genes/PIK3CA.md) mutations were equally frequent in sensitive (44.4%) and resistant (43.9%) tumors — not a resistance biomarker in this cohort. [PMID:32404308](../papers/32404308.md)
- 12/41 (29.3%) resistant biopsies carried two or more of the eight drivers, indicating frequent co-occurrence of resistance mechanisms. [PMID:32404308](../papers/32404308.md)
- Resistance cell lines independently acquired [KRAS](../genes/KRAS.md) G12V, [RB1](../genes/RB1.md) down-regulation, AURKA up-regulation, or [CCNE2](../genes/CCNE2.md) up-regulation under selection — convergent evolution confirmed. [PMID:32404308](../papers/32404308.md)

## Sources

- cBioPortal study: `brca_dfci_2020`
- DOI: [10.1158/2159-8290.CD-19-1390](https://doi.org/10.1158/2159-8290.CD-19-1390)

*This page was processed by **crosslinker** on **2026-05-16**.*
