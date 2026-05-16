---
name: Columbia GBM Anti-PD-1 Immunotherapy Cohort (gbm_columbia_2019)
studyId: gbm_columbia_2019
institution: Columbia University (primary, n=46); Northwestern University (n=20)
size: 66
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - bulk-rna-seq
  - single-cell-rna-seq
  - multiplexed-immunofluorescence
  - tcr-bcr-repertoire-seq
panels: []
tags:
  - glioblastoma
  - gbm
  - immunotherapy
  - anti-PD-1
  - nivolumab
  - pembrolizumab
  - PTEN
  - tumor microenvironment
processed_by: crosslinker
processed_at: 2026-05-16
---

# Columbia GBM Anti-PD-1 Immunotherapy Cohort (gbm_columbia_2019)

## Overview

Retrospective two-institution cohort of 66 adult patients with recurrent [GBM](../cancer_types/GBM.md) treated with PD-1 inhibitors ([nivolumab](../drugs/nivolumab.md) or [pembrolizumab](../drugs/pembrolizumab.md)) at Columbia University (n=46) and Northwestern University (n=20). All patients had received standard [temozolomide](../drugs/temozolomide.md) plus radiation prior to PD-1 inhibitor therapy. The study applied whole-exome sequencing, RNA-seq, single-cell RNA-seq (9,000 cells across 3 GBMs), quantitative multiplex immunofluorescence, and TCR/immunoglobulin repertoire profiling to identify genomic and microenvironmental determinants of response. Data deposited in cBioPortal as study `gbm_columbia_2019`. The [gbm_tcga](../datasets/gbm_tcga.md) IDH1-wildtype cohort (n=458/503) was used as a background reference for mutation-frequency comparisons.

## Composition

- **66 adult patients**: 17 long-term responders (≥6 months MRI-stable or pathologically predominantly inflammatory); 49 non-responders.
- **Cancer type:** recurrent [GBM](../cancer_types/GBM.md); [IDH1](../genes/IDH1.md) mutation status tested in 56 patients (11/56 IDH1-mutant, excluded from primary enrichment analysis).
- **Data modalities:** 58 matched tumor/blood whole exomes (~100× tumor, ~60× normal); 38 transcriptomes (longitudinal); cancer gene panel for 39 patients; single-cell RNA-seq from 9,000 cells across 3 GBMs; quantitative multiplex immunofluorescence (Opal/Vectra) on FFPE specimens from 17 patients with paired pre/post anti-PD-1 samples.
- **Bioinformatics:** reads mapped by [BWA](../methods/bwa.md) to hg19; somatic mutations by SAVI2; copy-number by [CNVkit](../methods/cnvkit.md); tumor purity by [ABSOLUTE](../methods/absolute.md); HLA typed by [POLYSOLVER](../methods/polysolver.md); RNA aligned by [STAR](../methods/star-aligner.md); pathway scoring by [ssGSEA/GSEA](../methods/gsea.md).

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — 58 matched tumor/blood pairs; ~100× tumor coverage.
- [Bulk RNA-seq](../methods/rna-seq.md) — 38 transcriptomes including longitudinal paired samples.
- [Single-cell RNA-seq](../methods/single-cell-rna-seq.md) — 9,000 cells from 3 GBMs.
- [Multiplexed immunofluorescence](../methods/multiplexed-immunofluorescence.md) — Opal/Vectra panel (CD3, CD8, [CD68](../genes/CD68.md), HLA-DR, PD-L1, [SOX2](../genes/SOX2.md)) on FFPE specimens.

## Papers using this cohort

- [PMID:30742119](../papers/30742119.md) — Zhao et al. 2019, *Nature Medicine*: [PTEN](../genes/PTEN.md) mutations and MAPK alterations as predictors of anti-PD-1 response in recurrent [GBM](../cancer_types/GBM.md); branched evolutionary dynamics in responders.

## Notable findings derived from this cohort

- [PTEN](../genes/PTEN.md) mutations enriched in non-responders among IDH1-wildtype tumors: 23/32 non-responders vs 3/13 responders (Fisher p=0.0063, OR=8.5, FDR-corrected p<0.05). PTEN-mutant tumors had an immunosuppressive [CD44](../genes/CD44.md)+ tumor-cell signature, lower tumor purity, and more [CD68](../genes/CD68.md)+HLA-DR- macrophages (p=0.011). [PMID:30742119](../papers/30742119.md)
- MAPK pathway alterations ([BRAF](../genes/BRAF.md), [PTPN11](../genes/PTPN11.md)) enriched in responders: 4/13 responders vs 1/32 non-responders (OR=12.8, p=0.019 within cohort; vs TCGA background: Fisher p=0.018, OR=5.1). [PMID:30742119](../papers/30742119.md)
- Tumor mutation burden and neoepitope load were not associated with response (median 47 nsSNVs; responders vs non-responders p=0.11); PD-L1 ([CD274](../genes/CD274.md)) RNA expression was not predictive (p=0.374). [PMID:30742119](../papers/30742119.md)
- Responders showed branched clonal evolution with elimination of predicted expressed neoepitopes; non-responders followed linear evolution (based on 5 patients with paired pre/post WES samples). [PMID:30742119](../papers/30742119.md)
- Responders had significantly better post-treatment survival (median 14.3 months vs 10.1 months for non-responders, p=0.0081 log-rank; full cohort 15.5 vs 5.7 months, p=2.2e-5). [PMID:30742119](../papers/30742119.md)
- Pre-treatment regulatory T-cell ([FOXP3](../genes/FOXP3.md)) signature enriched in non-responders (p=0.037); single-cell RNA-seq localized the immunosuppressive signature to [CD44](../genes/CD44.md)+ tumor cells (not [CD4](../genes/CD4.md)+[FOXP3](../genes/FOXP3.md)+ Tregs) in a PTEN-mutant GBM. [PMID:30742119](../papers/30742119.md)
- Non-responders had greater increase in T-cell clonal diversity (Shannon entropy, p=0.024) and B-cell clonality (p=0.048) after treatment, consistent with failure of selective lymphocyte recruitment. [PMID:30742119](../papers/30742119.md)

## Sources

- cBioPortal study: `gbm_columbia_2019` — https://www.cbioportal.org/study/summary?id=gbm_columbia_2019
- [PMID:30742119](../papers/30742119.md) — Zhao et al. 2019, *Nature Medicine*, DOI 10.1038/s41591-019-0349-y

*This page was processed by **crosslinker** on **2026-05-16**.*
