---
name: Skin Cutaneous Melanoma (Broad, Cell 2012)
studyId: skcm_broad
institution: Broad Institute
size: 121
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - melanoma
  - cutaneous
  - broad
  - skcm
processed_by: entity-page-writer
processed_at: "2026-05-06"
---

# Skin Cutaneous Melanoma (Broad, Cell 2012)

## Overview

The Broad melanoma dataset comprises 121 qualified melanoma tumor/normal pairs from 135 patients profiled by whole-exome sequencing. The study (Hodis et al., Cell 2012) focused on [SKCM](../cancer_types/SKCM.md) (cutaneous melanoma) with representation from multiple sample types (primary tumors, metastatic samples, short-term cultures from metastatic tissue). The cohort was used to discover six novel melanoma driver genes using the InVEx permutation statistical framework, which accounts for the high UV-induced somatic mutation background characteristic of melanoma.

## Composition

- 121 qualified tumor/normal pairs from 135 melanoma patients
- Subtypes: 95 cutaneous, 5 acral, 2 mucosal, 1 uveal, 18 unknown primary
- Sample types: 15 primary tumors, 30 metastatic, 76 short-term cultures from metastatic tissue
- Validation extension sets: n=59, n=63, and n=175 additional melanoma samples (Sequenom genotyping)
- Cancer type: [SKCM](../cancer_types/SKCM.md), [MEL](../cancer_types/MEL.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — solution-phase hybrid capture; 103-fold mean target coverage
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — copy-number analysis with GISTIC
- [gistic](../methods/gistic.md) — applied to SNP 6.0 copy-number data
- [sequenom-genotyping](../methods/sequenom-genotyping.md) — validation genotyping in extension sets

## Papers using this cohort

- [PMID:22817889](../papers/22817889.md) — Hodis et al. Cell 2012 primary analysis

## Notable findings derived from this cohort

- Median somatic mutation rate 14.4 coding mutations/Mb (highest of any tumor type at the time); 82.2% UV-signature C>T transitions [PMID:22817889](../papers/22817889.md)
- Six novel significantly mutated melanoma genes identified: [PPP6C](../genes/PPP6C.md), [RAC1](../genes/RAC1.md), [SNX31](../genes/SNX31.md), [TACC1](../genes/TACC1.md), STK19, [ARID2](../genes/ARID2.md) [PMID:22817889](../papers/22817889.md)
- RAC1 P29S validated as gain-of-function, UV-induced driver at 3.9% prevalence across discovery + extension sets (14/355 patients) [PMID:22817889](../papers/22817889.md)
- 83% of samples had hotspot [BRAF](../genes/BRAF.md) or [NRAS](../genes/NRAS.md) mutations (mutually exclusive, p=3e-14); [PTEN](../genes/PTEN.md) loss co-occurred with BRAF (44%) but rarely with NRAS (4%) [PMID:22817889](../papers/22817889.md)
- [NF1](../genes/NF1.md) loss-of-function enriched in BRAF/NRAS-WT melanomas (25% vs 2%, p=5.8e-3) [PMID:22817889](../papers/22817889.md)

## Sources

- [PMID:22817889](../papers/22817889.md) — Hodis et al. Cell 2012

*This page was processed by **entity-page-writer** on **2026-05-06**.*
