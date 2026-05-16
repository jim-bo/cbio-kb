---
name: Oncotator
slug: oncotator
kind: method
canonical_source: corpus
unverified: true
tags: [variant-annotation, bioinformatics, cancer-genomics]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Oncotator

## Overview

Oncotator is a cancer-focused variant annotation tool developed at the Broad Institute. It annotates somatic mutations with information from multiple cancer-specific databases including COSMIC, OncoKB, and UniProt, providing protein change information, functional impact predictions, and known oncogenicity classifications specifically tailored to somatic variant interpretation.

## Used by

- Applied alongside [annovar](../methods/annovar.md) for somatic variant annotation in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases); annotated SNVs and indels discovered by genome-wide sequencing in the pediatric brain tumor cohort [PMID:23817572](../papers/23817572.md)
- Used to annotate somatic variants from whole-exome sequencing of 45 [BRAF](../genes/BRAF.md) V600 metastatic melanoma tumors (DeCOG cohort) aligned to hg19 via the Broad Picard/Firehose pipeline [PMID:24265153](../papers/24265153.md).
- Used for somatic variant annotation in the rhabdomyosarcoma genomic landscape study (147 tumor/normal pairs); applied alongside ANNOVAR to annotate mutation consequences, known cancer hotspots, and pathway membership; reference build hg19 [PMID:24436047](../papers/24436047.md)
- Used to annotate somatic variants in 50 urothelial carcinoma tumors in the cisplatin-response WES study. [PMID:25096233](../papers/25096233.md)
- Used to annotate somatic variants in 69 matched CRC trios with COSMIC v65 annotations as part of the MSK-IMPACT concordance study. [PMID:25164765](../papers/25164765.md)
- Used to annotate somatic variants against dbSNP 134 and 1000 Genomes in the [DFCI-ONCOPANEL-1](../methods/DFCI-ONCOPANEL-1.md) pipeline for 29 metastatic cSCC samples; identified high UV-signature mutation rate (~33 mut/Mb) and recurrent RAS/RTK/PI3K pathway activating mutations [PMID:25589618](../papers/25589618.md)
- Oncotator used for variant annotation alongside Alamut in 243 [HCC](../cancer_types/HCC.md) exomes to classify somatic mutations for driver discovery. [PMID:25822088](../papers/25822088.md)
- Broad Institute Oncotator used to annotate somatic mutations identified by MuTect and VarScan in 109 microdissected PDA exomes. [PMID:25855536](../papers/25855536.md)
- Oncotator used for somatic mutation annotation in colorectal cancer genomic analysis [PMID:26343386](../papers/26343386.md)
- Oncotator used for functional annotation of somatic variants in 114 metastatic CRPC biopsies (whole-exome sequencing pipeline); variants annotated to identify non-silent SNVs and driver gene alterations [PMID:26855148](../papers/26855148.md)
- Used for SNV/INDEL annotation in anti-PD-1-treated metastatic melanoma WES data (38 tumor/normal pairs) [PMID:26997480](../papers/26997480.md)
- Used to annotate somatic variants identified by MuTect and SNVseeqer in 72 urothelial carcinoma tumours for functional classification. [PMID:27749842](../papers/27749842.md)
- Oncotator used to annotate somatic mutations pooled from four sequencing centers (Broad, Washington University, UCSC, BCCA) in the TCGA esophageal/stomach study of 164 oesophageal carcinomas [PMID:28052061](../papers/28052061.md).
- Variants from 304 DLBCLs annotated with Oncotator after MuTect/Indelocator calling [PMID:29713087](../papers/29713087.md)
- Used for variant annotation in the uniform somatic-calling pipeline (MuTect + Strelka + Oncotator) applied to 249 MSS tumor/normal WES samples from seven ICB cohorts [PMID:30150660](../papers/30150660.md)
- Used for somatic variant annotation in the high-grade UTUC WES study (37 tumor-normal pairs); re-annotated external TCGA (894) and Foundation Medicine (739) reference cohorts with VEP v88 via [vcf2maf](../methods/vcf2maf.md) alongside Oncotator [PMID:31278255](../papers/31278255.md)
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the lung_nci_2022 cohort [PMID:34493867](../papers/34493867.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Now largely superseded by Funcotator in GATK4 workflows, but widely used in early TCGA-era analyses.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24265153](../papers/24265153.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25096233](../papers/25096233.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25589618](../papers/25589618.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25822088](../papers/25822088.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25855536](../papers/25855536.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26343386](../papers/26343386.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26855148](../papers/26855148.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26997480](../papers/26997480.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27749842](../papers/27749842.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:29713087](../papers/29713087.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30150660](../papers/30150660.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
