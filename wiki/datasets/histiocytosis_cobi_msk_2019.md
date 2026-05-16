---
name: MSK Cobimetinib Histiocytosis Basket Trial (histiocytosis_cobi_msk_2019)
studyId: histiocytosis_cobi_msk_2019
institution: Memorial Sloan Kettering Cancer Center
size: 18
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel-seq
  - whole-exome-seq
  - rna-fusion-panel
panels:
  - MSK-IMPACT
  - MSK-HemePACT
tags:
  - histiocytosis
  - Erdheim-Chester disease
  - Langerhans cell histiocytosis
  - cobimetinib
  - MEK inhibitor
  - MAPK pathway
  - basket trial
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Cobimetinib Histiocytosis Basket Trial (histiocytosis_cobi_msk_2019)

## Overview

Single-institution, single-arm phase 2 basket trial (NCT02649972) at Memorial Sloan Kettering Cancer Center treating 18 adult patients with histiocytic neoplasms with the oral MEK1/2 inhibitor [cobimetinib](../drugs/cobimetinib.md) (60 mg daily, 21-of-28 days), regardless of tumor genotype. The cohort included Erdheim-Chester disease ([ECD](../cancer_types/ECD.md); n=12), Langerhans cell histiocytosis ([LCH](../cancer_types/LCH.md); n=2), Rosai-Dorfman disease ([RDD](../cancer_types/RDD.md); n=2), and mixed histiocytosis (n=2). Patient-level clinical data and sequencing results are deposited in cBioPortal as `histiocytosis_cobi_msk_2019`. Genomic profiling was performed per tissue availability using [MSK-IMPACT](../methods/msk-impact-panel.md), [MSK HemePACT](../methods/msk-hemepact.md), whole-exome sequencing with fingernail germline control, [Archer FusionPlex](../methods/archer-fusionplex.md) RNA fusion panel, and supplemental cell-free DNA, PCR, and Sequenom in subsets.

## Composition

- **18 adult patients**: [ECD](../cancer_types/ECD.md) 12 (67%), [LCH](../cancer_types/LCH.md) 2 (11%), [RDD](../cancer_types/RDD.md) 2 (11%), mixed histiocytosis 2 (11%).
- **Demographics:** median age 51.9 years (range 18.3–79.5); 72% male; 50% CNS involvement; 89% had ≥1 prior systemic therapy; ECOG 2–3 in 28%.
- **MAPK genotype:** at least one MAPK-pathway mutation identified in 83% (15/18); 3 patients had unknown mutational status.
- **Primary endpoint:** PET response (CR + PR) by FDG-PET; secondary: RECIST v1.1, duration of response, PFS, safety.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted exon sequencing (primary genomic profiling assay).
- [MSK HemePACT](../methods/msk-hemepact.md) — hematologic malignancy panel used in subset.
- [Whole-exome sequencing](../methods/whole-exome-seq.md) — with fingernail germline control in subset.
- [Archer FusionPlex](../methods/archer-fusionplex.md) — targeted RNA fusion detection in subset.

## Papers using this cohort

- [PMID:30867592](../papers/30867592.md) — Diamond et al. 2019, *Nature Medicine*: prospective phase 2 trial of [cobimetinib](../drugs/cobimetinib.md) in histiocytic neoplasms; 89% PET-defined ORR; functional characterization of novel MAPK alleles.

## Notable findings derived from this cohort

- PET-defined overall response rate 89% (90% CI 73–100) across 18 patients: 13 CR (72%), 3 PR (17%), 1 SD (6%); RECIST v1.1 ORR 57% in 14 evaluable patients. Median time to best PET response 3.2 months; at 1 year, 100% of responses ongoing and 94% of patients progression-free; no acquired resistance observed. [PMID:30867592](../papers/30867592.md)
- Responses occurred across all MAPK genotypes tested: [BRAF](../genes/BRAF.md) V600E (n=4), [BRAF](../genes/BRAF.md) N486_T491delinsK (n=1), [MAP2K1](../genes/MAP2K1.md) mutations (n=4), [KRAS](../genes/KRAS.md) (n=3), [ARAF](../genes/ARAF.md) (n=2), [RAF1](../genes/RAF1.md) K106N (n=1), [MAP2K2](../genes/MAP2K2.md) Y134H (n=1), [NRAS](../genes/NRAS.md) G12D (n=1); also in 2 of 3 patients with unknown mutational status. [PMID:30867592](../papers/30867592.md)
- Three novel MAPK alleles — [MAP2K2](../genes/MAP2K2.md) Y134H, [RAF1](../genes/RAF1.md) K106N, and [BRAF](../genes/BRAF.md) N486_T491delinsK — confirmed activating and cobimetinib-sensitive by Ba/F3 functional assays (ERK activation, IL3-independent growth, cobimetinib IC50 reduction; two-way ANOVA p<0.0001). [PMID:30867592](../papers/30867592.md)
- Responses included CNS sites of disease — a site historically associated with major morbidity in [ECD](../cancer_types/ECD.md). [PMID:30867592](../papers/30867592.md)
- 56% of patients required dose reduction; grade ≥3 adverse events included diarrhea (11%), hyponatremia (11%), anemia (11%), hypokalemia (11%), CPK elevation (6%), and central retinal vein occlusion (6%, permanent discontinuation). [PMID:30867592](../papers/30867592.md)
- Provides first prospective evidence supporting empiric MEK inhibition for histiocytic neoplasms regardless of MAPK genotype, extending targeted therapy to the ~50% of patients without [BRAF](../genes/BRAF.md) V600 who were previously ineligible for [vemurafenib](../drugs/vemurafenib.md). [PMID:30867592](../papers/30867592.md)

## Sources

- cBioPortal study: `histiocytosis_cobi_msk_2019` — https://www.cbioportal.org/study/summary?id=histiocytosis_cobi_msk_2019
- ClinicalTrials.gov: NCT02649972
- [PMID:30867592](../papers/30867592.md) — Diamond et al. 2019, *Nature Medicine*, DOI 10.1038/s41591-019-0366-x

*This page was processed by **crosslinker** on **2026-05-16**.*
