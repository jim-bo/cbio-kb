---
name: MSKCC Prostate Cancer Integrative Genomic Profiling
studyId: prad_mskcc
institution: Memorial Sloan Kettering Cancer Center
size: 218
reference_genome: hg18
canonical_source: cbioportal
unverified: false
assays:
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - MUTATION_EXTENDED
panels: []
tags:
  - prostate-cancer
  - copy-number
  - integrative-genomics
  - prad
processed_by: wiki-cli
processed_at: 2026-05-15
---

# MSKCC Prostate Cancer Integrative Genomic Profiling

## Overview

Integrative genomic profiling of 218 prostate cancers (181 primary tumors and 37 metastases) plus 12 cell lines/xenografts from Memorial Sloan Kettering Cancer Center. The dataset is publicly available on cBioPortal as `prad_mskcc` (GEO accession GSE21032). All samples had at least 70% tumor content; median follow-up approximately 5 years. The study combined DNA copy number, mRNA/miRNA expression, and targeted exon resequencing to characterize the genomic landscape of prostate cancer.

## Composition

- Cancer type: [PRAD](../cancer_types/PRAD.md)
- 218 prostate tumors: 181 primary + 37 metastases; 12 cell lines/xenografts
- Platforms: [Agilent 244K](../methods/agilent-244k.md) aCGH, Affymetrix Human Exon 1.0 ST (mRNA), Agilent miRNA V2
- Targeted resequencing: Sanger exon resequencing of 138 genes in 80 tumors; iPLEX [Sequenom](../methods/sequenom-genotyping.md) for 22 oncogene hotspots in 156 tumors
- Key clinical fields: Gleason score, pathological stage, biochemical recurrence, castration-resistance status

## Assays / panels (linked)

- [agilent-244k](../methods/agilent-244k.md) — Agilent 244K aCGH for DNA copy number
- [sequenom-genotyping](../methods/sequenom-genotyping.md) — iPLEX Sequenom for oncogene hotspot genotyping

## Papers using this cohort

- [PMID:20579941](../papers/20579941.md) — Taylor et al. 2010, integrative genomic profiling paper defining the cohort

## Notable findings derived from this cohort

- [NCOA2](../genes/NCOA2.md) amplification at 8q13.3 in ~11% of tumors (24.3% of metastases); overexpression correlated with enhanced [AR](../genes/AR.md) transcriptional output (p < 0.0001) [PMID:20579941](../papers/20579941.md)
- [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) fusion present in 52% of tumors; associated with a novel prostate-specific 3p14 deletion implicating [FOXP1](../genes/FOXP1.md), [RYBP](../genes/RYBP.md), and [SHQ1](../genes/SHQ1.md) as cooperative tumor suppressors [PMID:20579941](../papers/20579941.md)
- PI3K pathway altered in 42% of primary tumors and 100% of metastases; AR pathway altered in 56% of primaries and 100% of metastases [PMID:20579941](../papers/20579941.md)
- Unsupervised CNA-based hierarchical clustering identified 6 prognostic subgroups independent of Gleason score [PMID:20579941](../papers/20579941.md)
- Low somatic mutation rate (~0.31 mutations/Mb); [TP53](../genes/TP53.md) and [PTEN](../genes/PTEN.md) primarily lost through copy-number deletion rather than point mutation [PMID:20579941](../papers/20579941.md)
- Used as a validation cohort for somatic copy-number alteration and mutation profiling in metastatic castration-resistant prostate cancer [PMID:25024180](../papers/25024180.md)
- Referenced as a comparison cohort (218 cases, Taylor 2010) in the MSK-IMPACT prospective prostate cancer profiling study for contextualizing DDR gene alteration frequencies [PMID:28825054](../papers/28825054.md).
- Used (Taylor 2010 / GSE21034, n=140) in a fixed-effects BCR meta-analysis across CPGEA / MSKCC / TCGA / DKFZ yielding HR=2.49 (1.85–3.35, P=1.81e-9) for the NOL10 cell-cycle signature; also used for NOL10–EMT/AR signature correlation (n=150) [PMID:28927585](../papers/28927585.md).

## Sources

- [PMID:20579941](../papers/20579941.md) — Taylor et al., "Integrative genomic profiling of human prostate cancer," *Cancer Cell* 2010
- GEO: GSE21032
- cBioPortal: https://www.cbioportal.org/study/summary?id=prad_mskcc

*This page was processed by **entity-page-writer** on **2026-05-06**.*
- [PMID:25024180](../papers/25024180.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:28927585](../papers/28927585.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
