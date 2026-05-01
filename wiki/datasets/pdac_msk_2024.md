---
name: MSK PDAC Prospective Sequencing Cohort (2024)
studyId: pdac_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 2336
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays: [targeted-sequencing]
panels: [IMPACT341, IMPACT410, IMPACT468, IMPACT505]
tags:
  - pancreatic-cancer
  - PDAC
  - KRAS
  - allelic-imbalance
  - copy-number
  - real-world-data
processed_by: crosslinker
processed_at: 2026-04-30
---

# MSK PDAC Prospective Sequencing Cohort (2024)

## Overview

Prospective institutional cohort of 2,336 patients with pancreatic ductal adenocarcinoma (PDAC) sequenced with [MSK-IMPACT](../methods/msk-impact-panel.md) at Memorial Sloan Kettering between January 2014 and September 2021. Deep clinical curation was performed for 1,480 patients (63%). Released as cBioPortal study `pdac_msk_2024` by Varghese, Perry et al. 2025 [PMID:39753968](../papers/39753968.md).

## Composition

- 2,336 patients with [PAAD](../cancer_types/PAAD.md); stage distribution: 731 resectable (31%), 581 borderline-resectable/locally advanced (25%), 1,024 metastatic (44%); median [OS](../cancer_types/OS.md) 31/19/11 months respectively [PMID:39753968](../papers/39753968.md).
- Sample type: 1,424 (61%) primary tumor, 912 (39%) metastasis; median age 67 years (range 24–93) [PMID:39753968](../papers/39753968.md).
- 1,480 patients (63%) with manually curated treatment history, time on treatment, and best-response data from medical records [PMID:39753968](../papers/39753968.md).
- Allele-specific copy number inferred with [FACETS](../methods/facets.md) v0.5.14 in 1,555/2,322 tumors passing QC [PMID:39753968](../papers/39753968.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — FDA-authorized targeted DNA panel; median depth 606× (IQR 469–749×); four panel generations: [IMPACT341](../methods/IMPACT341.md) (n=17), [IMPACT410](../methods/IMPACT410.md) (n=438), [IMPACT468](../methods/IMPACT468.md) (n=1,536), [IMPACT505](../methods/IMPACT505.md) (n=345) [PMID:39753968](../papers/39753968.md).
- [MSK-Fusion](../methods/msk-fusion.md) ([archer-fusionplex](../methods/archer-fusionplex.md)) RNA-based fusion testing in 90 patients; additional [RNA-seq](../methods/rna-seq.md) in 11 tumors [PMID:39753968](../papers/39753968.md).

## Papers using this cohort

- [PMID:39753968](../papers/39753968.md) — Varghese, Perry et al. 2025: Defines three genomic subtypes of PDAC (KRAS-mutant 95%, other-MAPK-mutant 3%, MAPK-WT 2%); characterizes [KRAS](../genes/KRAS.md) mutant-allele dosage gains as a prognostic biomarker independent of stage; shows G12R confers better OS than G12D (HR_adj=0.78, P=0.003).

## Notable findings derived from this cohort

- Three genomic subtypes: KRAS-mutant (n=2,209, 95%), other-MAPK-mutant (n=76, 3%), and MAPK-WT (n=51, 2%); other-MAPK-mutant and MAPK-WT subtypes had longer OS than KRAS-mutant (HR_adj=0.69, P=0.014 and P=0.041 respectively) [PMID:39753968](../papers/39753968.md).
- [KRAS](../genes/KRAS.md) allele distribution: G12D 41%, G12V 32%, G12R 16%, G12C 1%, Q61H 1%; G12R associated with better OS than G12D (HR_adj=0.78, 95% CI 0.67–0.92, P=0.003) [PMID:39753968](../papers/39753968.md).
- Allelic imbalance at [KRAS](../genes/KRAS.md) in 42% of KRAS-mutant tumors with quality copy-number data; 93% of imbalance events preferentially gained/retained the mutant allele [PMID:39753968](../papers/39753968.md).
- KRAS mutant-allele dosage gains (non-WGD subset, n=934) independently predicted shorter OS (HR_adj=1.7, 95% CI 1.4–2.0, P=3.5×10⁻⁷) across all clinical stages [PMID:39753968](../papers/39753968.md).
- 10% of patients carried pathogenic germline variants: [BRCA2](../genes/BRCA2.md) 3.7%, [BRCA1](../genes/BRCA1.md) 1.8%, [ATM](../genes/ATM.md) 1.8%, [PALB2](../genes/PALB2.md) 0.5%; Lynch syndrome in 0.7% (17 patients), 6/17 MSI-H [PMID:39753968](../papers/39753968.md).
- ~10% of patients harbored OncoKB level 1 or 2 biomarkers; additional 78% met level 3A based on KRAS G12D/V/R/A/S [PMID:39753968](../papers/39753968.md).
- [RNF43](../genes/RNF43.md) alterations independently associated with shorter first-line OS (HR_adj=2.79, P_adj=0.047); [AKT2](../genes/AKT2.md) amplifications associated with shorter OS in metastatic, chemotherapy-treated patients (HR_adj=2.03, P_adj=0.048) [PMID:39753968](../papers/39753968.md).

## Sources

- cBioPortal study `pdac_msk_2024`. Varghese AM, Perry MA, et al. *Genomic subtypes and allelic imbalance of KRAS in pancreatic ductal adenocarcinoma.* 2025. [PMID:39753968](../papers/39753968.md).

*This page was processed by **crosslinker** on **2026-04-30**.*
