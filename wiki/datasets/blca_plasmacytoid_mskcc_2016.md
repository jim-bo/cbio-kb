---
name: Plasmacytoid Bladder Carcinoma MSKCC 2016 (Al-Ahmadie et al.)
studyId: blca_plasmacytoid_mskcc_2016
institution: Memorial Sloan Kettering Cancer Center
size: 31
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - targeted-panel-seq
  - bisulfite-seq
  - immunohistochemistry
panels:
  - IMPACT341
tags:
  - bladder-cancer
  - plasmacytoid-variant
  - urothelial-carcinoma
  - cdh1
  - e-cadherin
  - msk-impact
  - multi-cohort
processed_by: crosslinker
processed_at: 2026-05-14
---

# Plasmacytoid Bladder Carcinoma MSKCC 2016 (Al-Ahmadie et al.)

## Overview

Multi-cohort study of 31 plasmacytoid-variant bladder carcinomas ([SRCBC](../cancer_types/SRCBC.md)) profiled at MSKCC by whole-exome sequencing, targeted panel sequencing ([MSK-IMPACT](../methods/msk-impact-panel.md) 341-gene panel), and bisulfite sequencing of the [CDH1](../genes/CDH1.md) promoter. Represents the defining genomic characterization of this aggressive histologic variant, establishing truncating somatic [CDH1](../genes/CDH1.md) mutations and E-cadherin loss as pathognomonic events. An additional prospective clinical outcome cohort of 53 MSKCC patients is linked. Registered in cBioPortal as `blca_plasmacytoid_mskcc_2016`. [PMID:26901067](../papers/26901067.md)

## Composition

- **Discovery cohort:** 6 plasmacytoid-variant tumors with matched normal, profiled by whole-exome sequencing (SureSelect XT Human All Exon V4, HiSeq 2500, ~63M read pairs/sample, 94.4% of targets at ≥30×).
- **Validation cohort:** 19 additional plasmacytoid-variant tumors by a 300-gene exon-capture panel, plus 6 profiled with the CLIA-certified [MSK-IMPACT 341-gene panel](../methods/IMPACT341.md).
- **Prospective clinical cohort:** 62 invasive bladder cancer patients prospectively sequenced at MSKCC; 6 plasmacytoid-variant and 56 urothelial carcinoma NOS.
- **Clinical outcome cohort:** 53 MSKCC patients with predominantly plasmacytoid histology treated 7/1994–4/2014; 37 included in survival analyses. Compared against 978 patients with pure urothelial carcinoma, NOS (5/2001–3/2010). Median follow-up among survivors: 71.8 months.
- Cancer type: [SRCBC](../cancer_types/SRCBC.md) (plasmacytoid/signet-ring-cell bladder carcinoma), a variant of [BLCA](../cancer_types/BLCA.md).
- All molecular samples are single-institution (MSKCC pathology archive); centralized histologic review performed. [PMID:26901067](../papers/26901067.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — SureSelect XT Human All Exon V4, Illumina HiSeq 2500 (discovery cohort, n=6).
- [targeted-dna-seq](../methods/targeted-dna-seq.md) — 300-gene exon-capture panel (validation, n=19).
- [IMPACT341](../methods/IMPACT341.md) — MSK-IMPACT 341-gene CLIA-certified panel (validation, n=6; prospective, n=62).
- [whole-genome-bisulfite-seq](../methods/whole-genome-bisulfite-seq.md) — CDH1 promoter CpG island methylation (CDH1 WT tumors, n=5).
- [immunohistochemistry](../methods/immunohistochemistry.md) — E-cadherin IHC across all 31 plasmacytoid tumors.

## Papers using this cohort

- [PMID:26901067](../papers/26901067.md) — Al-Ahmadie et al., *Nat Genet* 2016: primary discovery study defining CDH1 mutations as the pathognomonic event in plasmacytoid-variant bladder cancer.

## Notable findings derived from this cohort

- CDH1 truncating mutations in 84% of plasmacytoid-variant tumors (vs. 0% in 127 TCGA urothelial NOS tumors from [blca_tcga_pub](../datasets/blca_tcga_pub.md)); E-cadherin loss is universal across all 31 plasmacytoid tumors [PMID:26901067](../papers/26901067.md).
- Promoter hypermethylation accounts for 4/5 mutation-negative plasmacytoid cases; no germline CDH1 alterations detected [PMID:26901067](../papers/26901067.md).
- Multi-region exon capture of one mixed tumor demonstrated that CDH1 Y68fs is plasmacytoid-specific while [CDKN1A](../genes/CDKN1A.md) (A45fs) and [PIK3C2G](../genes/PIK3C2G.md) (S48R) are truncal, supporting common precursor with urothelial NOS [PMID:26901067](../papers/26901067.md).
- Co-mutation profile beyond CDH1 resembles conventional urothelial carcinoma: recurrent [TP53](../genes/TP53.md), [RB1](../genes/RB1.md), [ARID1A](../genes/ARID1A.md), [ERBB2](../genes/ERBB2.md), [PIK3CA](../genes/PIK3CA.md), and [TSC1](../genes/TSC1.md) alterations flagged as clinically actionable [PMID:26901067](../papers/26901067.md).
- Plasmacytoid-variant patients have higher cumulative incidence of local recurrence and cancer-specific mortality than urothelial NOS; CRISPR/Cas9 CDH1 knockout in RT4 and MGHU4 cells enhanced migration, providing a mechanistic basis for the variant's peritoneal spread pattern [PMID:26901067](../papers/26901067.md).

## Sources

- cBioPortal study: `blca_plasmacytoid_mskcc_2016`
- [PMID:26901067](../papers/26901067.md) — Al-Ahmadie HA et al., "Truncating somatic alterations in the CDH1 gene define the plasmacytoid variant of urothelial carcinoma." *Nat Genet* 2016.

*This page was processed by **crosslinker** on **2026-05-14**.*
