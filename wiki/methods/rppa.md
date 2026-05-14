---
name: Reverse-Phase Protein Array (RPPA)
slug: rppa
kind: PROTEIN_LEVEL
canonical_source: corpus
unverified: true
tags: [proteomics, protein-expression, rppa]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Reverse-Phase Protein Array (RPPA)

## Overview

Reverse-phase protein array (RPPA) is a high-throughput antibody-based platform for quantifying protein and phosphoprotein expression levels across many samples simultaneously. Lysates from tumor tissue are arrayed on nitrocellulose slides and probed with validated antibodies; signal intensity is normalized and used to estimate relative protein abundance. RPPA enables pathway-level proteomics in large cohorts.

## Used by

- Applied to 214 [GBM](../cancer_types/GBM.md) samples (171 antibodies) as part of TCGA [GBM](../cancer_types/GBM.md) 2013 multi-platform analysis; 127/171 antibodies correlated with transcriptomic subtype; revealed non-linear genotype-to-signaling relationships (e.g., RTK-amplified samples had lower downstream p-AKT/S6K/MAPK signaling than expected) [PMID:24120142](../papers/24120142.md)
- Reverse-phase protein array (RPPA) applied to TCGA bladder carcinoma samples for protein and phosphoprotein expression profiling; contributed to multi-platform pathway-level characterization identifying therapeutic targets in 69% of tumors [PMID:24476821](../papers/24476821.md)
- Applied as one of five molecular platforms in the TCGA [HCC](../cancer_types/HCC.md) integrated characterisation of 196 patients alongside DNA copy number, methylation, mRNA, and miRNA [PMID:24798001](../papers/24798001.md)
- RPPA profiling of gastric adenocarcinomas ([stad_tcga_pub](../datasets/stad_tcga_pub.md)) revealed elevated [EGFR](../genes/EGFR.md) pY1068 phosphorylation in the CIN subtype and IL-12 signalling in EBV-positive tumors; used alongside six other molecular platforms [PMID:25079317](../papers/25079317.md)
- RPPA on 181 of 230 lung adenocarcinomas ([luad_tcga_pub](../datasets/luad_tcga_pub.md)) identified three mTOR activation patterns (basal; STK11-low/AMPK-low; high p-AKT/PIK3CA mutation), demonstrating that pathway-state biomarkers complement DNA-based stratification [PMID:25079552](../papers/25079552.md)
- Applied in TCGA PTC study to resolve proteomic differences between BVL (BRAFV600E-driven, high MEK/ERK activation) and RL (RAS-driven, elevated p90RSK phosphorylation, [TSC2](../genes/TSC2.md) inhibition, [BCL2](../genes/BCL2.md) over-expression) subtypes [PMID:25417114](../papers/25417114.md)

## Notes

- Coverage is limited to antibodies in the validated panel; cannot detect novel proteins or isoforms without prior selection.
- Non-linear genotype-to-protein relationships observed in [GBM](../cancer_types/GBM.md) (e.g., PI3K-mutant samples with lower p-AKT than PI3K-WT) highlight the complexity of translating genomic to proteomic signals.
- Widely used in TCGA pan-cancer studies for pathway activation profiling.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24798001](../papers/24798001.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079317](../papers/25079317.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079552](../papers/25079552.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25417114](../papers/25417114.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
