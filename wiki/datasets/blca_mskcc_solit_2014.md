---
name: MSKCC Bladder Cancer Genomics Cohort (Solit 2014)
studyId: blca_mskcc_solit_2014
institution: Memorial Sloan Kettering Cancer Center
size: 109
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
panels:
  - msk-impact-panel
tags:
  - bladder-cancer
  - urothelial-carcinoma
  - blca
  - targeted-sequencing
  - msk-impact
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# MSKCC Bladder Cancer Genomics Cohort (Solit 2014)

## Overview

Capture-based massively parallel sequencing (MSK-IMPACT panel) of 109 high-grade urothelial carcinomas of the bladder with matched germline, performed at Memorial Sloan Kettering Cancer Center. The primary goal was to identify genomic markers of recurrence and survival in patients treated with radical cystectomy (n=89 analyzable for prognosis). Reported by Kim et al. (2014) in Eur Urol.

## Composition

- Cancer type: high-grade urothelial carcinoma of the bladder ([BLCA](../cancer_types/BLCA.md))
- 109 patients: tumor + matched germline blood; 89-patient radical cystectomy subset analyzed for prognostic endpoints
- Mean coverage 579× across targeted exons; average 10 mutations per tumor (range 0–46)
- Key clinical variables: pT stage, nodal involvement, recurrence-free survival, cancer-specific survival

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md): capture-based targeted DNA sequencing
- [targeted-dna-seq](../methods/targeted-dna-seq.md)
- Orthogonal full-exon sequencing of STAG2, KDM6A, ARID1A, KMT2D (99.3% concordance with MSK-IMPACT calls)

## Papers using this cohort

- [PMID:25092538](../papers/25092538.md) — Kim et al. 2014, genomic markers of prognosis in high-grade urothelial carcinoma

## Notable findings derived from this cohort

- 240 mutated genes detected; 23 mutated in ≥5% of cases; TP53 most common (57%), enriched in extravesical (69%) and node-positive (77%) disease [PMID:25092538](../papers/25092538.md)
- Recurrent PIK3CA missense mutations (21%) associated with improved recurrence-free survival (HR 0.35, P=0.014) and cancer-specific survival (HR 0.35, P=0.040) after radical cystectomy; PI3K/AKT pathway alteration overall (35%) HR 0.34 for RFS (P=0.006) [PMID:25092538](../papers/25092538.md)
- CDKN2A alterations independently associated with worse outcomes: RFS HR 5.76 (P<0.001), CSS HR 2.94 (P=0.029) [PMID:25092538](../papers/25092538.md)
- KDM6A truncating mutations in 41%; chromatin-modifying gene mutations highly prevalent (83%) but not prognostic [PMID:25092538](../papers/25092538.md)
- STAG2 mutations present but not associated with outcomes (in contrast to some prior reports) [PMID:25092538](../papers/25092538.md)

## Sources

- cBioPortal studyId: blca_mskcc_solit_2014

*This page was processed by **entity-page-writer** on **2026-05-11**.*
