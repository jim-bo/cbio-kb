---
name: Medulloblastoma — PCGP WGS (mbl_pcgp)
studyId: mbl_pcgp
institution: St. Jude Children's Research Hospital / Washington University (Pediatric Cancer Genome Project)
size: 93
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - STRUCTURAL_VARIANT
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels: []
tags:
  - medulloblastoma
  - pediatric
  - wgs
  - cns
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Medulloblastoma — PCGP WGS (mbl_pcgp)

## Overview

A cohort of 93 medulloblastoma tumors assembled by the Pediatric Cancer Genome Project (PCGP), a collaboration between St. Jude Children's Research Hospital and Washington University. The discovery cohort comprised 37 medulloblastomas with matched normal blood subjected to whole-genome sequencing. A validation cohort of 56 additional medulloblastomas underwent targeted sequencing of 136 candidate genes. Tumors span all four molecular subgroups: WNT, SHH, subgroup-3, and subgroup-4. Data deposited in dbGaP (phs000409) and SRA (SRP008292).

## Composition

- Discovery cohort: 37 tumors — WNT (n=5), SHH (n=5), subgroup-3 (n=6), subgroup-4 (n=19), unclassified (n=2).
- Validation cohort: 56 tumors — WNT (n=6), SHH (n=8), subgroup-3 (n=11), subgroup-4 (n=19), unclassified (n=12).
- Cancer type: [MBL](../cancer_types/MBL.md) (medulloblastoma, pediatric).
- Key clinical fields: molecular subgroup, sex (relevant for KDM6A/UTY on chrY).

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — discovery cohort, 37 tumors; detected 22,887 validated somatic mutations, 536 SVs, and 5,802 CNVs.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — copy-number analysis.
- [sanger-sequencing](../methods/sanger-sequencing.md) — validation of candidate mutations.
- Affymetrix U133v2 — mRNA expression profiling.
- Custom capture arrays — targeted validation cohort.

## Papers using this cohort

- [PMID:22722829](../papers/22722829.md) — Medulloblastoma exome sequencing uncovers subtype-specific somatic mutations (Robinson et al., 2012).

## Notable findings derived from this cohort

- 49 genes recurrently mutated across all 93 tumors; 41 (84%) were novel for medulloblastoma [PMID:22722829](../papers/22722829.md).
- [KDM6A](../genes/KDM6A.md) inactivating mutations in 8/93 tumors (predominantly subgroup-4 males); co-deletion of UTY on chrY in 57% of KDM6A-mutant males [PMID:22722829](../papers/22722829.md).
- [DDX3X](../genes/DDX3X.md) DEAD-box domain mutations enriched in WNT subgroup (p<0.0001); alters RNA binding and expands LRLP lineage [PMID:22722829](../papers/22722829.md).
- [SMARCA4](../genes/SMARCA4.md) helicase-domain missense mutations in 4 WNT tumors (p<0.002) [PMID:22722829](../papers/22722829.md).
- [CTNNB1](../genes/CTNNB1.md) stabilizing mutations in 8/11 WNT tumors (p<0.0001) [PMID:22722829](../papers/22722829.md).
- [PIK3CA](../genes/PIK3CA.md) activating mutations in 3 tumors; accelerates but does not initiate WNT-medulloblastoma in mouse models [PMID:22722829](../papers/22722829.md).

## Sources

- [PMID:22722829](../papers/22722829.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
