---
name: Neuroblastoma
oncotree_code: NBL
main_type: Peripheral Nervous System
parent: PNS
tags: [pediatric, neuroblastoma, radiation, intra-tumoral-heterogeneity, mibg]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Neuroblastoma (NBL)

## Overview

Neuroblastoma (NBL) is the most common extracranial solid tumor in children, arising from neural [crest](../methods/crest.md) progenitor cells. High-risk neuroblastoma carries poor prognosis despite multimodal therapy including chemotherapy, surgery, RT, and 131I-MIBG targeted radiotherapy. Intra-tumoral heterogeneity is a recently appreciated feature of neuroblastoma and a focus of active investigation; the tumor's low mutational burden makes it tractable for mechanistic radiobiology study.

## Cohorts in the corpus

- ROBIN KIDSROBIN COG ANBL1531 cooperative trial (Harvard University and University of California, San Francisco) — accrual complete; frozen tissue from baseline and post-treatment second-look surgical samples obtained for single-cell spatial profiling (Xenium 10x Genomics). [PMID:41941260](../papers/41941260.md)
- KIDSROBIN NLP cohort — 7,597 clinical notes from 182 NBL patients secured for natural language processing studies. [PMID:41941260](../papers/41941260.md)
- 11 neuroblastoma tumors spanning INRG risk groups and INSS stages (5 high-risk MYCN-amplified/11q-deleted, 1 intermediate, 5 low-risk), 3 postnatal human adrenal glands, and 5 mouse adrenal glands; 4,224 single nuclei sequenced (3,212 high-quality) by Smart-Seq2 snRNA-seq. External validation in a 498-sample SEQC bulk RNA-seq cohort and 172-sample NCI TARGET cohort. [PMID:34493726](../papers/34493726.md)

## Recurrent alterations

No corpus-specific gene-level variant frequencies are reported; the focus is on intra-tumoral heterogeneity and treatment response at single-cell resolution.

- NBL is noted for low mutational burden, making it a genetically simple model alongside [DMG](../cancer_types/DMG.md) for mechanistic RT response research. [PMID:41941260](../papers/41941260.md)
- High-risk tumors are characterized by undifferentiated nC3 cluster cells overexpressing [MYCN](../genes/MYCN.md), [ALK](../genes/ALK.md), [NTRK2](../genes/NTRK2.md) (TRKB), [BCL11A](../genes/BCL11A.md), [TP63](../genes/TP63.md), and mesenchymal markers [PRRX1](../genes/PRRX1.md)/[YAP1](../genes/YAP1.md)/[PDGFRA](../genes/PDGFRA.md); low-risk tumors are dominated by noradrenergic clusters expressing [NTRK1](../genes/NTRK1.md) (TRKA), [TH](../genes/TH.md), [DBH](../genes/DBH.md), [PHOX2A](../genes/PHOX2A.md)/[PHOX2B](../genes/PHOX2B.md). [PMID:34493726](../papers/34493726.md)
- Chromosomal alterations in high-risk nC3 cells: recurrent 17q gain, 1p loss, 11q loss (confirmed by inferCNV and microarray in samples K87, K10, 23, K55, K3). [PMID:34493726](../papers/34493726.md)
- nC3 undifferentiated signature correlates with age-at-diagnosis (FDR = 8.12×10⁻³¹) and poor survival in 498-sample SEQC cohort (Kaplan-Meier Bonferroni-corrected p <0.01); noradrenergic nC7/nC8 signatures associate with better outcome. [PMID:34493726](../papers/34493726.md)
- LC-MS/MS proteomics of 15 neuroblastoma tumors stratified by [MYCN](../genes/MYCN.md) status revealed distinct proteomic signatures distinguishing MYCN-amplified from non-amplified tumors [PMID:22367537](../papers/22367537.md)
- CCLE pharmacogenomic profiling included neuroblastoma cell lines among 947 lines tested across 24 drugs, enabling genotype-response correlation analyses [PMID:22460905](../papers/22460905.md)
- WES/WGS of 240 neuroblastoma tumors identified [ALK](../genes/ALK.md), [PTPN11](../genes/PTPN11.md), and [ATRX](../genes/ATRX.md) as key recurrently mutated genes; low overall somatic mutation rate with enrichment in RAS-MAPK pathway [PMID:23334666](../papers/23334666.md)
- Comprehensive genomic analysis of neuroblastoma identified recurrent driver alterations including [MYCN](../genes/MYCN.md) amplification and [ALK](../genes/ALK.md) mutations with implications for targeted therapy [PMID:26466568](../papers/26466568.md)
- PIPseq cohort included 4 neuroblastoma cases; MYCN amplification + 1p/11q LOH + 17q gain used for risk-based therapy stratification; ATRX T1747fs identified as poor-prognosis marker; CDK4/MDM2 co-overexpression enrolled one patient on the NEPENTHE trial (NCT02780128); NRAS and KRAS activating mutations also identified [PMID:28007021](../papers/28007021.md)
- NBL (neuroblastoma) was modeled in an organ-on-a-chip system: a neuroblastoma-on-a-chip using collagen biomaterial at 36 dynes/cm² shear stress supported endothelial–NB co-culture capillary formation, while static cultures produced cell death, highlighting the role of flow in vascularized tumor modeling. [PMID:30643250](../papers/30643250.md)

