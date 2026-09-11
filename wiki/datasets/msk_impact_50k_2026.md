---
name: MSK-IMPACT 50K Clinical Sequencing Cohort (MSK, Cancer Cell 2026)
studyId: msk_impact_50k_2026
institution: Memorial Sloan Kettering Cancer Center (MSK)
size: 54331
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - msk-impact-panel
tags:
  - pan-cancer
  - hotspots
  - HLA
  - clinical-sequencing
  - MSK-IMPACT
processed_by: crosslinker
processed_at: 2026-09-11
---

# MSK-IMPACT 50K Clinical Sequencing Cohort (MSK, Cancer Cell 2026)

## Overview

MSK-50K: a pan-cancer, prospectively sequenced clinical cohort of 54,331 tumors with patient-matched normal blood from 48,179 patients at Memorial Sloan Kettering, spanning 448 detailed OncoTree histologies. Name, institution, size (54,331) and reference genome (hg19) are taken from the cBioPortal study record in `schema/ontology/studies.json`, matching the paper's own accrual figures [PMID:41895280](../papers/41895280.md).

## Composition

- 56,801 solid-tumor biopsies from 49,929 patients sequenced as routine clinical care between January 2014 and September 2021; after QC, 54,331 tumors from 48,179 patients were retained (5,070 patients had ≥2 sequenced specimens) [PMID:41895280](../papers/41895280.md).
- 448 detailed OncoTree subtypes among 43,485 patients (after excluding cancers of unknown primary and high-level-only annotations); 101 subtypes had ≥50 patients. 57% of tumors came from patients with metastatic disease; median histopathologic purity 45% [PMID:41895280](../papers/41895280.md).
- Association analyses used 40,657 patients (one tumor per patient) across 447 histologies after excluding MSI/POLE hypermutators and very-high mutational/copy-number-burden tumors; 37,080 patients across 96 cancer types (≥50 patients each) were used for canonical-gene discovery [PMID:41895280](../papers/41895280.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md), tumor + matched normal blood, CLIA-certified FDA-authorized assay; four panel versions used: [IMPACT341](../methods/IMPACT341.md) (n=2,661), [IMPACT410](../methods/IMPACT410.md) (n=9,674), [IMPACT468](../methods/IMPACT468.md) (n=36,323), [IMPACT505](../methods/IMPACT505.md) (n=8,143). Median coverage 615x tumor / 484x normal [PMID:41895280](../papers/41895280.md).
- Copy number/purity/WGD via [FACETS](../methods/facets.md); MSI via [msisensor](../methods/msisensor.md); HLA class I genotyping via [Polysolver](../methods/polysolver.md); somatic HLA LOH via [LOHHLA](../methods/lohhla.md) [PMID:41895280](../papers/41895280.md).

## Papers using this cohort

- [PMID:41895280](../papers/41895280.md) — Bandlamudi et al. (MSK), source publication: identifies 164 new single-codon mutational hotspots (incl. RAS-paralog hotspots in *[RRAS2](../genes/RRAS2.md)*), classifies drivers as canonical vs. non-canonical by cancer type, and characterizes HLA LOH relevant to neoantigen-directed TCR therapy eligibility.

## Notable findings derived from this cohort

- 164 new single-codon hotspots were identified, including RAS-paralog hotspots in *[RRAS2](../genes/RRAS2.md)*; drivers were classified into 1,215 canonical gene–cancer type pairs, with 32% of drivers occurring in non-canonical contexts (more subclonal, later-arising, less biallelic tumor-suppressor inactivation, more frequent in patients with high-penetrance germline variants) [PMID:41895280](../papers/41895280.md).
- Eligibility for current *[KRAS](../genes/KRAS.md)*/*[TP53](../genes/TP53.md)* neoantigen-directed TCR therapies varies sharply by ancestry, and at least 15% of otherwise-eligible patients have already lost the restricting HLA allele [PMID:41895280](../papers/41895280.md).

## Sources

- cBioPortal study record: `msk_impact_50k_2026` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:41895280](../papers/41895280.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
