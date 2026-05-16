---
name: Dana-Farber / MSKCC Bladder Urothelial Carcinoma Cisplatin Response (2014)
studyId: blca_dfarber_mskcc_2014
institution: Dana-Farber Cancer Institute / Memorial Sloan Kettering Cancer Center
size: "50"
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - urothelial-carcinoma
  - muscle-invasive-bladder-cancer
  - neoadjuvant-chemotherapy
  - cisplatin-response
  - dna-repair
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Dana-Farber / MSKCC Bladder Urothelial Carcinoma Cisplatin Response (2014)

## Overview

50-patient extreme-phenotype cohort of muscle-invasive urothelial carcinoma ([BLCA](../cancer_types/BLCA.md)) collected under Dana-Farber protocols 02-021/11-334 and MSKCC protocols 89-076/09-025. Cases were selected for neoadjuvant cisplatin-based chemotherapy followed by cystectomy, balanced 25 responders (pT0/pTis) vs. 25 non-responders (residual ≥pT2). Pre-treatment tumor and paired germline DNA were sequenced by whole-exome sequencing at mean 121× tumor / 130× germline coverage (hg19).

## Composition

- 50 patients; 25 cisplatin responders (no residual invasive disease), 25 non-responders (residual ≥pT2 disease).
- Cancer type: [BLCA](../cancer_types/BLCA.md).
- Assay: [whole-exome-seq](../methods/whole-exome-seq.md) (SureSelect v2, Illumina HiSeq); orthogonal amplicon validation by Fluidigm Access Array / MiSeq (35/50 cases).
- Variant calling: [mutect](../methods/mutect.md) (SNVs), [indelocator](../methods/indelocator.md) (indels), significance by [mutsig](../methods/mutsig.md) (MutSigCV).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)

## Papers using this cohort

- [PMID:25096233](../papers/25096233.md)

## Notable findings derived from this cohort

- [ERCC2](../genes/ERCC2.md) somatic mutations were found exclusively in cisplatin responders (9/25, 36% vs. 0/25 non-responders; q = 0.007), proposing ERCC2 as a predictive biomarker for cisplatin sensitivity in muscle-invasive urothelial carcinoma [PMID:25096233](../papers/25096233.md).
- Responders had significantly higher median mutation rate (9.7 vs 4.4 mutations/Mb; P = 0.0003); MutSigCV nominated [TP53](../genes/TP53.md), [RB1](../genes/RB1.md), [KDM6A](../genes/KDM6A.md), and [ARID1A](../genes/ARID1A.md) as significantly mutated across the full cohort [PMID:25096233](../papers/25096233.md).
- DFCI/MSKCC cohort used for ZFP36-family mutation frequency cross-validation in bladder cancer; ZFP36-family mutations reach ~9–10% across blca_dfarber_mskcc_2014 and two other bladder cohorts [PMID:33397444](../papers/33397444.md)

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:33397444](../papers/33397444.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
