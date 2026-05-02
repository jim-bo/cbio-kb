---
name: Multiparameter flow cytometry
slug: multiparameter-flow-cytometry
kind: method
canonical_source: corpus
unverified: true
tags: [immunophenotyping, flow-cytometry, peripheral-blood, biomarker]
processed_by: crosslinker
processed_at: 2026-04-30
---

# Multiparameter flow cytometry

## Overview

Multiparameter flow cytometry simultaneously measures multiple fluorescence-labeled surface or intracellular markers on individual cells in suspension, enabling quantitative immunophenotyping of cell populations at high throughput. In clinical oncology research, it is applied to peripheral blood mononuclear cells (PBMCs) to track immune-cell subsets longitudinally as pharmacodynamic biomarkers for immunotherapy. Panel configurations typically include lineage markers ([CD4](../genes/CD4.md), CD8), activation/exhaustion markers (PD-1, TIM-3), regulatory T-cell markers ([FOXP3](../genes/FOXP3.md)), and proliferation markers (Ki-67).

## Used by

- [PMID:38780927](../papers/38780927.md) — serial multiparameter flow cytometry of PBMCs from 51 patients on NCT03521570 at baseline, before each [nivolumab](../drugs/nivolumab.md) infusion during radiation, and at weeks 18, 30, 52, and 104; panel included CD4+, CD8+, FOXP3+, PD-1+ ([PDCD1](../genes/PDCD1.md)), and Ki-67+ ([MKI67](../genes/MKI67.md)) T-cell subsets. A ≥1.5-fold increase in PD-1+Ki-67+CD4+ T cells at week 2 or 4 trended toward worse PFS (HR 2.09, 95% CI 0.77–5.66, P = .14), contrary to analogous findings in lung cancer and melanoma [PMID:38780927](../papers/38780927.md).
- [PMID:41941260](../papers/41941260.md) — plasma immune profiling by flow cytometry is listed among the biospecimen assays in the ROBIN consortium Molecular Characterization Trials (MCTs), specifically in the OligoMET and ImmunoRad centers, for longitudinal immune monitoring of patients undergoing radiation therapy; used alongside scRNA-seq of PBMCs and T-cell receptor repertoire sequencing to characterize systemic immune responses pre- and post-RT [PMID:41941260](../papers/41941260.md).

## Notes

- The paradoxical association of early CD4+PD-1+Ki-67+ T-cell proliferative surge with worse PFS in the reirradiation context warrants prospective validation; the mechanism (regulatory skew, exhaustion, lymphatic effects of prior radiation) is unresolved [PMID:38780927](../papers/38780927.md).
- No correlation between CD8+ T-cell surge and PFS was observed; FOXP3+ T-cell surge trended toward worse PFS (HR 1.42, P = .43) without reaching significance [PMID:38780927](../papers/38780927.md).
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:38780927](../papers/38780927.md)
- [PMID:41941260](../papers/41941260.md)

*This page was processed by **crosslinker** on **2026-04-30**.*
