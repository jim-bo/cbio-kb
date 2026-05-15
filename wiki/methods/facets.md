---
name: FACETS
slug: facets
kind: method
canonical_source: 
unverified: true
tags: [copy-number, clonality, computational]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# FACETS

## Overview

Allele-specific copy-number and clonality inference tool for tumor/normal NGS data.

## Used by

- [PMID:36493333](../papers/36493333.md) — used to assess clonality in the appendiceal adenocarcinoma MSK-IMPACT cohort, supporting the molecular subtyping of mucinous appendiceal adenocarcinoma into RAS-mut, GNAS-mut, and TP53-mut predominant lineages [PMID:36493333](../papers/36493333.md).
- [PMID:37682528](../papers/37682528.md) — used to derive allele-specific copy-number calls from MSK-IMPACT in 1,507 urothelial carcinoma tumors, supporting assessment of [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) co-alteration patterns in [FGFR3](../genes/FGFR3.md)-altered disease [PMID:37682528](../papers/37682528.md).
- [PMID:37651310](../papers/37651310.md) — FACETS used for copy-number analysis in 1,882 endometrial carcinoma patients sequenced by MSK-IMPACT; supported identification of CN-H/TP53abn molecular subtype enriched in Black patients [PMID:37651310](../papers/37651310.md).
- [PMID:38630790](../papers/38630790.md) — FACETS used to assess tumor purity and detect genomic near-haploidization (LOH >80%) in 210 evaluable diffuse pleural mesothelioma patients from MSK-IMPACT sequencing [PMID:38630790](../papers/38630790.md).
- [PMID:38758238](../papers/38758238.md) — FACETS v0.5.6 used for allele-specific copy-number and LOH inference in pituitary neuroendocrine tumors; identified rcLOH pattern in 11/14 treatment-refractory corticotroph PitNETs [PMID:38758238](../papers/38758238.md).
- [PMID:38949888](../papers/38949888.md) — FACETS v0.5.6 used for copy-number analysis in 3,244 prostate cancer tumors from 2,257 patients sequenced by MSK-IMPACT [PMID:38949888](../papers/38949888.md).
- [PMID:39753968](../papers/39753968.md) — FACETS v0.5.14 used in a two-step pipeline for allele-specific copy-number inference in 2,336 PDAC patients sequenced with MSK-IMPACT; 1,555 of 2,322 tumors passed copy-number QC; FACETS output enabled classification of [KRAS](../genes/KRAS.md) allelic imbalance events (focal/arm amplifications, gains, CNLOH, LOH, post-WGD loss) and showed that [KRAS](../genes/KRAS.md) mutant-allele dosage gains independently predict shorter [OS](../cancer_types/OS.md) across all clinical stages [PMID:39753968](../papers/39753968.md).
- Used to assess tumor purity (>=25% threshold) in 22 primary-metastasis WES pairs for bladder cancer clonal evolution analysis [PMID:36543146](../papers/36543146.md)
- FACETS used for allele-specific copy-number estimation and clonality assessment in 151 advanced head and neck tumors sequenced with MSK-IMPACT; identified whole-genome duplication in 25% of HNSC cases and quantified 3p deletions enriched in recurrent HPV-positive disease [PMID:27442865](../papers/27442865.md)
- Applied FACETS algorithm to infer somatic copy number alterations and tumor purity/ploidy from sequencing data [PMID:28336552](../papers/28336552.md)
- Used to estimate cancer cell fraction and clonality of alterations in MSK-IMPACT-sequenced prostate cancer tumors (504 tumors from 451 patients); identified TP53 and BRCA2 somatic alterations as early truncal clonal events in patients who later developed metastasis [PMID:28825054](../papers/28825054.md)

## Notes

- In the appendiceal cohort, FACETS-derived clonality was paired with aneuploidy scoring (segment-length-weighted copy-number deviation from diploid), where TP53-mut predominant tumors were highly aneuploid and aneuploidy was independently associated with poor prognosis (P=.001) [PMID:36493333](../papers/36493333.md).

## Sources

- [PMID:36493333](../papers/36493333.md)
- [PMID:37682528](../papers/37682528.md)
- [PMID:37651310](../papers/37651310.md)
- [PMID:38630790](../papers/38630790.md)
- [PMID:38758238](../papers/38758238.md)
- [PMID:38949888](../papers/38949888.md)
- [PMID:39753968](../papers/39753968.md)

*This page was processed by **crosslinker** on **2026-05-04**.*
- [PMID:36543146](../papers/36543146.md)

*This page was processed by **wiki-cli** on **2026-05-05**.*
- [PMID:27442865](../papers/27442865.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28336552](../papers/28336552.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
