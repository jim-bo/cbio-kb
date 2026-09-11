---
name: Hereditary SDHB-Mutant Pheochromocytomas and Paragangliomas (A5 Consortium, Nature Comm 2025)
studyId: hnsc_a5consortium_2025
institution: A5 Consortium (international multi-site; coordinated by University of Melbourne Centre for Cancer Research, UMCCR-RADIO-Lab)
size: 94
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - rna-seq
  - mirna-seq
  - epic-methylation-array
  - c-circle-assay
  - snrna-seq
  - snatac-seq
panels: []
tags:
  - pheochromocytoma
  - paraganglioma
  - pcpg
  - SDHB
  - hereditary
  - A5-consortium
processed_by: crosslinker
processed_at: 2026-09-11
---

# Hereditary SDHB-Mutant Pheochromocytomas and Paragangliomas (A5 Consortium, Nature Comm 2025)

## Overview

94 primary and/or metastatic pheochromocytoma/paraganglioma ([PCPG](../cancer_types/PCPG.md)) tumors from 79 patients, all carrying pathogenic germline *[SDHB](../genes/SDHB.md)* variants, whole-genome and multi-omic profiled by the international A5 Consortium. Recruitment spanned 11 sites in Australia, the USA and Canada, plus Tufts Medical Center (USA), Waikato Hospital (New Zealand), the National Cancer Centre Singapore, and Uppsala University (Sweden). Name, institution, size (94) and reference genome (hg38) are taken from the cBioPortal study record in `schema/ontology/studies.json`; cBioPortal files this study under the `hnsc` cancer type even though the tumors are PCPG, not head & neck squamous carcinoma [PMID:40097403](../papers/40097403.md).

## Composition

- 94 tumors from 79 patients, all germline [SDHB](../genes/SDHB.md) carriers; histopathology and clinical review confirmed diagnosis in every case [PMID:40097403](../papers/40097403.md).
- Anatomical distribution of primaries: adrenal ([PHC](../cancer_types/PHC.md)) 6, extra-adrenal abdominal/thoracic paraganglioma 64, extra-adrenal bladder paraganglioma 11, head/neck (carotid, nasopharyngeal, vagus) 13 [PMID:40097403](../papers/40097403.md).
- 34/79 patients had confirmed metastatic disease; 40 tumors from 37 patients were non-metastatic with ≥12 months follow-up (median 60 months, range 12–456) [PMID:40097403](../papers/40097403.md).
- Four patients had paired synchronous/metachronous primary tumors, shown by discordant somatic profiles to be clonally independent [PMID:40097403](../papers/40097403.md).

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md), tumor + matched blood (Illumina NovaSeq 6000), n=94 [PMID:40097403](../papers/40097403.md)
- [RNA-seq](../methods/rna-seq.md) n=91, [miRNA-seq](../methods/mirna-seq.md) n=90, [Illumina EPIC methylation array](../methods/epic-methylation-array.md) n=93, [C-circle assay](../methods/c-circle-assay.md) n=89, 10x [snRNA-seq](../methods/snrna-seq.md) n=10, 10x [snATAC-seq](../methods/snatac-seq.md) n=7 [PMID:40097403](../papers/40097403.md)
- Plasma cfDNA sequencing with the [TruSight Oncology 500 ctDNA panel](../methods/trusight-oncology-500.md) (>35,000× depth) plus [ichorCNA](../methods/ichorcna.md) in one patient [PMID:40097403](../papers/40097403.md)

## Papers using this cohort

- [PMID:40097403](../papers/40097403.md) — Aidan et al., A5 Consortium, source publication: whole-genome and multi-omic characterization of hereditary SDHB-mutant PCPG.

## Notable findings derived from this cohort

- Every tumor had somatic 1p36.13 LOH, and SDHB [immunohistochemistry](../methods/immunohistochemistry.md) confirmed SDH deficiency [PMID:40097403](../papers/40097403.md).
- Germline *SDHB* variant spectrum by WGS: missense (n=41), nonsense (n=21), frameshift indels (n=6), large deletions (n=7), donor splice-site variants (n=4); two recurrent large deletions occurred in ≥2 unrelated patients, with homologous sequence at breakpoints implicating homologous recombination as a possible cause [PMID:40097403](../papers/40097403.md).

## Sources

- cBioPortal study record: `hnsc_a5consortium_2025` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:40097403](../papers/40097403.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
