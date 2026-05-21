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
processed_by: crosslinker
processed_at: 2026-05-21
---

# OncoKB Annotation

## Overview

A bioinformatics annotation step in which somatic variants identified by tumor sequencing are classified against the Memorial Sloan Kettering OncoKB precision oncology knowledge base ([oncokb](../methods/oncokb.md).org). OncoKB assigns evidence-based actionability levels (Level 1–4) to alterations based on FDA approvals, clinical trial data, and biological evidence. The annotation provides structured therapeutic implication tiers enabling prioritization of variants for clinical management or trial enrollment.

## Used by

- OncoKB database (accessed 6 January 2017) used to classify potentially oncogenic and actionable mutations in 19 anaplastic oligodendroglioma tumors from the [odg_msk_2017](../datasets/odg_msk_2017.md) cohort (MSK-IMPACT 410-gene panel); identified Level 2B alterations ([CDK4](../genes/CDK4.md) amplification, [TSC1](../genes/TSC1.md)) and Level 3B alterations ([IDH1](../genes/IDH1.md) R132H, [IDH2](../genes/IDH2.md) R172K, [KRAS](../genes/KRAS.md) Q61H, [PIK3CA](../genes/PIK3CA.md)) [PMID:28472509](../papers/28472509.md).
- Applied to MSK-IMPACT-profiled prostate cancer alterations (504 tumors from 451 patients) to identify actionable alterations; 36% of patients carried at least one potentially actionable alteration per OncoKB [PMID:28825054](../papers/28825054.md)
- OncoKB used to annotate oncogenic effect of alterations in 295 metastatic [EGC](../cancer_types/EGC.md) patients; 53% had at least one OncoKB-defined potentially actionable alteration [PMID:29122777](../papers/29122777.md)
- OncoKB actionability rates: 86% of MSI-H/hypermutated vs 37% of MSS metastatic [COADREAD](../cancer_types/COADREAD.md) carried potentially actionable alterations (p<0.001) in the 1,134-tumor MSK-IMPACT cohort [PMID:29316426](../papers/29316426.md)
- OncoKB (Sept 2017) used for pathway-level oncogenicity calls in SUMMIT basket-trial patients with ERBB2/ERBB3-mutant tumors; contributed to co-mutation pathway analysis [PMID:29420467](../papers/29420467.md)
- OncoKB used to rescue genes with ≥5 oncogenic variants from MutSig2CV in the prostate [prad_p1000](../datasets/prad_p1000.md) analysis; supplemented statistical significance filtering [PMID:29610475](../papers/29610475.md)
- Applied to classify somatic alterations from 195 cholangiocarcinoma patients; 47.6% had at least one alteration at OncoKB level 3B or higher; 16 patients (8%) had level 2B alterations ([ERBB2](../genes/ERBB2.md) amplification, TSC1/TSC2, BRCA1/2, [BRAF](../genes/BRAF.md) V600E, [MET](../genes/MET.md) amplification); no level 1 or 2A alterations found [PMID:29848569](../papers/29848569.md)
- OncoKB (annotated 22-Dec-2016) used to assess actionability of alterations in 189 advanced endometrial cancer patients; 67% (127/189) carried ≥1 actionable alteration; most common actionable events were [PIK3CA](../genes/PIK3CA.md) mutation (35%), [PTEN](../genes/PTEN.md) mutation (29%), MSI-H (16%), and [ERBB2](../genes/ERBB2.md) amplification (16%) [PMID:30068706](../papers/30068706.md)
- OncoKB levels 1–4 used to filter actionable variants; 24% of 127 advanced [HCC](../cancer_types/HCC.md) tumors had ≥1 actionable alteration, but no level 1/2A alterations were found [PMID:30373752](../papers/30373752.md)
- OncoKB used to define actionable gene targets in 81 GBCA tumors; 80% of patients carried ≥1 potentially actionable alteration [PMID:30427539](../papers/30427539.md)
- Used to annotate somatic alterations with actionability tier levels (OncoKB levels 1–4) in 80 metastatic panNET patients; guided identification of clinically actionable alterations [PMID:30687805](../papers/30687805.md)
- Variant annotation of 1,045 [ACC](../cancer_types/ACC.md) cases revealed 40.3% of R/M tumors harbored potentially targetable kinase mutations, but only 10.6% had OncoKB-supported clinical-level evidence, highlighting the gap between somatic alteration prevalence and actionability [PMID:31483290](../papers/31483290.md).
- OncoKB annotation (Aug 1, 2019) used to assign actionability levels in 424 mCSPC tumors; 50% (211/424) had at least one potentially actionable alteration; median 3 oncogenic alterations per tumor [PMID:32220891](../papers/32220891.md)
- Identified 735 actionable alterations across 30 genes in 604 resected [LUAD](../cancer_types/LUAD.md) tumors; RTK/RAS harbored 73% (536) of actionable alterations; 37% had level I evidence; LEP subtype had the highest fraction of level I targets (35%) [PMID:32791233](../papers/32791233.md)
- OncoKB oncogenicity annotation used to restrict variant calls in 696 melanoma tumors to oncogenic alterations; informed the 9-group MAPK driver classifier [PMID:33509808](../papers/33509808.md)
- OncoKB annotation used to classify oncogenic alterations in 412 iCCA tumors; VUS excluded; 12 canonical TCGA PanCancer Atlas signaling pathways evaluated [PMID:33765338](../papers/33765338.md)
- Used to classify oncogenic driver calls for genomic-survival analysis in 219 intrahepatic cholangiocarcinoma ([IHCH](../cancer_types/IHCH.md)) patients; IDH1/2 mutations, [FGFR2](../genes/FGFR2.md) fusions, TP53/KRAS mutations, and CDKN2A/B deletions annotated as oncogenic or likely oncogenic to define the high-risk composite biomarker [PMID:33963001](../papers/33963001.md)
- Applied to annotate somatic mutations detected by cf-IMPACT ([IMPACT410](../methods/IMPACT410.md)) and [MSK-ACCESS](../methods/ACCESS129.md) in 118 metastatic solid tumor patients; identified OncoKB level 1–4 actionable variants in 25% of patients by cf-IMPACT; level 1 actionable mutations detected in 41% of MSK-ACCESS samples [PMID:34059130](../papers/34059130.md)
- Used to classify clinical actionability for variants reported by MSK-ACCESS in 681 prospective plasma samples; 41% (278/681) had OncoKB level 1–3B alterations; level-1 yield was 48% in bladder, 37% in breast, and 33% in [NSCLC](../cancer_types/NSCLC.md) [PMID:34145282](../papers/34145282.md)
- Applied in the MSK early-onset colorectal cancer cohort (759 EO-CRC patients vs 687 AO-CRC) for somatic and germline profiling at Memorial Sloan Kettering Cancer Center [PMID:34405229](../papers/34405229.md)
- OncoKB used for cross-validation of recurrent oncogenic driver alterations in 237 esophageal/GEJ adenocarcinoma patients; 8 genes at ≥8% prevalence confirmed [PMID:35377946](../papers/35377946.md).
- OncoKB v2.8 used for oncogenicity annotation of [PIK3R1](../genes/PIK3R1.md) alterations in 1,417 MSK-IMPACT prostate cancers; 'driver' defined as predicted oncogenic by OncoKB [PMID:35670774](../papers/35670774.md)
- OncoKB used for actionability annotation of 7,494 sarcoma samples sequenced by FoundationOne Heme, classifying alterations into Levels 1–4 for treatment selection [PMID:35705558](../papers/35705558.md)
- OncoKB oncogenicity and actionability annotation applied to the 2,138-sarcoma MSK-IMPACT dataset to classify driver alterations and assign treatment-actionability levels [PMID:35705560](../papers/35705560.md)
- Applied to annotate oncogenic driver alterations in colitis-associated cancer (CAC); identified [IDH1](../genes/IDH1.md) R132 mutations and [FGFR2](../genes/FGFR2.md) amplification/fusion as actionable findings with FDA-approved therapies ([ivosidenib](../drugs/ivosidenib.md), FGFR inhibitors) applicable from other GI cancers [PMID:36611031](../papers/36611031.md)
- Used for driver annotation in aSCLC; identified [ALDH1L2](../genes/ALDH1L2.md) as the sole in-frame fusion involving a likely-oncogenic gene across all RNA-seq cases; annotated [CCND1](../genes/CCND1.md), [CDK4](../genes/CDK4.md), [MDM2](../genes/MDM2.md), [MYCL](../genes/MYCL.md) amplifications and MEN1/EIF1AX/ARID1A/ATM alterations as the dominant driver landscape [PMID:39185963](../papers/39185963.md)

