---
name: Skin Cutaneous Melanoma (TCGA, PanCancer Atlas 2018)
studyId: skcm_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 470
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - skcm
  - melanoma
  - skin
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Skin Cutaneous Melanoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Skin Cutaneous Melanoma PanCancer Atlas 2018 cohort is the [SKCM](../cancer_types/SKCM.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `skcm_tcga_pan_can_atlas_2018`. It covers approximately 470 melanoma samples (103 primary, 296 regional lymph-node metastases, 68 distant metastases) with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [SKCM](../cancer_types/SKCM.md) has among the highest mutation rates (UVB signature; C15:SKCM/UVM iCluster has highest mutation rates), the highest pan-cancer RTK-RAS pathway alteration frequency (95%), and the highest OncoKB Level 1/2A actionable-alteration rate (46%, driven by [BRAF](../genes/BRAF.md) hotspots).

## Composition

- Cancer type: Skin Cutaneous Melanoma ([SKCM](../cancer_types/SKCM.md)), OncoTree code [MEL](../cancer_types/MEL.md).
- Approximately 470 tumor samples: 103 primary, 296 regional lymph-node metastases, 68 distant metastases (SKCM is the exception to the primarily primary-tumor TCGA rule).
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline; among the highest SNV burden (UVB mutagenesis signature).
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.
- 4% metastatic samples in the broader 9,125-tumor pan-cancer dataset from SKCM.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)

## Notable findings derived from this cohort

- C15:SKCM/UVM iCluster (alongside uveal melanoma) shows the highest mutation rates pan-cancer, driven by UVB mutational signature; this contrasts with C14:[LUAD](../cancer_types/LUAD.md) (smoking signature) which is the other high-mutation iCluster. [PMID:29625048](../papers/29625048.md)
- RTK-RAS pathway altered in 95% of SKCM — the highest rate of any cancer type in the pan-cancer cohort; [BRAF](../genes/BRAF.md) hotspots in 51% of SKCM. [PMID:29625049](../papers/29625049.md)
- SKCM leads pan-cancer actionability with 46% of samples carrying an OncoKB Level 1 or 2A alteration (driven by BRAF hotspots); PI3K+RAF co-targeting opportunity in 12% of SKCM. [PMID:29625049](../papers/29625049.md)
- Within pan-cancer immune subtype C3 (Inflammatory), BRAF-mutant SKCM tumors have higher CD8 T-cell fraction than NRAS-mutant tumors (ANOVA P<2e-5), and a CD8-CD274(PD-L1)-PDCD1(PD-1) signaling loop supports BRAF+PD-L1 co-targeting rationale. [PMID:29625049](../papers/29625049.md)

## Sources

- cBioPortal study: `skcm_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
