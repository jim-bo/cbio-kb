---
symbol: TSHR
aliases: []
cancer_types:
  - THPA
tags:
  - thyroid-cancer
  - hormone-receptor
  - differentiation
processed_by: crosslinker
processed_at: 2026-05-14
---

# TSHR

## Overview

TSHR (Thyroid Stimulating Hormone Receptor) is a G protein-coupled receptor that mediates TSH signaling to regulate thyroid cell growth, differentiation, and function. TSHR is a key component of the thyroid differentiation program and is tracked as part of the Thyroid Differentiation Score (TDS) in the TCGA PTC analysis. Loss of TSHR expression correlates with dedifferentiation in papillary thyroid carcinoma.

## Alterations observed in the corpus

- TSHR is listed among the genes with somatic alterations in papillary thyroid carcinoma (PTC) in the TCGA PTC cohort (n=496); it is a component of the 16-gene Thyroid Differentiation Score (TDS) used to quantify thyroid metabolic and functional gene expression. [PMID:25417114](../papers/25417114.md)
- TDS (which includes TSHR expression) strongly correlated with the BRAFV600E-RAS Score (BRS) (Spearman 0.78, p=3.1×10⁻⁸⁰) and with [TERT](../genes/TERT.md) promoter mutations (Kruskal-Wallis p=4.2×10⁻⁵); BRAFV600E-positive low-TDS tumors had the worst prognosis. [PMID:25417114](../papers/25417114.md)

## Cancer types (linked)

- **[THPA](../cancer_types/THPA.md) (Papillary Thyroid Carcinoma):** TSHR expression is a component of the TDS; low TSHR/TDS correlates with aggressive BRAFV600E-driven PTC, high MACIS score (Spearman p=1.3×10⁻¹¹), high risk of recurrence, and older age. [PMID:25417114](../papers/25417114.md)

## Co-occurrence and mutual exclusivity

- Low TSHR/TDS is associated with BRAFV600E tumors (BVL phenotype) and [TERT](../genes/TERT.md) promoter mutations in PTC, reflecting a dedifferentiated, high-risk subset. [PMID:25417114](../papers/25417114.md)

## Therapeutic relevance

- TSHR expression levels contribute to thyroid differentiation scoring (TDS), which may guide patient stratification for radioiodine therapy (which requires a functional thyroid differentiation program). Low TDS/TSHR PTCs are candidates for redifferentiation therapy or BRAF-targeted approaches. [PMID:25417114](../papers/25417114.md)

## Open questions

- Specific somatic mutation frequency of TSHR in PTC and functional consequences of TSHR mutations (activating vs. inactivating) in the TCGA cohort are not detailed in the extracted data.
- Whether TSHR expression level provides independent prognostic value beyond BRAFV600E and TERT promoter status in PTC requires prospective validation.

## Sources

- [PMID:25417114](../papers/25417114.md) — TCGA integrated genomic characterization of 496 papillary thyroid carcinomas.

*This page was processed by **crosslinker** on **2026-05-14**.*
