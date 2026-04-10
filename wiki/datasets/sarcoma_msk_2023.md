---
name: "Radiation-Associated Sarcomas (MSK, 2023)"
slug: sarcoma_msk_2023
institution: "Memorial Sloan Kettering Cancer Center"
size: 82
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
tags:
  - radiation-associated-sarcoma
  - comparative-genomics
processed_by: crosslinker
processed_at: 2026-04-10
---

# Radiation-Associated Sarcomas (MSK, 2023)

## Overview

The sarcoma_msk_2023 dataset is a Memorial Sloan Kettering Cancer Center (MSK) cohort of 82 radiation-associated (RT) sarcoma patients spanning four histotypes: angiosarcoma, malignant peripheral nerve sheath tumor, undifferentiated pleomorphic sarcoma, and osteosarcoma. The study compared the genomic landscapes of RT-sarcomas with matched sporadic sarcoma controls (548 total sporadic cases) [PMID:37350195](../papers/37350195.md).

## Composition

- 44 RT-[ANGS](../cancer_types/ANGS.md) (38 from breast/chest wall) [PMID:37350195](../papers/37350195.md).
- 12 RT-[MPNST](../cancer_types/MPNST.md) [PMID:37350195](../papers/37350195.md).
- 14 RT-[MFH](../cancer_types/MFH.md) (UPS) [PMID:37350195](../papers/37350195.md).
- 12 RT-[OS](../cancer_types/OS.md) [PMID:37350195](../papers/37350195.md).
- Control groups: 135 sporadic AS, 64 sporadic [MPNST](../cancer_types/MPNST.md), 273 sporadic UPS, 76 sporadic [OS](../cancer_types/OS.md) [PMID:37350195](../papers/37350195.md).
- Demographics: 68 (83%) female, 14 (17%) male, age 37-88 years (mean 64) [PMID:37350195](../papers/37350195.md).
- Reference genome: GRCh37 (hg19) [PMID:37350195](../papers/37350195.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted DNA next-generation sequencing panel [PMID:37350195](../papers/37350195.md).

## Papers using this cohort

- [PMID:37350195](../papers/37350195.md) — Dermawan JK et al., "Distinct genomic landscapes in radiation-associated angiosarcoma compared with other radiation-associated sarcoma histologies," J Pathol 2023.

## Notable findings derived from this cohort

- RT-AS has a genomically distinct landscape from other RT-sarcoma histotypes, dominated by [MYC](../genes/MYC.md) amplification (75%), while other RT-sarcomas are driven by [TP53](../genes/TP53.md) and [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) loss [PMID:37350195](../papers/37350195.md).
- RT-MPNST showed the highest FGA (51%) and near-universal CDKN2A/B deletions (92%) [PMID:37350195](../papers/37350195.md).
- Each RT-sarcoma histotype harbored distinct mutations and copy number alterations, supporting histotype-specific therapeutic approaches [PMID:37350195](../papers/37350195.md).
- MYC-amplified RT-AS had significantly shorter latency from radiation to sarcoma diagnosis than non-MYC-amplified cases (P = 0.0083) [PMID:37350195](../papers/37350195.md).
- Predominant mutational signatures across all four RT-sarcoma histotypes were associated with errors in DNA repair and replication [PMID:37350195](../papers/37350195.md).

## Sources

- [PMID:37350195](../papers/37350195.md) — Dermawan JK et al., J Pathol 2023.

*This page was processed by **crosslinker** on **2026-04-10**.*
