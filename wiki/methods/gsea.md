---
name: GSEA
slug: gsea
kind: method
canonical_source: corpus
unverified: true
tags: [pathway-analysis, gene-sets, transcriptomics, enrichment]
processed_by: crosslinker
processed_at: 2026-05-21
---

# GSEA

## Overview

Gene Set Enrichment Analysis (GSEA) is a computational method for determining whether a predefined gene set (e.g., a biological pathway, GO term, or curated gene signature) shows statistically significant, concordant differences between two biological states. It uses a ranked gene list (by differential expression, correlation, or other metric) and calculates an enrichment score for each gene set, testing for nonrandom distribution of the set's genes within the ranked list. GSEA is widely used for pathway-level interpretation of transcriptomic data and for cross-dataset comparison of gene expression programs.

## Used by

- GSEA of 486 fulvestrant-responsive differentially expressed genes in Nf1Indel rat mammary tumors showed significant enrichment of genes induced by neoadjuvant [letrozole](../drugs/letrozole.md) (GSE5462) and [fulvestrant](../drugs/fulvestrant.md) (GSE71791) in patient datasets; 58-gene overlap included [PGR](../genes/PGR.md), AREG, SGK3, and other ER-response genes, validating cross-species transcriptome concordance. [PMID:26437033](../papers/26437033.md)
- Used to compare gene expression between long-fusion (breakpoint after exon 11) and short-fusion (exons 8/9) MYBL1/MYB [ACC](../cancer_types/ACC.md) subsets; identified 19 gene sets enriched in long fusions (RNA processing/translation) and 5 in short fusions (tissue development) [PMID:26631609](../papers/26631609.md).
- Used (alongside GSVA) with MSigDB C2/C6/C7 gene sets to identify the IPRES co-enriched transcriptional resistance program in anti-PD-1-treated metastatic melanoma [PMID:26997480](../papers/26997480.md)
- Used to evaluate enrichment of a YAP/TAZ transcriptional signature in NF2-loss vs NF2-WT uRCC, confirming Hippo pathway dysregulation in the NF2-loss subset. [PMID:27713405](../papers/27713405.md)
- Applied over REACTOME pathways to identify clonal enrichment in post-chemotherapy urothelial carcinoma tumours; highlighted [L1CAM](../genes/L1CAM.md) (OR=1.9, FDR=0.12) and integrin signaling (OR=2.8, FDR=0.02) as candidate resistance pathways. [PMID:27749842](../papers/27749842.md)
- Applied to CCA methylation data showing both Cluster 1 and Cluster 4 hypermethylation target PRC2 pathway gene sets (at CpG islands vs CpG shores respectively), and to transcriptome data for immune-pathway characterization across the four clusters [PMID:28667006](../papers/28667006.md)
- Applied to TCGA [PRAD](../cancer_types/PRAD.md) ranked by [NOL10](../genes/NOL10.md) expression; E2F targets and G2M checkpoint ranked as top hallmarks. Also applied to RNA-seq of NOL10-knockdown LNCaP, identifying 71 downregulated genes enriched in cell-cycle processes [PMID:28927585](../papers/28927585.md)
- GSEA used with IPA for pathway analysis of DEGs between on-therapy responders and non-responders in 45 melanoma RNA-seq samples; enriched pathways included PD-1 signaling, IFN-γ, IL-2, and TCR signaling [PMID:29033130](../papers/29033130.md)
- GSEA of PBAF-complex-perturbed A704 [CCRCC](../cancer_types/CCRCC.md) cells and PBRM1-LOF tumors revealed enrichment of IL6/JAK-STAT3, TNF-α/NF-κB, hypoxia, and cytokine-cytokine receptor gene sets (top hit FWER q=0.002) [PMID:29301960](../papers/29301960.md)
- GSEA against MSigDB Hallmark gene sets used to correlate arm-level aneuploidy with expression programs; revealed positive enrichment for E2F targets, G2M checkpoint, and mitotic spindle hallmarks, and negative enrichment for immune signatures after controlling for leukocyte fraction [PMID:29622463](../papers/29622463.md)
- Applied via ssGSEA with a 160-signature panel and mclust/BIC selection to define six pan-cancer immune subtypes (C1 Wound Healing through C6 TGF-β Dominant) across ~11,000 TCGA PanCancer Atlas tumors [PMID:29625049](../papers/29625049.md).
- Applied to validate genetic subtype transcriptional correlates; used to confirm [EZH2](../genes/EZH2.md) target upregulation in C3 GCB-DLBCL chromatin-modifier-mutant tumors [PMID:29713003](../papers/29713003.md)
- ssGSEA tested 9,292 MSigDB gene sets on [GBM](../cancer_types/GBM.md) longitudinal transcriptomes; regulatory T-cell ([FOXP3](../genes/FOXP3.md)) signatures enriched in non-responders pre-treatment (p=0.037); immunosuppressive signatures (FOXP3, [STAT3](../genes/STAT3.md)) elevated in responders post-treatment [PMID:30742119](../papers/30742119.md)
- Used for transcriptomic pathway enrichment analysis across four PLC clusters (n=367): EMT identified as top enriched pathway in P1 (combined-type/ICC-like cHCC-ICC); xenobiotic and bile acid metabolism enriched in P2 (mixed-type/HCC-like) [PMID:31130341](../papers/31130341.md)
- Applied in the [UTUC](../cancer_types/UTUC.md) molecular subtyping analysis for pathway comparison between the T-cell-depleted and T-cell-inflamed clusters and between UTUC and TCGA UCB; IFNG-response gene programs were down in the T-cell-depleted cluster [PMID:31278255](../papers/31278255.md)
- Applied on Hallmark and TissGDB/TiGER gene sets across 244 RNA-seq PPTC PDX models to characterize pathway enrichment by histology subtype; identified enrichment of hedgehog, TNFα, and p53 signaling in rhabdoid models [PMID:31693904](../papers/31693904.md).
- Applied in the Sherlock-Lung NS-LUAD transcriptomic subtyping study (n=684 tumors) to characterize pathway enrichment across steady, proliferative, and chaotic subtypes [PMID:32015526](../papers/32015526.md).
- Used (as fgsea) in the CCLE proteomics study (n=375 cell lines, 22 lineages) to identify pathway enrichment along proteome PC1; >200 MSigDB pathways enriched along proteome PC1 vs. far fewer along matched RNA-seq PC1, demonstrating that protein-level pathway co-expression dominates the CCLE proteome axis [PMID:31978347](../papers/31978347.md).
- GSEA pathway analysis identified cell-cycle/DNA-replication pathways (SMC1, MCM5, MCM7) enriched in PDX-engrafting UTUC tumors and ECM/focal-adhesion pathways in non-engrafters [PMID:32332851](../papers/32332851.md)
- Used in [prad_organoids_msk_2022](../datasets/prad_organoids_msk_2022.md) to characterize the four CRPC chromatin subtypes; CRPC-SCL was enriched for mammary stem cell signature, cancer stem cell markers, FGFR signaling, TGF-β/EMT/TNF-α/IFN response pathways [PMID:35617398](../papers/35617398.md)

## Notes

- Standard GSEA uses a Kolmogorov-Smirnov-like statistic with permutation-based FDR correction (Subramanian et al. 2005).
- MSigDB (Molecular Signatures Database) is the primary curated gene set library used with GSEA.
- Pre-ranked GSEA (fgsea/GSEA Preranked) is commonly used when the ranked list is derived from an external statistic (e.g., DESeq2 Wald statistic).

## Sources

- [PMID:26437033](../papers/26437033.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26631609](../papers/26631609.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26997480](../papers/26997480.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27713405](../papers/27713405.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27749842](../papers/27749842.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28667006](../papers/28667006.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28927585](../papers/28927585.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29301960](../papers/29301960.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29713003](../papers/29713003.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30742119](../papers/30742119.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31693904](../papers/31693904.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32015526](../papers/32015526.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31978347](../papers/31978347.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32332851](../papers/32332851.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35617398](../papers/35617398.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
