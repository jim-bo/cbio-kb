---
name: NIH Uterine Clear Cell Carcinoma Exome Cohort (NIH, JCO 2017)
studyId: uccc_nih_2017
institution: National Institutes of Health
size: 63
reference_genome: hg18
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - sanger-sequencing
panels: []
tags:
  - uterine-clear-cell-carcinoma
  - endometrial-cancer
  - exome-sequencing
  - msi
  - pi3k-pathway
  - rare-histology
processed_by: crosslinker
processed_at: 2026-05-15
---

# NIH Uterine Clear Cell Carcinoma Exome Cohort (NIH, JCO 2017)

## Overview

The uccc_nih_2017 dataset represents the largest exome-scale molecular characterization of uterine clear cell endometrial carcinoma (CCEC) to date, assembled at the National Institutes of Health. Le Gallo et al. combined a discovery whole-exome sequencing screen (16 paired tumor-normal samples) with a Sanger-sequencing prevalence screen of 22 genes-of-interest in 47 additional CCECs, for a total of 63 clinically diagnosed clear cell endometrial carcinomas. Note that reference alignment used the older NCBI Build 36 (hg18) reference genome. Raw exome data are deposited at dbGaP accession phs000967.v1.p1 and processed data are available via cBioPortal as study uccc_nih_2017. The study was the first to nominate [TAF1](../genes/TAF1.md) and [KMT2C](../genes/KMT2C.md) (MLL3) as candidate driver genes in this rare endometrial subtype.

## Composition

- **63 cases:** 59 pure CCEC plus 4 mixed-histology endometrial cancers (only the CCEC component sequenced).
- **Discovery cohort:** 16 paired tumor-normal DNAs by whole-exome sequencing (13 Illumina Truseq capture, 3 Agilent SureSelect; mean depth 75x; 89.3% of targeted bases at sufficient coverage).
- **Prevalence screen:** Sanger sequencing of 22 genes-of-interest in the remaining 47 CCECs.
- **MSI assessment:** Genotyping of five mononucleotide repeats ([msi-pcr-pentaplex](../methods/msi-pcr-pentaplex.md)); 11.3% of cases MSI-high.
- **Reference genome:** NCBI Build 36 (hg18) — reads aligned with CASAVA v1.8.0 + cross_match.
- **Variant calling:** bam2mpg, filtered with VarSifter; missense functional prediction via SIFT, Mutation Assessor, and PolyPhen-2 (called functional if ≥2 algorithms scored damaging).
- **Data:** dbGaP `phs000967.v1.p1`; cBioPortal study `uccc_nih_2017`.
- **Cancer type:** [UCCC](../cancer_types/UCCC.md) — Uterine Clear Cell Carcinoma.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — discovery screen of 16 paired tumor-normal samples.
- [sanger-sequencing](../methods/sanger-sequencing.md) — prevalence screen of 22 genes in 47 additional CCECs.
- [msi-pcr-pentaplex](../methods/msi-pcr-pentaplex.md) — microsatellite instability genotyping.

## Papers using this cohort

- [PMID:28485815](../papers/28485815.md) — Le Gallo et al., *JCO* 2017: Largest exome-scale CCEC study; 63 tumors; identified frequent mutations in [TP53](../genes/TP53.md) (39.7%), [PIK3CA](../genes/PIK3CA.md) (23.8%), [PIK3R1](../genes/PIK3R1.md) (15.9%), [ARID1A](../genes/ARID1A.md) (15.9%), [PPP2R1A](../genes/PPP2R1A.md) (15.9%), and [SPOP](../genes/SPOP.md) (14.3%); nominated [TAF1](../genes/TAF1.md) and [KMT2C](../genes/KMT2C.md) as novel CCEC candidate drivers; 11.3% MSI-high; PI3K axis mutated in 34.9%. [PMID:28485815](../papers/28485815.md)

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) is the most frequently mutated gene (39.7%), enriched in serous-like CCECs; PI3K axis ([PIK3CA](../genes/PIK3CA.md)–[PIK3R1](../genes/PIK3R1.md)–[PTEN](../genes/PTEN.md)) altered in 34.9% of all 63 CCECs. [PMID:28485815](../papers/28485815.md)
- [TAF1](../genes/TAF1.md) nominated as a novel CCEC candidate driver: 9.5% (6/63) of tumors carry 8 missense mutations, 5 of which localize to the putative HAT domain including recurrently mutated residues Arg843 and Ala850; all 8 predicted functional by ≥2 in-silico algorithms. [PMID:28485815](../papers/28485815.md)
- [KMT2C](../genes/KMT2C.md) (MLL3) is a second novel CCEC candidate driver: 7.9% (5 tumors), 3 frameshifts N-terminal to the SET methyltransferase domain consistent with loss-of-function. [PMID:28485815](../papers/28485815.md)
- CCECs are molecularly heterogeneous: cross-histology profiling distributes 27.0% serous-like, 19.1% mixed, 20.6% endometrioid-like, and 33.3% with no detectable alterations across the 7-gene + MSI panel. [PMID:28485815](../papers/28485815.md)
- 11.3% MSI-high cases raise the prospect of anti-PD-1 therapy in this subset; absence of [POLE](../genes/POLE.md) exonuclease-domain hotspot mutations contrasts with the favorable prognosis of POLE mutations in endometrioid endometrial cancer. [PMID:28485815](../papers/28485815.md)

## Sources

- dbGaP accession `phs000967.v1.p1`.
- cBioPortal study `uccc_nih_2017`.
- Le Gallo M, et al. *Exome sequencing of serous endometrial tumors identifies recurrent somatic mutations in chromatin-remodeling and ubiquitin ligase complex genes.* JCO. 2017. [PMID:28485815](../papers/28485815.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
