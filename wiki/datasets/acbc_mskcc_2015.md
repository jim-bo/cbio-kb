---
name: MSKCC Adenoid Cystic Carcinoma of the Breast 2015
studyId: acbc_mskcc_2015
institution: Memorial Sloan Kettering Cancer Center / Institut Curie
size: 12
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - adenoid-cystic-carcinoma
  - triple-negative-breast-cancer
  - rare-cancers
  - whole-exome-sequencing
processed_by: crosslinker
processed_at: 2026-05-14
---

# MSKCC Adenoid Cystic Carcinoma of the Breast 2015

## Overview

Twelve adenoid cystic carcinomas (AdCCs) of the breast — all triple-negative (ER−/PR−/HER2−) — collected from Institut Curie (Paris) and Memorial Sloan Kettering Cancer Center. This dataset was generated as part of the first massively parallel sequencing study of breast AdCC, a rare special-histology subtype comprising ~0.1% of invasive breast cancers. Fresh-frozen and FFPE material was used; histologic grade 1 (58%) or grade 2 (42%).

## Composition

- **Cancer types:** [ACBC](../cancer_types/ACBC.md) (adenoid cystic carcinoma of breast), a special subtype of [BRCA](../cancer_types/BRCA.md).
- **Sample count:** 12 tumor–matched normal pairs.
- **Clinical fields:** ER/PR/HER2 status (all triple-negative), histologic grade, growth pattern (tubular-cribriform, cribriform, solid), MYB-NFIB fusion status by FISH/RT-PCR.
- **Sequencing:** Whole-exome sequencing (Agilent SureSelect Human All Exon v4, Illumina HiSeq 2000); median depth 78× (range 43–129×); mean 88% of target ≥10× coverage. Reference genome GRCh37/hg19.
- **Copy number:** VarScan2 and GISTIC2.0; ABSOLUTE for purity/ploidy.
- **Raw data:** WES data deposited in NCBI SRA under accession SRP053134.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — primary somatic variant and CNA discovery.
- [fish](../methods/fish.md) — [MYB](../genes/MYB.md) rearrangement assessment (ZytoLight SPEC [MYB](../genes/MYB.md) Dual Color Break Apart Probe).
- [quantitative-rt-pcr](../methods/quantitative-rt-pcr.md) — MYB-NFIB fusion transcript confirmation.

## Papers using this cohort

- [PMID:26095796](../papers/26095796.md) — Martelotto et al. 2015, "Genomic landscape of adenoid cystic carcinoma of the breast," *J Pathol*.

## Notable findings derived from this cohort

- MYB-NFIB fusion detected in 10/12 (83%) breast AdCCs; breast AdCCs show a low somatic mutation rate (0.27 non-silent mutations/Mb), conspicuously lack [TP53](../genes/TP53.md) and [PIK3CA](../genes/PIK3CA.md) mutations, and share recurrent gene mutations with salivary gland AdCCs ([SF3B1](../genes/SF3B1.md), [FBXW7](../genes/FBXW7.md), [FGFR2](../genes/FGFR2.md), [PRKD1](../genes/PRKD1.md)) [PMID:26095796](../papers/26095796.md).
- Recurrent copy-number losses at 12q12-q14.1 (5/12 cases) and gains at 17q21-q25.1 (3/12 cases); no amplifications or homozygous deletions detected; genomic instability conspicuously lower than common-type triple-negative breast cancers [PMID:26095796](../papers/26095796.md).

## Sources

- cBioPortal study: `acbc_mskcc_2015`
- SRA accession: SRP053134

*This page was processed by **crosslinker** on **2026-05-14**.*
