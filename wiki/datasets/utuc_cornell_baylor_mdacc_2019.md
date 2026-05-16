---
name: Cornell / Baylor / MD Anderson UTUC WES+RNA-seq Cohort (2019)
studyId: utuc_cornell_baylor_mdacc_2019
institution: Weill Cornell Medicine / Baylor College of Medicine / MD Anderson Cancer Center
size: 37
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
panels: []
tags:
  - UTUC
  - upper-tract-urothelial-carcinoma
  - FGFR3
  - luminal-papillary
  - multi-institutional
processed_by: crosslinker
processed_at: 2026-05-16
---

# Cornell / Baylor / MD Anderson UTUC WES+RNA-seq Cohort (2019)

## Overview

Robinson, Vlachostergios et al. (*European Urology* 2019, [PMID:31278255](../papers/31278255.md)) performed integrated whole-exome and RNA sequencing of 37 high-grade upper tract urothelial carcinoma ([UTUC](../cancer_types/UTUC.md)) tumors from Weill Cornell Medicine (WCM, n=22) and Baylor College of Medicine / MD Anderson Cancer Center (BCM-MDA, n=15). The study compared UTUC against the TCGA muscle-invasive bladder cancer cohort ([blca_tcga_pub_2017](../datasets/blca_tcga_pub_2017.md)) to characterize the genomic, transcriptomic, and immune landscape of sporadic high-grade UTUC. The dataset is deposited as `utuc_cornell_baylor_mdacc_2019` on cBioPortal.

## Composition

- **37 high-grade UTUC tumor–normal pairs** by WES (WCM n=22, BCM-MDA n=15); conventional urothelial histology; 64.8% former/current smokers.
- RNA-seq meta-dataset: 32 UTUC tumors (WCM n=17, BCM-MDA n=15).
- Cancer type: high-grade [upper tract urothelial carcinoma (UTUC)](../cancer_types/UTUC.md).
- Functional validation: shRNA knockdown and pharmacologic [FGFR3](../genes/FGFR3.md) inhibition ([erdafitinib](../drugs/erdafitinib.md)) in RT-112, RT-4, and SW780 UCB cell lines (all FGFR3-fusion-positive).
- IHC validation: MMR proteins ([MLH1](../genes/MLH1.md), [PMS2](../genes/PMS2.md), [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md)) on 16 WCM UTUC vs. 14 stage-matched WCM UCB specimens.
- Comparator: [blca_tcga_pub_2017](../datasets/blca_tcga_pub_2017.md) (n=124 WES / n=128 RNA-seq).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 37 UTUC tumor-normal pairs (Illumina HiSeq 2500, ~85x for BCM-MDA)
- [rna-seq](../methods/rna-seq.md) — 32 UTUC tumors (aligned with [STAR](../methods/star-aligner.md))
- [mutect](../methods/mutect.md) / [strelka](../methods/strelka.md) / [varscan](../methods/varscan.md) — consensus SNV calling
- [oncotator](../methods/oncotator.md) — variant annotation
- [msisensor](../methods/msisensor.md) — microsatellite instability scoring
- [bayesian-nmf](../methods/bayesian-nmf.md) — mutational signature discovery
- [gsea](../methods/gsea.md) — gene set enrichment analysis
- [immunohistochemistry](../methods/immunohistochemistry.md) — MMR protein H-scores (Leica Bond III / HALO)

## Papers using this cohort

- [PMID:31278255](../papers/31278255.md) — Robinson, Vlachostergios et al. 2019, *European Urology*: defining publication for this dataset.

## Notable findings derived from this cohort

- FGFR3 activating mutations in 11/37 (29.7%) UTUC tumors — significantly higher than 13.7% in TCGA UCB (P=0.04); FGFR3 was outlier-overexpressed in 14/32 (43.7%) of UTUC tumors by RNA-seq outlier analysis [PMID:31278255](../papers/31278255.md).
- 27/32 (84.3%) of UTUC tumors classified as luminal by UNC BASE47 classifier vs. 46.1% of TCGA UCB; 20/32 (62.5%) luminal-papillary by TCGA classifier — significantly enriched compared to UCB [PMID:31278255](../papers/31278255.md).
- 28/32 (87.5%) UTUC tumors were T-cell depleted by 170-immune-gene classifier; FGFR3 mRNA was significantly higher in the T-cell-depleted cluster (Wilcoxon P=1.3×10⁻⁶); FGFR3 inhibition by shRNA or [erdafitinib](../drugs/erdafitinib.md) upregulated IFNG-response genes ([BST2](../genes/BST2.md), [MX2](../genes/MX2.md), [IRF9](../genes/IRF9.md), [GBP2](../genes/GBP2.md)), linking FGFR3 to T-cell exclusion [PMID:31278255](../papers/31278255.md).
- Mean TMB was 2.91 mutations/Mb in UTUC vs. 5.46 mutations/Mb in TCGA UCB (Mann-Whitney P=1.9×10⁻⁵); sporadic UTUC was not microsatellite-unstable despite significantly reduced MMR transcript and protein expression (MLH1, MSH2, MSH6, PMS2) [PMID:31278255](../papers/31278255.md).
- Dominant mutational signatures: APOBEC (COSMIC 2, 13), defective MMR (COSMIC 6), and ERCC2-like (COSMIC 5); no germline MMR mutations identified in WES of either cohort [PMID:31278255](../papers/31278255.md).

## Sources

- cBioPortal study: `utuc_cornell_baylor_mdacc_2019`
- Robinson, Vlachostergios et al. *European Urology* 2019. [PMID:31278255](../papers/31278255.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
