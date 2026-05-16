---
name: MSK Uterine Sarcoma (Hensley et al. 2020)
studyId: usarc_msk_2020
institution: Memorial Sloan Kettering Cancer Center
size: 107
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - uterine-sarcoma
  - leiomyosarcoma
  - MSK-IMPACT
  - sarcoma
  - prospective
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Uterine Sarcoma (Hensley et al. 2020)

## Overview

Prospective single-institution cohort of 107 women with histologically confirmed uterine sarcoma profiled at Memorial Sloan Kettering Cancer Center between April 2014 and April 2017 under IRB protocol NCT01775072. Tumors were sequenced by the [MSK-IMPACT](../methods/msk-impact-panel.md) targeted DNA panel, with [MSK-Fusion](../methods/msk-fusion.md) RNA sequencing in a diagnostic subset. Designed to characterize the genomic landscape of uterine sarcoma subtypes and identify actionable alterations. Released on cBioPortal as usarc_msk_2020. [PMID:32299819](../papers/32299819.md)

## Composition

- 107 women with uterine sarcoma; histologic breakdown: [ULMS](../cancer_types/ULMS.md) n=80, high-grade non-LMS n=22 (HG-ESS n=7, undifferentiated n=5, high-grade adenosarcoma with sarcomatous overgrowth n=4, other rare subtypes), [LGESS](../cancer_types/LGESS.md) n=4, STUMP n=2.
- Cancer type OncoTree code: [USARC](../cancer_types/USARC.md).
- 57% (n=61) FIGO stage I at diagnosis; 89% (n=95) recurrent or metastatic at time of sequencing; 94.3% (n=101) histologically high grade.
- Samples: 39% (n=42) primary, 61% (n=66) metastatic.
- Median survival from diagnosis 5.6 years (range 0.2–23.1). [PMID:32299819](../papers/32299819.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — three panel versions: 341-gene (n=44), 410-gene (n=44), 468-gene (n=20); average ~646x coverage.
- [MSK-Fusion](../methods/msk-fusion.md) — RNA panel used diagnostically in a subset for fusion detection.
- [MSIsensor](../methods/msisensor.md) v0.2 for MSI scoring; [FACETS](../methods/facets.md) v0.5.6 for allele-specific copy-number, purity, and ploidy.
- Germline variant annotation across 76 cancer-predisposition genes via MSK-IMPACT germline pipeline.
- Actionability annotated by OncoKB (October 2019). [PMID:32299819](../papers/32299819.md)

## Papers using this cohort

- [PMID:32299819](../papers/32299819.md) — Hensley et al., prospective genomic profiling of 107 uterine sarcomas; TP53/RB1/ATRX as dominant uLMS drivers; [BRCA2](../genes/BRCA2.md) homozygous deletions with PARP-inhibitor responses; [PDCD1](../genes/PDCD1.md) deletions enriched vs. pan-cancer.

## Notable findings derived from this cohort

- uLMS driver landscape: [TP53](../genes/TP53.md) 56%, [RB1](../genes/RB1.md) 51%, [ATRX](../genes/ATRX.md) 31% loss-of-function alterations; significantly more frequent than in high-grade non-LMS (14%, 14%, 5%; p<0.01 each). [PMID:32299819](../papers/32299819.md)
- [BRCA2](../genes/BRCA2.md) homozygous deletions in ~5% of uLMS (exclusively in uLMS); seven total somatic BRCA2 alterations; PARP-inhibitor-containing therapy produced sustained partial responses in BRCA2-altered uLMS patients. [PMID:32299819](../papers/32299819.md)
- [PDCD1](../genes/PDCD1.md) homozygous deletions in uLMS at the highest frequency among all cancer types with ≥25 cases in a concurrent 15,816-patient MSK-IMPACT pan-cancer cohort; IHC confirmed PD-1 protein loss. [PMID:32299819](../papers/32299819.md)
- Potentially actionable alterations in 45% (48/107); 17% (8/48) received matched therapy, with two radiographic responses. [PMID:32299819](../papers/32299819.md)
- 50.5% (50/99) of high-grade uterine sarcomas displayed whole-genome duplication; none of the low-grade tumors (p=0.04); WGD not associated with [OS](../cancer_types/OS.md). [PMID:32299819](../papers/32299819.md)
- Two MSI-H hypermutated uLMS cases (MSIsensor ≥10; IHC loss of [MSH2](../genes/MSH2.md) and [MSH6](../genes/MSH6.md) respectively); both remain disease-free at 5.9 and 13 years after multimodality therapy without immune checkpoint inhibitors. [PMID:32299819](../papers/32299819.md)
- [MED12](../genes/MED12.md) mutated in only 11% (9/80) of uLMS vs. ~70% in benign leiomyomas, arguing against uLMS evolving from antecedent leiomyomas. [PMID:32299819](../papers/32299819.md)
- Genomic profiling enabled diagnostic reclassification in 3 cases (2 uLMS to [IMT](../cancer_types/IMT.md) via [ALK](../genes/ALK.md) fusion; 1 uLMS to BCOR-mutated high-grade stromal sarcoma). [PMID:32299819](../papers/32299819.md)

## Sources

- [PMID:32299819](../papers/32299819.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
