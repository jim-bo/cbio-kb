---
name: Lower-Grade Glioma (TCGA)
oncotree_code: LGG
main_type: Glioma
parent: DIFG
tags:
  - brain
  - glioma
  - idh
  - tcga-cohort
unverified: true
canonical_source: corpus
processed_by: crosslinker
processed_at: 2026-05-15
---

# Lower-Grade Glioma / LGG (TCGA)

## Overview

LGG is the TCGA cohort identifier for lower-grade glioma (WHO grade II–III). The closest OncoTree equivalent is [LGGNOS](LGGNOS.md) (Lower Grade Glioma, NOS) or [DIFG](DIFG.md) (Diffuse Glioma). LGG is defined primarily by IDH mutation status and 1p/19q co-deletion, which separates oligodendroglioma from astrocytoma subtypes.

## Cohorts in the corpus

- TCGA LGG cohort: included as one of 33 cancer types in the pan-cancer fusion landscape study and the pan-cancer aneuploidy study; subset of the PanCancer Atlas.

## Recurrent alterations

- Pan-cancer fusion study (9,624 TCGA samples) found LGG has a median of 0 fusions per sample (low-fusion cancer type); IDH-mutant LGG clusters separately from IDH-wildtype [GBM](../cancer_types/GBM.md) by arm-level aneuploidy pattern [PMID:29617662](../papers/29617662.md).
- Pan-cancer aneuploidy study found [IDH1](../genes/IDH1.md) mutation defines the LGG subgroup that clusters separately from GBM by aneuploidy pattern, characterized by 1p loss and 19q gain; LGG clusters in the neural-lineage arm-level group with GBM and melanoma [PMID:29622463](../papers/29622463.md).

## Subtypes

- **IDH-mutant, 1p/19q co-deleted:** oligodendroglioma; characterized by low arm-level aneuploidy except 1p/19q.
- **IDH-mutant, 1p/19q intact:** astrocytoma; typically lower aneuploidy than GBM.
- **IDH-wildtype LGG:** behaviorally similar to GBM; not expected to be common in the TCGA LGG cohort by design.
- The 1p/19q co-deletion in LGG (Cairncross et al., 2013) is a precedent for arm-level alterations being therapeutically relevant [PMID:29622463](../papers/29622463.md).

## Therapeutic landscape

*No drug-specific findings for LGG reported in the current corpus beyond IDH-inhibitor relevance.*

## Sources

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion landscape (Gao et al., 2018)
- [PMID:29622463](../papers/29622463.md) — Pan-cancer aneuploidy landscape (Taylor et al., 2018)

*This page was processed by **crosslinker** on **2026-05-15**.*
