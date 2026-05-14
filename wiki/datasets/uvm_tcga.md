---
name: Uveal Melanoma — TCGA
studyId: uvm_tcga
institution: The Cancer Genome Atlas Research Network
size: 80
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - uveal-melanoma
  - UM
  - tcga
  - gnaq-gna11-pathway
  - plcb4
processed_by: crosslinker
processed_at: 2026-05-14
---

# Uveal Melanoma — TCGA

## Overview

The Cancer Genome Atlas (TCGA) uveal melanoma ([UM](../cancer_types/UM.md)) cohort comprising 80 samples released on 2015-11-14. This dataset serves as an external validation resource for [UM](../cancer_types/UM.md) driver discovery, particularly for the confirmation of novel recurrent mutations identified in other cohorts. Reference genome hg19.

## Composition

- **80 uveal melanoma samples** (released 2015-11-14 during peer review of the QIMR 2016 study).
- Cancer type: [UM](../cancer_types/UM.md) (uveal melanoma).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)

## Papers using this cohort

- [PMID:26683228](../papers/26683228.md) — Johansson et al. 2016, "Deep sequencing of uveal melanoma identifies a recurrent mutation in [PLCB4](../genes/PLCB4.md)," *Oncotarget* (external validation use).

## Notable findings derived from this cohort

- 2/80 TCGA [UM](../cancer_types/UM.md) samples carried codon p.D630 [PLCB4](../genes/PLCB4.md) mutations, corroborating the hotspot identified in [um_qimr_2016](../datasets/um_qimr_2016.md): TCGA-VD-A8KD with adjacent c.G1888T + c.A1889T variants (p.D630Y + p.D630V, or p.D630F in cis) and TCGA-YZ-A985 with c.G1888A (p.D630N) [PMID:26683228](../papers/26683228.md).

## Sources

- [PMID:26683228](../papers/26683228.md)
- TCGA data portal (uvm_tcga)

*This page was processed by **crosslinker** on **2026-05-14**.*
