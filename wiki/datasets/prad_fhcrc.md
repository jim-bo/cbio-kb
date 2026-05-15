---
name: Metastatic Castration-Resistant Prostate Cancer FHCRC 2016 (Kumar et al.)
studyId: prad_fhcrc
institution: Fred Hutchinson Cancer Research Center / University of Washington
size: 63
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - array-cgh
  - microarray-gene-expression
  - fish
  - immunohistochemistry
panels: []
tags:
  - prostate-cancer
  - metastatic-castration-resistant-prostate-cancer
  - mcrpc
  - rapid-autopsy
  - inter-metastasis-heterogeneity
  - fanconi-anemia
  - carboplatin
  - dna-repair
  - ar-signaling
processed_by: wiki-cli
processed_at: 2026-05-15
---

# Metastatic Castration-Resistant Prostate Cancer FHCRC 2016 (Kumar et al.)

## Overview

Rapid-autopsy multi-region genomic study of 63 men with metastatic castration-resistant prostate cancer ([PRAD](../cancer_types/PRAD.md)) enrolled in the University of Washington Prostate Cancer Donor Program. Tissue collected within 6 hours of death; 176 primary or metastatic tumors profiled by whole-exome sequencing, array CGH, and expression microarray. Established that metastases within a single patient are highly concordant for major oncogenic drivers, supporting single-biopsy clinical adequacy in mCRPC. Molecular profiling deposited at GEO accession GSE74685; registered in cBioPortal as `prad_fhcrc`. [PMID:26928463](../papers/26928463.md)

## Composition

- **63 men** with mCRPC at rapid autopsy.
- **176 primary or metastatic tumors:**
  - WES: 141 tumors from 56 men (Nimblegen V2/V3 capture, Illumina HiSeq 2000, 50/100 bp PE).
  - Array CGH: 149 tumors from 60 men (Agilent 2×400K SurePrint G3 CGH; CBS segmentation; GISTIC 2.0).
  - Expression microarray: 171 tumors from 63 men (Agilent 44K).
- Histology: 156 adenocarcinomas; 20 small-cell neuroendocrine tumors (from 2 men).
- All men received androgen deprivation therapy (ADT); most also received a systemic chemotherapy ([docetaxel](../drugs/docetaxel.md)) and an additional [AR](../genes/AR.md) pathway-targeted agent.
- 20/63 men were treated with [carboplatin](../drugs/carboplatin.md) and analyzed for DNA-repair biomarker response. [PMID:26928463](../papers/26928463.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Nimblegen V2/V3 capture, Illumina HiSeq 2000 (141 tumors).
- [array-cgh-agilent-1m](../methods/array-cgh-agilent-1m.md) — Agilent 2×400K SurePrint G3 CGH; CBS segmentation; GISTIC 2.0 (149 tumors).
- [microarray-gene-expression](../methods/microarray-gene-expression.md) — Agilent 44K (171 tumors).
- [fish](../methods/fish.md) — TMPRSS2-ERG status (53 tumors from 13 men).
- [immunohistochemistry](../methods/immunohistochemistry.md) — AR, GR, ER alpha/beta, chromogranin A, Ki-67.

## Papers using this cohort

- [PMID:26928463](../papers/26928463.md) — Kumar et al., *Nat Genet* 2016: primary study; established intra-individual concordance of metastatic drivers and Fanconi anemia pathway as [carboplatin](../drugs/carboplatin.md) response biomarker.

## Notable findings derived from this cohort

- Substantial inter-individual genomic diversity but limited intra-individual diversity: median 6.7% of CNA aberrations differed between tumors from the same patient vs 22.1% between different patients (P < 0.001) [PMID:26928463](../papers/26928463.md).
- AR amplification or mutation in 63% of men (vs rare in primary PC); 88% of patients had tumors with robust AR transcriptional activity despite prior AR-suppressive therapy [PMID:26928463](../papers/26928463.md).
- TMPRSS2-[ERG](../genes/ERG.md) status 100% concordant across metastases by FISH (53 tumors, 13 men); 94% concordant by array CGH [PMID:26928463](../papers/26928463.md).
- 5 men had hypermutated genomes with complex structural aberrations in [MSH2](../genes/MSH2.md) and [MSH6](../genes/MSH6.md); MMR deficiency apparent in matched primaries [PMID:26928463](../papers/26928463.md).
- Fanconi anemia pathway gene expression elevated in high-CCP (cell-cycle progression) tumors; [RB1](../genes/RB1.md) loss associated with elevated CCP and 15-gene FA signature (r = 0.78, P < 0.001) [PMID:26928463](../papers/26928463.md).
- Men with somatic DNA-repair pathway aberration (FA-gene homozygous loss or [ATM](../genes/ATM.md) inactivation) had significantly longer time on carboplatin (Kaplan-Meier log-rank P = 0.02, n=20 carboplatin-treated) [PMID:26928463](../papers/26928463.md).
- Metastasis-private mutations compared against [prad_tcga](../datasets/prad_tcga.md) and [prad_su2c_2015](../datasets/prad_su2c_2015.md) — only 2/51 private mutations occurred at >5% frequency in those cohorts, arguing most are non-driver events [PMID:26928463](../papers/26928463.md).
- Used as a comparison mCRPC cohort (63 cases) in the MSK-IMPACT prostate cancer profiling study; HR gene alteration frequencies were cross-validated against this cohort [PMID:28825054](../papers/28825054.md).
- Used for cross-cohort correlation of the NOL10 cell-cycle signature (CCS) with the clinical cell-cycle-progression (CCP) score [PMID:28927585](../papers/28927585.md).

## Sources

- cBioPortal study: `prad_fhcrc`
- Molecular profiling data: GEO accession GSE74685
- [PMID:26928463](../papers/26928463.md) — Kumar A et al., "Substantial interindividual and limited intraindividual genomic diversity among tumors from men with metastatic prostate cancer." *Nat Genet* 2016.

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:28927585](../papers/28927585.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
