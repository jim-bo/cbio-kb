---
name: MSK HCC Prospective IMPACT Cohort (2018)
studyId: hcc_mskimpact_2018
institution: Memorial Sloan Kettering Cancer Center
size: 127
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - hepatocellular-carcinoma
  - HCC
  - msk-impact
  - sorafenib
  - immune-checkpoint-inhibitor
  - wnt-pathway
  - pi3k-mtor-pathway
  - prospective-sequencing
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK HCC Prospective IMPACT Cohort (2018)

## Overview

A prospective single-institution cohort of 127 unique patients with advanced hepatocellular carcinoma ([HCC](../cancer_types/HCC.md)) sequenced at MSKCC under protocol NCT01775072 (August 2014 – August 2017) using the MSK-IMPACT targeted NGS assay. The study linked genotype to clinical outcomes on systemic therapy — specifically [sorafenib](../drugs/sorafenib.md) (n=81) and immune checkpoint inhibitors (ICI; n=31). Key findings were a PI3K-mTOR pathway predictive biomarker for sorafenib resistance and a WNT/β-catenin pathway predictive biomarker for ICI innate resistance. All data are available at cBioPortal (study `hcc_mskimpact_2018`) and cBioPortal DataHub. [PMID:30373752](../papers/30373752.md)

## Composition

- **127 unique patients** (134 specimens, including 7 serial biopsies); enrolled August 2014 – August 2017 at MSKCC. [PMID:30373752](../papers/30373752.md)
- **Cancer type:** conventional [HCC](../cancer_types/HCC.md); fibrolamellar and biphenotypic HCC-cholangiocarcinoma excluded. [PMID:30373752](../papers/30373752.md)
- **Demographics:** 79% male, 76% non-Asian; etiology HBV 17%, HCV 35%, nonviral 49%; BCLC stage A 29%, B 40%, C 30%. [PMID:30373752](../papers/30373752.md)
- **MSK-IMPACT panels:** [IMPACT341](../methods/IMPACT341.md) (21 cases), [IMPACT410](../methods/IMPACT410.md) (70 cases), [IMPACT468](../methods/IMPACT468.md) (36 cases); Illumina HiSeq 2500; mean coverage 690-fold; median tumor purity 60%. [PMID:30373752](../papers/30373752.md)
- **TMB and MSI:** TMB calculated per sample; MSI via [MSIsensor](../methods/msisensor.md) (MSI-H threshold ≥10 repeats). [PMID:30373752](../papers/30373752.md)
- **Treatment subsets:** sorafenib n=81 (75 first-line, 6 second-line); ICI n=31 (1 anti-CTLA-4 monotherapy, 25 anti-PD-1/PD-L1 monotherapy, 5 combination). [PMID:30373752](../papers/30373752.md)
- **Reference comparator:** TCGA HCC cohort ([lihc_tcga_pan_can_atlas_2018](../datasets/lihc_tcga_pan_can_atlas_2018.md)), N=196. [PMID:30373752](../papers/30373752.md)
- **Reference genome:** GRCh37

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md)
- [IMPACT341](../methods/IMPACT341.md)
- [IMPACT410](../methods/IMPACT410.md)
- [IMPACT468](../methods/IMPACT468.md)
- [msisensor](../methods/msisensor.md) — MSI status
- [oncokb-annotation](../methods/oncokb-annotation.md) — variant actionability tier 1–4 filtering

## Papers using this cohort

- [PMID:30373752](../papers/30373752.md) — Harding et al. 2019, "Prospective Genotyping of Hepatocellular Carcinoma: Clinical Implications of Next-Generation Sequencing for Matching Patients to Targeted and Immune Therapies," *Clinical Cancer Research*

## Notable findings derived from this cohort

- **Mutational landscape (134 specimens):** alterations detected in 95%; most frequent genes: [TERT](../genes/TERT.md) 55.6%, [CTNNB1](../genes/CTNNB1.md) 35.7%, [TP53](../genes/TP53.md) 32.5%, [ARID1A](../genes/ARID1A.md) 12.7%, [TSC2](../genes/TSC2.md) 10.6%. [PMID:30373752](../papers/30373752.md)
- **Mutual exclusivity:** [TP53](../genes/TP53.md) mutations vs. WNT pathway alterations (p=0.003) defines at least two major HCC genomic subsets. [PMID:30373752](../papers/30373752.md)
- **Sorafenib (n=81, 79 evaluable):** median PFS 4.8 months, median [OS](../cancer_types/OS.md) 16.4 months. Oncogenic PI3K-mTOR pathway alterations (n=12) associated with markedly shorter PFS (1.9 vs. 5.3 months; HR 3.8, 95% CI 2.0–7.5, p<0.0001) and OS (10.4 vs. 17.9 months; HR 2.5, p=0.01). [PMID:30373752](../papers/30373752.md)
- **Immune checkpoint inhibitors (n=31, 27 evaluable):** ORR 11.1%; activating WNT/β-catenin alterations ([CTNNB1](../genes/CTNNB1.md) gain-of-function or [AXIN1](../genes/AXIN1.md) loss) in 10 patients yielded 0/10 clinical benefit vs. 9/17 (53%) for non-WNT patients (p=0.009); WNT PFS 2.0 vs. 7.4 months (HR 9.2, 95% CI 2.9–28.8, p<0.0001). [PMID:30373752](../papers/30373752.md)
- **TMB not predictive for ICI:** median TMB 4.08 overall; no MSI-H cases; TMB did not stratify ICI response (median 3.8 vs. 3.9 mutations/Mb, p=0.98). [PMID:30373752](../papers/30373752.md)
- **Actionability:** 24% of patients harbored ≥1 actionable alteration via OncoKB; no level 1/2A alterations. Actionable hits include [TSC2](../genes/TSC2.md) 7%, [FGF19](../genes/FGF19.md) amplification 6.3%, [PTEN](../genes/PTEN.md) 3.9%, [MET](../genes/MET.md) amplification 1.5%. [PMID:30373752](../papers/30373752.md)
- **Genome-matched therapy:** 5/87 (5.7%) systemically-treated patients matched to genome-directed therapy; 4 received [everolimus](../drugs/everolimus.md) for TSC1/2-altered HCC; 3/4 achieved ≥5 months clinical benefit. [PMID:30373752](../papers/30373752.md)
- **Etiology:** virally mediated HCC enriched for [TP53](../genes/TP53.md) mutations vs. nonviral (45% vs. 21%, p=0.001). [PMID:30373752](../papers/30373752.md)

## Sources

- cBioPortal study ID: `hcc_mskimpact_2018`
- cBioPortal DataHub
- NCT01775072
- [PMID:30373752](../papers/30373752.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
