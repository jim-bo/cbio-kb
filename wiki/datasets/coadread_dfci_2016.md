---
name: "Colorectal Adenocarcinoma WES Cohort (Giannakis et al. 2016)"
studyId: coadread_dfci_2016
institution: Dana-Farber Cancer Institute / Broad Institute; Nurses' Health Study / Health Professionals Follow-up Study
size: 619
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - immunohistochemistry
panels: []
tags:
  - colorectal-cancer
  - crc
  - colon
  - rectal
  - neoantigen
  - tumor-infiltrating-lymphocytes
  - hla
  - msi
  - pole
  - nhs
  - hpfs
processed_by: crosslinker
processed_at: 2026-05-14
---

# Colorectal Adenocarcinoma WES Cohort (Giannakis et al. 2016)

## Overview

Population-based whole-exome sequencing cohort of 619 incident colorectal carcinomas with matched FFPE tumor-normal pairs drawn from two long-running U.S. prospective cohorts: the Nurses' Health Study (NHS, established 1976) and the Health Professionals Follow-up Study (HPFS, established 1986). The cohort is the primary discovery set for expanded CRC driver-gene identification and for demonstrating that neoantigen load correlates with lymphocytic infiltration and improved CRC-specific survival even within microsatellite-stable, POLE-wild-type tumors. Raw sequence data deposited under dbGaP: phs000722. [PMID:27149842](../papers/27149842.md)

## Composition

- Cancer type: [COADREAD](../cancer_types/COADREAD.md)
- 619 incident CRC cases with matched FFPE tumor-normal pairs (NHS + HPFS cohorts)
- 597 individuals with survival data (median follow-up 9.4 years, IQR 5.8–13.1)
- Mean exome coverage 90×; 87% of bases at ≥20×
- 488 non-hypermutated (≤12 mut/Mb) + 131 hypermutated; microsatellite status by 10-marker PCR panel
- 299 samples with H&E-based lymphocytic scoring and TMA [immunohistochemistry](../methods/immunohistochemistry.md) (CD3, CD8, CD45RO, [FOXP3](../genes/FOXP3.md))
- 4 MSS tumors with [POLE](../genes/POLE.md) exonuclease-domain hotspots flagged separately [PMID:27149842](../papers/27149842.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Illumina HiSeq 2000, SureSelect v.2 capture
- [MuTect](../methods/mutect.md) for SNV calling; Indelocator + [Strelka](../methods/strelka.md) for indels; [BWA](../methods/bwa.md)-MEM realignment
- [MutSig](../methods/mutsig.md)CV suite for significantly mutated gene discovery
- [POLYSOLVER](../methods/polysolver.md) for HLA class I typing and mutation calling
- [NetMHCpan](../methods/netmhcpan.md) v2.4 for neoantigen prediction (9- and 10-mer, <500 nM cutoff)
- [immunohistochemistry](../methods/immunohistochemistry.md) — TMA-based T-cell density quantification

## Papers using this cohort

- [PMID:27149842](../papers/27149842.md) — Giannakis et al. 2016, *Nature Genetics* — "Genomic Landscape of Colorectal Cancer in Japan: A Comparison with US Populations" / primary WES characterization of this NHS/HPFS CRC cohort.

## Notable findings derived from this cohort

- 90 significantly mutated genes in 488 non-hypermutated CRCs; 73 were new statistical drivers relative to prior TCGA and Seshagiri CRC studies. [PMID:27149842](../papers/27149842.md)
- Newly nominated CRC drivers include [BCL9L](../genes/BCL9L.md), [TCF7](../genes/TCF7.md) (WNT); [PRKCQ](../genes/PRKCQ.md), [MAP2K1](../genes/MAP2K1.md), [MAP2K7](../genes/MAP2K7.md) (RAS); [TGIF1](../genes/TGIF1.md) (TGF-beta); [RBM10](../genes/RBM10.md), [RBM12](../genes/RBM12.md) (RNA processing); [CTCF](../genes/CTCF.md), [KLF5](../genes/KLF5.md) (chromatin). [PMID:27149842](../papers/27149842.md)
- Neoantigen load significantly correlated with overall lymphocytic-reaction score (Spearman rho=0.29, P=2.6e-11) and with [TILs](../themes/tumor-infiltrating-lymphocytes.md) specifically (rho=0.36, P=2.0e-19); correlation held within MSS, [POLE](../genes/POLE.md)-wild-type tumors (P=0.035). [PMID:27149842](../papers/27149842.md)
- High neoantigen load (>450 predicted) associated with improved CRC-specific survival (multivariate HR=0.57, 95% CI 0.35–0.93, P=0.03), independent of stage, age, gender, tumor location, and differentiation. [PMID:27149842](../papers/27149842.md)
- HLA class I somatic mutations in 11% (66/619) of samples; enriched in TIL-rich tumors (chi-squared P=1.2e-22); mutated alleles carried more neoantigens than non-mutated alleles (Wilcoxon P=0.006), consistent with positive selection for immune escape. [PMID:27149842](../papers/27149842.md)
- Antigen-processing-machinery (APM) mutations ([B2M](../genes/B2M.md), [TAP1](../genes/TAP1.md), [TAP2](../genes/TAP2.md), [TAPBP](../genes/TAPBP.md), [CALR](../genes/CALR.md), [CANX](../genes/CANX.md), [HSPA5](../genes/HSPA5.md), [PDIA3](../genes/PDIA3.md)) collectively enriched in TIL-rich tumors, implicating adaptive immune-escape selection. [PMID:27149842](../papers/27149842.md)
- Frameshift indels produced a disproportionately high share of predicted neoantigens (8.1% of mutations vs 22.6% of neoantigens are indels). [PMID:27149842](../papers/27149842.md)

## Sources

- cBioPortal studyId: `coadread_dfci_2016`
- dbGaP accession: phs000722
- Giannakis M et al. "Genomic Correlates of Immune-Cell Infiltrates in Colorectal Carcinoma." *Cell Reports*. 2016;15(4):857-865. [PMID:27149842](../papers/27149842.md). DOI: 10.1016/j.celrep.2016.03.075.

*This page was processed by **crosslinker** on **2026-05-14**.*
