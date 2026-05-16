---
name: CTF Synodos Schwannomatosis (2025)
studyId: schw_ctf_synodos_2025
institution: Children's Tumor Foundation Synodos for Schwannomatosis Consortium (multi-institutional)
size: 165
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - epic-methylation-array
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
panels: []
tags:
  - schwannomatosis
  - schwannoma
  - nf2
  - lztr1
  - smarcb1
  - methylation
  - ctf-synodos
processed_by: crosslinker
processed_at: 2026-05-16
---

# CTF Synodos Schwannomatosis (2025)

## Overview

165 schwannomas (SWNs) from 72 schwannomatosis (SWNTS) patients assembled through the Children's Tumor Foundation Synodos for Schwannomatosis Consortium, the largest multi-omic schwannomatosis dataset to date. All tumors underwent Illumina Infinium HumanMethylationEPIC (EPIC) methylation array profiling; subsets received whole-exome sequencing (WES; n=29), whole-genome sequencing (WGS; n=22), and RNA-seq (n=24). Comparators included non-syndromic sporadic schwannomas (NS-SWNs) and 90 neurofibromas. Reference genome hg19 (DNA); hg38 (RNA-seq). Data released as cBioPortal study `schw_ctf_synodos_2025`.

## Composition

- 165 schwannomas from 72 SWNTS patients (female/male: 31/41).
- Comparator: non-syndromic sporadic schwannomas (NS-SWNs) and 90 neurofibromas (56 plexiform, 34 cutaneous) for DNA methylation profiling.
- SWNTS histology: [SCHW](../cancer_types/SCHW.md) (peripheral nerve sheath tumor); [MPNST](../cancer_types/MPNST.md) excluded.
- [LZTR1](../genes/LZTR1.md) vs. [SMARCB1](../genes/SMARCB1.md) germline mutation subgroups characterized.
- Methylation subgrouping: 4 clusters by anatomic location (lower extremity, upper extremity, spinal, truncal/head & neck).

## Assays / panels (linked)

- [EPIC methylation array](../methods/epic-methylation-array.md) (Illumina Infinium HumanMethylationEPIC; all 165 tumors)
- [Whole-exome sequencing](../methods/whole-exome-seq.md) (Agilent SureSelect All Exon V5+UTRs; ≥250× tumor / 50× normal; 29 SWNTS-SWNs + 25 NS-SWNs)
- [Whole-genome sequencing](../methods/whole-genome-seq.md) (Illumina HiSeqX; 60× tumor / 30× normal; 22 SWNTS-SWNs)
- [RNA-seq](../methods/rna-seq.md) (TruSeq Stranded Total RNA/Ribo-Zero Gold; 24 SWNTS-SWNs + 41 NS-SWNs)
- Variant calling: [MuTect](../methods/mutect.md), [Strelka](../methods/strelka.md), HaplotypeCaller
- SV calling: [DELLY](../methods/delly.md) v0.8.1 with MAVIS validation
- CN/LOH: [Sequenza](../methods/sequenza.md)
- Fusion discovery: [FusionCatcher](../methods/fusioncatcher.md) with RT-PCR confirmation
- Focal CN peaks: [GISTIC](../methods/gistic.md)
- Immune deconvolution: [CIBERSORTx](../methods/cibersortx.md)
- Methylation clustering: ConsensusClusterPlus + Ward linkage + [t-SNE](../methods/tsne.md) on top 10,000 variably methylated CpGs

## Papers using this cohort

- [PMID:33025139](../papers/33025139.md) — Mansouri et al. 2021, Acta Neuropathol: "Epigenomic, genomic, and transcriptomic landscape of schwannomatosis"

## Notable findings derived from this cohort

- [NF2](../genes/NF2.md) is the sole recurrent driver SNV; SWNTS-SWNs harbor NF2 mutation/loss in 83% vs. 58% in NS-SWNs (Chi-square, p<0.0001) — [PMID:33025139](../papers/33025139.md)
- 22q deletions in 80% of SWNTS-SWNs vs. 30% of NS-SWNs (p<0.01); 76% vs. 35% with deep deletions spanning LZTR1, SMARCB1, and NF2 — [PMID:33025139](../papers/33025139.md)
- DNA methylation separates SWNs from neurofibromas but not SWNTS-SWNs from NS-SWNs; four methylation subgroups within SWNTS-SWNs segregate by anatomic location — [PMID:33025139](../papers/33025139.md)
- [SH3PXD2A](../genes/SH3PXD2A.md)–[HTRA1](../genes/HTRA1.md) fusion detected by RT-PCR in 14% of SWNTS-SWNs, enriched in LZTR1-mutant (p=0.025) and painful tumors — [PMID:33025139](../papers/33025139.md)
- Painful SWNTS-SWNs carry 4.4-fold higher CNV (p=0.042) and are enriched for lower-extremity location, female sex, germline LZTR1 mutation, and SH3PXD2A-HTRA1 fusion — [PMID:33025139](../papers/33025139.md)
- TMB is low (WES 0.17/Mb SWNTS vs. 0.22/Mb NS-SWN); COSMIC signatures 1A, 6, 15, and 2 present; APOBEC signature 2 absent from NS-SWNs — [PMID:33025139](../papers/33025139.md)

## Sources

- [PMID:33025139](../papers/33025139.md)
- cBioPortal study: `schw_ctf_synodos_2025`

*This page was processed by **crosslinker** on **2026-05-16**.*
