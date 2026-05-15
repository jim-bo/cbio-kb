---
name: Prostate Adenocarcinoma Pan-1000 Meta-Cohort (Armenia et al. 2018)
studyId: prad_p1000
institution: Multi-institutional (aggregated)
size: 1013
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
panels: []
tags:
  - prostate
  - prad
  - meta-cohort
  - whole-exome-seq
  - pan-1000
processed_by: crosslinker
processed_at: 2026-05-15
---

# Prostate Adenocarcinoma Pan-1000 Meta-Cohort (Armenia et al. 2018)

## Overview

`prad_p1000` is a pan-1000 prostate cancer meta-cohort assembled by Armenia et al. (2018) by aggregating and uniformly re-analyzing whole-exome sequencing from 1,013 prostate tumor/normal pairs drawn from prior published cohorts. It comprises 680 primary (treatment-naive) and 333 metastatic castration-resistant prostate cancer (CRPC) tumors. The dataset is publicly available in cBioPortal at study ID `prad_p1000`. Uniform reprocessing used PICARD re-alignment, MuTect v1.1.6 (SNVs), Strelka v1.0.11 (indels), ReCapSeg + GISTIC 2.0 (copy number), and FACETS v0.5.10 (allele-specific CN / purity / ploidy).

## Composition

- Cancer type: Prostate Adenocarcinoma ([PRAD](../cancer_types/PRAD.md)), OncoTree code [PRAD](../cancer_types/PRAD.md).
- N = 1,013 tumor/normal WES pairs: 680 primary, 333 metastatic castration-resistant.
- Mean target coverage: 104.7x (tumor), 103.8x (normal); ContEst < 5% (mean 0.6%).
- Sources aggregated from multiple prior TCGA and non-TCGA WES studies, uniformly reprocessed.
- Validation cohorts: 706 advanced prostate cancers from [msk_impact_2017](../datasets/msk_impact_2017.md); 204 prostate cancers from Foundation Medicine (phs001179).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [mutect](../methods/mutect.md)
- [strelka](../methods/strelka.md)
- [facets](../methods/facets.md)
- [gistic](../methods/gistic.md)

## Papers using this cohort

- [PMID:29610475](../papers/29610475.md) — Armenia et al., discovery paper defining this cohort

## Notable findings derived from this cohort

- 97 significantly mutated genes (SMGs) identified by MutSig2CV, including 70 not previously implicated in prostate cancer and 9 novel across all cancer types; most novel SMGs are mutated in fewer than 5% of tumors and required over 900 samples to detect [PMID:29610475](../papers/29610475.md).
- Metastatic tumors carry higher non-synonymous mutation rate (mean 2.93 mut/Mb vs. 1.36 mut/Mb in primary, p<0.001) and higher copy-number burden [PMID:29610475](../papers/29610475.md).
- [CUL3](../genes/CUL3.md) identified as a new SPOP-like prostate-cancer driver (1.3%, recurrent hotspot p.Met299Arg), mutually exclusive with [SPOP](../genes/SPOP.md) mutations; validated in [msk_impact_2017](../datasets/msk_impact_2017.md) (9 additional cases) [PMID:29610475](../papers/29610475.md).
- Spliceosome pathway ([SF3B1](../genes/SF3B1.md) 1.1%, [U2AF1](../genes/U2AF1.md) 0.5%) nominated as a new recurrent prostate cancer pathway [PMID:29610475](../papers/29610475.md).
- [SPEN](../genes/SPEN.md) identified as a metastasis-enriched AR-pathway driver (2.4%, predominantly truncating, q=0.008) [PMID:29610475](../papers/29610475.md).
- 20% of samples carry alterations in epigenetic/chromatin-remodeling genes; enriched in ETS-fusion-negative tumors and those lacking known drivers [PMID:29610475](../papers/29610475.md).
- DNA-repair pathway altered in 16%; novel prostate-specific SMGs include [MRE11](../genes/MRE11.md) and [PALB2](../genes/PALB2.md); [CDK12](../genes/CDK12.md) mutations predominantly truncating with frequent biallelic inactivation [PMID:29610475](../papers/29610475.md).

## Sources

- cBioPortal study: `prad_p1000` (http://www.cbioportal.org/study?id=prad_p1000)
- Armenia J, et al. *The long tail of oncogenic drivers in prostate cancer.* Nat Genet. 2018. [PMID:29610475](../papers/29610475.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
