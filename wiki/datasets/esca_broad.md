---
name: Esophageal Adenocarcinoma — Broad/Columbia (Dulak 2013)
studyId: esca_broad
institution: Broad Institute / Columbia University
size: 149
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
panels: []
tags:
  - ESCA
  - esophageal adenocarcinoma
  - EAC
  - GEJ
processed_by: crosslinker
processed_at: 2026-05-09
---

# Esophageal Adenocarcinoma — Broad/Columbia (Dulak 2013)

## Overview

Whole-exome and whole-genome sequencing study of 149 fresh-frozen, surgically-resected, treatment-naïve esophageal adenocarcinoma (EAC) and gastro-esophageal junction ([GEJ](../cancer_types/GEJ.md)) tumor/normal pairs from Dulak et al. (Nature Genetics 2013). Raw data deposited under dbGaP phs000598.v1.p1. [PMID:23525077](../papers/23525077.md)

## Composition

- 149 EAC/GEJ tumor/normal pairs subjected to whole-exome sequencing (SureSelect v2 Exome bait, Illumina HiSeq; mean coverage 83.3× tumor / 85.9× normal); 16 pairs additionally subjected to whole-genome sequencing (~49× tumor / 30× germline); 14 WGS samples additionally profiled on Affymetrix mRNA expression arrays (GEO GSE42363). [PMID:23525077](../papers/23525077.md)
- Cancer types: [ESCA](../cancer_types/ESCA.md) (esophageal adenocarcinoma) and [GEJ](../cancer_types/GEJ.md) (gastric-esophageal junction adenocarcinoma). [PMID:23525077](../papers/23525077.md)
- Four MSI-positive hypermutated tumors (mutation frequencies 14.6–50.9/Mb; [MSH6](../genes/MSH6.md) + [MSH3](../genes/MSH3.md) mutations) excluded from significance analysis, leaving 145 evaluable tumors. [PMID:23525077](../papers/23525077.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — SureSelect v2 Exome capture (Agilent), Illumina HiSeq, mutation calling via MuTect and Indelocator. [PMID:23525077](../papers/23525077.md)
- [whole-genome-seq](../methods/whole-genome-seq.md) — 101 bp paired-end reads; rearrangement calling via dRanger. [PMID:23525077](../papers/23525077.md)
- [mutsig](../methods/mutsig.md) — MutSig significance algorithm used to nominate 26 SMGs at FDR q<0.1. [PMID:23525077](../papers/23525077.md)
- Sequenom mass-spectrometry genotyping for mutation validation. [PMID:23525077](../papers/23525077.md)
- Affymetrix expression arrays on 14 WGS samples (GEO GSE42363). [PMID:23525077](../papers/23525077.md)

## Papers using this cohort

- [PMID:23525077](../papers/23525077.md) — Dulak et al., "Exome and whole genome sequencing of esophageal adenocarcinoma identifies recurrent driver events and mutational complexity," *Nat Genet* 2013.

## Notable findings derived from this cohort

- Median genome-wide mutation frequency 9.9/Mb (range 7.1–25.2/Mb), exceeded in solid tumors only by lung cancer and melanoma; median 104 non-silent coding mutations per tumor. [PMID:23525077](../papers/23525077.md)
- A novel EAC-specific mutational signature dominated by A>C transversions at AA dinucleotides accounts for 29% of all genome-wide mutations; the signature shows transcription-coupled repair attenuation and strong enrichment at AAG trinucleotides (49.3/Mb). [PMID:23525077](../papers/23525077.md)
- 26 significantly mutated genes (MutSig FDR q<0.1): confirmed [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), [SMAD4](../genes/SMAD4.md), [PIK3CA](../genes/PIK3CA.md), [ARID1A](../genes/ARID1A.md); novel candidates [ELMO1](../genes/ELMO1.md), [DOCK2](../genes/DOCK2.md), [SPART](../genes/SPART.md), [TLR4](../genes/TLR4.md), [SMARCA4](../genes/SMARCA4.md), [ARID2](../genes/ARID2.md). [PMID:23525077](../papers/23525077.md)
- [ELMO1](../genes/ELMO1.md) or [DOCK2](../genes/DOCK2.md) mutations in 25/145 (17%) of EACs; EAC-derived [ELMO1](../genes/ELMO1.md) mutants augment NIH/3T3 invasion 2–7-fold over wild-type, implicating aberrant [RAC1](../genes/RAC1.md) signaling. [PMID:23525077](../papers/23525077.md)
- SWI/SNF family members [ARID1A](../genes/ARID1A.md), [SMARCA4](../genes/SMARCA4.md), [ARID2](../genes/ARID2.md) mutated in 20% of tumors; 24% of EACs harbored chromatin-modifying-factor mutations when including [PBRM1](../genes/PBRM1.md) and [JARID2](../genes/JARID2.md). [PMID:23525077](../papers/23525077.md)
- 23% of tumors had mutations in genes with approved/preclinical targeted agents; combined with copy-number amplification, 48% had a targetable alteration. [PMID:23525077](../papers/23525077.md)

## Sources

- dbGaP: phs000598.v1.p1
- GEO: GSE42363 (Affymetrix expression arrays)
- DOI: 10.1038/ng.2591

*This page was processed by **crosslinker** on **2026-05-09**.*
