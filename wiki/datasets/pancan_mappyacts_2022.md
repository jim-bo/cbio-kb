---
name: "MAPPYACTS Pan-Pediatric Precision Oncology Trial (Europe, Nat Med 2022)"
studyId: pancan_mappyacts_2022
institution: "Institut Curie / Gustave Roussy / European multicenter (France, Italy, Ireland, Spain)"
size: 787
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - cfdna-wes
panels: []
tags:
  - pediatric-oncology
  - precision-medicine
  - pan-cancer
  - actionability
  - cfDNA
  - relapsed-refractory
  - germline
processed_by: crosslinker
processed_at: 2026-05-21
---

# MAPPYACTS Pan-Pediatric Precision Oncology Trial (Europe, Nat Med 2022)

## Overview

`pancan_mappyacts_2022` is the genomic dataset from MAPPYACTS (NCT02613962), a European prospective precision-medicine trial that performed on-purpose tumor sampling plus paired tumor/germline whole-exome sequencing (WES) and RNA-seq in pediatric and young-adult patients with recurrent/refractory malignancies across France, Italy, Ireland, and Spain (February 2016 – July 2020). Data are also deposited at EGA under accession `EGAS00001005935`. The study was the genomic backbone for the AcSé-ESMART platform trial (NCT02813135).

## Composition

- **n = 787** patients consented, 774 underwent ≥1 procedure (833 procedures total); median age 11.6 years (range 0.5–38.5); 59% male.
- **Successful sequencing:** 624 patients (91% WES success, 90% RNA-seq success); 547 WES+RNA-seq, 81 WES only, 2 RNA-seq+panel, others.
- **Tumor distribution (n=774):** sarcomas 37%, CNS tumors 28%, other solid tumors 23%, leukemia 7%, lymphoma 4%.
- **Cancer types:** [RMS](../cancer_types/RMS.md) ([ARMS](../cancer_types/ARMS.md)/[ERMS](../cancer_types/ERMS.md)), osteosarcoma [OS](../cancer_types/OS.md), Ewing sarcoma [ES](../cancer_types/ES.md), [DSRCT](../cancer_types/DSRCT.md), [MPNST](../cancer_types/MPNST.md), [NBL](../cancer_types/NBL.md), [HGGNOS](../cancer_types/HGGNOS.md), [LGGNOS](../cancer_types/LGGNOS.md), [MBL](../cancer_types/MBL.md), [EPM](../cancer_types/EPM.md), [ATRT](../cancer_types/ATRT.md), [ALCL](../cancer_types/ALCL.md), B-ALL, T-ALL, [AML](../cancer_types/AML.md), and others.
- **Actionable yield:** 69% of patients (432/624) with at least one potentially actionable alteration; 10% of those (44/432) had a "ready-for-routine-use" alteration.
- **cfDNA ancillary arm:** plasma WES at 100× in 234 extracerebral solid-tumor patients; 76% of tumor actionable SNVs also detected in plasma.

## Assays / panels (linked)

- [Whole-exome sequencing (WES)](../methods/whole-exome-seq.md) — paired tumor/germline; Agilent SureSelect / Twist Human Core Exome; 100× mean depth; hg19/GRCh37. SNVs/indels called with GATK3 + samtools + Varscan.
- [RNA-seq](../methods/rna-seq.md) — TruSeq Stranded mRNA; fusion calling via in-house metacaller.
- [cfDNA-WES](../methods/cfdna-wes.md) — plasma whole-exome sequencing at 100× in the ancillary liquid biopsy arm.

## Papers using this cohort

- [PMID:35292802](../papers/35292802.md) — Gröbner et al. / Berlanga et al., *Nature Medicine* 2022: Primary MAPPYACTS report; 787 patients enrolled; 69% actionable; 30% received matched targeted therapy; overall ORR 17% (38% for ready-for-routine-use alterations); cfDNA WES recovered 76% of tumor actionable SNVs. [PMID:35292802](../papers/35292802.md)

## Notable findings derived from this cohort

- 69% (432/624) of patients harbored at least one potentially actionable alteration; 10% (44 patients) had a "ready-for-routine-use" alteration — predominantly fusions in [ALK](../genes/ALK.md), [BRAF](../genes/BRAF.md), [NTRK1/2/3](../genes/NTRK1.md), [ROS1](../genes/ROS1.md), [RET](../genes/RET.md), and [COL1A1](../genes/COL1A1.md)/[PDGFB](../genes/PDGFB.md) [PMID:35292802](../papers/35292802.md).
- 30% (107/356) of patients with ≥12 months follow-up received ≥1 matched targeted therapy; overall ORR was 17%, rising to 38% for ready-for-routine-use alterations and 56% globally (including pre-MAPPYACTS matches) [PMID:35292802](../papers/35292802.md).
- Most-recommended drug classes: [WEE1](../genes/WEE1.md) inhibitors (n=150), mTOR (n=123), CDK4/6 (n=105), MEK (n=95), PARP (n=64) [PMID:35292802](../papers/35292802.md).
- [TP53](../genes/TP53.md) was the most frequently altered gene (215 deleterious events); [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) deletions/inactivating events in 157 cases; RAS family ([KRAS](../genes/KRAS.md)/[NRAS](../genes/NRAS.md)/[HRAS](../genes/HRAS.md)) in 42 cases [PMID:35292802](../papers/35292802.md).
- Median TMB was 0.6 mut/Mb; 7 patients had TMB >10 mut/Mb, including 3 with probable constitutional mismatch repair deficiency (CMMRD) involving [MSH2](../genes/MSH2.md), [MLH1](../genes/MLH1.md), or [MSH6](../genes/MSH6.md) [PMID:35292802](../papers/35292802.md).
- 42% of ready-for-routine-use alterations had been previously unknown to the patient's clinical workup, underscoring the value of comprehensive genomic profiling at relapse [PMID:35292802](../papers/35292802.md).
- 7%–12% of patients harbored germline cancer-predisposition findings; genetic counseling recommended for 51/674 patients (7.6%) [PMID:35292802](../papers/35292802.md).

## Sources

- cBioPortal study `pancan_mappyacts_2022`.
- EGA accession `EGAS00001005935`.
- MAPPYACTS trial NCT02613962; AcSé-ESMART platform NCT02813135.
- Berlanga P, et al. *Identification of Rare Actionable Mutations and Genomic Alterations in Pediatric Patients with Relapsed or Refractory Cancer in France.* Nat Med. 2022. [PMID:35292802](../papers/35292802.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
