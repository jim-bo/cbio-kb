---
name: MSKCC Upper Tract Urothelial Carcinoma 2015
studyId: utuc_mskcc_2015
institution: Memorial Sloan Kettering Cancer Center
size: 83
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - STRUCTURAL_VARIANT
panels:
  - msk-impact-panel
tags:
  - upper-tract-urothelial-carcinoma
  - urothelial-carcinoma
  - targeted-sequencing
  - msk-impact
processed_by: crosslinker
processed_at: 2026-05-14
---

# MSKCC Upper Tract Urothelial Carcinoma 2015

## Overview

Eighty-three upper tract urothelial carcinoma ([UTUC](../cancer_types/UTUC.md)) tumors from patients treated with radical nephroureterectomy at Memorial Sloan Kettering Cancer Center, sequenced with the MSK-IMPACT 300-gene hybrid-capture panel. At the time of publication, this represented the largest NGS-profiled [UTUC](../cancer_types/UTUC.md) cohort. The dataset is publicly available through the MSKCC cBioPortal for Cancer Genomics. A high-grade UCB comparator cohort (n=102; study [blca_mskcc_solit_2014](../datasets/blca_mskcc_solit_2014.md)) was profiled on the same platform.

## Composition

- **Cancer types:** [UTUC](../cancer_types/UTUC.md) (upper tract urothelial carcinoma); all primary urothelial histology, no predominant variants.
- **Sample count:** 83 tumors (60 high-grade, 23 low-grade); all obtained at radical nephroureterectomy.
- **Clinical fields:** tumor grade, T stage, smoking history, age, sex, history of UTUC.
- **Sequencing:** MSK-IMPACT 300-gene custom hybrid-capture panel, Illumina HiSeq 2500; mean coverage 650× (UTUC cohort); reference genome hg19.
- **Variant calling:** BWA v0.6.2, MuTect v1.0.27783 (SNVs), SomaticIndelDetector (indels), DELLY (structural rearrangements). Orthogonal validation with MiSeq and Sanger sequencing (100% concordance for 10-gene re-test).
- **Patient demographics:** median age 70 yr (IQR 63–76); matched to the UCB comparator cohort on age, sex, smoking, and stage distributions.

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md) — 300 cancer-associated genes; hybrid-capture targeted DNA sequencing.
- [sanger-sequencing](../methods/sanger-sequencing.md) — orthogonal validation.

## Papers using this cohort

- [PMID:26278805](../papers/26278805.md) — Sfakianos et al. 2015, "Genomic Characterization of Upper Tract Urothelial Carcinoma," *European Urology*.

## Notable findings derived from this cohort

- UTUC and UCB share the same gene catalog but differ in prevalence: UTUC enriched for [FGFR3](../genes/FGFR3.md) (35.6% vs 21.6%), [HRAS](../genes/HRAS.md) (13.6% vs 1.0%, p=0.001), and [CDKN2B](../genes/CDKN2B.md) deletions (15.3% vs 3.9%), while UCB enriched for [TP53](../genes/TP53.md) (25.4% vs 57.8%, p<0.001) and [RB1](../genes/RB1.md) (0% vs 18.6%, p<0.001) alterations [PMID:26278805](../papers/26278805.md).
- First description of a [POLE](../genes/POLE.md) V411L ultramutated urothelial tumor (422 somatic mutations) in UTUC; five intrachromosomal FGFR3-TACC3 fusions identified exclusively in high-grade UTUC (8.5% vs 2.0% in UCB) [PMID:26278805](../papers/26278805.md).
- 22/23 low-grade UTUC tumors (96%) harbored activating [FGFR3](../genes/FGFR3.md) mutations; all 23 were [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md) wild-type, supporting a low-grade-tumor-progression model distinct from de novo high-grade UCB [PMID:26278805](../papers/26278805.md).

## Sources

- cBioPortal study: `utuc_mskcc_2015`

*This page was processed by **crosslinker** on **2026-05-14**.*
