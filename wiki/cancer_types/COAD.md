---
name: Colon Adenocarcinoma
oncotree_code: COAD
main_type: Colorectal Cancer
parent: COADREAD
tags: [colorectal, gi-oncology]
processed_by: crosslinker
processed_at: 2026-05-03
---

# Colon Adenocarcinoma (COAD)

## Overview

Colon Adenocarcinoma is a Colorectal Cancer (parent [COADREAD](../cancer_types/COADREAD.md)).

## Cohorts in the corpus

- [coad_silu_2022](../datasets/coad_silu_2022.md): 348 treatment-naive primary colon cancer patients (AC-ICAM) with matched tumor and healthy colon tissue, profiled by [RNA-seq](../methods/rna-seq.md), WES, deep TCRβ-seq, 16S rRNA-seq, and tumor WGS; median follow-up 4.6 years [PMID:37202560](../papers/37202560.md).
- [bowel_colitis_msk_2022](../datasets/bowel_colitis_msk_2022.md): 174 patients with colitis-associated colon cancer (CAC); 161 in the genomic cohort with 166 tumors sequenced by MSK-IMPACT ([IMPACT468](../methods/IMPACT468.md)); 56% ulcerative colitis, 44% Crohn's disease; 84.9% with ≥10 years of IBD at CAC diagnosis. [PMID:36611031](../papers/36611031.md)
- [coadread_tcga](../datasets/coadread_tcga.md) used as a comparator [PMID:37202560](../papers/37202560.md).
- HCT-116 (HER2−, COAD cell line): negative-control model in ADC radiosensitization study — T-DM1 IC50 >100 nM and no tumor-growth benefit from adding T-DM1 to IR in HCT-116 xenografts, demonstrating receptor-selectivity of the approach. [PMID:27698471](../papers/27698471.md)

## Recurrent alterations

- No single driver gene is proposed as a biomarker; the paper's gene-level claims focus on the 20-gene Immunologic Constant of Rejection (ICR) module [PMID:37202560](../papers/37202560.md).
- [ERBB2](../genes/ERBB2.md) (HER2): HCT-116 is HER2− (T-DM1 IC50 >100 nM), serving as the definitive HER2-negative colon cancer negative control demonstrating receptor-selectivity of ADC radiosensitization. [PMID:27698471](../papers/27698471.md)
- Colitis-associated cancer (CAC) is genetically distinct from sporadic CRC: [TP53](../genes/TP53.md) altered in 90% (vs. ~50% in sporadic CRC at early stages), [KRAS](../genes/KRAS.md) 31%, [MYC](../genes/MYC.md) 20% (focal amplifications more frequent), [APC](../genes/APC.md) only 20% (vs. dominant in sporadic CRC), [SMAD4](../genes/SMAD4.md) 13%. [PMID:36611031](../papers/36611031.md)
- Wnt pathway alterations infrequent in CAC ([APC](../genes/APC.md) 20%); RNA-seq shows lower Wnt ssGSEA score vs. sporadic CRC; APC-mutant and Wnt-WT CAC organoids grew without exogenous Wnt supplementation, indicating transcriptional rewiring. [PMID:36611031](../papers/36611031.md)
- [PIK3CA](../genes/PIK3CA.md) and [IDH1](../genes/IDH1.md) alterations significantly enriched in Crohn's disease vs. ulcerative colitis CAC; [IDH1](../genes/IDH1.md) R132 mutants confirmed 2-HG production and showed sensitivity to IDH1 and FGFR inhibitors in PDX. [PMID:36611031](../papers/36611031.md)
- Germline pathogenic variants identified in 10/73 (14%) CAC patients: [APC](../genes/APC.md) I1307K (3 cases), [PMS2](../genes/PMS2.md), [ATM](../genes/ATM.md), [RAD51B](../genes/RAD51B.md), [DICER1](../genes/DICER1.md), [FANCA](../genes/FANCA.md), [FANCC](../genes/FANCC.md). [PMID:36611031](../papers/36611031.md)
- Multiple primary CAC lesions in the same patient arise as genetically independent events (no shared driver alterations in 6 multifocal patients); convergent [TP53](../genes/TP53.md) evolution observed across independent lesions. [PMID:36611031](../papers/36611031.md)
- The ICR signature includes [IFNG](../genes/IFNG.md), [TBX21](../genes/TBX21.md), [CD8A](../genes/CD8A.md), [CD8B](../genes/CD8B.md), [IL12B](../genes/IL12B.md), [STAT1](../genes/STAT1.md), [IRF1](../genes/IRF1.md), [CCL5](../genes/CCL5.md), [CXCL9](../genes/CXCL9.md), [CXCL10](../genes/CXCL10.md), [GNLY](../genes/GNLY.md), [PRF1](../genes/PRF1.md), [GZMA](../genes/GZMA.md), [GZMB](../genes/GZMB.md), [GZMH](../genes/GZMH.md), [CD274](../genes/CD274.md), [CTLA4](../genes/CTLA4.md), [FOXP3](../genes/FOXP3.md), [IDO1](../genes/IDO1.md), [PDCD1](../genes/PDCD1.md) [PMID:37202560](../papers/37202560.md).

