---
name: MSK DCIS-IDC Paired Evolution (Pareja et al. 2020)
studyId: brca_pareja_msk_2020
institution: Memorial Sloan Kettering Cancer Center
size: 60
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels:
  - IMPACT410
  - IMPACT468
tags:
  - breast-cancer
  - DCIS
  - IDC
  - clonal-evolution
  - paired-samples
  - WES
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK DCIS-IDC Paired Evolution (Pareja et al. 2020)

## Overview

Prospective cohort from Memorial Sloan Kettering Cancer Center sequencing synchronously diagnosed ductal carcinoma in situ ([DCIS](../cancer_types/DCIS.md)) and matched invasive ductal carcinomas of no special type (IDC-NST) from 25 patients, plus 7 pure DCIS that did not progress. Whole-exome sequencing (WES) was performed on 56 samples at median 186x tumor / 126x normal depth; 4 additional samples used the MSK-IMPACT targeted panel ([IMPACT410](../methods/IMPACT410.md) and [IMPACT468](../methods/IMPACT468.md)). The cohort was designed to characterize the somatic genomic relationship between synchronous DCIS and IDC-NST and to identify events associated with clonal progression to invasion. Released on cBioPortal as [brca_pareja_msk_2020](../datasets/brca_pareja_msk_2020.md). [PMID:32220886](../papers/32220886.md)

## Composition

- 25 patients with synchronously diagnosed DCIS (n=27 samples) and IDC-NST (n=26 samples); 7 additional patients with pure DCIS (n=7 samples) that did not progress.
- Cancer types: [DCIS](../cancer_types/DCIS.md), [IDC](../cancer_types/IDC.md)-NST, [BRCA](../cancer_types/BRCA.md).
- Median patient age 50 years (range 26–76); 41% intermediate-grade DCIS, 59% high-grade DCIS; 56% of synchronous DCIS and 54% of IDC-NSTs were ER+/HER2−.
- Only intermediate- and high-grade DCIS included; low-grade excluded by design.
- Comparator: age-, menopausal-status-, and ER/HER2-matched IDC-NSTs from [brca_tcga_pub](../datasets/brca_tcga_pub.md) (1:3 ratio). [PMID:32220886](../papers/32220886.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 56 samples; median 186x tumor / 126x normal.
- [MSK-IMPACT](../methods/msk-impact-panel.md) — 4 samples (Cases 3 and 9); [IMPACT410](../methods/IMPACT410.md) for Case 3, [IMPACT468](../methods/IMPACT468.md) for Case 9; median 596x tumor / 549x normal. [PMID:32220886](../papers/32220886.md)

## Papers using this cohort

- [PMID:32220886](../papers/32220886.md) — Pareja et al., genomic analysis of synchronous DCIS and IDC-NST revealing clonal relatedness in 92% of pairs and clonal selection in 28% of progression events.

## Notable findings derived from this cohort

- 92% (23/25) of synchronous DCIS–IDC-NST pairs were clonally related by SNV-based clonality index; two unrelated pairs (Cases 5 and 24) had DCIS and IDC-NST in different breast quadrants. [PMID:32220886](../papers/32220886.md)
- Clonal selection (minor DCIS subclone dominating matched IDC-NST) was identified by [PyClone](../methods/pyclone.md) in 28% (7/25) of cases; DCIS with clonal selection had significantly higher Shannon and Gini-Simpson diversity than DCIS without selection. [PMID:32220886](../papers/32220886.md)
- [TP53](../genes/TP53.md) mutated in 52% synchronous DCIS vs. 54% IDC-NST (P>0.05); [PIK3CA](../genes/PIK3CA.md) in 41% vs. 42% (P>0.05); [GATA3](../genes/GATA3.md) in 26% vs. 23% (P>0.05) — no statistically significant differences between DCIS and IDC-NST for any cancer gene. [PMID:32220886](../papers/32220886.md)
- Pure DCIS lacked [PIK3CA](../genes/PIK3CA.md) mutations entirely (0% vs. 41% in synchronous DCIS; P>0.05), suggesting [PIK3CA](../genes/PIK3CA.md) activation may be associated with co-occurrence of synchronous invasion. [PMID:32220886](../papers/32220886.md)
- Whole-genome doubling (by [FACETS](../methods/facets.md) / [ABSOLUTE](../methods/absolute.md)) was truncal (present in both DCIS and IDC-NST) in 3/7 WGD cases and IDC-NST-restricted in 4/7, supporting WGD as a progression mechanism in some cases. [PMID:32220886](../papers/32220886.md)
- Grade-3 DCIS carried significantly more non-synonymous mutations than grade-2 (P<0.01) and 75% [TP53](../genes/TP53.md) mutation frequency vs. 0% in grade-2 (P<0.001). [PMID:32220886](../papers/32220886.md)

## Sources

- [PMID:32220886](../papers/32220886.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
