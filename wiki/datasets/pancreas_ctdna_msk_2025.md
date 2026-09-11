---
name: Pancreatic Cancer cfDNA (MSK, J Natl Cancer Inst 2025)
studyId: pancreas_ctdna_msk_2025
institution: Memorial Sloan Kettering Cancer Center (MSK)
size: 412
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - ctdna-seq
  - targeted-dna-seq
panels:
  - msk-impact-panel
tags:
  - pancreatic-cancer
  - PAAD
  - ctDNA
  - liquid-biopsy
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Pancreatic Cancer cfDNA (MSK, J Natl Cancer Inst 2025)

## Overview

414 patients with pancreatic ductal adenocarcinoma ([PAAD](../cancer_types/PAAD.md)) who had ≥1 plasma sample sequenced with the 129-gene MSK-ACCESS ctDNA assay at Memorial Sloan Kettering between August 2019 and July 2022, with paired MSK-IMPACT tissue sequencing available in a subset. Name, institution, size (412) and reference genome (hg19) are taken from the cBioPortal study record in `schema/ontology/studies.json`; the portal's 412-sample count is close to but does not exactly match the paper's 414-patient cohort [PMID:40511613](../papers/40511613.md).

## Composition

- 414 patients, ≥1 ctDNA sample each: stage I–II n=115 (28%), stage III n=88 (21%), stage IV n=211 (51%) at time of ctDNA testing [PMID:40511613](../papers/40511613.md).
- 55% (n=227) had received treatment before ctDNA testing; 44% (n=187) were treatment-naive [PMID:40511613](../papers/40511613.md).
- Tissue–ctDNA matched-pair subcohorts: untreated stage I–III with matched tissue (29/68), untreated stage IV with matched tissue (62/120); 131 matched pairs total [PMID:40511613](../papers/40511613.md).

## Assays / panels (linked)

- [MSK-ACCESS](../methods/ACCESS129.md), a 129-gene hybridization-capture deep-sequencing ctDNA assay with matched buffy-coat germline filtering [PMID:40511613](../papers/40511613.md).
- Matched tissue via [MSK-IMPACT](../methods/msk-impact-panel.md) ([IMPACT468](../methods/IMPACT468.md)/[IMPACT505](../methods/IMPACT505.md)) [PMID:40511613](../papers/40511613.md).

## Papers using this cohort

- [PMID:40511613](../papers/40511613.md) — Keane, O'Reilly et al. (MSK), source publication: characterizes ctDNA detection rates by stage and disease burden, and tissue–ctDNA concordance.

## Notable findings derived from this cohort

- ctDNA was detected in 56% of patients overall, rising with stage (34% stage I–II, 38% stage III, 75% stage IV); in stage IV, detection was higher with liver metastases (82% vs 52%, P<.001) and ≥2 organs involved (76% vs 38%, P=.025) [PMID:40511613](../papers/40511613.md).
- In untreated stage IV patients with matched tissue (n=62), ctDNA–tissue critical success index was 93.1% for *[KRAS](../genes/KRAS.md)*, 84.3% for *[TP53](../genes/TP53.md)*, 89.5% for *[CDKN2A](../genes/CDKN2A.md)* and 63.6% for *[SMAD4](../genes/SMAD4.md)*, but agreement was much lower in untreated stage I–III disease (KRAS CSI 39.3%, n=29) [PMID:40511613](../papers/40511613.md).

## Sources

- cBioPortal study record: `pancreas_ctdna_msk_2025` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:40511613](../papers/40511613.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
