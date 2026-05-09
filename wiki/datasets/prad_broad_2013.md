---
name: Prostate Adenocarcinoma — Broad/Cornell (Baca 2013)
studyId: prad_broad_2013
institution: Broad Institute / Weill Cornell Medical College
size: 57
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - affymetrix-snp6
  - rna-seq
panels: []
tags:
  - PRAD
  - prostate cancer
  - chromoplexy
processed_by: crosslinker
processed_at: 2026-05-09
---

# Prostate Adenocarcinoma — Broad/Cornell (Baca 2013)

## Overview

Whole-genome sequencing study of 57 prostate cancers by Baca et al. (Cell 2013), focused on characterizing complex chromosomal rearrangements ("chromoplexy") and their role in driver gene co-disruption and tumor evolution. BAM, RNA-seq, and SNP-array data deposited at dbGaP phs000447.v1.p1. [PMID:23622249](../papers/23622249.md)

## Composition

- 55 treatment-naïve primary [PRAD](../cancer_types/PRAD.md) adenocarcinomas spanning Gleason score 6–9 and pathological stages pT2N0–pT4N1, plus 2 neuroendocrine ([PRNE](../cancer_types/PRNE.md)) metastases arising after castration-based therapy. [PMID:23622249](../papers/23622249.md)
- Extended cohort of 199 prostate adenocarcinomas used for SCNA recurrence and GISTIC analysis (this study combined with [PMID:22610119](../papers/22610119.md)). [PMID:23622249](../papers/23622249.md)

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — Illumina GAIIx paired-end 101 bp reads, BWA alignment; mean coverage 61× tumor and 34× matched normal; rearrangement detection via [dRanger](../methods/dranger.md) and [BreakPointer](../methods/breakpointer.md); filtering against a panel of 172–176 non-cancerous genomes. [PMID:23622249](../papers/23622249.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — somatic copy-number profiling analyzed by [gistic](../methods/gistic.md) v2 and [ABSOLUTE](../methods/absolute.md). [PMID:23622249](../papers/23622249.md)
- [rna-seq](../methods/rna-seq.md) — on 20 tumors with matched benign prostate tissue for 16 cases; used for ETS fusion identification. [PMID:23622249](../papers/23622249.md)
- [fish](../methods/fish.md) and Sanger resequencing — validation of ETS fusions. [PMID:23622249](../papers/23622249.md)
- New algorithms introduced: [ChainFinder](../methods/chainfinder.md) (graph-theory chromoplexy detection), [CLONET](../methods/clonet.md) (clonality estimation from SNP allelic fractions). [PMID:23622249](../papers/23622249.md)

## Papers using this cohort

- [PMID:23622249](../papers/23622249.md) — Baca et al., "Punctuated Evolution of Prostate Cancer Genomes," *Cell* 2013.

## Notable findings derived from this cohort

- Chromoplectic chains of ≥5 rearrangements (≥10 breakpoints) detected in 50/57 tumors (88%); 39% of rearrangements participated in chains vs. 2.8% in simulated controls (p<10⁻⁴); events span multiple chromosomes simultaneously, distinct from chromothripsis. [PMID:23622249](../papers/23622249.md)
- ETS+ tumors show more inter-chromosomal chromoplexy in transcriptionally active regions (androgen receptor-coupled); ETS−/[CHD1](../genes/CHD1.md)del tumors show intra-chromosomal rearrangements in GC-poor heterochromatin. [PMID:23622249](../papers/23622249.md)
- 15/26 (58%) [ERG](../genes/ERG.md)-positive cases acquired the [TMPRSS2](../genes/TMPRSS2.md)–[ERG](../genes/ERG.md) fusion within a chromoplexy chain; chromoplexy coordinately disrupts multiple tumor suppressors in a single event — e.g., [PTEN](../genes/PTEN.md) (9 cases), [NKX3-1](../genes/NKX3-1.md) (8 cases), [TP53](../genes/TP53.md) (4 cases). [PMID:23622249](../papers/23622249.md)
- CLONET-derived clonal ordering establishes a consensus progression path: early [NKX3-1](../genes/NKX3-1.md) deletion and [TMPRSS2](../genes/TMPRSS2.md)–[ERG](../genes/ERG.md) fusion → intermediate [CDKN1B](../genes/CDKN1B.md)/[TP53](../genes/TP53.md) loss → late [PTEN](../genes/PTEN.md) deletion. [PMID:23622249](../papers/23622249.md)
- Chromoplexy is not prostate-specific: ChainFinder detected chains of ≥5 rearrangements in melanoma, [NSCLC](../cancer_types/NSCLC.md), [HNSC](../cancer_types/HNSC.md), and breast adenocarcinoma across an additional 59 genomes. [PMID:23622249](../papers/23622249.md)
- Gleason grade tracks genomic derangement: tumors with predominant Gleason pattern 4 had more recurrent SCNAs than pattern 3 tumors (p=0.0059, 199-tumor cohort), independent of overall SCNA load, purity, and mutation burden. [PMID:23622249](../papers/23622249.md)

## Sources

- dbGaP: phs000447.v1.p1
- DOI: 10.1016/j.cell.2013.03.021

*This page was processed by **crosslinker** on **2026-05-09**.*