## Notes

- OncoKB actionability tiers: Level 1 (FDA-recognized biomarker with approved therapy in this tumor type), Level 2 (standard care or FDA-recognized in another tumor type), Level 3 (clinical evidence), Level 4 (compelling biological evidence).
- Annotation is database-version-dependent; therapeutic implications evolve as new trial data accrue (e.g., [KRAS](../genes/KRAS.md) G12C was unactionable at time of early MSK-IMPACT publications but gained Level 1 evidence post-approval of [sotorasib](../drugs/sotorasib.md)).
- Distinct from the OncoKB programmatic annotation tool (see [oncokb](../methods/oncokb.md)) used in MSK-IMPACT routine pipeline; this page captures the variant-classification annotation step as applied in specific papers.

## Sources

- [PMID:28472509](../papers/28472509.md) — Thomas et al., MSK HDC-ASCT phase II trial in anaplastic oligodendroglioma; OncoKB-classified actionable variants in 19 tumor exomes.

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29122777](../papers/29122777.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29316426](../papers/29316426.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29610475](../papers/29610475.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29848569](../papers/29848569.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30373752](../papers/30373752.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30427539](../papers/30427539.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30687805](../papers/30687805.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31483290](../papers/31483290.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32220891](../papers/32220891.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32791233](../papers/32791233.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33509808](../papers/33509808.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33765338](../papers/33765338.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33963001](../papers/33963001.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34059130](../papers/34059130.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34405229](../papers/34405229.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35377946](../papers/35377946.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35670774](../papers/35670774.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705558](../papers/35705558.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705560](../papers/35705560.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:36611031](../papers/36611031.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:39185963](../papers/39185963.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
