---
name: MSKCC NSCLC Immunotherapy WES Cohort (CheckMate-012, 2018)
studyId: nsclc_mskcc_2018
institution: Memorial Sloan Kettering Cancer Center
size: 75
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - STRUCTURAL_VARIANT
panels:
  - msk-impact-panel
tags:
  - nsclc
  - immunotherapy
  - tumor-mutation-burden
  - whole-exome-seq
  - checkmate-012
  - pd-1
  - ctla-4
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSKCC NSCLC Immunotherapy WES Cohort (CheckMate-012, 2018)

## Overview

Prospective whole-exome sequencing cohort of 75 patients with advanced non-small-cell lung cancer ([NSCLC](../cancer_types/NSCLC.md)) enrolled on the CheckMate-012 trial at Memorial Sloan Kettering Cancer Center. Patients received combined PD-1 plus CTLA-4 blockade ([nivolumab](../drugs/nivolumab.md) + [ipilimumab](../drugs/ipilimumab.md)). The study was designed to evaluate tumor mutation burden (TMB) as a predictive biomarker for combination immune-checkpoint therapy. WES was performed on tumor and paired germline DNA; TMB was also estimated from the [MSK-IMPACT](../methods/msk-impact-panel.md) 468-gene panel and the FoundationOne 315-gene panel for comparison.

## Composition

- **n = 75** patients with advanced [NSCLC](../cancer_types/NSCLC.md); 79% non-squamous, 21% squamous; 88% stage IV.
- 60/75 (80%) were current or former smokers; PD-L1 expression known in 70/75 (93%).
- WES performed on tumor and paired blood; mean tumor coverage 148X (IQR 116–182X), normal 81X (IQR 70–98X); 94% of targets at ≥20X depth in tumors.
- Median TMB 158 nonsynonymous mutations (range not specified); high-TMB defined as >median.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) (primary assay; Agilent capture, Illumina sequencing).
- [MSK-IMPACT](../methods/msk-impact-panel.md) 468-gene panel (in silico TMB estimation for clinical comparability).
- FoundationOne 315-gene panel (in silico TMB estimation for clinical comparability).

## Papers using this cohort

- [PMID:29657128](../papers/29657128.md) — Hellmann et al. 2018, New England Journal of Medicine — "Tumor Mutational Burden and Efficacy of Nivolumab Monotherapy and in Combination with Ipilimumab in Small-Cell Lung Cancer."

## Notable findings derived from this cohort

- High TMB (>median 158 nonsynonymous mutations) was strongly associated with improved objective response (ORR 51% vs 13%, OR 6.97, Fisher's exact p=0.0005), durable clinical benefit (65% vs 34%, p=0.011), and progression-free survival (median 17.1 vs 3.7 months, HR 0.41, p=0.0024) [PMID:29657128](../papers/29657128.md).
- TMB and PD-L1 expression were independent biomarkers (Spearman r = −0.087, p=0.48); combining high TMB and PD-L1 ≥1% identified patients with the highest response rates (chi-square for trend p<0.0001) [PMID:29657128](../papers/29657128.md).
- TMB estimated from the [MSK-IMPACT](../methods/msk-impact-panel.md) 468-gene panel was similarly predictive to WES-derived TMB, supporting clinical panel use [PMID:29657128](../papers/29657128.md).
- [TP53](../genes/TP53.md) mutations were enriched in responders (OR 2.9, p=0.048); [STK11](../genes/STK11.md) mutations (n=7) and [PTEN](../genes/PTEN.md) mutations (n=4) were exclusively associated with non-response [PMID:29657128](../papers/29657128.md).

## Sources

- Hellmann MD et al. "Tumor Mutational Burden and Efficacy of Nivolumab Monotherapy and in Combination with Ipilimumab in Small-Cell Lung Cancer." New England Journal of Medicine. 2018;378(22):2093-2104. [PMID:29657128](../papers/29657128.md). DOI: 10.1056/NEJMoa1801019.

*This page was processed by **crosslinker** on **2026-05-16**.*
