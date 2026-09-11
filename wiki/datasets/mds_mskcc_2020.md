---
name: Myelodysplastic (MSK, 2020)
studyId: mds_mskcc_2020
institution: Memorial Sloan Kettering Cancer Center (MSKCC)
size: 4231
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - whole-genome-amplification
panels: []
tags:
  - myelodysplastic-syndrome
  - MDS
  - CMML
  - splicing
  - clonal-evolution
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Myelodysplastic (MSK, 2020)

## Overview

Per the cBioPortal study record in `schema/ontology/studies.json`, this composite cohort has 4,231 samples on hg19 and is backed by three constituent publications: Papaemmanuil et al., *Blood* 2013 ([PMID:24030381](../papers/24030381.md)); Papaemmanuil et al., *NEJM* 2016 (PMID:27276561); and Tyner et al., *Nature* 2018 (PMID:30333627). Only the first of these ([PMID:24030381](../papers/24030381.md)) is a citing paper for this wiki entry; the other two constituent publications are not yet compiled here, and their cohort details are not asserted on this page.

## Composition

- The cBioPortal `mds_mskcc_2020` record aggregates 4,231 samples across its three constituent publications; this total does **not** correspond to any single publication's own cohort.
- The [PMID:24030381](../papers/24030381.md) constituent cohort (ICGC Chronic Myeloid Disorders Working Group, Papaemmanuil et al. 2013) targeted-sequenced 111 cancer genes in 738 patients with myelodysplastic syndromes ([MDS](../cancer_types/MDS.md)) or closely related neoplasms, including chronic myelomonocytic leukemia ([CMML](../cancer_types/CMML.md)); 595 of these patients had outcome data [PMID:24030381](../papers/24030381.md).

## Assays / panels (linked)

- [PMID:24030381](../papers/24030381.md) constituent cohort: [whole-genome-amplification](../methods/whole-genome-amplification.md) followed by RNA-bait capture [targeted DNA sequencing](../methods/targeted-dna-seq.md) of 111 genes (tumor-only, no matched germline).

## Papers using this cohort

- [PMID:24030381](../papers/24030381.md) — Papaemmanuil et al. (ICGC Chronic Myeloid Disorders Working Group), one of three source publications backing this composite cBioPortal study: proposes a genetic "predestination" model of MDS clonal evolution.

## Notable findings derived from this cohort

- In the [PMID:24030381](../papers/24030381.md) cohort, 78% of patients had at least one oncogenic lesion, spanning 43 genes led by *[SF3B1](../genes/SF3B1.md)* (24%), *[TET2](../genes/TET2.md)* (22%) and *[SRSF2](../genes/SRSF2.md)* (14%); 46 significant pairwise gene–gene associations centered on spliceosome genes and epigenetic modifiers [PMID:24030381](../papers/24030381.md).
- Allele-fraction ordering suggested splicing and DNA-methylation mutations occur early and chromatin/signaling mutations occur later; leukemia-free survival fell from a median of 49 months with 1 driver lesion to 4 months with ≥6, independent of IPSS [PMID:24030381](../papers/24030381.md).

## Sources

- cBioPortal study record: `mds_mskcc_2020` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`; 3 constituent PMIDs per the record's `pmid` field).
- [PMID:24030381](../papers/24030381.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
