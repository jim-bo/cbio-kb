---
name: Advanced Thyroid Carcinoma MSKCC 2016 (Landa et al.)
studyId: thyroid_mskcc_2016
institution: Memorial Sloan Kettering Cancer Center
size: 117
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel-seq
  - array-cgh
  - microarray-gene-expression
panels:
  - IMPACT341
tags:
  - thyroid-cancer
  - poorly-differentiated-thyroid-carcinoma
  - anaplastic-thyroid-carcinoma
  - msk-impact
  - braf-v600e
  - tert-promoter
  - eif1ax
  - rapid-progression
  - FFPE
processed_by: crosslinker
processed_at: 2026-05-14
---

# Advanced Thyroid Carcinoma MSKCC 2016 (Landa et al.)

## Overview

Patient-derived cohort of 117 advanced thyroid tumors — 84 poorly differentiated thyroid carcinomas ([PDTC](../cancer_types/THPD.md)) and 33 anaplastic thyroid carcinomas ([ATC](../cancer_types/THAP.md)) — collected at MSKCC and profiled by deep targeted sequencing ([MSK-IMPACT](../methods/msk-impact-panel.md) 341-gene panel), array CGH, and transcriptomics. The defining study characterizing the genomic landscape of advanced thyroid cancers and their relationship to papillary thyroid carcinoma (PTC). Data deposited in cBioPortal under studyId `thyroid_mskcc_2016`. [PMID:26878173](../papers/26878173.md)

## Composition

- **117 patient-derived tumors:** 84 [PDTC](../cancer_types/THPD.md) and 33 [ATC](../cancer_types/THAP.md).
- Median age: 58 years (PDTC), 66 years (ATC); female:male 1.5:1 (PDTC) and 1.2:1 (ATC).
- 92/117 primary tumors; 25/117 nodal or distant metastases.
- Paired normal tissue available for 106/117 (78 PDTC, 28 ATC).
- Sample preservation: 80 FFPE / 37 fresh-frozen.
- **Transcriptomics and CNAs** from 37 fresh-frozen tumors (17 PDTC + 20 ATC): Affymetrix U133 Plus 2.0 expression array and Agilent SurePrint G3 1×1M array-CGH; expression data at GEO accession GSE76039.
- Mean sequencing depth: 584× tumor / 236× normal (739× for ATCs due to low purity from macrophage infiltration). [PMID:26878173](../papers/26878173.md)

## Assays / panels (linked)

- [IMPACT341](../methods/IMPACT341.md) — MSK-IMPACT 341-gene targeted capture panel; mean depth 584× tumor / 236× normal.
- [Affymetrix U133 Plus 2.0 array](../methods/affymetrix-u133-plus2.md) — gene expression profiling (37 tumors).
- [Agilent SurePrint G3 1×1M array-CGH](../methods/array-cgh-agilent-1m.md) — copy-number profiling (37 tumors).

## Papers using this cohort

- [PMID:26878173](../papers/26878173.md) — Landa et al., *J Clin Invest* 2016: primary discovery study defining the genomic landscape of PDTC and ATC; used [thca_tcga_pub](../datasets/thca_tcga_pub.md) as reference comparator.

## Notable findings derived from this cohort

- Stepwise mutation-burden increase: median mutations ATC 6 > PDTC 2 > PTC 1 (each pairwise P < 1×10⁻⁴); higher burden in PDTC tracked with older age, larger tumors, distant metastasis, and worse survival [PMID:26878173](../papers/26878173.md).
- [BRAF](../genes/BRAF.md) V600E in 33% PDTC and 45% ATC; RAS mutations in 28% PDTC and 24% ATC; mutually exclusive with [BRAF](../genes/BRAF.md) and gene fusions [PMID:26878173](../papers/26878173.md).
- [TERT](../genes/TERT.md) promoter mutations show stepwise enrichment: 9% PTC → 40% PDTC → 73% ATC; TERT-mutant ATC patients had markedly shorter survival (median 147 vs 732 days, P = 0.03) [PMID:26878173](../papers/26878173.md).
- [EIF1AX](../genes/EIF1AX.md) mutated in ~10% of advanced thyroid cancers with near-perfect co-occurrence with RAS (OR 58.3, P < 0.001); thyroid-specific p.A113splice mutation [PMID:26878173](../papers/26878173.md).
- [TP53](../genes/TP53.md) mutated in 73% ATC vs 8% PDTC (P < 1×10⁻⁴) — a defining dichotomy between the two entities [PMID:26878173](../papers/26878173.md).
- SWI/SNF complex mutations in 36% ATC vs 6% PDTC (P = 1×10⁻⁴); histone methyltransferase mutations in 24% ATC vs 7% PDTC — first systematic characterization of chromatin-modifier disruption in advanced thyroid cancer [PMID:26878173](../papers/26878173.md).
- Gene fusions present in 14% of PDTC (RET/PTC, PAX8-PPARG, [ALK](../genes/ALK.md) fusions) and absent in ATC; novel NUTM1-BRD4 fusion in one ATC [PMID:26878173](../papers/26878173.md).
- BRAF-RAS score (BRS) showed ATCs are uniformly BRAF-like irrespective of driver, consistent with stepwise oncogenesis from differentiated precursors [PMID:26878173](../papers/26878173.md).

## Sources

- cBioPortal study: `thyroid_mskcc_2016`
- Expression data: GEO accession GSE76039
- [PMID:26878173](../papers/26878173.md) — Landa I et al., "Genomic and transcriptomic hallmarks of poorly differentiated and anaplastic thyroid cancers." *J Clin Invest* 2016.

*This page was processed by **crosslinker** on **2026-05-14**.*
