---
name: Colon Adenocarcinoma
oncotree_code: COAD
main_type: Colorectal Cancer
parent: COADREAD
tags: [colorectal, gi-oncology]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Colon Adenocarcinoma (COAD)

## Overview

Colon Adenocarcinoma is a Colorectal Cancer (parent [COADREAD](../cancer_types/COADREAD.md)).

## Cohorts in the corpus

- [coad_silu_2022](../datasets/coad_silu_2022.md): 348 treatment-naive primary colon cancer patients (AC-ICAM) with matched tumor and healthy colon tissue, profiled by [RNA-seq](../methods/rna-seq.md), WES, deep TCRβ-seq, 16S rRNA-seq, and tumor WGS; median follow-up 4.6 years [PMID:37202560](../papers/37202560.md).
- [coadread_tcga](../datasets/coadread_tcga.md) used as a comparator [PMID:37202560](../papers/37202560.md).
- HCT-116 (HER2−, COAD cell line): negative-control model in ADC radiosensitization study — T-DM1 IC50 >100 nM and no tumor-growth benefit from adding T-DM1 to IR in HCT-116 xenografts, demonstrating receptor-selectivity of the approach. [PMID:27698471](../papers/27698471.md)

## Recurrent alterations

- No single driver gene is proposed as a biomarker; the paper's gene-level claims focus on the 20-gene Immunologic Constant of Rejection (ICR) module [PMID:37202560](../papers/37202560.md).
- [ERBB2](../genes/ERBB2.md) (HER2): HCT-116 is HER2− (T-DM1 IC50 >100 nM), serving as the definitive HER2-negative colon cancer negative control demonstrating receptor-selectivity of ADC radiosensitization. [PMID:27698471](../papers/27698471.md)
- The ICR signature includes [IFNG](../genes/IFNG.md), [TBX21](../genes/TBX21.md), [CD8A](../genes/CD8A.md), [CD8B](../genes/CD8B.md), [IL12B](../genes/IL12B.md), [STAT1](../genes/STAT1.md), [IRF1](../genes/IRF1.md), [CCL5](../genes/CCL5.md), [CXCL9](../genes/CXCL9.md), [CXCL10](../genes/CXCL10.md), [GNLY](../genes/GNLY.md), [PRF1](../genes/PRF1.md), [GZMA](../genes/GZMA.md), [GZMB](../genes/GZMB.md), [GZMH](../genes/GZMH.md), [CD274](../genes/CD274.md), [CTLA4](../genes/CTLA4.md), [FOXP3](../genes/FOXP3.md), [IDO1](../genes/IDO1.md), [PDCD1](../genes/PDCD1.md) [PMID:37202560](../papers/37202560.md).
- NCI-60 CellMiner pharmacogenomics analysis identified [ABCB1](../genes/ABCB1.md) expression and [EGFR](../genes/EGFR.md) pathway activity as determinants of drug sensitivity in colon cancer cell lines [PMID:22802077](../papers/22802077.md)
- 74-tumor WES cohort of colorectal adenocarcinoma (Genentech) identified RSPO2/RSPO3 fusions mutually exclusive with [APC](../genes/APC.md) mutations, implicating Wnt pathway activation as a universal driver [PMID:22895193](../papers/22895193.md)
- In 69 matched MSS colorectal cancer primary/metastasis trios (40% right colon, 44% left colon), [KRAS](../genes/KRAS.md)/[NRAS](../genes/NRAS.md)/[BRAF](../genes/BRAF.md) status was 100% concordant, supporting use of either primary or metastatic biopsy for clinical RAS/RAF testing. [PMID:25164765](../papers/25164765.md)
- Whole-exome and targeted resequencing of 103 MSS [COAD](../cancer_types/COAD.md) from African Americans identified 20 new significantly mutated genes, including [EPHA6](../genes/EPHA6.md) and [FLCN](../genes/FLCN.md) as AA-specific driver candidates, with a ~twofold higher mutation rate per tumor versus 129 Caucasian CRCs (P<0.001). [PMID:25583493](../papers/25583493.md)
- In the MSK-IMPACT pan-cancer cohort, KRAS was mutated in 44% of COAD (90% in PAAD); POLE and MMR mutation signatures predominated in colorectal cancer alongside elevated MSI rates; MSI COAD patients showed responses to immune checkpoint blockade. [PMID:28481359](../papers/28481359.md)
- In MSK-IMPACT sequencing of 1,134 CRCs, colon cancer showed enrichment for KRAS, BRAF, PIK3CA, RNF43, and SMAD4 alterations in right-sided versus left-sided tumors; 37% of left-sided MSS mCRC lacked detectable mitogenic-pathway mutations, suggesting ligand-driven RTK activation [PMID:29316426](../papers/29316426.md)
- In the SUMMIT basket trial (n=12 colorectal), HER2-mutant colon cancer showed no RECIST responses to neratinib, consistent with lineage-based resistance; the study speculates combination HER-targeted therapy may be needed to overcome this resistance [PMID:29420467](../papers/29420467.md)
- MC3 pan-cancer mutation-calling project (10,510 TCGA pairs) included COAD; concordance with PanCan12 MAF exceeded 90%; MSI-high colorectal tumors are prominent hypermutators in the MC3 dataset [PMID:29596782](../papers/29596782.md)
- Pan-cancer fusion study (9,624 TCGA samples) included COAD as one of 33 cancer types in the pan-cancer cohort [PMID:29617662](../papers/29617662.md)
- Pan-cancer aneuploidy study placed COAD in the gastrointestinal arm-level cluster (co-gaining 8q, 13q, chromosome 20 alongside READ, STAD, PAAD); COAD and READ are exceptions to the positive aneuploidy–mutation-rate correlation due to MSI-high and POLE-mutant cases [PMID:29622463](../papers/29622463.md)
- Included in TCGA PanCancer Atlas integrative molecular analysis; COAD/READ tumors form pan-GI iCluster C4 (CIN-enriched) and C18 (MSI-enriched, with STAD) [PMID:29625048](../papers/29625048.md)
- COAD/READ tumors with APC+KRAS drivers share mRNA cluster 15 and RPPA C8 but partition into methylation clusters 10 vs 11; TP53 and KRAS are mutually exclusive in COAD/READ but co-occur in PAAD [PMID:29625049](../papers/29625049.md)
- KRAS hotspot mutations present in 69% of colorectal genomically stable tumors; MSI-H and POLE-mutant subtypes carry highest mutation burden [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); all four endpoints (OS, PFI, DFI, DSS) recommended without reservation for COAD [PMID:29625055](../papers/29625055.md)
- MSI-H detected in 19.7% of colon adenocarcinoma cases by MANTIS WES caller; one of the four classic Lynch syndrome-associated tumor types with highest MSI prevalence in the pan-cancer 39-type analysis [PMID:29850653](../papers/29850653.md)

