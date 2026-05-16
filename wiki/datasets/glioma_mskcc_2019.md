---
name: MSK Glioma Clinical Sequencing Cohort (2019)
studyId: glioma_mskcc_2019
institution: Memorial Sloan Kettering Cancer Center (MSKCC)
size: 1004
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - foundationone
panels:
  - IMPACT341
  - IMPACT468
  - FoundationOne
tags:
  - glioma
  - glioblastoma
  - IDH
  - IMPACT
  - clinical-sequencing
  - germline
  - prospective
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Glioma Clinical Sequencing Cohort (2019)

## Overview

Jonsson et al. (*Nature Medicine* 2019, [PMID:31263031](../papers/31263031.md)) integrated prospective clinical sequencing of 1,004 tumors (733 primary, 271 recurrent) from 923 adult glioma patients at Memorial Sloan Kettering Cancer Center with curated treatment and survival outcomes. Sequencing was performed using [MSK-IMPACT](../methods/msk-impact-panel.md) tumor/normal panels (n=837) and [FoundationOne](../methods/foundationone.md) tumor-only panels (n=167). Patients were enrolled from July 2013 through July 2017. The dataset is deposited as `glioma_mskcc_2019` on cBioPortal.

## Composition

- **923 patients / 1,004 tumors** prospectively sequenced at MSKCC; 733 primary and 271 recurrent samples; 57 patients had matched pre/post-treatment pairs.
- Cancer types: WHO 2016 diffuse glioma ([DIFG](../cancer_types/DIFG.md)) spanning IDH-mutant [astrocytoma](../cancer_types/ASTR.md) (grades II–IV), IDH-mutant 1p/19q co-deleted [oligodendroglioma](../cancer_types/ODG.md), IDH-WT and IDH-mutant [glioblastoma](../cancer_types/GBM.md), and [HGGNOS](../cancer_types/HGGNOS.md) subtypes.
- 355 IDH-mutant vs. 649 IDH-WT tumors.
- [MGMT](../genes/MGMT.md) promoter methylation data available for 636 patients.
- Germline analysis restricted to 764 MSK-IMPACT patients (tumor/normal pairs).
- External reference cohorts for meta-analysis: AACR GENIE (498), TCGA (894), Foundation Medicine (739) — combined n=3,130 for novel hotspot discovery.

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md) — paired tumor/normal, n=837 tumors
- [foundationone](../methods/foundationone.md) — tumor-only, n=167 tumors
- [facets](../methods/facets.md) — allele-specific copy number (v0.3.9)
- [mutational-signatures](../methods/mutational-signatures.md) — signature 11 (alkylator-induced hypermutation calling)
- [vcf2maf](../methods/vcf2maf.md) — variant annotation with VEP v88 for external cohort harmonization

## Papers using this cohort

- [PMID:31263031](../papers/31263031.md) — Jonsson et al. 2019, *Nature Medicine*: defining publication for this dataset.

## Notable findings derived from this cohort

- 13% (103/764) of evaluable patients harbored a pathogenic or likely pathogenic germline variant; 28% of these targeted DNA-repair effectors including [NF1](../genes/NF1.md), [TP53](../genes/TP53.md), [PTEN](../genes/PTEN.md), [RB1](../genes/RB1.md), [BRCA2](../genes/BRCA2.md), and Lynch-syndrome MMR genes [PMID:31263031](../papers/31263031.md).
- Cell-cycle pathway alterations (chiefly [CDKN2A/B](../genes/CDKN2A.md) focal deletions) were enriched in MRI-enhancing IDH-mutant 1p19q-intact astrocytomas (44% vs. 8% non-enhancing, P<0.001) and independently associated with shorter PFS at recurrence (HR=2.6, 95% CI 1.6–5.7, P=0.02); cell-cycle defects preceded [temozolomide](../drugs/temozolomide.md) exposure in three matched pre/post-treatment pairs [PMID:31263031](../papers/31263031.md).
- 38 hypermutated tumors were identified (mutational signature 11 driven); alkylator-induced hypermutation was more common in IDH-mutant tumors (29% vs. 12%, P=0.004) and in MGMT-methylated patients (30% vs. 10%, P=0.006) [PMID:31263031](../papers/31263031.md).
- [BRAF](../genes/BRAF.md) V600 mutations were clonal and restricted to epithelioid IDH-WT GBMs or secondary high-grade tumors; 4/7 BRAF V600E patients treated with RAF/MEK inhibitors ([vemurafenib](../drugs/vemurafenib.md), [dabrafenib](../drugs/dabrafenib.md), [trametinib](../drugs/trametinib.md)) had partial/near-complete responses; the one early progressor had subclonal V600E [PMID:31263031](../papers/31263031.md).
- Meta-analysis across 3,130 glioma samples identified 34 novel hotspots in [EGFR](../genes/EGFR.md) and [PDGFRA](../genes/PDGFRA.md), and candidate driver mutations in [MAP3K1](../genes/MAP3K1.md) and [SF3B1](../genes/SF3B1.md) — two genes not previously linked to glioma [PMID:31263031](../papers/31263031.md).
- 32% of patients (295/923) harbored a potentially actionable lesion (OncoKB levels 1–3); [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) fusions were identified in 16 patients [PMID:31263031](../papers/31263031.md).

## Sources

- cBioPortal study: `glioma_mskcc_2019`
- Jonsson et al. *Nature Medicine* 2019. [PMID:31263031](../papers/31263031.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
