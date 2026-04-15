---
name: Anaplastic Thyroid Carcinoma (GATCI, 2024)
studyId: thyroid_gatci_2024
institution: Global Anaplastic Thyroid Cancer Initiative (GATCI); 15 institutions
size: 292
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays: [bulk-rna-seq, snp-microarray, whole-exome-seq, whole-genome-seq]
panels: []
tags: [thyroid, anaplastic, THAP, multi-institution]
processed_by: entity-page-writer
processed_at: 2026-04-11
---

# Anaplastic Thyroid Carcinoma (GATCI, 2024)

## Overview

Multi-institutional genomic characterization of anaplastic thyroid carcinoma (ATC) and co-occurring differentiated thyroid carcinoma (DTC) assembled by the Global Anaplastic Thyroid Cancer Initiative (GATCI) across 15 institutions. The dataset includes 329 tumor regions from 292 patients profiled by WES, WGS, RNA-seq, and copy-number microarrays. It is the largest comprehensive genomic study of ATC to date. Data deposited in cBioPortal as `thyroid_gatci_2024`. [PMID:38412093](../papers/38412093.md)

## Composition

- 213 tumor regions from ATC patients: 179 primary ATC, 1 metastatic ATC, 34 co-occurring DTC (co-DTC) within ATC specimens.
- 115 papillary thyroid cancer (PTC) regions as comparator.
- 13 ATC cell lines.
- Cancer type: anaplastic thyroid carcinoma ([THAP](../cancer_types/THAP.md)).
- WES: n = 132 ATCs, 28 co-DTCs, 114 PTCs; WGS: n = 9 ATCs for clonal evolution analysis; copy-number arrays: n = 110 ATCs, 22 co-DTCs, 112 PTCs; RNA-seq: n = 24 primary ATCs + 13 cell lines. [PMID:38412093](../papers/38412093.md)

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md)
- [Whole-genome sequencing](../methods/whole-genome-seq.md) — multi-region, 9 patients for clonal evolution.
- [RNA-seq](../methods/rna-seq.md)
- SNP microarrays — copy-number profiling.

## Papers using this cohort

- [PMID:38412093](../papers/38412093.md) — The genomic and evolutionary landscapes of anaplastic thyroid carcinoma.

## Notable findings derived from this cohort

- ATCs harbor 3.8 ± 1.2 SNVs/Mb and 120 ± 44 CNAs per tumor — more than PTCs but fewer than most adult cancers. [PMID:38412093](../papers/38412093.md)
- 42 recurrently mutated genes identified by SeqSig analysis (FDR < 0.05); top five: [TP53](../genes/TP53.md), [NRAS](../genes/NRAS.md), [BRAF](../genes/BRAF.md), [PIK3CA](../genes/PIK3CA.md), and [USH2A](../genes/USH2A.md). [PMID:38412093](../papers/38412093.md)
- Five CNA subtypes (A–E) by consensus clustering; [CDKN2A](../genes/CDKN2A.md) deleted in 42% of ATCs; [BRCA2](../genes/BRCA2.md) deleted in 33.6% of ATCs. [PMID:38412093](../papers/38412093.md)
- [BRAF](../genes/BRAF.md) V600E frequency declined from 50.9% in PTCs to 21.3% in ATCs; [TP53](../genes/TP53.md) mutations increased from 0.9% (PTC) to 36.8% (ATC). [PMID:38412093](../papers/38412093.md)
- Multi-region WGS confirmed ATC and co-occurring DTC share a common clonal ancestor harboring ~95% of CNAs but only 19.1% of SNVs. [PMID:38412093](../papers/38412093.md)
- [BRCA2](../genes/BRCA2.md) deletion was associated with better survival (HR = 0.48, 95% CI 0.29–0.80, p = 0.005). [PMID:38412093](../papers/38412093.md)
- Germline variants detected in cancer predisposition genes: [RECQL4](../genes/RECQL4.md) (5% of ATCs), [BRCA2](../genes/BRCA2.md) (n = 3), [FANCF](../genes/FANCF.md) (n = 3). [PMID:38412093](../papers/38412093.md)

## Sources

- cBioPortal study `thyroid_gatci_2024`. [PMID:38412093](../papers/38412093.md)

*This page was processed by **entity-page-writer** on **2026-04-11**.*
