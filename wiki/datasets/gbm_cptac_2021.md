---
name: CPTAC Glioblastoma Proteogenomics 2021
studyId: gbm_cptac_2021
institution: Clinical Proteomic Tumor Analysis Consortium (CPTAC)
size: 99
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - WGS
  - WES
  - RNA-seq
  - TMT-proteomics
  - phosphoproteomics
  - methylation-array
  - metabolomics
  - lipidomics
panels: []
tags:
  - glioblastoma
  - proteogenomics
  - multi-omics
  - CPTAC
  - IDH-wildtype
processed_by: crosslinker
processed_at: 2026-05-16
---

# CPTAC Glioblastoma Proteogenomics 2021

## Overview

Prospective multi-omics characterization of 99 treatment-naive adult [glioblastoma](../cancer_types/GBM.md) ([GBM](../cancer_types/GBM.md)) tumors collected through the Clinical Proteomic Tumor Analysis Consortium (CPTAC) from 10 tissue source sites in 6 countries. Tumors were profiled across ten platforms spanning genomics, transcriptomics, epigenomics, proteomics, phosphoproteomics, acetylomics, metabolomics, and lipidomics. Raw data are available at CPTAC Data Portal (studies S048, S057), GDC project CPTAC-3, and the Proteomic Data Commons; the genomics component is deposited on cBioPortal as `gbm_cptac_2021`.

## Composition

- **Cancer type:** [Glioblastoma (GBM)](../cancer_types/GBM.md)
- **N = 99** treatment-naive adult GBM tumors; males n=55, females n=44; age range 24–88
- **IDH-mutant subset:** 6 [IDH1](../genes/IDH1.md) R132H-mutant tumors + 1 non-hotspot R222C mutation; median onset 47 vs. 59 years (IDH-WT)
- **Reference normals:** 10 unmatched GTEx frontal cortex samples
- **snRNA-seq validation:** 18 tumors (7 im1, 5 im2, 1 im3, 5 im4)
- **Lipidome:** 582 lipids quantified across 75 tumors
- **Independent validation cohort:** 39 high-grade brain tumors from Children's Brain Tumor Tissue Consortium (CBTTC)
- **Key clinical fields:** overall survival, NMF subtype (nmf1/2/3/mixed), immune subtype (im1–im4), [MGMT](../genes/MGMT.md) methylation status

## Assays / panels (linked)

- [WGS](../methods/whole-genome-seq.md) — PCR-free on HiSeq X, minimum 15× tumor coverage
- [WES](../methods/whole-exome-seq.md) — HiSeq 4000, minimum 150× on-target
- [RNA-seq](../methods/rna-seq.md) — total RNA, HiSeq 4000, ≥120M reads/sample, hg38
- [miRNA-seq](../methods/mirna-seq.md) — ≥10M reads
- [snRNA-seq](../methods/snrna-seq.md) — 10X Chromium on 18 tumors
- [Illumina Infinium MethylationEPIC](../methods/epic-methylation-array.md) — >850k CpGs
- [TMT-11-plex LC-MS/MS](../methods/tmt-proteomics.md) — global proteome, Orbitrap Fusion Lumos
- [IMAC-enriched phosphoproteome](../methods/tmt-phosphoproteomics.md)
- Label-free GC-MS metabolome and LC-MS lipidome
- [LINCS L1000](../methods/lincs-l1000.md) — drug-connectivity analysis

## Papers using this cohort

- [PMID:33577785](../papers/33577785.md) — CPTAC GBM multi-omics proteogenomic characterization

## Notable findings derived from this cohort

- Multi-omics NMF clustering reproduced TCGA expression subtypes (proneural nmf1, mesenchymal nmf2, classical nmf3) but reclassified 29% of tumors; 12 "mixed-subtype" tumors had significantly worse overall survival (log-rank p=1.7e-4). [PMID:33577785](../papers/33577785.md)
- [EGFR](../genes/EGFR.md) structural variants in 45/99 tumors (all amplified); [TERT](../genes/TERT.md) promoter mutations (C228T/C250T) in 74% of primary GBMs; [MGMT](../genes/MGMT.md) promoter hypermethylation in 38/90 tumors (42%) with concordant RNA (p=4.9e-11) and protein (p=2.6e-6) downregulation. [PMID:33577785](../papers/33577785.md)
- [PTPN11](../genes/PTPN11.md) Y62 and [PLCG1](../genes/PLCG1.md) Y783 phosphosites identified as convergent RTK signaling hubs downstream of both [EGFR](../genes/EGFR.md) and [PDGFRA](../genes/PDGFRA.md). [PMID:33577785](../papers/33577785.md)
- Four immune subtypes (im1–im4) defined by xCell deconvolution and validated by snRNA-seq; im4 was uniformly immunologically cold (1.3% T cells, 6% TAM). [PMID:33577785](../papers/33577785.md)
- Drug-connectivity analysis via [LINCS L1000](../methods/lincs-l1000.md) nominated broader kinase inhibitors (beyond [EGFR](../genes/EGFR.md) inhibitors) for EGFR-altered tumors and MAPK inhibitors for [NF1](../genes/NF1.md)-altered tumors. [PMID:33577785](../papers/33577785.md)
- Lipidomics: mesenchymal-like GBM enriched for triacylglycerols and depleted in phosphatidylcholines; proneural-like enriched for VLCFAs and long-chain PUFA glycerophospholipids; ferroptosis markers [ACSL4](../genes/ACSL4.md) and [ALOX5](../genes/ALOX5.md) upregulated only in mesenchymal-like tumors. [PMID:33577785](../papers/33577785.md)

## Sources

- CPTAC Data Portal: studies S048, S057
- GDC project: CPTAC-3
- Proteomic Data Commons
- cBioPortal study: `gbm_cptac_2021`
- [PMID:33577785](../papers/33577785.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
