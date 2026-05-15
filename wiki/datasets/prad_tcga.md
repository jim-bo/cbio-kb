---
name: Prostate Adenocarcinoma (TCGA, 2015)
studyId: prad_tcga
institution: The Cancer Genome Atlas
size: 499
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [bulk-rna-seq, methylation-array, snp-microarray, whole-exome-seq]
panels: []
tags: [prostate-cancer, prad, tcga, multi-platform]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# Prostate Adenocarcinoma (TCGA, 2015)

## Overview

TCGA multi-platform genomic characterization of prostate adenocarcinoma, representing one of the foundational reference datasets for prostate cancer genomics. Used as a comparator in studies of prostate cancer PDX models and [FGFR1](../genes/FGFR1.md) expression patterns. [PMID:38488813](../papers/38488813.md)

## Composition

- 499 prostate adenocarcinoma ([PRAD](../cancer_types/PRAD.md)) patients; multi-platform TCGA profiling. [PMID:38488813](../papers/38488813.md)
- Used as cross-reference validation for promoter CpG methylation–expression correlations of [FGFR1](../genes/FGFR1.md) and other prostate cancer driver genes. [PMID:38488813](../papers/38488813.md)

## Assays / panels (linked)

- Whole-exome sequencing, RNA-seq, DNA methylation arrays, copy-number analysis. [PMID:38488813](../papers/38488813.md)

## Papers using this cohort

- [PMID:38488813](../papers/38488813.md) — Integrative Molecular Analyses of the MD Anderson Prostate Cancer Patient-derived Xenograft (MDA PCa PDX) Series.
- [PMID:26855148](../papers/26855148.md) — Beltran et al. 2016, *Nature Medicine*: queried for NEPC classifier validation (n=460 treatment-naïve adenocarcinomas scored NEPC-high at 0%).
- [PMID:26928463](../papers/26928463.md) — Kumar et al., *Nat Genet* 2016: queried to verify metastasis-private mutations from prad_fhcrc rapid-autopsy cohort are non-driver.

## Notable findings derived from this cohort

- [FGFR1](../genes/FGFR1.md) promoter CpG methylation inversely correlated with [FGFR1](../genes/FGFR1.md) expression in both PDXs and TCGA-PRAD, confirming epigenetic regulation of FGFR1 in prostate cancer. [PMID:38488813](../papers/38488813.md)
- Queried for the NEPC classifier validation (n=460 treatment-naïve adenocarcinomas); 0% scored NEPC-high, confirming the classifier's specificity for castration-resistant neuroendocrine disease [PMID:26855148](../papers/26855148.md)
- Used alongside prad_su2c_2015 to validate that metastasis-private mutations found at autopsy in the prad_fhcrc cohort are unlikely to be drivers (only 2/51 occurred at >5% frequency in these cohorts) [PMID:26928463](../papers/26928463.md)
- Used for TRMT10A expression analysis vs normal prostate (n=52 normal, n=500 tumor), tumor-stage stratification, HR-gene Spearman correlations, and TRMT10A amplification/deletion frequencies (1.22–5.26% across mCRPC cohorts) [PMID:28068672](../papers/28068672.md)
- Cited as a comparison primary-prostate-cancer cohort in the MSK-IMPACT prostate study; MSK locoregional tumors showed higher TP53 and FOXA1 frequencies than TCGA primaries [PMID:28825054](../papers/28825054.md).
- Used to validate NOL10 overexpression in tumor vs. normal prostate, allele-specific BCR and survival outcomes (rs4519489 A/A genotype HR=13.05 for OS, P=0.038), and correlation of elevated NOL10 with advanced T stage (P=0.0058), lymph-node metastasis (P=0.045), and Gleason score (P=0.015) [PMID:28927585](../papers/28927585.md).

## Sources

- cBioPortal study `prad_tcga` [PMID:38488813](../papers/38488813.md).
- [PMID:26855148](../papers/26855148.md) — Beltran et al. 2016, *Nature Medicine*: NEPC classifier validation using this cohort (n=460 treatment-naïve adenocarcinomas).

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28068672](../papers/28068672.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:28927585](../papers/28927585.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
