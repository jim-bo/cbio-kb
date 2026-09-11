---
name: Colorectal Cancer Radiation (MSK, 2024)
studyId: rectal_radiation_msk_2024
institution: Memorial Sloan Kettering Cancer Center (MSKCC)
size: 48
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - whole-exome-seq
panels:
  - msk-impact-panel
tags:
  - rectal-cancer
  - secondary-malignancy
  - radiation
  - prostate-cancer
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Colorectal Cancer Radiation (MSK, 2024)

## Overview

A single-institution case-control study at MSKCC of 64 men who developed rectal adenocarcinoma ([READ](../cancer_types/READ.md)) ≥5 years after radiotherapy for prostate cancer ([PRAD](../cancer_types/PRAD.md)) — termed secondary rectal cancer (SRC) — compared genomically and clinically against primary rectal cancer (PRC) patients treated at MSKCC from 1994–2022. Name, institution, size (48) and reference genome (hg19) are taken from the cBioPortal study record in `schema/ontology/studies.json`; the 48-sample portal count is inferred (not stated in the paper) to correspond to the 31 MSK-IMPACT + 17 WES secondary-tumor samples [PMID:40100215](../papers/40100215.md).

## Composition

- 64 secondary rectal cancer (SRC) patients (100% male, median age 78) identified from 498 patients with colorectal adenocarcinoma and a prostate-cancer history [PMID:40100215](../papers/40100215.md).
- Targeted sequencing: 31 SRC tumors vs. 541 PRC tumors (223 female, 318 male); whole-exome sequencing: 17 of the 31 SRC tumors (54.8%) vs. 28 PRC tumors [PMID:40100215](../papers/40100215.md).
- Clinical PRC control set: 843 patients with rectal cancer and no prostate-cancer/pelvic-RT history; 64 PRC patients 1:1 propensity-matched to SRC patients for outcome comparisons [PMID:40100215](../papers/40100215.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted sequencing ([IMPACT341](../methods/IMPACT341.md)–[IMPACT505](../methods/IMPACT505.md)) [PMID:40100215](../papers/40100215.md).
- [Whole-exome sequencing](../methods/whole-exome-seq.md) recapture (×150 tumor / ×70 normal depth) via the MSKCC [TEMPO](../methods/tempo.md) pipeline [PMID:40100215](../papers/40100215.md).

## Papers using this cohort

- [PMID:40100215](../papers/40100215.md) — MSKCC study, source publication: compares clinical outcomes and genomics of radiation-associated secondary rectal cancer vs. primary rectal cancer.

## Notable findings derived from this cohort

- Secondary rectal cancer patients were older (median 78 vs 55 years) with smaller, earlier-stage, more distal/anterior tumors, received neoadjuvant therapy less often, and had worse 5-year overall, disease-free, and distant recurrence-free survival than 1:1 propensity-matched primary rectal cancer patients; secondary status remained independently associated with worse DFS and DRFS (not OS) after adjusting for treatment [PMID:40100215](../papers/40100215.md).
- MSK-IMPACT sequencing showed lower tumor mutational burden, fewer *[APC](../genes/APC.md)*/Wnt-pathway alterations, and more *[SMAD4](../genes/SMAD4.md)* inactivation in secondary vs. primary rectal cancer; whole-exome sequencing showed more frameshift deletions, inframe deletions and splice-site variants in secondary tumors, with no COSMIC mutational-signature difference between groups [PMID:40100215](../papers/40100215.md).

## Sources

- cBioPortal study record: `rectal_radiation_msk_2024` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:40100215](../papers/40100215.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
