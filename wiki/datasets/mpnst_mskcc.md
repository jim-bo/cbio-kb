---
name: Malignant Peripheral Nerve Sheath Tumor — MSKCC
studyId: mpnst_mskcc
institution: Memorial Sloan Kettering Cancer Center
size: 15 (WES discovery) + 37 FFPE MPNSTs + 7 neurofibromas (validation)
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - affymetrix-snp6
  - msk-impact-panel
panels:
  - msk-impact-panel
tags:
  - sarcoma
  - mpnst
  - prc2
  - neurofibromatosis
  - polycomb
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# Malignant Peripheral Nerve Sheath Tumor — MSKCC

## Overview

Multi-platform genomic characterization of malignant peripheral nerve sheath tumors (MPNSTs) generated at Memorial Sloan Kettering Cancer Center by Lee et al. (2014). The discovery cohort used whole-exome sequencing, SNP6.0 copy number arrays, and RNA-seq on 15 fresh-frozen tumor/normal pairs from 12 patients. A validation cohort of 37 FFPE MPNSTs and 7 neurofibromas from 32 NF1 patients was profiled by MSK-IMPACT targeted hybrid-capture sequencing.

## Composition

- **Cancer type:** [MPNST](../cancer_types/MPNST.md) (malignant peripheral nerve sheath tumor).
- **Discovery cohort:** 15 fresh-frozen MPNSTs from 12 patients — 6 NF1-associated, 4 sporadic, 4 radiotherapy-associated, 1 epithelioid.
- **Validation cohort:** 37 FFPE MPNSTs and 7 neurofibromas from 32 NF1 patients.
- **Functional validation:** ST88-14 (NF1-associated, SUZ12-deficient) and MPNST724 (PRC2-wt) cell lines.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Illumina HiSeq-2500, paired-end 51 bp; aligned to hg19 with STAR v2.3; MuTect, Strelka, VarScan variant calling.
- [rna-seq](../methods/rna-seq.md) — TruSeq, Illumina HiSeq-2500, ~68M paired-end reads/sample; STAR alignment.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — Affymetrix SNP6.0 arrays for copy-number profiling.
- [msk-impact-panel](../methods/msk-impact-panel.md) — targeted hybrid-capture (includes NF1, SUZ12, EED, CDKN2A, TP53) on validation cohort.

## Papers using this cohort

- [PMID:25240281](../papers/25240281.md) — Lee et al. (2014), *Nature Genetics*. PRC2 is recurrently inactivated through EED or SUZ12 loss in malignant peripheral nerve sheath tumors.

## Notable findings derived from this cohort

- Loss-of-function alterations in EED or SUZ12 (PRC2 core components) are found in 92% of sporadic, 70% of NF1-associated, and 90% of radiotherapy-associated MPNSTs; EED and SUZ12 alterations are mutually exclusive [PMID:25240281](../papers/25240281.md).
- NF1, CDKN2A, and PRC2 (EED or SUZ12) alterations significantly co-occur (Fleiss' κ=0.21, P=0.001) [PMID:25240281](../papers/25240281.md).
- PRC2 loss produces aberrant re-expression of developmentally suppressed homeobox master regulators (FOXN4, IGF2, PAX2, TLX1) and is detectable by H3K27me3 IHC loss in tumor cells [PMID:25240281](../papers/25240281.md).
- H3K27me3 IHC is retained in all 7 neurofibromas and lost at MPNST/neurofibroma interfaces, proposing a biomarker for malignant transformation [PMID:25240281](../papers/25240281.md).
- Epithelioid MPNST harbors no PRC2, NF1, or CDKN2A alterations, suggesting it is a molecularly distinct entity [PMID:25240281](../papers/25240281.md).

## Sources

- cBioPortal study: `mpnst_mskcc`.

*This page was processed by **entity-page-writer** on **2026-05-11**.*
