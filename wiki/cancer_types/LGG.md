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
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Lower-Grade Glioma / LGG (TCGA)

## Overview

LGG is the TCGA cohort identifier for lower-grade glioma (WHO grade II–III). The closest OncoTree equivalent is [LGGNOS](LGGNOS.md) (Lower Grade Glioma, NOS) or [DIFG](DIFG.md) (Diffuse Glioma). LGG is defined primarily by IDH mutation status and 1p/19q co-deletion, which separates oligodendroglioma from astrocytoma subtypes.

## Cohorts in the corpus

- TCGA LGG cohort: included as one of 33 cancer types in the pan-cancer fusion landscape study and the pan-cancer aneuploidy study; subset of the PanCancer Atlas.

## Recurrent alterations

- Pan-cancer fusion study (9,624 TCGA samples) found LGG has a median of 0 fusions per sample (low-fusion cancer type); IDH-mutant LGG clusters separately from IDH-wildtype [GBM](../cancer_types/GBM.md) by arm-level aneuploidy pattern [PMID:29617662](../papers/29617662.md).
- Pan-cancer aneuploidy study found [IDH1](../genes/IDH1.md) mutation defines the LGG subgroup that clusters separately from GBM by aneuploidy pattern, characterized by 1p loss and 19q gain; LGG clusters in the neural-lineage arm-level group with GBM and melanoma [PMID:29622463](../papers/29622463.md).
- Included in TCGA PanCancer Atlas; IDH1-mutant LGG dominates iCluster C11 (highest silhouette); IDH1-wildtype LGG co-clusters with GBM in C23; pan-cancer analysis identifies IDH1 as the defining molecular feature [PMID:29625048](../papers/29625048.md)
- IDH1 defines methylation cluster 1 in LGG (330/351 samples IDH1-mutant); IDH1-driven gliomas show lower STAT1 and reduced CXCL10/immune infiltrate; ATRX- or TP53-mutant LGG tumors have more macrophages and fewer CD8 T-cells (ANOVA P<2e-8) [PMID:29625049](../papers/29625049.md)
- RTK-RAS alteration rate 82% in IDHwt LGG; EGFR altered in 52% of IDHwt LGG; IDH+PI3K inhibitor combination actionable in 14% of IDH-mutant LGG [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); IDH/1p19q status established as more robust survival predictor than histologic subtype, contributing evidence to WHO 2016 glioma diagnostic update [PMID:29625055](../papers/29625055.md)
- LGG (WHO grade II–III) comprised 39/85 patients in the MSK-IMPACT CSF liquid-biopsy cohort; truncal alterations (IDH1/IDH2, TP53, ATRX, TERT, 1p/19q codeletion) were 100% concordant between CSF ctDNA and matched tumor tissue in all 10/10 non-hypermutated LGG pairs. [PMID:30675060](../papers/30675060.md)

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
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30675060](../papers/30675060.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
