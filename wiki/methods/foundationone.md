---
name: FoundationOne
slug: foundationone
kind: method
canonical_source: cbioportal
unverified: false
tags:
  - sequencing-panel
  - targeted-dna-seq
  - clinical-sequencing
  - tumor-only
processed_by: wiki-cli
processed_at: 2026-05-21
---

# FoundationOne

## Overview

FoundationOne is a commercially available, FDA-approved comprehensive genomic profiling (CGP) assay developed by Foundation Medicine. It performs targeted hybrid-capture DNA sequencing of all coding exons of ≥300 cancer-relevant genes, detecting substitutions, insertion/deletions, copy-number alterations, and selected fusions/rearrangements from routine formalin-fixed paraffin-embedded (FFPE) tumor tissue. FoundationOne is typically deployed as a tumor-only (unmatched) assay; germline variants cannot be reliably distinguished from somatic variants without a paired normal. The assay also reports tumor mutational burden (TMB) and microsatellite instability (MSI) status. It is listed in the cBioPortal gene-panels ontology under the canonical `genePanelId` "FoundationOne".

## Used by

- Used for tumor-only sequencing of 167 of 1,004 adult glioma tumors in the 923-patient MSK glioma prospective cohort ([glioma_mskcc_2019](../datasets/glioma_mskcc_2019.md)); tumor-only design precludes germline analysis for this subset, biasing the germline-variant prevalence denominator to the 837 MSK-IMPACT paired samples [PMID:31263031](../papers/31263031.md)
- Applied to 730 R/M [ACC](../cancer_types/ACC.md) cases at median exon coverage >×500; constituted the largest single platform in the 1,045-case integrated [ACC](../cancer_types/ACC.md) genomic study, enabling discovery of [NOTCH1](../genes/NOTCH1.md) enrichment (26.3% R/M) and chromatin-remodeling alterations [PMID:31483290](../papers/31483290.md).
- FoundationOne Heme hybrid-capture panel (465 genes, median 704× coverage, plus RNA-seq of 333 rearrangement genes) used for tumor-only profiling of 7,494 sarcoma samples across 44 histologies; reads aligned to hg19 via BWA v0.5.9 [PMID:35705558](../papers/35705558.md)
- Used for targeted NGS of 34 of 166 colitis-associated cancer (CAC) tumors (315-gene panel); combined with MSK-IMPACT for the overall genomic landscape study of IBD-associated colorectal neoplasia [PMID:36611031](../papers/36611031.md)

## Notes

- Tumor-only sequencing means paired germline analysis is not possible; reported somatic variants may include germline variants of uncertain significance.
- Canonical `genePanelId` in cBioPortal: `FoundationOne`.
- Coverage spans coding exons of ≥300 genes; also reports TMB (mut/Mb) and MSI status from the targeted capture data.
- Complementary to MSK-IMPACT (paired tumor-normal) in multi-institutional sequencing cohorts; FoundationOne samples in those settings are often limited to actionability analysis rather than germline studies.

## Sources

- [PMID:31263031](../papers/31263031.md) — Jonsson et al. used FoundationOne (tumor-only, n=167) alongside MSK-IMPACT (paired, n=837) in 923 adult glioma patients; FoundationOne samples excluded from germline analysis.

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31483290](../papers/31483290.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705558](../papers/35705558.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:36611031](../papers/36611031.md)

*This page was processed by **wiki-cli** on **2026-05-21**.*
