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
processed_at: 2026-05-15
---

# OncoKB Annotation

## Overview

A bioinformatics annotation step in which somatic variants identified by tumor sequencing are classified against the Memorial Sloan Kettering OncoKB precision oncology knowledge base ([oncokb](../methods/oncokb.md).org). OncoKB assigns evidence-based actionability levels (Level 1–4) to alterations based on FDA approvals, clinical trial data, and biological evidence. The annotation provides structured therapeutic implication tiers enabling prioritization of variants for clinical management or trial enrollment.

## Used by

- OncoKB database (accessed 6 January 2017) used to classify potentially oncogenic and actionable mutations in 19 anaplastic oligodendroglioma tumors from the [odg_msk_2017](../datasets/odg_msk_2017.md) cohort (MSK-IMPACT 410-gene panel); identified Level 2B alterations ([CDK4](../genes/CDK4.md) amplification, [TSC1](../genes/TSC1.md)) and Level 3B alterations ([IDH1](../genes/IDH1.md) R132H, [IDH2](../genes/IDH2.md) R172K, [KRAS](../genes/KRAS.md) Q61H, [PIK3CA](../genes/PIK3CA.md)) [PMID:28472509](../papers/28472509.md).
- Applied to MSK-IMPACT-profiled prostate cancer alterations (504 tumors from 451 patients) to identify actionable alterations; 36% of patients carried at least one potentially actionable alteration per OncoKB [PMID:28825054](../papers/28825054.md)

## Notes

- OncoKB actionability tiers: Level 1 (FDA-recognized biomarker with approved therapy in this tumor type), Level 2 (standard care or FDA-recognized in another tumor type), Level 3 (clinical evidence), Level 4 (compelling biological evidence).
- Annotation is database-version-dependent; therapeutic implications evolve as new trial data accrue (e.g., KRAS G12C was unactionable at time of early MSK-IMPACT publications but gained Level 1 evidence post-approval of [sotorasib](../drugs/sotorasib.md)).
- Distinct from the OncoKB programmatic annotation tool (see [oncokb](../methods/oncokb.md)) used in MSK-IMPACT routine pipeline; this page captures the variant-classification annotation step as applied in specific papers.

## Sources

- [PMID:28472509](../papers/28472509.md) — Thomas et al., MSK HDC-ASCT phase II trial in anaplastic oligodendroglioma; OncoKB-classified actionable variants in 19 tumor exomes.

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
