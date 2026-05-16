---
name: OncoSG Stomach Adenocarcinoma WGS Cohort (2018)
studyId: stad_oncosg_2018
institution: National Cancer Centre Singapore / Genome Institute of Singapore
size: 40
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - STRUCTURAL_VARIANT
  - MRNA_EXPRESSION
panels: []
tags:
  - gastric-cancer
  - stad
  - whole-genome-seq
  - rna-seq
  - non-coding-drivers
  - ctcf
  - singapore
  - oncosg
processed_by: crosslinker
processed_at: 2026-05-16
---

# OncoSG Stomach Adenocarcinoma WGS Cohort (2018)

## Overview

Whole-genome sequencing cohort of 40 gastric adenocarcinoma ([STAD](../cancer_types/STAD.md)) tumor/normal pairs newly sequenced in Singapore by the OncoSG consortium. The cohort was combined with previously published TCGA (n=40), ICGC/EGAD00001003132 (n=32), and Wang et al. Hong Kong (n=100) WGS datasets to form a pooled 212-sample discovery cohort for non-coding driver analysis. The Singapore cohort contributed 19 matched tumor-normal RNA-seq pairs used for cis-expression validation. Alignment was to hg19 using [BWA](../methods/bwa.md); somatic events called by a random-forest ensemble (SMuRF) of four callers.

## Composition

- **n = 40** primary gastric adenocarcinoma tumor/normal pairs from Singapore patients.
- Sequenced on Illumina HiSeq (101 bp or 151 bp paired-end, 300–400 bp inserts).
- RNA-seq available for 19/40 matched tumor-normal pairs (used for cis-expression analysis).
- Cancer type: [STAD](../cancer_types/STAD.md) (stomach adenocarcinoma); molecular subtypes include CIN, GS, EBV, and MSI (per TCGA classification applied to pooled cohort).

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md) on Illumina HiSeq; ~30× tumor coverage, matched normal.
- [RNA-seq](../methods/rna-seq.md) on 19 matched tumor-normal pairs; RSEM normalization.
- Somatic variant calling via ensemble random-forest classifier (SMuRF) using [VarScan](../methods/varscan.md), [MuTect](../methods/mutect.md), VarDict, and FreeBayes.

## Papers using this cohort

- [PMID:29670109](../papers/29670109.md) — Guo et al. 2018, Nature Communications — "Mutational signature of non-coding driver mutations at [CTCF](../genes/CTCF.md) binding sites in gastric adenocarcinoma."

## Notable findings derived from this cohort

- The Singapore 40-sample cohort was pooled with TCGA, ICGC, and Hong Kong WGS data (total n=212) to identify 34 significant non-coding SNV hotspots genome-wide; 11 overlap CTCF binding sites (CBSs), appearing in 25% of gastric tumors [PMID:29670109](../papers/29670109.md).
- RNA-seq from 19 Singapore matched pairs validated cis-expression changes at three of four tested CBS hotspots: [CENPQ](../genes/CENPQ.md) and [MMUT](../genes/MMUT.md) upregulated (CBS at chr6:50.57 Mb), [KCNQ5](../genes/KCNQ5.md) downregulated (chr6:73.12 Mb CBS), and [SPART](../genes/SPART.md) nominally downregulated (chr13:36.55 Mb CBS) [PMID:29670109](../papers/29670109.md).
- CBS hotspot mutations were enriched in CIN-subtype tumors (71% of CBS-hotspot mutations, Fisher's exact p=0.012) and were clonal early events (VAFs indistinguishable from paired coding driver mutations, paired Wilcoxon p=0.49) [PMID:29670109](../papers/29670109.md).

## Sources

- Guo S et al. "Mutational signature of non-coding driver mutations at CTCF binding sites in gastric adenocarcinoma." Nature Communications. 2018;9(1):1648. [PMID:29670109](../papers/29670109.md). DOI: 10.1038/s41467-018-04042-w.

*This page was processed by **crosslinker** on **2026-05-16**.*
