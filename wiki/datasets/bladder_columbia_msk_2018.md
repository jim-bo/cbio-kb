---
name: Bladder Cancer (Columbia University/MSK, Cell 2018)
studyId: bladder_columbia_msk_2018
institution: Columbia University Medical Center / Memorial Sloan Kettering Cancer Center
size: 22
reference_genome: GRCh37/hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-sequencing
  - WES
  - RNA-seq
panels:
  - IMPACT468
tags:
  - bladder
  - urothelial
  - organoid
  - patient-derived
  - Columbia
  - MSK
  - BLCA
processed_by: crosslinker
processed_at: 2026-05-16
---

# Bladder Cancer (Columbia University/MSK, Cell 2018)

## Overview

Patient-derived bladder cancer organoid biobank established from 18 patients (17 urothelial carcinoma [BLCA](../cancer_types/BLCA.md), 1 bladder squamous cell carcinoma [BLSC](../cancer_types/BLSC.md)) undergoing transurethral resection (TUR) or nephroureterectomy at Columbia University Medical Center and Memorial Sloan Kettering Cancer Center. Sequencing data are available in cBioPortal as `bladder_columbia_msk_2018`. The biobank comprises 22 organoid lines (SCBO-1 through SCBO-16, with metachronous variants) established at ~70% efficiency; lines underwent serial passaging up to 26 passages, cryopreservation, and conversion to orthotopic xenografts at 83% efficiency (15/18). Reference genome: GRCh37/hg19 (BWA alignment, MuTect for SNVs, Pindel for indels). [PMID:29625057](../papers/29625057.md)

## Composition

- **Patients:** 18 total — 13 males / 5 females, ages 48–86 (median 72.7). [PMID:29625057](../papers/29625057.md)
- **Organoid lines:** 22 patient-derived lines; predominantly non-muscle-invasive disease (only ~4 muscle-invasive lines from TUR samples). [PMID:29625057](../papers/29625057.md)
- **Cancer types:** [BLCA](../cancer_types/BLCA.md) (17 patients), [BLSC](../cancer_types/BLSC.md) (1 patient); 2 patients contributed PDX lines from nephroureterectomy (upper-tract urothelial carcinoma [UTUC](../cancer_types/UTUC.md)) at MSK. [PMID:29625057](../papers/29625057.md)
- **Sequencing:** Targeted sequencing with [MSK-IMPACT](../methods/msk-impact-panel.md) 468-gene panel ([IMPACT468](../methods/IMPACT468.md)) at ~500× coverage; whole-exome sequencing on 24 samples from 5 lines (Agilent SureSelect V4, HiSeq 2500, ~240× on-target). [PMID:29625057](../papers/29625057.md)
- **Reference genome:** GRCh37/hg19 (BWA alignment, MuTect for SNVs, Pindel for indels <50 bp, VEP/vcf2maf annotation). [PMID:29625057](../papers/29625057.md)

## Assays / panels (linked)

- [IMPACT468](../methods/IMPACT468.md) (MSK-IMPACT 468-gene targeted sequencing)
- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md) (RNA-seq deposited GEO GSE103990)
- [organoid-drug-screening](../methods/organoid-drug-screening.md)

## Papers using this cohort

- [PMID:29625057](../papers/29625057.md) — Patient-derived bladder cancer organoids recapitulate the genomic landscape and drug responses of bladder cancer (Lee et al., Cell 2018)

## Notable findings derived from this cohort

- Epigenetic regulators ([ARID1A](../genes/ARID1A.md), [KMT2C](../genes/KMT2C.md), [KMT2D](../genes/KMT2D.md), [KDM6A](../genes/KDM6A.md)) mutated collectively in 73% (11/15) of non-recurrent lines; [FGFR3](../genes/FGFR3.md) activating mutations in 60% (9/15); [TP53](../genes/TP53.md) in 33% (5/15). [PMID:29625057](../papers/29625057.md)
- [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) fusion (exon 17–exon 11 junction) validated in SCBO-10 and its parental tumor; identical junction previously reported in glioblastoma GBM-021 and bladder cell line RT112. [PMID:29625057](../papers/29625057.md)
- 11 of the analyzed lines showed >80% mutational concordance with their parental tumor; only 4 lines showed <60% concordance, supporting organoid fidelity as preclinical models. [PMID:29625057](../papers/29625057.md)
- Luminal-to-basal phenotypic shift in 64% (14/22) of organoid lines is largely reversible in xenografts (88% revert to luminal) and recurs to basal in xenograft-derived organoids (100%), consistent with epigenetic plasticity. [PMID:29625057](../papers/29625057.md)
- [FGFR3](../genes/FGFR3.md) mutation alone insufficient to predict MEK/ERK-inhibitor response: 2 of 4 FGFR3-mutant lines responded to [trametinib](../drugs/trametinib.md)/SCH772984; 2 did not. No lines responded to any of three tested FGFR inhibitors in organoid culture. [PMID:29625057](../papers/29625057.md)
- [TSC1](../genes/TSC1.md) nonsense mutation in SCBO-6 conferred mTOR-inhibitor ([AZD8055](../drugs/azd8055.md)) sensitivity; additive benefit observed combining [erdafitinib](../drugs/erdafitinib.md) (JNJ-42756493) with [AZD8055](../drugs/azd8055.md) or [sirolimus](../drugs/sirolimus.md). [PMID:29625057](../papers/29625057.md)
- Metachronous organoid pair SCBO-3 vs SCBO-3.2 (post-BCG + [mitomycin-C](../drugs/mitomycin-c.md)) demonstrated markedly increased broad drug resistance after intravesical therapy, modeling treatment-resistance evolution. [PMID:29625057](../papers/29625057.md)
- APOBEC and smoking mutational signatures detected in organoid lines and stable across passages; SCBO-3/SCBO-3.2 TMB resembled low-grade NMIBC; SCBO-4/5/6 TMB resembled high-grade NMIBC/MIBC. [PMID:29625057](../papers/29625057.md)
- Orthotopic xenograft drug studies (NOG mice) confirmed in vitro responses: significant tumor reduction on ultrasound for [trametinib](../drugs/trametinib.md) (SCBO-6) and [gemcitabine](../drugs/gemcitabine.md) (SCBO-5), with decreased Ki67 ([trametinib](../drugs/trametinib.md)) and increased cleaved caspase-3 ([gemcitabine](../drugs/gemcitabine.md)) on histology. [PMID:29625057](../papers/29625057.md)

## Sources

- cBioPortal study: `bladder_columbia_msk_2018`
- [PMID:29625057](../papers/29625057.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
