---
name: NF Open Science Initiative / JHCNC Nerve Sheath Tumor Biorepository (NTAP)
studyId: nst_nfosi_ntap
institution: Johns Hopkins Comprehensive Neurofibromatosis Center (JHCNC) / NF Open Science Initiative
size: 23
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - patient-derived-xenograft
panels: []
tags:
  - neurofibromatosis-type-1
  - nerve-sheath-tumor
  - mpnst
  - neurofibroma
  - biospecimen-repository
  - pdx
  - data-descriptor
processed_by: crosslinker
processed_at: 2026-05-16
---

# NF Open Science Initiative / JHCNC Nerve Sheath Tumor Biorepository

## Overview

The nst_nfosi_ntap study is a clinically and genomically annotated biospecimen repository of nerve sheath tumors from patients with neurofibromatosis type 1 ([NF1](../genes/NF1.md)), assembled at the Johns Hopkins Comprehensive Neurofibromatosis Center (JHCNC) as part of the NF Open Science Initiative (NTAP). The first data release provides whole-exome sequencing and/or RNA sequencing of 55 tumor samples from 23 unique patients, spanning the cNF → pNF → ANNUBP → [MPNST](../cancer_types/MPNST.md) malignant transformation spectrum, together with derived cell lines and patient-derived xenografts (PDX). Primary data are hosted on Synapse at syn4939902; code archived via Zenodo (DOI 10.5281/zenodo.3726380). [PMID:32561749](../papers/32561749.md)

## Composition

- **23 NF1 patients**, **55 tumor samples** (tumor biopsies plus derived cell lines and PDX where available).
- Histologies: cutaneous neurofibroma (cNF), superficial diffuse infiltrating neurofibroma, plexiform neurofibroma (pNF) ([NFIB](../cancer_types/NFIB.md)), atypical neurofibromatous neoplasm of uncertain biologic potential (ANNUBP), and malignant peripheral nerve sheath tumor ([MPNST](../cancer_types/MPNST.md)).
- Includes matched germline DNA (PBMC or, when unavailable, normal adjacent tissue). [PMID:32561749](../papers/32561749.md)
- Reference genome: GRCh37 (hg19). [PMID:32561749](../papers/32561749.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Agilent SureSelectXT HumanAllExon V6 capture, Illumina HiSeq2500, 125-bp paired-end; SNV calling via BWA-MEM → GATK v4.0.1.1 VQSR → Annovar + DeepVariant 0.8 cross-check; CNA via GATK copy-ratio pipeline. [PMID:32561749](../papers/32561749.md)
- [rna-seq](../methods/rna-seq.md) — paired-end on flash-frozen tumor; Salmon 0.11.3 quantification against Gencode v29; 28 retained RNA-seq samples (one cNF dropped for >90% duplication). [PMID:32561749](../papers/32561749.md)
- [patient-derived-xenograft](../methods/patient-derived-xenograft.md) — subcutaneous / pre-tibial / pre-sacral implantation in NSG mice; PDX take rate 50% for [MPNST](../cancer_types/MPNST.md). [PMID:32561749](../papers/32561749.md)

## Papers using this cohort

- [PMID:32561749](../papers/32561749.md) — Pollard et al. (2020), *Scientific Data*: A clinically and genomically annotated nerve sheath tumor biospecimen repository.

## Notable findings derived from this cohort

- Mutational profiles of canonical NF1 nerve-sheath-tumor drivers — [NF1](../genes/NF1.md), [CDKN2A](../genes/CDKN2A.md), [TP53](../genes/TP53.md), [EED](../genes/EED.md)/[SUZ12](../genes/SUZ12.md), and [ATRX](../genes/ATRX.md) — were preserved between original tumor, patient-derived cell line, and PDX, confirming genetic fidelity of the derived models. [PMID:32561749](../papers/32561749.md)
- PRC2 complex alterations ([EED](../genes/EED.md), [SUZ12](../genes/SUZ12.md)) were absent except in the single [MPNST](../cancer_types/MPNST.md) sample, consistent with PRC2 loss as a marker of malignant transformation rather than benign neurofibromas. [PMID:32561749](../papers/32561749.md)
- [NF1](../genes/NF1.md) locus 50% copy-ratio reduction in the MPNST sample (patient 2-031) was recapitulated faithfully in both the derived cell line and xenograft. [PMID:32561749](../papers/32561749.md)
- A second cohort (51 additional WES + 28 additional RNA-seq samples) was described as being processed at the time of publication. [PMID:32561749](../papers/32561749.md)

## Sources

- cBioPortal study: `nst_nfosi_ntap`
- Synapse project: syn4939902 (`http://synapse.org/jhubiobank`)
- Code: `github.com/Sage-Bionetworks/JHU-biobank`; Zenodo DOI 10.5281/zenodo.3726380
- DOI: [10.1038/s41597-020-0508-5](https://doi.org/10.1038/s41597-020-0508-5)

*This page was processed by **crosslinker** on **2026-05-16**.*
