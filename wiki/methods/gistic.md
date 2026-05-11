---
name: GISTIC
slug: gistic
kind: method
canonical_source: "[PMID:18772890](../papers/18772890.md)"
unverified: true
tags: [copy-number, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-11
---

# GISTIC

## Overview

Genomic Identification of Significant Targets in Cancer (GISTIC) is a bioinformatic tool used to identify regions of the genome that are significantly amplified or deleted across a set of samples.

## Used by

- Used to analyze DNA copy number data from 206 glioblastoma samples to identify significantly altered regions and core pathways [PMID:18772890](../papers/18772890.md).
- Used alongside RAE to identify statistically significant somatic copy-number alterations in 207 high-grade soft tissue sarcoma samples across seven subtypes, including ~90% frequency of 12q amplification in [DDLS](../cancer_types/DDLS.md) [PMID:20601955](../papers/20601955.md).
- Applied to Affymetrix SNP6 copy number data from 489 [HGSOC](../cancer_types/HGSOC.md) samples to identify 113 significant focal DNA copy number aberrations in the TCGA ovarian carcinoma study [PMID:21720365](../papers/21720365.md)
- GISTIC applied to identify significant somatic copy-number alterations in prostate adenocarcinoma from the Broad WES cohort [PMID:22610119](../papers/22610119.md)
- GISTIC applied to Affymetrix SNP 6.0 copy-number data from 257 TCGA colorectal carcinoma tumors to identify significant focal amplifications and deletions [PMID:22810696](../papers/22810696.md)
- GISTIC applied to Affymetrix SNP 6.0 copy-number data from 121 melanoma samples (Broad) to identify significant focal amplifications and deletions including [CDKN2A](../genes/CDKN2A.md) loss, [BRAF](../genes/BRAF.md) amplification [PMID:22817889](../papers/22817889.md)
- Applied to JHU [SCLC](../cancer_types/SCLC.md) cohort (36 tumors) to identify recurrent focal amplifications including [SOX2](../genes/SOX2.md) and [MYCL](../genes/MYCL.md) and deletions of [RB1](../genes/RB1.md) [PMID:22941189](../papers/22941189.md)
- Applied to TCGA [LUSC](../cancer_types/LUSC.md) cohort (178 tumors) to identify focal amplifications ([SOX2](../genes/SOX2.md), [FGFR1](../genes/FGFR1.md)) and deletions ([CDKN2A](../genes/CDKN2A.md)) from SNP6 array data [PMID:22960745](../papers/22960745.md)
- GISTIC analysis of SNP 6.0 copy-number data from 160 CLL tumors identified del(13q14), del(11q22-23), and del(17p13) as recurrent focal deletions [PMID:23415222](../papers/23415222.md)
- GISTIC v2.0.12 applied to Affymetrix SNP 6.0 copy-number profiles of 38 OSCC tumors; identified recurrent focal amplifications ([CCND1](../genes/CCND1.md), [EGFR](../genes/EGFR.md)) and deletions ([CDKN2A](../genes/CDKN2A.md), [FHIT](../genes/FHIT.md)) [PMID:23619168](../papers/23619168.md)
- GISTIC v2 applied to an extended cohort of 199 prostate adenocarcinomas to call recurrent SCNAs; [CHD1](../genes/CHD1.md) deletion associated with elevated recurrent SCNA burden (p=1.5×10⁻⁸) and Gleason grade tracked SCNA count (p=0.0059) [PMID:23622249](../papers/23622249.md)
- GISTIC applied to Affymetrix SNP 6.0 data from 363 endometrial carcinomas; identified recurrent focal amplifications of [MYC](../genes/MYC.md), [ERBB2](../genes/ERBB2.md), [CCNE1](../genes/CCNE1.md), [FGFR3](../genes/FGFR3.md), and [SOX17](../genes/SOX17.md) defining the copy-number-high serous-like subgroup [PMID:23636398](../papers/23636398.md)
- Applied as GISTIC2.0 in 60-sample ACC study to identify significant recurrent copy-number alterations: high-level losses at 6q24, 12q13, and 14q; 14q loss associated with solid histology (Fisher p=2.0×10⁻⁴), 6q24 loss enriched for advanced stage (p=4.0×10⁻²) [PMID:23685749](../papers/23685749.md)
- Used on 492 [GBM](../cancer_types/GBM.md) samples for SCNA peak calling; identified recurrent amplifications on chr7 (EGFR/MET/CDK6), chr12 (CDK4/MDM2), chr4 ([PDGFRA](../genes/PDGFRA.md)) and defined [QKI](../genes/QKI.md) as sole target of 6q26 minimal deletion [PMID:24120142](../papers/24120142.md)
- Reimplemented GISTIC-style analysis on WGS-derived CNA data from 99 [BLCA](../cancer_types/BLCA.md) tumors; identified 84 focal amplification regions and 80 focal deletion regions including [DHFR](../genes/DHFR.md) amplification (14%) and CDKN2A/B deletion (50%) [PMID:24121792](../papers/24121792.md)
- GISTIC applied to Affymetrix SNP 6.0 copy-number data from 153 multiple myeloma patients; identified 7 significant homozygous deletion peaks covering NF-kB regulators ([TRAF3](../genes/TRAF3.md), BIRC2/BIRC3, [CYLD](../genes/CYLD.md)), [CDKN2C](../genes/CDKN2C.md), [PTPRD](../genes/PTPRD.md), and an 8p23.1 locus [PMID:24434212](../papers/24434212.md)
- GISTIC 2.0 applied to Affymetrix SNP 6.0 data from 131 TCGA bladder carcinoma samples; identified most common focal deletion at 9p21.3 ([CDKN2A](../genes/CDKN2A.md), 47% of samples) and multiple focal amplifications including [PPARG](../genes/PPARG.md) (17%), [EGFR](../genes/EGFR.md) (11%), [MDM2](../genes/MDM2.md) (9%), and [ERBB2](../genes/ERBB2.md) (7%) [PMID:24476821](../papers/24476821.md)
- GISTIC used for copy-number peak calling in 65 TET cases; identified focal BCL2 amplification correlated with increased BCL2 mRNA expression [PMID:24974848](../papers/24974848.md)

## Notes

- Helped identify frequent alterations in *[EGFR](../genes/EGFR.md)* (45%), *CDKN2A/B* (>50%), and other key drivers in [GBM](../cancer_types/GBM.md) [PMID:18772890](../papers/18772890.md).
- Identified [CDK4](../genes/CDK4.md) and [MDM2](../genes/MDM2.md) as focal 12q amplification targets in [DDLS](../cancer_types/DDLS.md); results informed functional shRNA validation and pharmacologic CDK4/CDK6 inhibition with [palbociclib](../drugs/palbociclib.md) [PMID:20601955](../papers/20601955.md).

## Sources

- [PMID:18772890](../papers/18772890.md)
- [PMID:20601955](../papers/20601955.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:21720365](../papers/21720365.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22610119](../papers/22610119.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22810696](../papers/22810696.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22817889](../papers/22817889.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22941189](../papers/22941189.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22960745](../papers/22960745.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23415222](../papers/23415222.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23619168](../papers/23619168.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23622249](../papers/23622249.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23636398](../papers/23636398.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23685749](../papers/23685749.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24120142](../papers/24120142.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24121792](../papers/24121792.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24434212](../papers/24434212.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24974848](../papers/24974848.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
