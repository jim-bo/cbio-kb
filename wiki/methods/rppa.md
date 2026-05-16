---
name: Reverse-Phase Protein Array (RPPA)
slug: rppa
kind: PROTEIN_LEVEL
canonical_source: corpus
unverified: true
tags: [proteomics, protein-expression, rppa]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Reverse-Phase Protein Array (RPPA)

## Overview

Reverse-phase protein array (RPPA) is a high-throughput antibody-based platform for quantifying protein and phosphoprotein expression levels across many samples simultaneously. Lysates from tumor tissue are arrayed on nitrocellulose slides and probed with validated antibodies; signal intensity is normalized and used to estimate relative protein abundance. RPPA enables pathway-level proteomics in large cohorts.

## Used by

- Applied to 214 [GBM](../cancer_types/GBM.md) samples (171 antibodies) as part of TCGA [GBM](../cancer_types/GBM.md) 2013 multi-platform analysis; 127/171 antibodies correlated with transcriptomic subtype; revealed non-linear genotype-to-signaling relationships (e.g., RTK-amplified samples had lower downstream p-AKT/S6K/MAPK signaling than expected) [PMID:24120142](../papers/24120142.md)
- Reverse-phase protein array (RPPA) applied to TCGA bladder carcinoma samples for protein and phosphoprotein expression profiling; contributed to multi-platform pathway-level characterization identifying therapeutic targets in 69% of tumors [PMID:24476821](../papers/24476821.md)
- Applied as one of five molecular platforms in the TCGA [HCC](../cancer_types/HCC.md) integrated characterisation of 196 patients alongside DNA copy number, methylation, mRNA, and miRNA [PMID:24798001](../papers/24798001.md)
- RPPA profiling of gastric adenocarcinomas ([stad_tcga_pub](../datasets/stad_tcga_pub.md)) revealed elevated [EGFR](../genes/EGFR.md) pY1068 phosphorylation in the CIN subtype and IL-12 signalling in EBV-positive tumors; used alongside six other molecular platforms [PMID:25079317](../papers/25079317.md)
- RPPA on 181 of 230 lung adenocarcinomas ([luad_tcga_pub](../datasets/luad_tcga_pub.md)) identified three mTOR activation patterns (basal; STK11-low/AMPK-low; high p-AKT/PIK3CA mutation), demonstrating that pathway-state biomarkers complement DNA-based stratification [PMID:25079552](../papers/25079552.md)
- Applied in TCGA PTC study to resolve proteomic differences between BVL (BRAFV600E-driven, high MEK/ERK activation) and RL (RAS-driven, elevated p90RSK phosphorylation, [TSC2](../genes/TSC2.md) inhibition, [BCL2](../genes/BCL2.md) over-expression) subtypes [PMID:25417114](../papers/25417114.md)
- Applied in TCGA [HNSC](../cancer_types/HNSC.md) multi-platform profiling (n=279) for protein-level characterization, integrated with genomic subtypes to characterize therapeutic targets across the atypical/mesenchymal/basal/classical expression subtypes [PMID:25631445](../papers/25631445.md)
- Reverse-phase protein array (RPPA, 181 cancer-related proteins/phosphoproteins) on 202 melanoma samples revealed pathway-specific signaling differences: phospho-MEK/ERK elevated in BRAF/RAS subtypes, highest [KIT](../genes/KIT.md) protein in Triple-WT, highest CRAF in [NF1](../genes/NF1.md) subtype. [PMID:26091043](../papers/26091043.md)
- Applied to 633 of 817 breast tumor samples in the TCGA ILC/IDC study; quantified 180+ proteins including phospho-AKT S473/T308, total/phospho-EGFR, pSTAT3 Y705, p70S6K T389; revealed that [ILC](../cancer_types/ILC.md) has the highest average pAKT of any breast subtype, matching HER2+ and Basal-like [IDC](../cancer_types/IDC.md) despite predominantly Luminal A classification [PMID:26451490](../papers/26451490.md)
- Reverse phase protein array profiling performed on 152 of 333 primary prostate adenocarcinomas in the TCGA molecular taxonomy study as part of multi-platform molecular characterization [PMID:26544944](../papers/26544944.md).
- Applied to 473 glioma samples in the TCGA pan-glioma study for protein-level pathway analysis complementing genomic and transcriptomic data [PMID:26824661](../papers/26824661.md)
- Reverse-phase protein array (RPPA) profiled 113 oesophageal/gastric tumors in the TCGA esophageal/stomach study; ESCC2 showed elevated cleaved Caspase-7; RPPA helped distinguish ESCC subtypes [PMID:28052061](../papers/28052061.md).
- RPPA applied to 173 PCPG tumors in the TCGA PCPG study; RPPA cluster 3 (RAS-MAPK signaling) enriched in kinase signaling subtype; MAML3 fusion-positive tumors showed elevated β-catenin, DVL3, and GSK3 by RPPA [PMID:28162975](../papers/28162975.md).
- Applied to 343/412 BLCA tumors with 208 antibodies; five proteomic clusters with distinct outcomes (p=0.019) identified, including HER2-high clusters proposed for trastuzumab and an EGFR-high cluster for EGFR inhibitors [PMID:28988769](../papers/28988769.md)
- Applied to 206 TCGA sarcomas for protein expression profiling; STLMS showed highest PD-L1 expression among sarcoma subtypes (p=4×10⁻⁵ vs ULMS) [PMID:29100075](../papers/29100075.md)
- Reverse-phase protein array data available for 7,858 of 11,286 TCGA PanCancer Atlas samples across 32 tumor types (LAML excluded); used for single-platform RPPA clustering into 10 protein groups [PMID:29625048](../papers/29625048.md).
- Used for proteomics profiling of TCGA PanCancer Atlas tumors; RPPA data contributed to characterization of immune subtype associations with driver mutations across the 11,000-tumor cohort [PMID:29625049](../papers/29625049.md).

## Notes

- Coverage is limited to antibodies in the validated panel; cannot detect novel proteins or isoforms without prior selection.
- Non-linear genotype-to-protein relationships observed in [GBM](../cancer_types/GBM.md) (e.g., PI3K-mutant samples with lower p-AKT than PI3K-WT) highlight the complexity of translating genomic to proteomic signals.
- Widely used in TCGA pan-cancer studies for pathway activation profiling.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24798001](../papers/24798001.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079317](../papers/25079317.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079552](../papers/25079552.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25417114](../papers/25417114.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25631445](../papers/25631445.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26544944](../papers/26544944.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28162975](../papers/28162975.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29100075](../papers/29100075.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
