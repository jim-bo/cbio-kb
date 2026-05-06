---
name: Johns Hopkins Pancreatic Neuroendocrine Tumor Exome Sequencing
studyId: panet_jhu_2011
institution: Johns Hopkins University / Memorial Sloan Kettering Cancer Center
size: 68
reference_genome: hg18
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
panels: []
tags:
  - pancreatic-neuroendocrine-tumor
  - panet
  - whole-exome-sequencing
  - chromatin-remodeling
  - mtor
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Johns Hopkins Pancreatic Neuroendocrine Tumor Exome Sequencing

## Overview

Whole-exome sequencing study of 68 sporadic, non-familial pancreatic neuroendocrine tumors (PanNETs) from Johns Hopkins University and Memorial Sloan Kettering Cancer Center. The study used a two-stage design: 10 tumors for whole-exome discovery (Illumina GAIIx with SureSelect capture, mean 101x coverage) and 58 additional tumors for targeted Sanger validation. Familial syndrome-associated tumors and small cell/large cell neuroendocrine carcinomas were excluded. All tumors were microdissected to >80% neoplastic cellularity.

## Composition

- Cancer type: [PANET](../cancer_types/PANET.md)
- 68 sporadic PanNETs: 10 discovery (WES) + 58 validation (Sanger)
- Key clinical fields: survival, stage, grade, Ki-67 index, metastatic status
- Assays: [whole-exome-seq](../methods/whole-exome-seq.md) (discovery set) and [sanger-sequencing](../methods/sanger-sequencing.md) (validation set)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Illumina GAIIx, SureSelect capture, ~18,000 genes
- [sanger-sequencing](../methods/sanger-sequencing.md) — targeted validation in 58 additional cases

## Papers using this cohort

- [PMID:21252315](../papers/21252315.md) — Jiao et al. 2011, exome sequencing of PanNETs identifying MEN1/DAXX/ATRX driver landscape

## Notable findings derived from this cohort

- [MEN1](../genes/MEN1.md) mutated in 44.1% (30/68) of PanNETs; 25/30 mutations were inactivating (indels, nonsense, splice-site) [PMID:21252315](../papers/21252315.md)
- [DAXX](../genes/DAXX.md) mutated in 25% and [ATRX](../genes/ATRX.md) in 17.6%; mutations were mutually exclusive; combined DAXX/ATRX pathway alteration rate 42.6% [PMID:21252315](../papers/21252315.md)
- mTOR pathway genes mutated in 14%: [PTEN](../genes/PTEN.md) 7.3%, [TSC2](../genes/TSC2.md) 8.8%, [PIK3CA](../genes/PIK3CA.md) 1.4% [PMID:21252315](../papers/21252315.md)
- [MEN1](../genes/MEN1.md) and DAXX/ATRX mutations associated with significantly better prognosis: 100% survival at 10 years vs. >60% mortality within 5 years in mutation-negative patients [PMID:21252315](../papers/21252315.md)
- PanNETs have a distinct genetic landscape from pancreatic ductal adenocarcinoma: [KRAS](../genes/KRAS.md) 0% and [TP53](../genes/TP53.md) 3% in PanNETs vs. ~100% and ~85% in PDAC [PMID:21252315](../papers/21252315.md)
- Mean 16 somatic mutations per tumor; 91% of discovery-set mutations validated by Sanger sequencing [PMID:21252315](../papers/21252315.md)

## Sources

- [PMID:21252315](../papers/21252315.md) — Jiao et al., "DAXX/ATRX, MEN1, and mTOR pathway genes are frequently altered in pancreatic neuroendocrine tumors," *Science* 2011

*This page was processed by **entity-page-writer** on **2026-05-06**.*
