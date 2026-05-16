---
name: "Colorectal Cancer in Nigerian Patients (ARGO/MSKCC, 2020)"
studyId: crc_nigerian_2020
institution: "African Research Group for Oncology (ARGO); Obafemi Awolowo University / MSKCC"
size: 64
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - rrbs
  - immunohistochemistry
panels:
  - msk-impact-panel
tags:
  - colorectal-cancer
  - west-africa
  - global-oncology
  - microsatellite-instability
  - health-disparities
  - lynch-syndrome
  - msk-impact
processed_by: crosslinker
processed_at: 2026-05-16
---

# Colorectal Cancer in Nigerian Patients (ARGO/MSKCC, 2020)

## Overview

Prospective cohort of 64 Nigerian colorectal cancer ([COAD](../cancer_types/COAD.md)/[READ](../cancer_types/READ.md)) specimens collected through the African Research Group for Oncology (ARGO), spanning 12 Nigerian tertiary care facilities affiliated with Obafemi Awolowo University. Patients were enrolled April 2013–November 2018. Tumors underwent [MSK-IMPACT](../methods/msk-impact-panel.md) paired tumor-normal targeted sequencing, with a subset profiled by genome-wide DNA methylation ([RRBS](../methods/rrbs.md)) and MMR protein [IHC](../methods/immunohistochemistry.md). The dataset was deposited in cBioPortal to enable race-stratified molecular comparisons against MSKCC and TCGA colorectal cohorts. [PMID:34819518](../papers/34819518.md)

## Composition

- 64 Nigerian [COADREAD](../cancer_types/COADREAD.md) specimens profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) paired tumor-normal sequencing. [PMID:34819518](../papers/34819518.md)
- 94 Nigerian tumors with MMR protein IHC ([MLH1](../genes/MLH1.md), [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md), [PMS2](../genes/PMS2.md)). [PMID:34819518](../papers/34819518.md)
- 25 of the 64 MSK-IMPACT specimens also had genome-wide DNA methylation by [RRBS](../methods/rrbs.md). [PMID:34819518](../papers/34819518.md)
- Median patient age 55.8 years; 50.8% rectal, 53.8% stage IV at presentation. [PMID:34819518](../papers/34819518.md)
- 100% of specimens genetically determined to be of African ancestry by ADMIXTURE v1.3 against 1000 Genomes references. [PMID:34819518](../papers/34819518.md)
- Clinical comparator: 1,145 MSKCC [COADREAD](../cancer_types/COADREAD.md) MSK-IMPACT specimens (April 2014–September 2016). [PMID:34819518](../papers/34819518.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — paired tumor-normal targeted NGS on all 64 specimens.
- [Immunohistochemistry](../methods/immunohistochemistry.md) — MMR protein panel (MLH1, MSH2, MSH6, PMS2) on 94 specimens.
- [RRBS](../methods/rrbs.md) — Zymo Methyl-MiniSeq genome-wide DNA methylation on 25 specimens.
- [MSIsensor](../methods/msisensor.md) — microsatellite instability scoring.
- [ADMIXTURE](../methods/admixture.md) — global ancestry estimation.

## Papers using this cohort

- [PMID:34819518](../papers/34819518.md) — Alatise et al. (2021) — primary study describing race-stratified molecular profiling of Nigerian vs. MSKCC CRC.

## Notable findings derived from this cohort

- 28.1% (18/64) of Nigerian tumors were MSI-H by [MSIsensor](../methods/msisensor.md), vs. 14.2% TCGA and 8.5% MSKCC (P<0.001); among MSI-H cases, [BRAF](../genes/BRAF.md) V600E was absent and [KRAS](../genes/KRAS.md) mutations trended higher (61.1% vs. 41.1%) compared to MSKCC MSI-H. [PMID:34819518](../papers/34819518.md)
- Only 28.6% of Nigerian MSI-H tumors showed [MLH1](../genes/MLH1.md) hypermethylation and only 8% were CIMP-H — substantially lower than predominant somatic MSI mechanism in high-income country cohorts; 16.7% (3/18) of Nigerian MSI-H patients carried germline Lynch syndrome MMR mutations. [PMID:34819518](../papers/34819518.md)
- In microsatellite-stable tumors, [APC](../genes/APC.md) was depleted in Nigeria (36.9% vs. 76.0%, P<0.01) and overall WNT-pathway alteration was 47.8% vs. 81.9% (P<0.001); RAS-pathway alteration was enriched (76.1% vs. 59.6%, P=0.03); [PIK3R1](../genes/PIK3R1.md) (8.7% vs. 2.2%, P=0.02) and [PIK3CB](../genes/PIK3CB.md) (4.3% vs. 0.5%, P=0.04) were enriched. [PMID:34819518](../papers/34819518.md)

## Sources

- cBioPortal study: `crc_nigerian_2020`
- Primary publication: [PMID:34819518](../papers/34819518.md) · DOI: 10.1038/s41467-021-27106-w · *Nature Communications* (2021)

*This page was processed by **crosslinker** on **2026-05-16**.*