## Subtypes

High-risk NBL is the focus of KIDSROBIN; no further subtype stratification in the corpus.

- High-risk neuroblastoma (typically children >18 months) contains an undifferentiated nC3 cluster transcriptionally resembling a novel [NTRK2](../genes/NTRK2.md)+/CLDN11+ postnatal human cholinergic progenitor unique to human adrenal gland (absent in mouse); low-risk tumors resemble noradrenergic/chromaffin cells. These may represent two distinct disease entities rather than a single spectrum. [PMID:34493726](../papers/34493726.md)

## Therapeutic landscape

- ROBIN KIDSROBIN center (U54 CA274516; Harvard University and UCSF) uses Xenium single-cell spatial profiling on baseline and post-131I-MIBG second-look surgical NBL samples to identify cell populations differentially depleted or enriched following 131I-MIBG therapy. [PMID:41941260](../papers/41941260.md)
- ctDNA nucleosome positioning studies performed at baseline and after 131I-MIBG therapy identified differential changes in transcription factor profiles in samples with subsequent ctDNA rises — candidate biomarkers of response. [PMID:41941260](../papers/41941260.md)
- Serum miRNA profiling following 131I-MIBG therapy identified a number of differentially modulated miRNAs as candidate response/resistance biomarkers. [PMID:41941260](../papers/41941260.md)
- Paired 123I-/131I-MIBG diagnostic scans and SPECT/CT images analyzed to estimate tumor-absorbed dose per unit administered activity — enabling dosimetry-based understanding of differential outcomes after 131I-MIBG. [PMID:41941260](../papers/41941260.md)
- The KIDSROBIN team notes that insights from infrequent pediatric cancers including NBL have historically proven generalizable to more common adult cancers. [PMID:41941260](../papers/41941260.md)
- [NTRK1](../genes/NTRK1.md) (TRKA) vs. [NTRK2](../genes/NTRK2.md) (TRKB) expression are mutually exclusive outcome biomarkers at single-cell level, validated by RNAscope ISH: [NTRK1](../genes/NTRK1.md)+ low-risk tumors have favorable prognosis while [NTRK2](../genes/NTRK2.md)+ undifferentiated cells associate with poor outcome. [PMID:34493726](../papers/34493726.md)
- nC3 transcriptional signature stratifies 498 SEQC patients by survival; the nC3 cluster gene program enriches for DNA damage/repair and cell motility GO terms. [PMID:34493726](../papers/34493726.md)

## Sources

- [PMID:41941260](../papers/41941260.md)
- [PMID:34493726](../papers/34493726.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22367537](../papers/22367537.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22460905](../papers/22460905.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23334666](../papers/23334666.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26466568](../papers/26466568.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:28007021](../papers/28007021.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:30643250](../papers/30643250.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
