---
name: Endometrial Carcinoma MSI (MSK, Clin Cancer Res 2022)
studyId: ucec_ccr_msk_2022
institution: Memorial Sloan Kettering Cancer Center
size: 184
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT (IMPACT341, IMPACT410, IMPACT468)
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - endometrial cancer
  - MMR deficiency
  - MSI-H
  - MLH1 methylation
  - Lynch syndrome
  - paired tumor-normal
processed_by: crosslinker
processed_at: 2026-05-21
---

# Endometrial Carcinoma MSI (MSK, Clin Cancer Res 2022)

## Overview

Prospective tumor-normal MSK-IMPACT sequencing cohort of 184 MSI-H or pathogenic-germline-MMR endometrial carcinomas (ECs) filtered from 1,157 consented patients at MSK between March 2015 and July 2020. The cohort was designed to characterize clinical and genomic differences among three MMR-D mechanisms: germline (Lynch syndrome, n=25), somatic MMR mutation (n=39), and [MLH1](../genes/MLH1.md) promoter hypermethylation (MLH1ph, n=120). Patients with pathogenic [POLE](../genes/POLE.md) mutations were excluded a priori. Tumors were sequenced with MSK-IMPACT (341/410/468-gene panels) at median depth 637x. Orthogonal validation by four-marker MMR IHC and bisulfite-based methylation assay.

## Composition

- 184 patients: 25 germline MMR (Lynch, 14%), 39 somatic MMR (21%), 120 MLH1ph (65%)
- Cancer type: endometrial carcinoma ([UCEC](../cancer_types/UCEC.md) / [UEC](../cancer_types/UEC.md))
- Primarily endometrioid histology (82–92% per group); others include carcinosarcoma, clear cell, mixed, undifferentiated/dedifferentiated
- Survival cohort: 119 patients with initial MSK care and sequencing within 6 months of diagnosis
- ICI-response sub-cohort: 18 patients with recurrent EC on on-label [pembrolizumab](../drugs/pembrolizumab.md)
- Reference genome: hg19

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md): [IMPACT410](../methods/IMPACT410.md) / [IMPACT468](../methods/IMPACT468.md) panels; paired tumor-normal
- [MSIsensor](../methods/msisensor.md) for MSI status (≥10 MSI-H; 3–<10 indeterminate; <3 MSS)
- [FACETS](../methods/facets.md) for copy-number and LOH analysis
- [deconstructSigs](../methods/deconstructsigs.md) for COSMIC v3.1 mutational signatures
- [Kaplan-Meier](../methods/kaplan-meier.md) and [Cox proportional-hazards](../methods/cox-proportional-hazards.md) survival models
- Four-marker MMR IHC (MLH1/MSH2/MSH6/PMS2) and bisulfite methylation assay for orthogonal validation

## Papers using this cohort

- [PMID:35849120](../papers/35849120.md) — Primary study characterizing clinical, genomic, and immune differences across MMR-D mechanisms in MSI-H endometrial cancer.

## Notable findings derived from this cohort

- MLH1ph ECs were clinically distinct (older, obese, higher FIGO stage, more LVSI) with lower TMB (median 32 vs 44/48 mt/Mb; p<0.001), lower TIL infiltrate, and worse stage-I/II PFS; germline (Lynch) ECs enriched for [ERBB2](../genes/ERBB2.md) (29%), [ERBB3](../genes/ERBB3.md) (25%), and [FBXW7](../genes/FBXW7.md) (46%) hotspot mutations; MLH1ph ECs enriched for [JAK1](../genes/JAK1.md) frameshifts (45%); pembrolizumab response lower in MLH1ph (25% progression) vs germline/somatic (0/2 progressed) in exploratory ICI analysis (n=18) [PMID:35849120](../papers/35849120.md)

## Sources

- cBioPortal study: `ucec_ccr_msk_2022`
- Citation: MSK Clin Cancer Res 2022 [PMID:35849120](../papers/35849120.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
