---
name: Pan-Cancer Analysis of Whole Genomes (PCAWG)
studyId: pcawg
institution: 
size: 
reference_genome: GRCh37
canonical_source: 
unverified: true
assays: []
panels: []
tags: []
processed_by: entity-page-writer
processed_at: 2026-05-16
description: "Pan-Cancer Analysis of Whole Genomes (PCAWG) — whole-genome sequencing of ~2,780 tumor/normal pairs across cancer types. Used in the cbio-kb corpus as a comparator for mutational burden and signatures. Note: PCAWG is not catalogued by cBioPortal."
cancerTypeId: mixed
pmid: null
allSampleCount: null
---

# Pan-Cancer Analysis of Whole Genomes (PCAWG)

> **Unverified:** PCAWG is not catalogued by cBioPortal as a `studyId` in `schema/ontology/studies.json`. This page uses a corpus-derived slug and is flagged `unverified: true` per the cbio-kb ontology protocol [PMID:36723991](../papers/36723991.md).

## Overview

PCAWG is the ICGC/TCGA Pan-Cancer Analysis of Whole Genomes project, a reference pan-cancer WGS resource. Within the cbio-kb corpus, PCAWG is used as an external benchmark for whole-genome mutational burden and signature analyses rather than as a primary cohort of record [PMID:36723991](../papers/36723991.md).

## Composition

- Approximately 2,780 tumor/normal whole genomes spanning multiple cancer types, as referenced by citing papers [PMID:36723991](../papers/36723991.md).

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md) [PMID:36723991](../papers/36723991.md).

## Papers using this cohort

- [PMID:36723991](../papers/36723991.md) — Maura et al. benchmarked the mutational burden of their classic Hodgkin lymphoma WGS cohort against PCAWG (n=2,780) and a multiple myeloma WGS cohort, placing cHL HRS cells (median 5,279 SBS+indels per genome) within the range of other cancers represented in PCAWG [PMID:36723991](../papers/36723991.md).
- [PMID:34493867](../papers/34493867.md) — The NCI Sherlock-Lung study used PCAWG LUAD (n=38) as a smoker comparator to benchmark mutational burden and signature profiles in lung cancers in never smokers (LCINS); median TMB in LCINS was >7-fold lower than LUAD-smokers in PCAWG (p=7.0e-73), and SBS4 (tobacco smoking) was absent in all LCINS tumors [PMID:34493867](../papers/34493867.md).

## Notable findings derived from this cohort

- Used as a pan-cancer mutational-burden reference in cHL WGS analysis; PCAWG provided the comparator range against which cHL SBS and indel burdens were evaluated [PMID:36723991](../papers/36723991.md).
- PCAWG LUAD (n=38) served as the smoker reference for mutational burden and signature comparisons in the Sherlock-Lung never-smoker LCINS cohort; LCINS median TMB (1.1 Mut/Mb) was >7-fold lower than LUAD-smokers in PCAWG, and LCINS telomeres were significantly longer (6.4 kb, 95% CI 5.3–7.6, p=7.1e-11) [PMID:34493867](../papers/34493867.md).

## Sources

- Corpus-derived slug. PCAWG is not catalogued by cBioPortal, so there is no canonical `studyId` for this resource [PMID:36723991](../papers/36723991.md).

*This page was processed by **entity-page-writer** on **2026-05-16**.*
