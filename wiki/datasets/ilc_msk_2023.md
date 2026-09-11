---
name: Breast Invasive Lobular Carcinoma (MSK, NPJ Precis Oncol 2024)
studyId: ilc_msk_2023
institution: Memorial Sloan Kettering Cancer Center (MSK)
size: 25
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - whole-genome-seq
panels:
  - msk-impact-panel
tags:
  - breast-cancer
  - lobular-carcinoma
  - CDH1
  - AXIN2
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Breast Invasive Lobular Carcinoma (MSK, NPJ Precis Oncol 2024)

## Overview

25 primary invasive lobular carcinomas ([ILC](../cancer_types/ILC.md)) of the breast lacking bi-allelic *CDH1* (E-cadherin) inactivating genetic alterations, drawn from a screening cohort of 364 primary ILCs with clinical MSK-IMPACT tumor–normal sequencing at Memorial Sloan Kettering. Name, institution, size (25) and reference genome (hg19) are taken from the cBioPortal study record in `schema/ontology/studies.json` [PMID:38347189](../papers/38347189.md).

## Composition

- 25 primary [ILC](../cancer_types/ILC.md) cases with no CDH1 inactivating genetic alteration, identified from a screen of 364 primary ILCs [PMID:38347189](../papers/38347189.md).
- 16 of the 25 cases had FFPE material sufficient for CDH1 promoter methylation testing; 10/16 (62.5%) were methylated, and 9 of those 10 also had 16q loss and complete E-cadherin loss [PMID:38347189](../papers/38347189.md).
- 3 cases had inactivating *[AXIN2](../genes/AXIN2.md)* alterations (one W78* truncating mutation, a PLXDC1-AXIN2 fusion, and a 17q inversion) [PMID:38347189](../papers/38347189.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) tumor–normal targeted sequencing (somatic mutations, copy-number alterations, structural variants) deposited in cBioPortal for all 25 cases [PMID:38347189](../papers/38347189.md).
- [Whole-genome sequencing](../methods/whole-genome-seq.md) of 3 cases (mean depth 63x tumor / 37x normal, GRCh37/hg19) [PMID:38347189](../papers/38347189.md).

## Papers using this cohort

- [PMID:38347189](../papers/38347189.md) — Dopeso, Gazzo, Derakhshan et al. (MSK), source publication: identifies non-CDH1 mechanisms (promoter methylation + 16q loss, AXIN2 inactivation) driving the ILC phenotype.

## Notable findings derived from this cohort

- Whole-genome sequencing confirmed the *AXIN2* W78* mutation in one case and found a new t(3;11) *[CTNND1](../genes/CTNND1.md)*–*[DENND6A](../genes/DENND6A.md)* fusion removing the armadillo repeats of p120; this AXIN2-mutant case also carried bi-allelic *[BRCA2](../genes/BRCA2.md)* inactivation with an HRDetect score of 0.99 [PMID:38347189](../papers/38347189.md).
- CRISPR-Cas9 knockout of AXIN2 in MCF7 cells produced lobular-like traits (anoikis resistance, increased migration, reduced E-cadherin protein with unchanged CDH1 mRNA), supporting AXIN2 loss as a CDH1-independent route to the lobular phenotype [PMID:38347189](../papers/38347189.md).

## Sources

- cBioPortal study record: `ilc_msk_2023` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:38347189](../papers/38347189.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
