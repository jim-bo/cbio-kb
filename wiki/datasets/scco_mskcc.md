---
name: Small Cell Carcinoma of the Ovary (MSKCC 2014)
studyId: scco_mskcc
institution: Memorial Sloan Kettering Cancer Center
size: 12
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
panels:
  - msk-impact-panel
tags:
  - ovarian-cancer
  - rare-cancer
  - swi-snf
  - targeted-sequencing
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# Small Cell Carcinoma of the Ovary (MSKCC 2014)

## Overview

Targeted sequencing cohort of 12 paired tumor/normal samples from small cell carcinoma of the ovary, hypercalcemic type (SCCOHT) — a rare, aggressive ovarian malignancy predominantly affecting young women. Collected at MSKCC (1998–2012) plus collaborating centers; formalin-fixed, paraffin-embedded tissue. Sequenced with the MSK-IMPACT panel (279 cancer-associated genes) on Illumina HiSeq 2000 (2×75 bp; mean depth 442×; ≥100× at 97% of targeted exons). Mutations validated by Sanger sequencing of genomic DNA and cDNA; protein loss confirmed by immunohistochemistry and immunoblot.

## Composition

- 12 paired tumor–normal SCCOHT samples ([SCCO](../cancer_types/SCCO.md)).
- FFPE tissue sourced from MSKCC and collaborating institutions.
- All 12 tumors with biallelic [SMARCA4](../genes/SMARCA4.md) inactivation; 4 non-recurrent somatic mutations found across all other 278 sequenced genes combined.

## Assays / panels (linked)

- [MSK-IMPACT panel](../methods/msk-impact-panel.md) — 279 cancer-associated genes, hybrid-capture targeted sequencing
- [Sanger sequencing](../methods/sanger-sequencing.md) — validation of all 12 cases

## Papers using this cohort

- [PMID:24658004](../papers/24658004.md) — Jelinic et al. (2014): recurrent SMARCA4 mutations establish SCCOHT as a SWI/SNF-driven malignancy.

## Notable findings derived from this cohort

- Biallelic inactivating [SMARCA4](../genes/SMARCA4.md) mutations detected in 100% (12/12) of SCCOHT tumors (P < 2.22×10⁻¹⁶); mutation classes included nonsense, frameshift, splice-site, and homozygous intragenic deletions — no missense mutations observed [PMID:24658004](../papers/24658004.md).
- Only 4 additional non-recurrent somatic mutations found across all other 278 sequenced genes combined — strikingly low mutational burden compared to TCGA non-hypermutated cancers [PMID:24658004](../papers/24658004.md).
- Loss of SMARCA4 (BRG1) protein confirmed by IHC and immunoblot; one case with in-frame deletion retained protein expression but is predicted to encode a catalytically dead helicase [PMID:24658004](../papers/24658004.md).
- One case harbored a heterozygous germline [SMARCA4](../genes/SMARCA4.md) nonsense mutation with somatic loss of the wild-type allele, supporting a hereditary component to SCCOHT [PMID:24658004](../papers/24658004.md).
- Synthetic-lethal vulnerability proposed: mutual exclusivity of [SMARCA2](../genes/SMARCA2.md) and [SMARCA4](../genes/SMARCA4.md) inactivation suggests SMARCA2 ATPase inhibition as a therapeutic strategy [PMID:24658004](../papers/24658004.md).

## Sources

- [PMID:24658004](../papers/24658004.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
