---
name: Uveal Melanoma — QIMR 2016
studyId: um_qimr_2016
institution: QIMR Berghofer Medical Research Institute
size: 28
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - whole-exome-seq
  - sanger-sequencing
panels: []
tags:
  - uveal-melanoma
  - UM
  - driver-discovery
  - gnaq-gna11-pathway
  - mutational-signatures
processed_by: crosslinker
processed_at: 2026-05-14
---

# Uveal Melanoma — QIMR 2016

## Overview

Whole-genome (n=14 primary tumors) and whole-exome (n=14: 9 tumors + 5 primary tumor-derived cell lines) sequencing of 28 untreated uveal melanoma ([UM](../cancer_types/UM.md)) samples with matched germline (blood or saliva) from QIMR Berghofer Medical Research Institute. The study focused on identifying novel driver mutations beyond the canonical [GNAQ](../genes/GNAQ.md), [GNA11](../genes/GNA11.md), [EIF1AX](../genes/EIF1AX.md), [SF3B1](../genes/SF3B1.md), and [BAP1](../genes/BAP1.md). Reference genome GRCh37 (hg19); alignment with BWA + GATK; annotation with ANNOVAR.

## Composition

- 28 untreated [UM](../cancer_types/UM.md) samples with matched germline:
  - 14 primary tumors: [whole-genome-seq](../methods/whole-genome-seq.md).
  - 9 additional tumors + 5 primary cell lines: [whole-exome-seq](../methods/whole-exome-seq.md).
- Cancer type: [UM](../cancer_types/UM.md) (uveal melanoma).
- Low mutation burden: mean 10.6 protein-changing mutations/sample (0.50/Mb).

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) (BWA + GATK indel realignment/base quality recalibration; GRCh37/hg19)
- [whole-exome-seq](../methods/whole-exome-seq.md)
- [sanger-sequencing](../methods/sanger-sequencing.md) ([PLCB4](../genes/PLCB4.md) hotspot validation)
- [annovar](../methods/annovar.md) (variant annotation)
- [mutational-signatures](../methods/mutational-signatures.md) (30 COSMIC signatures; Alexandrov et al. decomposition)

## Papers using this cohort

- [PMID:26683228](../papers/26683228.md) — Johansson et al. 2016, "Deep sequencing of uveal melanoma identifies a recurrent mutation in [PLCB4](../genes/PLCB4.md)," *Oncotarget*.

## Notable findings derived from this cohort

- Recurrent [PLCB4](../genes/PLCB4.md) p.D630Y (c.G1888T) hotspot identified in 2/28 samples, mutually exclusive with [GNAQ](../genes/GNAQ.md)/[GNA11](../genes/GNA11.md) mutations; proposed gain-of-function driver in the Gαq signaling pathway [PMID:26683228](../papers/26683228.md).
- Canonical [UM](../cancer_types/UM.md) drivers confirmed: [GNA11](../genes/GNA11.md) p.Q209P (14 samples), [GNAQ](../genes/GNAQ.md) p.Q209P/p.G48L (8 samples), [BAP1](../genes/BAP1.md) truncating/splice/missense mutations (11 samples), [SF3B1](../genes/SF3B1.md) mutations (3 samples), [EIF1AX](../genes/EIF1AX.md) mutations (4 samples, mutually exclusive with [BAP1](../genes/BAP1.md)) [PMID:26683228](../papers/26683228.md).
- 79% of samples carry COSMIC signature 3 (BRCA/defective DSB repair); no UV signature (COSMIC signature 7) detected in any sample [PMID:26683228](../papers/26683228.md).
- Monosomy 3 or copy-neutral LOH of chromosome 3 in 8/14 WGS samples (57%); all 6 BAP1-mutant samples were hemizygous for chromosome 3 [PMID:26683228](../papers/26683228.md).
- 8q gain is a late event: 93% of mutations on gained 8q arose before the duplication (bimodal VAF analysis) [PMID:26683228](../papers/26683228.md).

## Sources

- [PMID:26683228](../papers/26683228.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