## Subtypes

- ICR consensus clustering segregates tumors into ICR-high (hot), ICR-medium, and ICR-low (cold) [PMID:37202560](../papers/37202560.md).
- CAC genomic subsets: clonal [TP53](../genes/TP53.md) (74%), subclonal TP53 (14%), TP53 wild-type (12%); the subclonal TP53 group is significantly enriched for Wnt pathway alterations (P=0.017). [PMID:36611031](../papers/36611031.md)
- Tumor site distribution in CAC cohort: small intestine 10.3%, right colon 27.1%, left colon 29.5%, rectum 31.3%. Bone and pelvic metastases significantly enriched vs. sporadic CRC. [PMID:36611031](../papers/36611031.md)
- ICR outperforms consensus molecular subtype (CMS) and MSI classifications for prognosis and retains prognostic value within the CMS4/mesenchymal subtype [PMID:37202560](../papers/37202560.md).
- ICR prognostic effect: ICR-high vs ICR-low HR=0.54 (95% CI 0.34–0.86, P=0.0095); ICR-medium vs ICR-low HR=0.63 (0.43–0.91, P=0.014) [PMID:37202560](../papers/37202560.md).
- Quantifying genetic immunoediting further refines ICR's prognostic value [PMID:37202560](../papers/37202560.md).
- A *Ruminococcus bromii*-driven microbiome signature combined with ICR (mICRoScore) identifies patients with excellent survival probability [PMID:37202560](../papers/37202560.md).

## Therapeutic landscape

- Paper does not directly test predictive utility for immunotherapy in colon cancer [PMID:37202560](../papers/37202560.md).
- HCT-116 (HER2−) colon xenografts showed no benefit from T-DM1 + IR vs. IR alone, confirming that receptor expression is required for ADC-mediated radiosensitization. [PMID:27698471](../papers/27698471.md)
- CAC is genomically distinct from sporadic CRC: functional IDH1 inhibition and FGFR inhibition suppressed CAC PDX growth; porcupine inhibitor LGK-974 and tankyrase inhibitor G007-LK did not suppress Wnt-independent CAC PDX growth, arguing against Wnt-targeted therapy in CAC. [PMID:36611031](../papers/36611031.md)
- Routine surveillance does not eliminate CAC risk: 17% of patients had a colonoscopy within one year of diagnosis; 15% had quiescent IBD off treatment. Germline testing is clinically informative (14% pathogenic variants). [PMID:36611031](../papers/36611031.md)
- [TRIM24](../genes/TRIM24.md)-BRAF fusions identified in 43% of BRAF-fusion-positive colorectal cases; frequent co-mutations include [RNF43](../genes/RNF43.md) (64%), [TP53](../genes/TP53.md) (57%), [KMT2D](../genes/KMT2D.md) (43%), [MSH3](../genes/MSH3.md) (42%), and [ARID1A](../genes/ARID1A.md) (36%) [PMID:38922339](../papers/38922339.md).

## Sources

- [PMID:37202560](../papers/37202560.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:27698471](../papers/27698471.md)
- [PMID:36611031](../papers/36611031.md) — Chatila et al., largest CAC genomic series (n=174); MSK, 2023.

*This page was processed by **crosslinker** on **2026-05-03**.*
