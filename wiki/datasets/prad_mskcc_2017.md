---
name: MSK-IMPACT Prostate Cancer Clinical Sequencing Cohort 2017 (Abida et al.)
studyId: prad_mskcc_2017
institution: Memorial Sloan Kettering Cancer Center
size: 504
reference_genome: GRCh37/hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels: []
tags:
  - prostate-cancer
  - mCRPC
  - DDR
  - germline
  - MSK-IMPACT
  - castration-resistant
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# MSK-IMPACT Prostate Cancer Clinical Sequencing Cohort 2017 (Abida et al.)

## Overview

The MSK-IMPACT prostate cancer cohort is a prospective clinical sequencing study of 504 tumors from 451 patients with prostate adenocarcinoma spanning the full clinical spectrum — locoregional, metastatic noncastrate, and metastatic castration-resistant prostate cancer (mCRPC) — conducted at Memorial Sloan Kettering Cancer Center. Abida et al. applied the [MSK-IMPACT](../methods/msk-impact-panel.md) hybridization-capture targeted DNA panel (>300 cancer-related genes), with paired germline analysis in 221 patients. The study identified potentially actionable alterations in 36% of patients (per OncoKB annotation) and established a 27% combined germline-or-somatic alteration rate in DDR genes ([BRCA2](../genes/BRCA2.md), [BRCA1](../genes/BRCA1.md), [ATM](../genes/ATM.md), [CHEK2](../genes/CHEK2.md)), arguing for routine paired germline + somatic profiling as standard of care in advanced [PRAD](../cancer_types/PRAD.md). Released as `prad_mskcc_2017` on cBioPortal [PMID:28825054](../papers/28825054.md).

## Composition

- **Patients:** 451; **tumors profiled:** 504 (44 patients had >1 tumor sequenced).
- **Disease-state composition (last known):** 348 metastatic (77%), 53 biochemically recurrent (12%), 50 locoregional (11%).
- **Disease-state at tissue acquisition (504 tumors):** 140 locoregional, 51 metastatic noncastrate prostate, 54 metastatic noncastrate metastasis sites, 95 mCRPC prostate, 164 mCRPC metastasis sites.
- **Metastatic biopsy sites:** lymph node 45%, bone 22%, liver 14%, lung 5%, other soft tissue 14%.
- **Sequencing success rate:** 504/746 (68%); bone and lung samples most challenging (42–52% success).
- **Assay:** [MSK-IMPACT](../methods/msk-impact-panel.md) hybridization-capture targeted DNA panel (>300 cancer-related genes) for SNVs, indels, somatic copy number alterations, and structural rearrangements; matched normal blood for germline filtering.
- **Germline analysis:** 221 patients consented to germline analysis of 76 known cancer-predisposing genes.
- **Clonality:** estimated via cancer cell fraction with the [FACETS](../methods/facets.md) algorithm.
- **Actionability annotation:** [OncoKB](../methods/oncokb-annotation.md).
- **Comparison cohorts:** [prad_su2c_2015](../datasets/prad_su2c_2015.md) and [prad_tcga_pub](../datasets/prad_tcga_pub.md) [PMID:28825054](../papers/28825054.md).

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md)
- [facets](../methods/facets.md)
- [oncokb-annotation](../methods/oncokb-annotation.md)

## Papers using this cohort

- [PMID:28825054](../papers/28825054.md) — Abida et al. 2017; inaugural clinical description of the MSK-IMPACT prostate cohort, defining DDR alteration prevalence and disease-state enrichment patterns across the spectrum of prostate cancer.

## Notable findings derived from this cohort

- Mutation burden increases with castration resistance: mean nonsynonymous mutations/megabase rose from 1.74 (locoregional) to 4.02 (mCRPC), P<0.001; metastatic noncastrate tumors similar to locoregional (2.08 mut/Mb) [PMID:28825054](../papers/28825054.md).
- Somatic homologous recombination (HR) gene alterations in 22% of patients: [BRCA2](../genes/BRCA2.md) 7%, [CDK12](../genes/CDK12.md) 7%, [ATM](../genes/ATM.md) 5%, [FANCA](../genes/FANCA.md) 3%, [PALB2](../genes/PALB2.md) 2%, [BRCA1](../genes/BRCA1.md) 1%, [RAD50](../genes/RAD50.md) 1% [PMID:28825054](../papers/28825054.md).
- Germline pathogenic alterations in 19% of the 221 consented patients: [BRCA2](../genes/BRCA2.md) 9%, [CHEK2](../genes/CHEK2.md) 4%, [ATM](../genes/ATM.md) 2%, [BRCA1](../genes/BRCA1.md) 1%; combined germline-or-somatic DDR alteration rate 27% in the four canonical genes [PMID:28825054](../papers/28825054.md).
- mCRPC-enriched alterations vs locoregional: [AR](../genes/AR.md) (2%→52%), [TP53](../genes/TP53.md) (27%→48%), [PTEN](../genes/PTEN.md) (12%→29%), [RB1](../genes/RB1.md) (2%→18%), [ATM](../genes/ATM.md) (2%→11%), [APC](../genes/APC.md) (4%→15%), [CDK12](../genes/CDK12.md) (4%→11%) [PMID:28825054](../papers/28825054.md).
- [SPOP](../genes/SPOP.md) alterations enriched in earlier disease states (locoregional 12%→mCRPC 5%), suggesting potential androgen-deprivation sensitivity (functional validation pending) [PMID:28825054](../papers/28825054.md).
- [APC](../genes/APC.md) enriched specifically in metastatic disease states relative to locoregional; [ATM](../genes/ATM.md) specifically enriched in mCRPC vs metastatic noncastrate — implicating distinct roles in metastasis vs castration resistance [PMID:28825054](../papers/28825054.md).
- [TP53](../genes/TP53.md) and somatic [BRCA2](../genes/BRCA2.md) alterations were present early and clonal (cancer cell fraction>0.9) in primary tumors of patients who later developed metastasis; [AR](../genes/AR.md) alterations and [PIK3CA](../genes/PIK3CA.md) E545K acquired late [PMID:28825054](../papers/28825054.md).
- OncoKB-annotated actionability: 36% of patients carried at least one potentially actionable alteration; MMR gene alterations in 3% produce hypermutator phenotype, nominating PD-1 blockade candidacy [PMID:28825054](../papers/28825054.md).

## Sources

- Abida W, Armenia J, Gopalan A, et al. Prospective genomic profiling of prostate cancer across disease states reveals germline and somatic alterations that may affect clinical decision making. *JCO Precision Oncology.* 2017;1:1-16. [PMID:28825054](../papers/28825054.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
