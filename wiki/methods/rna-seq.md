---
name: RNA sequencing
slug: rna-seq
kind: method
canonical_source: 
unverified: true
tags: [transcriptomics, sequencing]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# RNA sequencing

## Overview

Bulk RNA sequencing of tumor (and where available matched normal) tissue for gene expression quantification, fusion detection, and downstream signature/classifier analysis.

## Used by

- [PMID:35927489](../papers/35927489.md) — RNA-seq on n=712 CLL samples (603 treatment-naive used for clustering); unsupervised clustering identified 8 robust expression clusters that are independent prognostic factors beyond IGHV/epitype [PMID:35927489](../papers/35927489.md).
- [PMID:36862133](../papers/36862133.md) — select targeted RNA sequencing alongside MSK-IMPACT in the Make-an-IMPACT program; detected actionable fusions including a PRDX1-NTRK1 fusion in histiocytosis only via targeted RNA-seq, plus MS4A6A-BRAF, DOCK8-BRAF, HLA-A-BRAF, and TFG-ALK [PMID:36862133](../papers/36862133.md).
- [PMID:37202560](../papers/37202560.md) — bulk RNA-seq on 348 AC-ICAM colon cancer tumor/normal pairs; underpins the ICR signature, ConsensusTME deconvolution, and CMS classification used for prognostic analysis [PMID:37202560](../papers/37202560.md).
- [PMID:27634761](../papers/27634761.md) — RNA-seq (platform-independent, multiple normalization schemes including RSEM, FPKM, RPKM, TPM) used as the sole molecular feature (~500 features for site of origin, ~200 for lineage) in the ATLAS tumor classification model; trained on 8,249 TCGA/CCLE samples and validated on 10,376 samples [PMID:27634761](../papers/27634761.md).
- [PMID:34433969](../papers/34433969.md) — mRNA-seq on 121 fresh-frozen meningiomas from the University Health Network Brain Tumor BioBank; integrated with WES, EPIC methylation array, and snRNA-seq to define four stable molecular groups [PMID:34433969](../papers/34433969.md).
- [PMID:38117484](../papers/38117484.md) — RNA-seq on 54 glioma patients in the GLASS International consortium; paired with 450K/EPIC methylation arrays and WES/WGS; identified [HOXD13](../genes/HOXD13.md) as master regulator of IDH-mutant astrocytoma progression [PMID:38117484](../papers/38117484.md).
- [PMID:38412093](../papers/38412093.md) — RNA-seq on 24 primary anaplastic thyroid carcinomas and 13 cell lines, integrated with TCGA PTC data [PMID:38412093](../papers/38412093.md).
- [PMID:38488813](../papers/38488813.md) — RNA-seq on 44 prostate cancer PDX models; paired with WGS (30X) and targeted sequencing for integrative multi-platform analysis; confirmed ETS fusion-driven expression changes [PMID:38488813](../papers/38488813.md).
- [PMID:38895302](../papers/38895302.md) — RNA-seq paired with WES using G&T-seq protocol on single-cell clones from normal skin melanocytes; supported mutation calling via RNA evidence and phasing [PMID:38895302](../papers/38895302.md).
- [PMID:30325352](../papers/30325352.md) — Illumina HiSeq 2500 RNA-seq (TruSeq Total Stranded RNA + Ribo-Zero) on 130 of 211 NSCLC subjects; reads aligned to hg19 with STAR v2.3, quantified with Cufflinks v2.0.2 in FPKM; RIN <2.5 excluded; part of the [nsclc-radiogenomics-stanford](../datasets/nsclc-radiogenomics-stanford.md) public radiogenomic resource [PMID:30325352](../papers/30325352.md).

## Notes

- In the CLL-map study, RNA-seq is one arm of an integrated WES/WGS + RNA-seq + methylation analysis used to derive an integrated outcome model [PMID:35927489](../papers/35927489.md).
- In the AC-ICAM atlas, RNA-seq drives both immune signature scoring and downstream microbiome integration [PMID:37202560](../papers/37202560.md).
- In the NSCLC radiogenomics dataset, RNA-seq (n=130) complements CT/PET-CT imaging and SNaPshot mutational testing for EGFR/KRAS/ALK, with 17 subjects having both RNA-seq and microarray expression data [PMID:30325352](../papers/30325352.md).

## Sources

- [PMID:35927489](../papers/35927489.md)
- [PMID:36862133](../papers/36862133.md)
- [PMID:37202560](../papers/37202560.md)
- [PMID:27634761](../papers/27634761.md)
- [PMID:34433969](../papers/34433969.md)
- [PMID:38117484](../papers/38117484.md)
- [PMID:38412093](../papers/38412093.md)
- [PMID:38488813](../papers/38488813.md)
- [PMID:38895302](../papers/38895302.md)
- [PMID:30325352](../papers/30325352.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
