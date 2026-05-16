---
name: Uterine Carcinosarcoma (TCGA, PanCancer Atlas 2018)
studyId: ucs_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 57
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - ucs
  - uterine
  - carcinosarcoma
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Uterine Carcinosarcoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Uterine Carcinosarcoma PanCancer Atlas 2018 cohort is the [UCS](../cancer_types/UCS.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `ucs_tcga_pan_can_atlas_2018`. It covers approximately 57 uterine carcinosarcoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [UCS](../cancer_types/UCS.md) was among cancer types with substantial intra-type molecular heterogeneity (<50% of samples in any single iCluster). HER2+PI3K co-targeting opportunity exists in 7% of UCS per pan-cancer pathway analysis.

## Composition

- Cancer type: Uterine Carcinosarcoma ([UCS](../cancer_types/UCS.md)), OncoTree code MMMT.
- Approximately 57 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)

## Notable findings derived from this cohort

- UCS was among 8 cancer types with <50% of samples in any single iCluster, indicating substantial residual molecular heterogeneity; C20: mixed (stromal/immune) contains UCS among 25 of 33 tumor types. [PMID:29625048](../papers/29625048.md)
- HER2+PI3K co-targeting opportunity in 7% of UCS (alongside 7% in [UCEC](../cancer_types/UCEC.md) CN-high and 7% in cervical adenocarcinoma) per pan-cancer actionable combination analysis. [PMID:29625049](../papers/29625049.md)
- Pan-cancer somatic driver and germline analysis (11,000 tumors, 33 cancer types) included UCS in co-occurrence/mutual-exclusivity driver networks. [PMID:29625049](../papers/29625049.md)

## Sources

- cBioPortal study: `ucs_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
