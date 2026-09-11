---
name: Soft Tissue Sarcoma MYOD1 (MSK, Sci Adv 2026)
studyId: soft_tissue_myod1_msk_2025
institution: Memorial Sloan Kettering Cancer Center (MSK)
size: 20
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - msk-impact-panel
tags:
  - rhabdomyosarcoma
  - MYOD1
  - sarcoma
  - IGF2
  - PI3K-AKT-mTOR
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Soft Tissue Sarcoma MYOD1 (MSK, Sci Adv 2026)

## Overview

20 patients with MYOD1-mutant spindle cell/sclerosing rhabdomyosarcoma ([SCSRMS](../cancer_types/SCSRMS.md)) profiled by MSK-IMPACT targeted tumor-normal sequencing at Memorial Sloan Kettering, part of a broader single-nucleus RNA-seq and PDX-based study of MYOD1L122R biology. Name, institution, size (20) and reference genome (hg19) are taken from the cBioPortal study record in `schema/ontology/studies.json` [PMID:41758938](../papers/41758938.md).

## Composition

- 20 unique patients with *[MYOD1](../genes/MYOD1.md)*-mutant SCSRMS profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) (341–505 gene matched tumor-normal panel); median disease-specific survival 42.4 months, PFS 27.3 months (5-year DSS 35%, PFS 29%) [PMID:41758938](../papers/41758938.md).
- All patients received neoadjuvant chemotherapy (most commonly vincristine/dactinomycin/cyclophosphamide, "VAC") followed by delayed resection [PMID:41758938](../papers/41758938.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md), 341–505 gene matched tumor-normal DNA sequencing panel [PMID:41758938](../papers/41758938.md).

## Papers using this cohort

- [PMID:41758938](../papers/41758938.md) — MSK study, source publication: single-nucleus RNA-seq/protein-activity analysis of MYOD1L122R SCSRMS, with this MSK-IMPACT cohort used to characterize recurrent genomic co-alterations.

## Notable findings derived from this cohort

- *MYOD1* VAF exceeded 50% in 19/20 cases (range 0.43–0.98, median 0.78), consistent with mutant-allele enrichment via chromosome 11p aneuploidy (5 patients with high-level 11p amplification) [PMID:41758938](../papers/41758938.md).
- The most recurrent, largely mutually exclusive co-alterations were *[IGF2](../genes/IGF2.md)* amplification and PI3K/AKT/mTOR pathway genes — *[PIK3CA](../genes/PIK3CA.md)* (20%), *[PTEN](../genes/PTEN.md)* (10%), AKT/*[PIK3R3](../genes/PIK3R3.md)*/*[PIK3C2G](../genes/PIK3C2G.md)* (5% each) — enriched in post-treatment samples, supporting a paracrine IGF2–IGF1R–PI3K/AKT/mTOR axis as a mutation-independent therapeutic target [PMID:41758938](../papers/41758938.md).

## Sources

- cBioPortal study record: `soft_tissue_myod1_msk_2025` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:41758938](../papers/41758938.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
