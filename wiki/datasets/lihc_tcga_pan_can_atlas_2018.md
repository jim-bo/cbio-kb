---
name: Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: lihc_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 373
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - lihc
  - liver
  - hepatocellular
  - HCC
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Liver Hepatocellular Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Liver Hepatocellular Carcinoma PanCancer Atlas 2018 cohort is the [LIHC](../cancer_types/LIHC.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `lihc_tcga_pan_can_atlas_2018`. It covers approximately 373 hepatocellular carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. C26:[LIHC](../cancer_types/LIHC.md) was one of eight pan-cancer iClusters dominated by a single tumor type, and more than 80% of LIHC samples grouped into this single iCluster.

## Composition

- Cancer type: Liver Hepatocellular Carcinoma ([LIHC](../cancer_types/LIHC.md)), OncoTree code [HCC](../cancer_types/HCC.md).
- Approximately 373 tumor samples.
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

- C26:LIHC was one of eight pan-cancer iClusters dominated by a single tumor type; >80% of LIHC samples grouped together in this single iCluster, reflecting the molecular homogeneity of hepatocellular carcinoma relative to other GI cancers. [PMID:29625048](../papers/29625048.md)
- [ESR1](../genes/ESR1.md) (ER-α), [AR](../genes/AR.md), and [IGFBP2](../genes/IGFBP2.md) high-expression RPPA groups contain luminal [BRCA](../cancer_types/BRCA.md), [UCEC](../cancer_types/UCEC.md), [OV](../cancer_types/OV.md), and some LIHC samples, indicating estrogen/androgen pathway activity shared across these cancer types. [PMID:29625048](../papers/29625048.md)
- [CTNNB1](../genes/CTNNB1.md) is mutually exclusive with [TP53](../genes/TP53.md) and is a major WNT-pathway driver in LIHC; somatic co-occurrence/exclusivity networks tested across 33 cancer types including LIHC. [PMID:29625049](../papers/29625049.md)
- Provided TCGA-HCC reference arm (TCGA-LIHC) for the pan-Asia cHCC-ICC multi-omic study; TP53 mutation rate in TCGA-HCC (31%) was significantly lower than in cHCC-ICC (49.2%, p<0.001), and TERT promoter mutation rate was higher in TCGA-HCC (46%, p<0.001); also contributed to the 367-sample pan-liver-cancer transcriptomic clustering [PMID:31130341](../papers/31130341.md)

## Sources

- cBioPortal study: `lihc_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
