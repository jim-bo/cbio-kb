---
name: MSK Paired Bladder Cancer Primary-Metastasis Study (2022)
studyId: paired_bladder_2022
institution: Memorial Sloan Kettering Cancer Center
size: 1313
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - whole-exome-seq
  - liquid-biopsy
panels:
  - msk-impact-panel
  - msk-access
tags:
  - bladder-cancer
  - urothelial-carcinoma
  - genomic-heterogeneity
  - primary-metastasis-concordance
  - cfdna
  - clonal-evolution
  - precision-oncology
processed_by: crosslinker
processed_at: 2026-05-05
---

# MSK Paired Bladder Cancer Primary-Metastasis Study (2022)

## Overview

Institutional cohort from Memorial Sloan Kettering Cancer Center profiling 1,313 patients with bladder urothelial carcinoma by [MSK-IMPACT](../methods/msk-impact-panel.md) (prospectively enrolled 2014–2021). The study includes 119 matched primary-metastasis tumor pairs sequenced by MSK-IMPACT targeted sequencing, 22 pairs sequenced by whole-exome sequencing, and 123 patients with at least one tumor sample and paired plasma cfDNA via [MSK-ACCESS](../methods/msk-access.md) (~20,000x raw coverage, ~1,000x duplex). The dataset is publicly available on cBioPortal as `paired_bladder_2022`.

## Composition

- 1,313 patients with [BLCA](../cancer_types/BLCA.md) or [UTUC](../cancer_types/UTUC.md) prospectively sequenced at MSK.
- 119 matched primary-metastasis pairs by MSK-IMPACT; 22 pairs by WES (tumor purity >=25% by [FACETS](../methods/facets.md)).
- 45 patients with primary tumor, metastasis, and plasma cfDNA; 123 patients with at least one tumor sample and cfDNA.
- Key clinical fields: grade, stage, tumor site, lines of prior therapy, time between primary and metastatic sample collection (median 10.5 months, IQR 2.6–25.5).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted tumor-normal sequencing
- [whole-exome-seq](../methods/whole-exome-seq.md) — 22 primary-metastasis pairs
- [MSK-ACCESS](../methods/msk-access.md) — plasma cfDNA (~20,000x raw, ~1,000x duplex)
- [FACETS](../methods/facets.md) — allele-specific copy number and tumor purity estimation

## Papers using this cohort

- [PMID:36543146](../papers/36543146.md) — Clinton et al., *Cell Reports* 2022. Genomic heterogeneity as a barrier to precision oncology in urothelial cancer.

## Notable findings derived from this cohort

- Mean mutational concordance by WES between primary and metastatic tumors was only 42% (range 6%–84%), consistent with early branched evolution; 23% of potentially actionable gene mutations ([FGFR3](../genes/FGFR3.md), [PIK3CA](../genes/PIK3CA.md), [TSC1](../genes/TSC1.md), [ERBB2](../genes/ERBB2.md)) were discordant between paired sites [PMID:36543146](../papers/36543146.md).
- [ARID1A](../genes/ARID1A.md) mutations, when discordant between primary and metastatic sites, were always exclusive to the metastatic sample (16% of ARID1A-mutant patients), suggesting late acquisition during metastatic progression [PMID:36543146](../papers/36543146.md).
- [ERBB2](../genes/ERBB2.md) showed the highest discordance rate (38%) among targetable genes, followed by [PIK3CA](../genes/PIK3CA.md) (27%), [TSC1](../genes/TSC1.md) (17%), and [FGFR3](../genes/FGFR3.md) (9%) [PMID:36543146](../papers/36543146.md).
- Plasma cfDNA by MSK-ACCESS identified 17% of targetable alterations (60% concordant, 17% cfDNA-exclusive, 23% tissue-exclusive) and detected convergent evolution with 4 distinct oncogenic [FGFR3](../genes/FGFR3.md) alterations in one patient during [erdafitinib](../drugs/erdafitinib.md) therapy [PMID:36543146](../papers/36543146.md).

## Sources

- cBioPortal study: `paired_bladder_2022`
- Associated publication: [PMID:36543146](../papers/36543146.md)

*This page was processed by **crosslinker** on **2026-05-05**.*
