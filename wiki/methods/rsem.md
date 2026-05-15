---
name: RSEM (RNA-Seq by Expectation-Maximization)
slug: rsem
kind: method
canonical_source: corpus
unverified: true
tags: [rna-seq, quantification, expression, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# RSEM (RNA-Seq by Expectation-Maximization)

## Overview

RSEM uses an expectation-maximization algorithm to estimate transcript- and gene-level expression from RNA-seq data, explicitly modeling multi-mapping reads by distributing read counts probabilistically across isoforms. It outputs expected counts, TPM (transcripts per million), and FPKM/RPKM values. RSEM is typically used after STAR or HISAT2 alignment and is the standard quantification tool in TCGA and many cancer genomics pipelines.

## Used by

- Used to quantify transcript-level gene expression from STAR-aligned RNA-seq reads (hg38) for 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)) in the BC Cancer POG WGTA pipeline; expression values fed into edgeR differential expression, consensus hierarchical clustering, t-SNE visualization, and VIPER master-regulator analyses [PMID:40328872](../papers/40328872.md).
- Used for RNA-seq quantification in bulk transcriptomics of 35 AAV-CRISPR-edited rat mammary tumors, enabling ANOVA-based identification of 1,579 differentially expressed genes and GSEA-based comparison with human endocrine therapy response datasets [PMID:26437033](../papers/26437033.md)
- RSEM used for transcript-level quantification of RNA-seq data from 17 ACC tumors; confirmed NFIB overexpression vs normal tissue (p=0.002) independent of fusion status, and MYB overexpression in fusion-positive tumors [PMID:26862087](../papers/26862087.md)
- MapSplice/RSEM pipeline used for mRNA quantification in the TCGA esophageal/stomach study of 164 oesophageal carcinomas and 359 gastric adenocarcinomas [PMID:28052061](../papers/28052061.md).
- Used to quantify transcript-level expression from RNA-seq data in AALE chr_3p-deleted cell experiments and in the TCGA pan-cancer expression dataset (Broad GDAC Firehose 2016_01_28 release) [PMID:29622463](../papers/29622463.md)

## Notes

- RSEM estimates are probabilistic; multi-mapping reads across highly similar isoforms are distributed by expectation, not assigned deterministically.
- RSEM expected counts (not raw counts) are suitable input for edgeR/DESeq2 when passed as rounded integers; TPM is preferred for cross-sample comparisons.
- RSEM requires pre-built reference indices (rsem-prepare-reference) that include transcript and genome FASTA plus annotation GTF.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:26437033](../papers/26437033.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26862087](../papers/26862087.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
