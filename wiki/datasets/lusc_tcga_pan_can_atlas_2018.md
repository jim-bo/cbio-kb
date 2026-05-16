---
name: Lung Squamous Cell Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: lusc_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 501
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - lusc
  - lung
  - squamous
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Lung Squamous Cell Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Lung Squamous Cell Carcinoma PanCancer Atlas 2018 cohort is the [LUSC](../cancer_types/LUSC.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `lusc_tcga_pan_can_atlas_2018`. It covers approximately 501 lung squamous cell carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [LUSC](../cancer_types/LUSC.md) co-clusters in pan-squamous iClusters with [HNSC](../cancer_types/HNSC.md), [CESC](../cancer_types/CESC.md), and [ESCA](../cancer_types/ESCA.md), sharing dNp63/TAp63 squamous signaling. LUSC has the highest somatic-to-germline genome-integrity disruption ratio (89% somatic vs 4% germline) across all 33 TCGA cancer types. All four clinical endpoints are recommended without reservation for LUSC by TCGA-CDR.

## Composition

- Cancer type: Lung Squamous Cell Carcinoma ([LUSC](../cancer_types/LUSC.md)), OncoTree code LUSC.
- Approximately 501 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline; high SNV burden consistent with tobacco-associated mutagenesis (C>A transversions).
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)
- [PMID:29625050](../papers/29625050.md) — TCGA PanCancer Atlas oncogenic pathway analysis (Sanchez-Vega et al., 2018)

## Notable findings derived from this cohort

- LUSC co-clusters in pan-squamous iClusters (C10, C25 chr11 amp, C27 HPV+); shares dNp63/TAp63 squamous signaling, proliferation, hypoxia, and basal signaling programs with HNSC, CESC, and ESCA. [PMID:29625048](../papers/29625048.md)
- LUSC has the highest somatic genome-integrity disruption rate (89%) vs 4% germline — the most extreme germline-somatic ratio across all 33 TCGA cancer types; [OV](../cancer_types/OV.md) is most skewed in both germline and somatic compartments. [PMID:29625049](../papers/29625049.md)
- JAK2/STAT1/3/6 signaling upregulated in pan-squamous iClusters including LUSC; C3 and C20 (immune-enriched) also co-activate JAK-STAT with LUSC's pan-SCC cluster. [PMID:29625048](../papers/29625048.md)
- PI3K pathway dominant in LUSC (68% alteration frequency); NRF2/oxidative-stress pathway peaks in LUSC (25%) and esophagogastric squamous (23%); NRF2-PI3K co-occurring alterations concentrated in LUSC. [PMID:29625050](../papers/29625050.md)
- 289 disease-free vs 41 never-disease-free LUSC cases in the TCGA-CDR landmark analysis (3 months post-diagnosis): NTE rate 21.8% vs 68.2%, Cox HR=6.68 (95% CI 4.25–10.51, FDR q<0.05). All four endpoints recommended without reservation for LUSC. [PMID:29625049](../papers/29625049.md)

## Sources

- cBioPortal study: `lusc_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
