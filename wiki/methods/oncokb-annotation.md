---
name: OncoKB Annotation
slug: oncokb-annotation
kind: method
canonical_source: corpus
unverified: true
tags:
  - annotation
  - actionability
  - oncokb
  - clinical-interpretation
processed_by: wiki-cli
processed_at: 2026-05-16
---

# OncoKB Annotation

## Overview

A bioinformatics annotation step in which somatic variants identified by tumor sequencing are classified against the Memorial Sloan Kettering OncoKB precision oncology knowledge base ([oncokb](../methods/oncokb.md).org). OncoKB assigns evidence-based actionability levels (Level 1–4) to alterations based on FDA approvals, clinical trial data, and biological evidence. The annotation provides structured therapeutic implication tiers enabling prioritization of variants for clinical management or trial enrollment.

## Used by

- OncoKB database (accessed 6 January 2017) used to classify potentially oncogenic and actionable mutations in 19 anaplastic oligodendroglioma tumors from the [odg_msk_2017](../datasets/odg_msk_2017.md) cohort (MSK-IMPACT 410-gene panel); identified Level 2B alterations ([CDK4](../genes/CDK4.md) amplification, [TSC1](../genes/TSC1.md)) and Level 3B alterations ([IDH1](../genes/IDH1.md) R132H, [IDH2](../genes/IDH2.md) R172K, [KRAS](../genes/KRAS.md) Q61H, [PIK3CA](../genes/PIK3CA.md)) [PMID:28472509](../papers/28472509.md).
- Applied to MSK-IMPACT-profiled prostate cancer alterations (504 tumors from 451 patients) to identify actionable alterations; 36% of patients carried at least one potentially actionable alteration per OncoKB [PMID:28825054](../papers/28825054.md)
- OncoKB used to annotate oncogenic effect of alterations in 295 metastatic EGC patients; 53% had at least one OncoKB-defined potentially actionable alteration [PMID:29122777](../papers/29122777.md)
- OncoKB actionability rates: 86% of MSI-H/hypermutated vs 37% of MSS metastatic [COADREAD](../cancer_types/COADREAD.md) carried potentially actionable alterations (p<0.001) in the 1,134-tumor MSK-IMPACT cohort [PMID:29316426](../papers/29316426.md)
- OncoKB (Sept 2017) used for pathway-level oncogenicity calls in SUMMIT basket-trial patients with ERBB2/ERBB3-mutant tumors; contributed to co-mutation pathway analysis [PMID:29420467](../papers/29420467.md)
- OncoKB used to rescue genes with ≥5 oncogenic variants from MutSig2CV in the prostate prad_p1000 analysis; supplemented statistical significance filtering [PMID:29610475](../papers/29610475.md)
- Applied to classify somatic alterations from 195 cholangiocarcinoma patients; 47.6% had at least one alteration at OncoKB level 3B or higher; 16 patients (8%) had level 2B alterations (ERBB2 amplification, TSC1/TSC2, BRCA1/2, BRAF V600E, MET amplification); no level 1 or 2A alterations found [PMID:29848569](../papers/29848569.md)
- OncoKB (annotated 22-Dec-2016) used to assess actionability of alterations in 189 advanced endometrial cancer patients; 67% (127/189) carried ≥1 actionable alteration; most common actionable events were PIK3CA mutation (35%), PTEN mutation (29%), MSI-H (16%), and ERBB2 amplification (16%) [PMID:30068706](../papers/30068706.md)
- OncoKB levels 1–4 used to filter actionable variants; 24% of 127 advanced HCC tumors had ≥1 actionable alteration, but no level 1/2A alterations were found [PMID:30373752](../papers/30373752.md)
- OncoKB used to define actionable gene targets in 81 GBCA tumors; 80% of patients carried ≥1 potentially actionable alteration [PMID:30427539](../papers/30427539.md)
- Used to annotate somatic alterations with actionability tier levels (OncoKB levels 1–4) in 80 metastatic panNET patients; guided identification of clinically actionable alterations [PMID:30687805](../papers/30687805.md)
- Variant annotation of 1,045 ACC cases revealed 40.3% of R/M tumors harbored potentially targetable kinase mutations, but only 10.6% had OncoKB-supported clinical-level evidence, highlighting the gap between somatic alteration prevalence and actionability [PMID:31483290](../papers/31483290.md).

## Notes

- OncoKB actionability tiers: Level 1 (FDA-recognized biomarker with approved therapy in this tumor type), Level 2 (standard care or FDA-recognized in another tumor type), Level 3 (clinical evidence), Level 4 (compelling biological evidence).
- Annotation is database-version-dependent; therapeutic implications evolve as new trial data accrue (e.g., KRAS G12C was unactionable at time of early MSK-IMPACT publications but gained Level 1 evidence post-approval of [sotorasib](../drugs/sotorasib.md)).
- Distinct from the OncoKB programmatic annotation tool (see [oncokb](../methods/oncokb.md)) used in MSK-IMPACT routine pipeline; this page captures the variant-classification annotation step as applied in specific papers.

## Sources

- [PMID:28472509](../papers/28472509.md) — Thomas et al., MSK HDC-ASCT phase II trial in anaplastic oligodendroglioma; OncoKB-classified actionable variants in 19 tumor exomes.

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29122777](../papers/29122777.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29316426](../papers/29316426.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29610475](../papers/29610475.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29848569](../papers/29848569.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30373752](../papers/30373752.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30427539](../papers/30427539.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30687805](../papers/30687805.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31483290](../papers/31483290.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
