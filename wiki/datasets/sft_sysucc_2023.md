---
name: Solitary Fibrous Tumors (SYSUCC, Nat Commun 2023)
studyId: sft_sysucc_2023
institution: Sun Yat-sen University Cancer Center (SYSUCC)
size: 131
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - immunohistochemistry
panels:
  - geneplus-1021-gene-panel
tags:
  - solitary-fibrous-tumor
  - SFT
  - IDH1
  - MTOR
  - NAB2-STAT6
processed_by: crosslinker
processed_at: 2026-09-11
---

# Solitary Fibrous Tumors (SYSUCC, Nat Commun 2023)

## Overview

The SYSUCC discovery cohort (n=131) of the Zhang, Yang, Hu et al. solitary fibrous tumor ([SFT](../cancer_types/SFT.md)) study, resected 2008–2020 at Sun Yat-sen University Cancer Center and profiled with a 1021-gene targeted NGS panel; three independent validation cohorts (FAHSYSU, CHCAMS1, CHCAMS2, total n=277) were also profiled but are not part of this cBioPortal record. Name, institution, size (131) and reference genome (hg19) are taken from the cBioPortal study record in `schema/ontology/studies.json` [PMID:37980418](../papers/37980418.md).

## Composition

- 131 histologically confirmed SFTs, the SYSUCC discovery cohort within a larger 408-tumor, four-cohort study [PMID:37980418](../papers/37980418.md).
- [STAT6](../genes/STAT6.md) IHC positivity (diagnostic surrogate for the *[NAB2](../genes/NAB2.md)*–*[STAT6](../genes/STAT6.md)* fusion) in 91.60% (120/131); RT-PCR in 11 IHC-negative cases confirmed the fusion in 5 more, bringing molecular/IHC confirmation to 95.42% (125/131) [PMID:37980418](../papers/37980418.md).

## Assays / panels (linked)

- [Geneplus 1021-gene panel](../methods/geneplus-1021-gene-panel.md) (Geneplus-Beijing, hybrid-capture, ~1.1 Mb), run on the SYSUCC discovery cohort only [PMID:37980418](../papers/37980418.md).
- Multiplex [immunohistochemistry](../methods/immunohistochemistry.md) (STAT6, Ki-67, [CD68](../genes/CD68.md), CD163, HLA-DPB1, PD-L1, CD3, [CD4](../genes/CD4.md), CD8, [FOXP3](../genes/FOXP3.md), CD11c, CD20) quantified with HALO 2.3 digital pathology [PMID:37980418](../papers/37980418.md).

## Papers using this cohort

- [PMID:37980418](../papers/37980418.md) — Zhang, Yang, Hu et al. (SYSUCC), source publication: identifies an actionable *[IDH1](../genes/IDH1.md)* p.R132S hotspot and a macrophage-dominant PD-L1-high immune subset, and builds a four-variable integrated risk model for PFS.

## Notable findings derived from this cohort

- *[IDH1](../genes/IDH1.md)* p.R132S was found in 6.9% (9/131) of SYSUCC SFTs, enriched in malignant/high-pleomorphism/high-cellularity tumors; 24.4% (32/131) showed a macrophage-dominant, PD-L1-high immune infiltrate [PMID:37980418](../papers/37980418.md).
- Across the 1021-gene panel, the most frequently altered genes in the SYSUCC cohort were *[ZFHX3](../genes/ZFHX3.md)* (25%), *[KMT2C](../genes/KMT2C.md)* (21%) and *[TERT](../genes/TERT.md)* (19%); *[MTOR](../genes/MTOR.md)* mutation (3.05–8.70% across cohorts) was associated with shorter PFS (HR 8.31) and became one of four variables (with mitotic count, Ki-67+ density, CD163+ density) in an integrated risk model that outperformed the WHO classification, mDemicco model, and G-score [PMID:37980418](../papers/37980418.md).

## Sources

- cBioPortal study record: `sft_sysucc_2023` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:37980418](../papers/37980418.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
