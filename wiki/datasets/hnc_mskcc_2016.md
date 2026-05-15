---
name: Recurrent and Metastatic Head & Neck Cancer (MSK, JAMA Oncol 2016)
studyId: hnc_mskcc_2016
institution: Memorial Sloan Kettering Cancer Center
size: 151
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - IMPACT410
tags:
  - head-and-neck-cancer
  - recurrent-metastatic
  - MSK-IMPACT
  - HPV-positive
  - HPV-negative
  - TERT-promoter
  - precision-oncology
  - rare-cancers
  - basket-trials
processed_by: crosslinker
processed_at: 2026-05-14
---

# Recurrent and Metastatic Head & Neck Cancer (MSK, JAMA Oncol 2016)

## Overview

Morris et al. assembled this cohort of 151 patients with advanced, treatment-resistant head and neck tumors who underwent clinical-grade genomic profiling at Memorial Sloan Kettering Cancer Center between January 2014 and July 2015, under IRB protocol NCT01775072. All samples were sequenced with the CLIA-approved [MSK-IMPACT 410-gene panel](../methods/IMPACT410.md), enabling genome-wide copy number analysis and paired matched normal sequencing. The study represents the first large clinical-grade molecular landscape of recurrent and metastatic head and neck cancers and is publicly available on cBioPortal.

## Composition

- **N = 151 patients** (95 men, 56 women; mean age 61.8 years, range 17–100).
- **Disease distribution:** 53 [HNSC](../cancer_types/HNSC.md), 56 salivary carcinomas (36 [ACYC](../cancer_types/ACYC.md) plus 20 other salivary types), 27 cutaneous carcinomas (21 [CSCC](../cancer_types/CSCC.md), 4 [BCC](../cancer_types/BCC.md), 2 skin adnexal), 8 [NPC](../cancer_types/NPC.md), 3 [HNNE](../cancer_types/HNNE.md), 2 odontogenic carcinomas, 2 olfactory neuroblastomas ([ONBL](../cancer_types/ONBL.md)).
- **Site distribution:** 66 patients with locoregional recurrence, 106 with distant metastases, 6 with locally advanced surgically unresectable tumors.
- Enrollment: January 2014 – July 2015 (224 enrolled total; 151 with ≥6-month follow-up).
- Reference genome: hg19.

## Assays / panels (linked)

- [IMPACT410](../methods/IMPACT410.md) — MSK-IMPACT targeted NGS of 410 cancer-relevant genes; median coverage 600× (range 82×–1165×); CLIA-approved; with matched normal DNA.
- [FACETS](../methods/facets.md) — allele-specific copy number and clonality analysis.
- [mutational-signatures](../methods/mutational-signatures.md) — APOBEC, tobacco, and UV-light signature decomposition.

## Papers using this cohort

- [PMID:27442865](../papers/27442865.md) — Morris et al., "The Molecular Landscape of Recurrent and Metastatic Head and Neck Cancers: Insights From a Precision Oncology Sequencing Platform," *JAMA Oncology* 2017. (Defining study for this cohort.)

## Notable findings derived from this cohort

- NGS guided therapy in **21/151 patients (14%)** overall and **13/53 (25%)** of [HNSC](../cancer_types/HNSC.md) patients; 28/135 (21%) harbored potentially actionable alterations. [PMID:27442865](../papers/27442865.md)
- [TERT](../genes/TERT.md) promoter mutations identified in 53% of HPV-negative [HNSC](../cancer_types/HNSC.md), 52% of [CSCC](../cancer_types/CSCC.md), 75% of [BCC](../cancer_types/BCC.md), and 14% of [ACYC](../cancer_types/ACYC.md) — the first report of [TERT](../genes/TERT.md) promoter mutations in salivary cancers; zero in HPV-positive HNSC. [PMID:27442865](../papers/27442865.md)
- [NOTCH1](../genes/NOTCH1.md) activating mutations or amplifications enriched in recurrent/metastatic [ACYC](../cancer_types/ACYC.md) (8/36, 22.2%; OR 8.3 vs primary [ACYC](../cancer_types/ACYC.md); P=.005), with recurrent truncating events at serine 2467 nominating γ-secretase inhibitors. [PMID:27442865](../papers/27442865.md)
- 43% of advanced HPV-positive [HNSC](../cancer_types/HNSC.md) tumors acquired an "HPV-negative-like" genotype enriched for [TP53](../genes/TP53.md) mutation, whole-genome duplication, and 3p deletion; these tumors trended toward worse survival (HR 2.3; P=.19). [PMID:27442865](../papers/27442865.md)
- [ETV6](../genes/ETV6.md)-[NTRK3](../genes/NTRK3.md) fusions reclassified 2 acinic cell carcinomas as [MASC](../cancer_types/MASC.md); both patients had major or near-complete responses on a TRK inhibitor basket trial. [PMID:27442865](../papers/27442865.md)
- Mismatch repair gene mutations ([MLH1](../genes/MLH1.md) truncating, [MSH2](../genes/MSH2.md)/[MSH6](../genes/MSH6.md)/[POLD1](../genes/POLD1.md) missense) in 4 tumors associated with markedly elevated mutation counts (17.3 vs 4.5; P<.001). [PMID:27442865](../papers/27442865.md)

## Sources

- cBioPortal study ID: `hnc_mskcc_2016`
- DOI: 10.1001/jamaoncol.2016.1790
- IRB protocol: NCT01775072
- Reference genome: hg19

*This page was processed by **crosslinker** on **2026-05-14**.*
