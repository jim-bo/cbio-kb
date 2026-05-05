---
name: MSK Metastatic Urothelial Carcinoma cfDNA (CALGB 90601, 2025)
studyId: blca_msk_2025
institution: Memorial Sloan Kettering Cancer Center
size: 201
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays: [cfDNA-sequencing, targeted-sequencing]
panels: [ACCESS129]
tags:
  - bladder-cancer
  - urothelial-carcinoma
  - liquid-biopsy
  - cfDNA
  - ctDNA
  - DDR
  - cisplatin
processed_by: crosslinker
processed_at: 2026-05-04
---

# MSK Metastatic Urothelial Carcinoma cfDNA (CALGB 90601, 2025)

## Overview

Pretreatment plasma cell-free DNA (cfDNA) cohort of 201 patients with metastatic urothelial carcinoma (mUC) nested within the phase 3 CALGB 90601 (Alliance) randomized trial (NCT00942331) of first-line gemcitabine/cisplatin with or without [bevacizumab](../drugs/bevacizumab.md). Released via cBioPortal per the data availability statement of Guercio et al. 2025 [PMID:40256659](../papers/40256659.md).

## Composition

- 201 patients with metastatic urothelial carcinoma (bladder primary 76%, upper tract 20%, other 3.5%); drawn from 506-patient CALGB 90601 trial; 212/506 (42%) consented to blood collection with successful cfDNA sequencing in 201/212 (95%) [PMID:40256659](../papers/40256659.md).
- Median [OS](../cancer_types/OS.md) 14 months (95% CI 13–18) on chemo+[bevacizumab](../drugs/bevacizumab.md); 16 months (95% CI 15–18) on chemo+placebo [PMID:40256659](../papers/40256659.md).
- 107 patients (53%) had matched archival tumor sequencing via [MSK-IMPACT](../methods/msk-impact-panel.md) [PMID:40256659](../papers/40256659.md).
- Cancer type: metastatic [BLCA](../cancer_types/BLCA.md) (urothelial carcinoma).

## Assays / panels (linked)

- [MSK-ACCESS](../methods/msk-access.md) — 129-gene tumor-uninformed cfDNA panel with unique molecular indexes; depth >15,000×; allele-frequency detection threshold 0.1% [PMID:40256659](../papers/40256659.md).
- [MSK-IMPACT panel](../methods/msk-impact-panel.md) — matched archival tumor sequencing in 107/201 patients [PMID:40256659](../papers/40256659.md).

## Papers using this cohort

- [PMID:40256659](../papers/40256659.md) — Guercio et al. 2025: ctDNA features ([TERT](../genes/TERT.md) promoter, [PIK3CA](../genes/PIK3CA.md), [ERBB2](../genes/ERBB2.md) alterations, and ³√VAF₇₅ₚc) as candidate prognostic biomarkers for mUC patients receiving cisplatin-based chemotherapy; DDR gene alterations ([ERCC2](../genes/ERCC2.md)) were not associated with improved outcomes in this underpowered analysis.

## Notable findings derived from this cohort

- 87.1% (175/201) of samples harbored ≥1 alteration in queried genes; most frequent: [TERT](../genes/TERT.md) 57%, [TP53](../genes/TP53.md) ~52%, [FGFR3](../genes/FGFR3.md) 19%, [KDM6A](../genes/KDM6A.md) 18%, [ERBB2](../genes/ERBB2.md) 14% [PMID:40256659](../papers/40256659.md).
- Higher pretreatment ctDNA VAF associated with shorter [OS](../cancer_types/OS.md) (multivariable HR 2.51, 95% CI 1.26–5.00; p=0.009) and shorter PFS (HR 2.18, 95% CI 1.02–4.67; p=0.045) [PMID:40256659](../papers/40256659.md).
- [TERT](../genes/TERT.md) promoter alterations associated with shorter OS (multivariable HR 1.59, 95% CI 1.15–2.19; p=0.005) [PMID:40256659](../papers/40256659.md).
- [PIK3CA](../genes/PIK3CA.md) alterations (17% cfDNA) associated with shorter OS (HR 1.91, 95% CI 1.20–3.04; p=0.006) [PMID:40256659](../papers/40256659.md).
- [ERBB2](../genes/ERBB2.md) alterations (14% cfDNA) associated with shorter OS (HR 1.64, 95% CI 1.08–2.49; p=0.019) [PMID:40256659](../papers/40256659.md).
- Oncogenic DDR gene alterations detected in 27/201 (13%) cfDNA samples ([ATM](../genes/ATM.md) 5.5%, [ERCC2](../genes/ERCC2.md) 4.5%, [BRCA1](../genes/BRCA1.md) 3%, [BRCA2](../genes/BRCA2.md) 1%); no significant association with response, OS, or PFS [PMID:40256659](../papers/40256659.md).
- cfDNA detected numerically higher alteration rates than matched archival tumor for [PIK3CA](../genes/PIK3CA.md) (17% vs 13%), [RB1](../genes/RB1.md) (14% vs 12%), [ERCC2](../genes/ERCC2.md) (6.5% vs 4.7%), [BRAF](../genes/BRAF.md) (5.6% vs 4.7%), and [KRAS](../genes/KRAS.md) (5.6% vs 3.7%) in the 107-patient concordance subset [PMID:40256659](../papers/40256659.md).

## Sources

- cBioPortal study `blca_msk_2025`. Data available per: Guercio BJ, et al. *Circulating Tumor DNA Features Associated with Outcomes in Metastatic Urothelial Carcinoma Treated with Gemcitabine-Cisplatin: Results from the Phase III Alliance CALGB 90601 Trial.* Eur Urol. 2025. [PMID:40256659](../papers/40256659.md).

*This page was processed by **crosslinker** on **2026-05-04**.*
