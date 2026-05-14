---
name: METABRIC Breast Cancer (brca_metabric)
studyId: brca_metabric
institution: Molecular Taxonomy of Breast Cancer International Consortium (METABRIC); UK and Canada tumour banks
size: 1992
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels: []
tags:
  - breast cancer
  - integrative clustering
  - copy number
  - expression
processed_by: crosslinker
processed_at: 2026-05-14
---

# METABRIC Breast Cancer (brca_metabric)

## Overview

METABRIC (Molecular Taxonomy of Breast Cancer International Consortium) is a large-scale integrative genomic study of primary breast tumours from UK and Canadian tumour banks. The dataset comprises a discovery cohort of 997 tumours and an independent validation cohort of 995 tumours (total n = 1,992). Genomic profiling used Affymetrix SNP 6.0 arrays for copy-number and SNP genotyping; transcriptomic profiling used Illumina HT-12 v3 expression arrays. [TP53](../genes/TP53.md) mutational status was assessed on a subset. Data are deposited at the European Genome-Phenome Archive (EGAS00000000083).

## Composition

- Discovery cohort: 997 primary breast tumours
- Validation cohort: 995 primary breast tumours (total n = 1,992)
- Cancer type: [BRCA](../cancer_types/BRCA.md)
- ER-positive/LN-negative patients did not receive chemotherapy; ER-negative/LN-positive patients did; no HER2+ patients received [trastuzumab](../drugs/trastuzumab.md) during this study period

## Assays / panels (linked)

- [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md)
- [Illumina gene-expression microarray](../methods/illumina-microarray.md)

## Papers using this cohort

- [PMID:22522925](../papers/22522925.md)

## Notable findings derived from this cohort

- Joint integrative clustering of CNA and expression data identified 10 integrative clusters (IntClust 1-10) with distinct copy-number profiles and clinical outcomes, validated in the independent 995-tumour cohort [PMID:22522925](../papers/22522925.md)
- IntClust 5 (ERBB2-amplified, n = 94) showed the worst disease-specific survival at 5 and 15 years (discovery HR 3.899, 95% CI 2.234-6.804) [PMID:22522925](../papers/22522925.md)
- IntClust 2 (11q13/14 cis-acting, ER-positive, n = 45) was a high-risk subgroup driven by [CCND1](../genes/CCND1.md), [EMSY](../genes/EMSY.md), [PAK1](../genes/PAK1.md), and [RSF1](../genes/RSF1.md) amplifications (discovery HR 3.620, 95% CI 1.905-6.878) [PMID:22522925](../papers/22522925.md)
- IntClust 4 (CNA-devoid, n = 167) had favourable prognosis and was enriched for lymphocytic infiltration and adaptive immune response signatures [PMID:22522925](../papers/22522925.md)
- Germline variants and somatic CNAs influenced expression of >39% (11,198/28,609) of expression probes genome-wide [PMID:22522925](../papers/22522925.md)
- Used as an external reference cohort for cross-species transcriptome comparison; 10.5% TP53/PIK3CA co-mutation rate cited to contextualize rat CRISPR model findings [PMID:26437033](../papers/26437033.md)
- Served as the validation cohort for the three [ILC](../cancer_types/ILC.md) transcriptional subtypes (reactive-like, immune-related, proliferative); reactive-like ILC had better DSS (HR=0.47, p=0.038) and [OS](../cancer_types/OS.md) (HR=0.50, p=0.023) than proliferative ILC [PMID:26451490](../papers/26451490.md)

## Sources

- [PMID:22522925](../papers/22522925.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26437033](../papers/26437033.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
