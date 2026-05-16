---
name: Early-Onset Prostate Cancer — DKFZ 2018
studyId: prostate_dkfz_2018
institution: German Cancer Research Center (DKFZ)
size: 292
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - rna-seq
  - hm450-methylation-array
panels: []
tags:
  - prostate-cancer
  - PRAD
  - early-onset
  - whole-genome-sequencing
  - methylation
  - APOBEC
  - ESRP1
  - structural-variants
processed_by: crosslinker
processed_at: 2026-05-16
---

# Early-Onset Prostate Cancer — DKFZ 2018

## Overview

The DKFZ 2018 prostate cancer cohort (prostate_dkfz_2018) was assembled at the German Cancer Research Center to characterize the earliest somatic events in prostate cancer (PC), with emphasis on early-onset PC (EOPC). The study integrated whole-genome sequencing (WGS), transcriptome profiling (mRNA-seq), and methylome profiling (450k array) to define molecular risk markers, temporal order of alterations, and prognostic subgroups. A subset of 41 WGS samples was re-used from a prior DKFZ cohort (Fraser et al. 2017). The cohort underpins the PEPCI methylation risk score, the PRESCIENT event-ordering model, and the identification of [ESRP1](../genes/ESRP1.md) as an independent prognostic biomarker validated in 11,954 TMA cores.

## Composition

- **Total samples:** 292 primary prostate cancers — 203 early-onset PC (EOPC, age at diagnosis ≤ 55 years) and 89 late-onset PC (LOPC).
- **Cancer type:** [PRAD](../cancer_types/PRAD.md) (prostate adenocarcinoma).
- **WGS:** 184 EOPC + 85 LOPC tumor/blood pairs.
- **450k methylation array:** 203 EOPC + 45 LOPC tumor samples.
- **mRNA-seq:** 96 EOPC samples.
- Independent validation via [prad_tcga_pub](../datasets/prad_tcga_pub.md) (462 samples with RNA-seq).
- IHC tissue-microarray validation of [ESRP1](../genes/ESRP1.md) on 11,954 radical-prostatectomy cores (University Medical Center Hamburg-Eppendorf, 1992–2014; median follow-up 48 months).

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — tumor + matched blood; structural variant and SNV calling
- [rna-seq](../methods/rna-seq.md) — 96 EOPC samples; co-expression cluster analysis
- [450k-methylation-array](../methods/450k-methylation-array.md) — tumor methylome; PEPCI score derivation
- [immunohistochemistry](../methods/immunohistochemistry.md) — [ESRP1](../genes/ESRP1.md) protein staining on TMA
- [fish](../methods/fish.md) — ESRP1 locus (8q22.1) using BAC RP11-267M23 / RP11-22C11 with centromere 8 reference probe

## Papers using this cohort

- [PMID:30537516](../papers/30537516.md) — Gerhauser et al. 2018, "Molecular Evolution of Early-Onset Prostate Cancer Identifies Molecular Risk Markers and Clinical Trajectories," *Cancer Cell*.

## Notable findings derived from this cohort

- Lower SNV burden in EOPC than LOPC (median 0.47 vs 0.53 SNVs/Mb; p < 0.001); SV and SNV counts both increase significantly with age [PMID:30537516](../papers/30537516.md).
- 70% of EOPC tumors carry a structural variant consistent with an ETS-fusion event; [TMPRSS2](../genes/TMPRSS2.md)–[ERG](../genes/ERG.md) is the canonical fusion; [ERG](../genes/ERG.md) is the most frequent initiating event in the PRESCIENT temporal model [PMID:30537516](../papers/30537516.md).
- Top recurrent SV-affected loci in EOPC: chromosome 8p ([NKX3-1](../genes/NKX3-1.md), 37%), 3p14 ([FOXP1](../genes/FOXP1.md), 30%), 13q22 ([KLF5](../genes/KLF5.md), 27%), 8q22 ([ESRP1](../genes/ESRP1.md), 17%) [PMID:30537516](../papers/30537516.md).
- [ESRP1](../genes/ESRP1.md) 8q22 duplications associated with >1.5-fold mRNA increase and elevated Gleason Score (p < 1×10⁻¹¹, chi-squared); ESRP1 is an independent prognostic marker for [BCR](../genes/BCR.md) validated in 11,954 TMA cores [PMID:30537516](../papers/30537516.md).
- PEPCI (Purity-adjusted Epigenetic Prostate Cancer Index): high PEPCI correlates with high pT (p < 1×10⁻⁷), high Gleason Score (p < 1×10⁻¹⁷), and BCR (log-rank p < 0.0001); AUC = 0.831 for GS, 0.702 for BCR; PEPCI-high tumors enriched for ESRP1 gain (OR = 15.7) [PMID:30537516](../papers/30537516.md).
- Six mutational signatures observed (clock-like 1/5, DDR 3/6, APOBEC 2/13); [APOBEC3B](../genes/APOBEC3B.md)-driven kataegis co-localizes with SV breakpoints; germline [APOBEC3B](../genes/APOBEC3B.md) deletion carriers shift from A3B-like to [APOBEC3A](../genes/APOBEC3A.md)-like mutagenesis [PMID:30537516](../papers/30537516.md).
- Germline DDR PTVs in [BRCA1](../genes/BRCA1.md), [BRCA2](../genes/BRCA2.md), [PALB2](../genes/PALB2.md), [ATM](../genes/ATM.md), [CHEK2](../genes/CHEK2.md) significantly elevated SV/SNV burden and signature 3 (BRCAness) [PMID:30537516](../papers/30537516.md).
- >40% of EOPC patients could be matched to a PI3K, mTOR, or PARP inhibitor at pre-clinical or clinical-trial stage [PMID:30537516](../papers/30537516.md).

## Sources

- [PMID:30537516](../papers/30537516.md)
- cBioPortal study: prostate_dkfz_2018

*This page was processed by **crosslinker** on **2026-05-16**.*