## Subtypes

- ICR consensus clustering segregates tumors into ICR-high (hot), ICR-medium, and ICR-low (cold) [PMID:37202560](../papers/37202560.md).
- ICR outperforms consensus molecular subtype (CMS) and MSI classifications for prognosis and retains prognostic value within the CMS4/mesenchymal subtype [PMID:37202560](../papers/37202560.md).
- ICR prognostic effect: ICR-high vs ICR-low HR=0.54 (95% CI 0.34–0.86, P=0.0095); ICR-medium vs ICR-low HR=0.63 (0.43–0.91, P=0.014) [PMID:37202560](../papers/37202560.md).
- Quantifying genetic immunoediting further refines ICR's prognostic value [PMID:37202560](../papers/37202560.md).
- A *Ruminococcus bromii*-driven microbiome signature combined with ICR (mICRoScore) identifies patients with excellent survival probability [PMID:37202560](../papers/37202560.md).

## Therapeutic landscape

- Paper does not directly test predictive utility for immunotherapy in colon cancer [PMID:37202560](../papers/37202560.md).
- HCT-116 (HER2−) colon xenografts showed no benefit from T-DM1 + IR vs. IR alone, confirming that receptor expression is required for ADC-mediated radiosensitization. [PMID:27698471](../papers/27698471.md)
- [TRIM24](../genes/TRIM24.md)-BRAF fusions identified in 43% of BRAF-fusion-positive colorectal cases; frequent co-mutations include [RNF43](../genes/RNF43.md) (64%), [TP53](../genes/TP53.md) (57%), [KMT2D](../genes/KMT2D.md) (43%), [MSH3](../genes/MSH3.md) (42%), and [ARID1A](../genes/ARID1A.md) (36%) [PMID:38922339](../papers/38922339.md).

## Sources

- [PMID:37202560](../papers/37202560.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:27698471](../papers/27698471.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22802077](../papers/22802077.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22895193](../papers/22895193.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583493](../papers/25583493.md)

- [PMID:28481359](../papers/28481359.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29316426](../papers/29316426.md)
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29850653](../papers/29850653.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
