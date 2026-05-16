---
name: MSK Lung Adenocarcinoma Resection Cohort (2020)
studyId: luad_mskcc_2020
institution: Memorial Sloan Kettering Cancer Center
size: 604
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - msk-impact-panel
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - lung-adenocarcinoma
  - resected-tumors
  - histologic-subtypes
  - whole-genome-doubling
  - apobec
  - recurrence
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Lung Adenocarcinoma Resection Cohort (2020)

## Overview

The luad_mskcc_2020 cohort comprises 604 patients with stage I–III lung adenocarcinoma ([LUAD](../cancer_types/LUAD.md)) who underwent complete surgical resection at Memorial Sloan Kettering Cancer Center and had targeted next-generation sequencing via the [MSK-IMPACT panel](../methods/msk-impact-panel.md) performed between February 2010 and December 2018. The cohort was stratified by predominant histologic subtype (lepidic [LEP], acinar/papillary [ACI/PAP], and micropapillary/solid [MIP/SOL]) to characterize genomic landscape, recurrence risk, and therapeutic actionability across architectural grades. [PMID:32791233](../papers/32791233.md)

## Composition

- **n = 604** patients with stage I–III [LUAD](../cancer_types/LUAD.md) after complete resection.
- Histologic-subtype distribution: LEP 88 (15%), ACI 368 (61%), PAP 43 (7%), MIP 37 (6%), SOL 68 (11%). Grouped: LEP 88 (15%), ACI/PAP 411 (68%), MIP/SOL 105 (17%).
- Pathologic stage: I 447 (74%); II 95 (16%); III 62 (10%).
- Demographics: median age 68 (IQR 62–74); 67% female; 77% ever-smokers (median 20 pack-years).
- 116 patients (19%) received adjuvant therapy; median follow-up 2.51 years (IQR 2.08–3.14).
- Sequencing panel versions: 8 patients on [IMPACT341](../methods/IMPACT341.md) (0.98 Mb), 190 on [IMPACT410](../methods/IMPACT410.md) (1.06 Mb), 406 on [IMPACT468](../methods/IMPACT468.md) (1.22 Mb). [PMID:32791233](../papers/32791233.md)

## Assays / panels (linked)

- [MSK-IMPACT panel](../methods/msk-impact-panel.md) — targeted NGS; panel versions [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), and [IMPACT468](../methods/IMPACT468.md).
- [FACETS](../methods/facets.md) — allele-specific copy-number analysis; fraction of genome altered ([FGA](../genes/FGA.md)) and WGD detection.

## Papers using this cohort

- [PMID:32791233](../papers/32791233.md) — Caso et al. (2020): genomic landscape across LUAD histologic subtypes; MIP/SOL tumors show highest TMB, FGA, and WGD rates; APOBEC signatures SBS2/SBS13 associate with recurrence risk.

## Notable findings derived from this cohort

- Median TMB increased monotonically with histologic invasiveness: LEP 3.9, ACI/PAP 4.9, MIP/SOL 7.9 mutations/Mb (p<0.001); median FGA followed the same pattern (p=0.001). [PMID:32791233](../papers/32791233.md)
- Whole-genome doubling rate was highest in MIP/SOL (18%) vs. ACI/PAP (10%) vs. LEP (4.5%), p=0.008. [PMID:32791233](../papers/32791233.md)
- [EGFR](../genes/EGFR.md) was enriched in LEP tumors (42% vs. 31% vs. 19%; p=0.001); [BRAF](../genes/BRAF.md)-V600E was enriched in MIP/SOL (5% vs. 1.2% vs. 1.1%; p=0.046); [TP53](../genes/TP53.md) was strongly enriched in MIP/SOL (62% vs. 33% vs. 16%; p<0.001). [PMID:32791233](../papers/32791233.md)
- APOBEC signatures SBS2 (SHR 2.07; p=0.021) and SBS13 (SHR 2.27; p=0.005) were independently associated with increased postresection recurrence risk across all patients. [PMID:32791233](../papers/32791233.md)
- Three-year cumulative incidence of recurrence: 8% LEP, 23% ACI/PAP, 37% MIP/SOL (p<0.001). [PMID:32791233](../papers/32791233.md)
- OncoKB annotation identified 735 actionable alterations across 30 genes; LEP tumors had the highest fraction of level I targets (35% vs. 27% vs. 21%). [PMID:32791233](../papers/32791233.md)

## Sources

- cBioPortal study `luad_mskcc_2020`.
- Caso et al. (2020) *Journal of Thoracic Oncology* [PMID:32791233](../papers/32791233.md).

*This page was processed by **crosslinker** on **2026-05-16**.*
