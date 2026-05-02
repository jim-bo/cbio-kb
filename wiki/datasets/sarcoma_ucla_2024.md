---
name: UCLA Sarcoma Patient-Derived Tumor Organoid Biobank (2024)
studyId: sarcoma_ucla_2024
institution: University of California, Los Angeles
size: 194
reference_genome: GRCh38
canonical_source: cbioportal
unverified: false
assays: [targeted-sequencing, whole-genome-seq, rna-seq, organoid-drug-screening]
panels: [DFCI-ONCOPANEL-3]
tags:
  - sarcoma
  - bone-sarcoma
  - soft-tissue-sarcoma
  - organoid
  - drug-screening
  - PDTO
  - functional-precision-medicine
processed_by: crosslinker
processed_at: 2026-04-30
---

# UCLA Sarcoma Patient-Derived Tumor Organoid Biobank (2024)

## Overview

UCLA biobank of 194 sarcoma specimens from 126 patients spanning 24 distinct bone and soft-tissue subtypes (February 2018–May 2022), combined with a high-throughput patient-derived tumor organoid (PDTO) "mini-ring" drug-screening platform returning drug-sensitivity profiles within one week. RNAseq, DNA panel sequencing, and single-agent screening data deposited at Synapse (PDTOSarcoma); panel-sequencing data also shared via cBioPortal as `sarcoma_ucla_2024` [PMID:39305899](../papers/39305899.md).

## Composition

- 194 sarcoma specimens from 126 patients; 11 biopsies, 183 surgical resections; 46% metastatic, 41% primary, 13% recurrent; 27 patients (21%) contributed multiple samples [PMID:39305899](../papers/39305899.md).
- Patient demographics: 50% adult, 35% adolescent/young adult (AYA), 13% pediatric; 62% male; 71% had prior systemic therapy [PMID:39305899](../papers/39305899.md).
- 24 distinct bone and soft-tissue sarcoma subtypes: [osteosarcoma](../cancer_types/OS.md) (73 specimens, 28 patients), [chordoma](../cancer_types/CHDM.md) (14, 10), [chondrosarcoma](../cancer_types/CHS.md) (13, 12), [leiomyosarcoma](../cancer_types/LMS.md) (12, 10), undifferentiated pleomorphic sarcoma (11, 10), [Ewing sarcoma](../cancer_types/ES.md), [synovial sarcoma](../cancer_types/SYNS.md), [MPNST](../cancer_types/MPNST.md), [rhabdomyosarcoma](../cancer_types/RMS.md) ([ARMS](../cancer_types/ARMS.md)/[ERMS](../cancer_types/ERMS.md)/[SCSRMS](../cancer_types/SCSRMS.md)), [epithelioid sarcoma](../cancer_types/EPIS.md), [DSRCT](../cancer_types/DSRCT.md), [PEComa](../cancer_types/PECOMA.md), [myxofibrosarcoma](../cancer_types/MFS.md), [WDLS](../cancer_types/WDLS.md), [DDCHS](../cancer_types/DDCHS.md), and CIC-rearranged sarcoma [PMID:39305899](../papers/39305899.md).
- Organoid take rate ~93%; 124 samples seeded; 92 specimens screened against ≥10 of >400 single agents and combinations [PMID:39305899](../papers/39305899.md).

## Assays / panels (linked)

- [PDTO mini-ring drug screen](../methods/organoid-drug-screening.md) — >400 compounds; viability via CellTiter-Glo at day 5 [PMID:39305899](../papers/39305899.md).
- [DFCI-ONCOPANEL-3](../methods/DFCI-ONCOPANEL-3.md) — targeted DNA panel sequencing at Brigham CAMD [PMID:39305899](../papers/39305899.md).
- [Whole-genome sequencing](../methods/whole-genome-seq.md) — BWA-MEM2, MuSE, Mutect2, SomaticSniper, Strelka2, Battenberg/ASCAT [PMID:39305899](../papers/39305899.md).
- [RNA-seq](../methods/rna-seq.md) — KAPA Hyper Prep, NovaSeq6000, STAR, aligned to GRCh38.108 [PMID:39305899](../papers/39305899.md).
- [FISH](../methods/fish.md) — [MDM2](../genes/MDM2.md) and NTRK1/2/3 (NeoGenomics) [PMID:39305899](../papers/39305899.md).

## Papers using this cohort

- [PMID:39305899](../papers/39305899.md) — Al Shihabi et al. 2024: Demonstrates PDTO drug-screening platform identifies ≥1 FDA-approved or NCCN-recommended effective regimen for 59% of sarcoma specimens; organoid responses to neoadjuvant MAP tracked post-resection necrosis and PFS in 3 osteosarcoma cases; motivates the prospective PREMOST trial (NCT06064682).

## Notable findings derived from this cohort

- 80.4% (74/92) of specimens screened against ≥10 compounds had ≥1 significant response (top 5% viability score); 59% of specimens and 58% of patients had ≥1 FDA-approved or NCCN-recommended top-five regimen [PMID:39305899](../papers/39305899.md).
- [Osteosarcoma](../cancer_types/OS.md) PDTOs significantly more sensitive than pan-sarcoma average to [ceralasertib](../drugs/ceralasertib.md) (p=0.00026), [topotecan](../drugs/topotecan.md) (p=0.028), [cabozantinib](../drugs/cabozantinib.md) (p=0.024), and [everolimus](../drugs/everolimus.md) (p=0.012) [PMID:39305899](../papers/39305899.md).
- [Chordoma](../cancer_types/CHDM.md) PDTOs preferentially sensitive to TAK-285 ([EGFR](../genes/EGFR.md)/[ERBB2](../genes/ERBB2.md) kinase inhibitor, p=0.034) and significantly less sensitive to [bortezomib](../drugs/bortezomib.md) (p=1.8×10⁻⁵) and [everolimus](../drugs/everolimus.md) (p=0.022) [PMID:39305899](../papers/39305899.md).
- [PIK3CA](../genes/PIK3CA.md) H1047L hotspot in SARC0117 (undifferentiated spindle cell sarcoma) drove broad PI3K/mTOR pathway sensitivity ([alpelisib](../drugs/alpelisib.md), apitolisib, copanlisib, BGT226, vistusertib) [PMID:39305899](../papers/39305899.md).
- PDTO-predicted [larotrectinib](../drugs/larotrectinib.md) resistance in SARC0127 correctly distinguished high-grade spindle cell/sclerosing [RMS](../cancer_types/RMS.md) ([SCSRMS](../cancer_types/SCSRMS.md)) from infantile fibrosarcoma ([ETV6](../genes/ETV6.md)–[NTRK3](../genes/NTRK3.md) fusion absent by FISH) within one week versus 18 days for pathology [PMID:39305899](../papers/39305899.md).
- Normalized organoid viability correlated with time-to-next-treatment in n=5 patients who received organoid-matched treatment (R²=0.921, p=0.009) [PMID:39305899](../papers/39305899.md).

## Sources

- cBioPortal study `sarcoma_ucla_2024`. Raw data also at Synapse (PDTOSarcoma). Al Shihabi A, et al. *Personalized chemo-sensitivity profiling of patient-derived sarcoma organoids for treatment guidance.* Nature Cancer. 2024. [PMID:39305899](../papers/39305899.md).

*This page was processed by **crosslinker** on **2026-04-30**.*
