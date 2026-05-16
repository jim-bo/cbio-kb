---
name: MSK NTRK Fusion Clinical Cohort (2019)
studyId: ntrk_msk_2019
institution: Memorial Sloan Kettering Cancer Center (MSKCC)
size: 76
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-seq
  - rna-fusion-panel
  - fish
  - immunohistochemistry
panels:
  - msk-impact-panel
  - msk-fusion
tags:
  - NTRK
  - TRK-fusion
  - pan-cancer
  - fusion
  - larotrectinib
  - clonal-hematopoiesis
  - MSK-IMPACT
  - tumor-agnostic
  - TMB
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK NTRK Fusion Clinical Cohort (2019)

## Overview

This prospective real-world cohort captures all TRK fusion-positive cancers identified through the center-wide sequencing program at Memorial Sloan Kettering Cancer Center from April 7, 2015 through August 15, 2018. From a denominator of 26,312 prospectively sequenced patients, 76 confirmed TRK fusion-positive cases were identified (0.28% overall prevalence). Tumors were identified by DNA-based MSK-IMPACT (versions 1–3, 310–468 genes) and/or RNA-based MSK-Fusion anchored multiplex PCR, enabling an assessment of the complementarity of DNA and RNA assays for fusion detection. The cohort spans 17 cancer types and 48 unique rearrangements, making it the largest real-world TRK fusion series at publication.

## Composition

- **TRK fusion-positive patients:** 76 (from 26,312 prospectively sequenced patients; 0.28% prevalence)
- **Cancer types (n≥4):** salivary carcinoma / [MASC](../cancer_types/MASC.md) n=12 (15.8%), thyroid n=10 (13.2%), sarcoma NOS n=9 (11.8%), colon n=8 (10.5%), lung n=6 (7.9%), melanoma n=5 (6.6%), glioblastoma n=4 (5.3%), pancreatic n=4 (5.3%); plus uterine sarcoma, infantile fibrosarcoma, breast, biliary, appendiceal, and others
- **Enrollment window:** April 7, 2015 – August 15, 2018
- **Advanced-disease subset:** 51 patients who progressed to advanced disease with outcomes data

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — DNA-based panel, versions 1/310, 2/410, 3/468 genes; MSK-IMPACT v3 added intronic tiling of [NTRK1](../genes/NTRK1.md) introns 3, 7, 8, 9, 10, 11, 12 and [NTRK2](../genes/NTRK2.md) intron 15, plus [ETV6](../genes/ETV6.md) introns 4–5
- [msk-fusion](../methods/msk-fusion.md) — RNA-based anchored multiplex PCR ([ArcherDx FusionPlex](../methods/archer-fusionplex.md)) for fusion detection
- [fish](../methods/fish.md) — ETV6 break-apart FISH accepted as inferred TRK evidence in secretory carcinoma
- [immunohistochemistry](../methods/immunohistochemistry.md) — pan-TRK IHC in [select](../methods/select.md) cases for confirmation

## Papers using this cohort

- [PMID:31871300](../papers/31871300.md) — Rosen et al. 2019, genomic landscape and clinical outcomes of TRK fusion-positive cancers at MSK

## Notable findings derived from this cohort

- Overall TRK fusion prevalence was 0.28% (74/26,312); highest in salivary cancers (5.29%) and thyroid (2.22%); 0 of >1,561 prostate cancers were TRK fusion-positive. [PMID:31871300](../papers/31871300.md)
- 26% (12/46) of true fusions tested by both DNA and RNA were missed by DNA alone — driven by NTRK2/3 introns too large for MSK-IMPACT to tile — establishing the need for reflex RNA testing. [PMID:31871300](../papers/31871300.md)
- TRK fusion-positive tumors were profoundly depleted of concurrent MAPK-pathway driver alterations: 1.5% vs 31.4% in TRK-negative cases (p<0.001); median TMB was 1.8 vs 3.5 mut/Mb (p<0.001). [PMID:31871300](../papers/31871300.md)
- 6/7 (86%) of TRK fusion-positive colorectal tumors were MSI-H, consistent with kinase-fusion enrichment in hypermethylated/MMR-deficient CRC; no non-CRC TRK fusion-positive case was MSI-H. [PMID:31871300](../papers/31871300.md)
- Among 51 patients with advanced disease, chemotherapy ORR was 62.5% across all lines; TRK inhibitor ORR was 64.7% (23/34); checkpoint-inhibitor response was observed in only 1/12 patients (the single MSI-H CRC patient, a CR lasting 3.5 years). [PMID:31871300](../papers/31871300.md)
- Longitudinal profiling in 17 patients showed TRK fusion present at all timepoints in 82% (14/17); one glioblastoma lost the TPM3-NTRK1 fusion at progression on a brain-penetrant TRK inhibitor while acquiring focal [EGFR](../genes/EGFR.md) amplification (19.6×). [PMID:31871300](../papers/31871300.md)

## Sources

- cBioPortal study: `ntrk_msk_2019`
- Primary publication: [PMID:31871300](../papers/31871300.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
