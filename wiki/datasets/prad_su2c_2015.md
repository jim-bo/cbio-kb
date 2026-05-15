---
name: "Prostate Adenocarcinoma SU2C / PCF 2015 (Robinson et al.)"
studyId: prad_su2c_2015
institution: "SU2C–PCF International Dream Team (Broad Institute, University of Michigan; 8 clinical sites)"
size: 150
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
panels: []
tags:
  - metastatic-castration-resistant-prostate-cancer
  - mcrpc
  - su2c
  - integrative-genomics
  - parp-inhibitor
  - dna-repair
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# Prostate Adenocarcinoma SU2C / PCF 2015 (Robinson et al.)

## Overview

Prospective integrative clinical sequencing cohort of 150 men with metastatic castration-resistant prostate cancer (mCRPC), assembled by the SU2C–PCF International Dream Team and published in *Cell* 2015 (PMID:26000489). All cases received whole-exome sequencing (WES) and paired transcriptome sequencing of biopsies from bone or soft tissue metastases, along with matched germline. Eight clinical sites contributed; analysis was performed at the Broad Institute and University of Michigan. The study was powered to compare mCRPC with 440 primary prostate cancer exomes to identify selectively enriched alterations in the metastatic castration-resistant setting.

## Composition

- **N = 150** men with mCRPC who met ≥20% tumor content threshold (from 189 enrolled, 175 sequenced after pathology review).
- **Cancer type:** [PRAD](../cancer_types/PRAD.md) (mCRPC).
- **Biopsy sites:** lymph node (42%), bone (28.7%), liver (12.7%), other soft tissues (16.7%).
- **Histology:** 96.4% high-grade prostate adenocarcinoma; 2.9% with neuroendocrine differentiation; 0.7% small-cell neuroendocrine features.
- **Clinical context:** patients being considered for [abiraterone](../drugs/abiraterone.md) or [enzalutamide](../drugs/enzalutamide.md) as standard of care, or as part of clinical trials including PARP inhibitors and aurora-kinase inhibitors.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — SureSelect Exome v4; mean target coverage 160× (tumor) / 100× (normal). Reference genome hg19/GRCh37.
- [rna-seq](../methods/rna-seq.md) — paired-end on Illumina HiSeq 2500 (2×100 nt, ~50M paired reads); FPKM via Cufflinks; fusion detection via [tophat-fusion](../methods/tophat-fusion.md).
- [mutect](../methods/mutect.md) — somatic mutation calling.
- [mutsig](../methods/mutsig.md) — recurrence analysis.

## Papers using this cohort

- [PMID:26000489](../papers/26000489.md) — Robinson et al., *Cell* 2015: integrative clinical genomics of 150 mCRPC; primary discovery study for this cohort.
- [PMID:26855148](../papers/26855148.md) — Beltran et al. 2016, *Nature Medicine*: used as external validation cohort for the 70-gene NEPC classifier; up to 8% of metastatic cases scored NEPC-high.
- [PMID:26928463](../papers/26928463.md) — Kumar et al., *Nat Genet* 2016: queried to verify metastasis-private mutations from prad_fhcrc rapid-autopsy cohort are non-driver.

## Notable findings derived from this cohort

- 89% of mCRPC cases harbored a clinically actionable aberration: [AR](../genes/AR.md) alterations 62.7%, other cancer-gene alterations 65%, actionable pathogenic germline 8%. [PMID:26000489](../papers/26000489.md)
- DNA repair pathway (including [BRCA2](../genes/BRCA2.md), [BRCA1](../genes/BRCA1.md), [ATM](../genes/ATM.md)) biallelic loss in 19.3% of cases; 5.3% carried germline [BRCA2](../genes/BRCA2.md) with somatic second hit — supporting PARP inhibitor candidacy and germline testing in mCRPC. [PMID:26000489](../papers/26000489.md)
- [TP53](../genes/TP53.md) most selectively mutated gene in mCRPC vs. primary prostate cancer (q<0.001); [AR](../genes/AR.md), [KMT2D](../genes/KMT2D.md), [APC](../genes/APC.md), [BRCA2](../genes/BRCA2.md), [GNAS](../genes/GNAS.md) also selectively enriched (q<0.1). [PMID:26000489](../papers/26000489.md)
- Novel recurrent focal homozygous deletion at chr11q23 narrowed to [ZBTB16](../genes/ZBTB16.md) in 8 cases (5%) — androgen-regulated gene linked to MAPK upregulation and androgen resistance. [PMID:26000489](../papers/26000489.md)
- Novel activating [PIK3CB](../genes/PIK3CB.md) mutations at positions equivalent to canonical [PIK3CA](../genes/PIK3CA.md) hotspots, co-occurring with [PTEN](../genes/PTEN.md) loss; activating [PIK3CB](../genes/PIK3CB.md) fusions also identified — nominating PIK3CB-specific inhibitors. [PMID:26000489](../papers/26000489.md)
- ETS fusions (predominantly [ERG](../genes/ERG.md)) in 56% of mCRPC cases; WNT pathway ([APC](../genes/APC.md)/[CTNNB1](../genes/CTNNB1.md)/[RNF43](../genes/RNF43.md)/[ZNRF3](../genes/ZNRF3.md)/[RSPO2](../genes/RSPO2.md)) in 18%; recurrent [BRAF](../genes/BRAF.md) and [RAF1](../genes/RAF1.md) fusions in ~3%. [PMID:26000489](../papers/26000489.md)
- Used as an external validation cohort (n=150 mCRPC) for the 70-gene NEPC classifier; up to 8% of metastatic cases scored NEPC-high and 0% of treatment-naïve adenocarcinomas did [PMID:26855148](../papers/26855148.md)
- Used alongside prad_tcga to assess frequency of metastasis-private mutations from the prad_fhcrc rapid-autopsy cohort; only 2/51 patient-99-091 private mutations occurred at >5% frequency, arguing most are non-driver [PMID:26928463](../papers/26928463.md)

## Sources

- cBioPortal study: `prad_su2c_2015`
- [PMID:26855148](../papers/26855148.md) — Beltran et al. 2016, *Nature Medicine*: NEPC classifier validation using this cohort.

*This page was processed by **entity-page-writer** on **2026-05-15**.*
