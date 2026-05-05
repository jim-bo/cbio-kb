---
name: MSKCC Sarcoma Genome Project
studyId: sarc_mskcc
institution: Memorial Sloan Kettering Cancer Center
size: 207
reference_genome: hg18
canonical_source: cbioportal
unverified: false
assays:
  - targeted-resequencing-722-genes
  - affymetrix-250k-snp-array
  - oligonucleotide-expression-array
  - sequenom-genotyping
panels: []
tags: [sarcoma, soft-tissue-sarcoma, copy-number, subtype-specific, liposarcoma, leiomyosarcoma, gist]
processed_by: crosslinker
processed_at: 2026-05-04
---

# MSKCC Sarcoma Genome Project

## Overview

The MSKCC Sarcoma Genome Project (`sarc_mskcc`) is an integrative genomic study of 207 high-grade soft tissue sarcomas across seven major subtypes, generated at Memorial Sloan Kettering Cancer Center. Raw data were deposited in NCBI GEO under accession **GSE21124**. The study was published in 2010 and aimed to identify subtype-specific genomic drivers to inform targeted therapy in sarcoma. [PMID:20601955](../papers/20601955.md)

## Composition

- **207 patients** with high-grade soft tissue sarcoma across seven subtypes: [DDLS](../cancer_types/DDLS.md) (n=50, 24.2%), [MRLS](../cancer_types/MRLS.md) (n=21, 10.1%), [PLLS](../cancer_types/PLLS.md) (n=24, 11.6%), [LMS](../cancer_types/LMS.md) (n=27, 13%), [GIST](../cancer_types/GIST.md) (n=22, 10.6%), [MFS](../cancer_types/MFS.md) (n=38, 18.4%), [SYNS](../cancer_types/SYNS.md) (n=24, 11.6%). [PMID:20601955](../papers/20601955.md)
- Targeted resequencing performed on 47 tumor/normal pairs; extended genotyping on 160 additional tumors via [sequenom-genotyping](../methods/sequenom-genotyping.md). [PMID:20601955](../papers/20601955.md)
- Somatic copy-number alterations profiled via [affymetrix-250k-snp-array](../methods/affymetrix-250k-snp-array.md) (n=207); LOH analysis (n=200); oligonucleotide expression arrays (n=149). [PMID:20601955](../papers/20601955.md)

## Assays / panels (linked)

- [affymetrix-250k-snp-array](../methods/affymetrix-250k-snp-array.md) — genome-wide copy-number and LOH profiling (n=207)
- [sequenom-genotyping](../methods/sequenom-genotyping.md) — extended targeted genotyping of 160 additional tumors
- [gistic](../methods/gistic.md) — statistical analysis of significant copy-number alterations
- [shrna-rnai-screen](../methods/shrna-rnai-screen.md) — functional screen of 385 genes (2,007 shRNAs) in three [DDLS](../cancer_types/DDLS.md) cell lines

## Papers using this cohort

- [PMID:20601955](../papers/20601955.md) — Barretina et al. (2010), "Subtype-specific genomic alterations define new targets for soft tissue sarcoma therapy," *Nature Genetics*.

## Notable findings derived from this cohort

- **[TP53](../genes/TP53.md)** mutated in 17% of [PLLS](../cancer_types/PLLS.md); the only subtype in this cohort with TP53 mutations detected. [PMID:20601955](../papers/20601955.md)
- **[NF1](../genes/NF1.md)** mutated in 10.5% of [MFS](../cancer_types/MFS.md) and 8% of [PLLS](../cancer_types/PLLS.md) via point mutations and genomic deletions; biallelic inactivation observed; first report of somatic NF1 alteration outside MPNST/GIST in NF1 patients. [PMID:20601955](../papers/20601955.md)
- **[PIK3CA](../genes/PIK3CA.md)** mutated in 18% (13/71) of [MRLS](../cancer_types/MRLS.md); helical-domain mutations (E542K, E545K) associated with AKT activation and shorter disease-specific survival (log-rank p=0.036). [PMID:20601955](../papers/20601955.md)
- **Chromosome 12q amplification** found in ~90% of [DDLS](../cancer_types/DDLS.md), encompassing [CDK4](../genes/CDK4.md), [MDM2](../genes/MDM2.md), and [YEATS4](../genes/YEATS4.md) as functionally validated therapeutic targets. [PMID:20601955](../papers/20601955.md)
- **CDK4** identified as top dependency in DDLS via shRNA screen; pharmacologic inhibition with [palbociclib](../drugs/palbociclib.md) (PD0332991) induced G1 arrest. [PMID:20601955](../papers/20601955.md)
- **[MRLS](../cancer_types/MRLS.md), [SYNS](../cancer_types/SYNS.md), and [GIST](../cancer_types/GIST.md)** had relatively simple karyotypes; **DDLS, [PLLS](../cancer_types/PLLS.md), [LMS](../cancer_types/LMS.md), and [MFS](../cancer_types/MFS.md)** had complex genomic landscapes. [PMID:20601955](../papers/20601955.md)

## Sources

- NCBI GEO accession: [GSE21124](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE21124)
- cBioPortal study: [sarc_mskcc](https://www.cbioportal.org/study/summary?id=sarc_mskcc)
- Primary publication: [PMID:20601955](../papers/20601955.md)

*This page was processed by **crosslinker** on **2026-05-04**.*
