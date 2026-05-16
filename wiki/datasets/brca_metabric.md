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
processed_by: wiki-cli
processed_at: 2026-05-16
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
- [PMID:27161491](../papers/27161491.md) — Pereira et al. 2016, *Nature Communications*: targeted sequencing of 173 genes in 2,433 primary METABRIC tumors; primary expanded-driver characterization study.
- [PMID:30867590](../papers/30867590.md) — Rueda et al. 2019, *Nature*: multistate Markov model of breast cancer recurrence applied to METABRIC (1,980 patients with molecular data); characterizes long-term relapse trajectories by IntClust subtype.

## Notable findings derived from this cohort

- Joint integrative clustering of CNA and expression data identified 10 integrative clusters (IntClust 1-10) with distinct copy-number profiles and clinical outcomes, validated in the independent 995-tumour cohort [PMID:22522925](../papers/22522925.md)
- IntClust 5 (ERBB2-amplified, n = 94) showed the worst disease-specific survival at 5 and 15 years (discovery HR 3.899, 95% CI 2.234-6.804) [PMID:22522925](../papers/22522925.md)
- IntClust 2 (11q13/14 cis-acting, ER-positive, n = 45) was a high-risk subgroup driven by [CCND1](../genes/CCND1.md), [EMSY](../genes/EMSY.md), [PAK1](../genes/PAK1.md), and [RSF1](../genes/RSF1.md) amplifications (discovery HR 3.620, 95% CI 1.905-6.878) [PMID:22522925](../papers/22522925.md)
- IntClust 4 (CNA-devoid, n = 167) had favourable prognosis and was enriched for lymphocytic infiltration and adaptive immune response signatures [PMID:22522925](../papers/22522925.md)
- Germline variants and somatic CNAs influenced expression of >39% (11,198/28,609) of expression probes genome-wide [PMID:22522925](../papers/22522925.md)
- Used as an external reference cohort for cross-species transcriptome comparison; 10.5% TP53/PIK3CA co-mutation rate cited to contextualize rat CRISPR model findings [PMID:26437033](../papers/26437033.md)
- Served as the validation cohort for the three [ILC](../cancer_types/ILC.md) transcriptional subtypes (reactive-like, immune-related, proliferative); reactive-like [ILC](../cancer_types/ILC.md) had better DSS (HR=0.47, p=0.038) and [OS](../cancer_types/OS.md) (HR=0.50, p=0.023) than proliferative [ILC](../cancer_types/ILC.md) [PMID:26451490](../papers/26451490.md)
- Targeted sequencing of 173 genes in 2,433 METABRIC tumors (+ 650 normals) identified 40 Mut-driver genes; PIK3CA (40.1%), TP53 (35.4%), KMT2C (11.4%), GATA3 (11.1%) dominated; 45.2% of all tumours carried an Akt-pathway functional mutation. [PMID:27161491](../papers/27161491.md)
- PIK3CA mutations carried distinct prognostic value by IntClust background: shorter BCSS specifically in ER+ IntClust1 (17q23-amp), IntClust2 (11q13–14-amp), and IntClust9 (8q24-amp), resolving contradictory prior PIK3CA literature. [PMID:27161491](../papers/27161491.md)
- 22.6% of all tumours harboured mutations in chromatin-function Mut-drivers ([KMT2C](../genes/KMT2C.md), [ARID1A](../genes/ARID1A.md), [NCOR1](../genes/NCOR1.md), [CTCF](../genes/CTCF.md), [KDM6A](../genes/KDM6A.md), [PBRM1](../genes/PBRM1.md), [TBL1XR1](../genes/TBL1XR1.md)). [PMID:27161491](../papers/27161491.md)
- High MATH (intra-tumour heterogeneity) scores associated with worse BCSS in ER+ (P=0.003) but not ER-; IntClust2 had paradoxically low MATH despite poor outcome, due to the [CCND1](../genes/CCND1.md)/[PAK1](../genes/PAK1.md) 11q13–14 co-amplification being a single early clonal event. [PMID:27161491](../papers/27161491.md)
- Rueda et al. applied a multistate Markov model to 1,980 METABRIC patients with copy-number and expression data, identifying four late-recurring ER+/HER2-negative IntClust subgroups (1, 2, 6, 9; 26% of ER+ cases) with 42–56% 20-year relapse probability, each defined by a characteristic copy-number driver; IntClust significantly improved late-relapse prediction (C-index +0.07, P=0.00011 at 10 years) beyond IHC and clinical covariates. [PMID:30867590](../papers/30867590.md)
- Used as outcome-validation comparator for NMF luminal subtype reassignment; METABRIC confirmed intermediate outcomes for PAM50-LumA samples reassigned to NMF LumB-I [PMID:33212010](../papers/33212010.md)

## Sources

- [PMID:22522925](../papers/22522925.md)
- [PMID:26437033](../papers/26437033.md)
- [PMID:26451490](../papers/26451490.md)
- [PMID:27161491](../papers/27161491.md)
- [PMID:30867590](../papers/30867590.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
- [PMID:33212010](../papers/33212010.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
