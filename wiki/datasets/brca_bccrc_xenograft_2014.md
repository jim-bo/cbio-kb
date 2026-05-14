---
name: Breast Cancer Xenografts (British Columbia, Nature 2015)
studyId: brca_bccrc_xenograft_2014
institution: BC Cancer Research Centre / British Columbia Cancer Agency
size: 116
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - breast-cancer
  - brca
  - patient-derived-xenograft
  - pdx
  - clonal-dynamics
  - whole-genome-seq
  - single-cell-sequencing
  - british-columbia
processed_by: crosslinker
processed_at: 2026-05-14
---

# Breast Cancer Xenografts (British Columbia, Nature 2015)

## Overview

Patient-derived xenograft (PDX) series generated from 55 breast cancer patients at the BC Cancer Research Centre and British Columbia Cancer Agency. Thirty serially-passaged PDX lines were transplanted into NOD/SCID/IL2rγ⁻/⁻ (NSG) and NOD/RAG1⁻/⁻IL2rγ⁻/⁻ (NRG) mice and sequenced across up to 16 transplant generations over three years. The primary aim was to characterize clonal selection and evolution during breast cancer PDX engraftment and serial passaging at single-cell resolution, using WGS, deep targeted amplicon sequencing, Affymetrix SNP6.0 CNA profiling, and single-cell targeted sequencing. Processed data available at cbioportal.org; raw sequencing deposited at EGA under accession EGAS00001000952.

## Composition

- **Cancer type:** Breast carcinoma ([BRCA](../cancer_types/BRCA.md))
- **Patients:** 55 breast cancer donors; 15 patient series (10 primary tumor, 5 pleural effusion/metastasis) with matched tumor, normal, and xenograft WGS
- **Xenograft lines:** 30 PDX lines; up to 16 generations over 3 years; transplant sites: subcutaneous (SC), subrenal capsule (SR), mammary fat pad (MFP); hosts: NSG and NRG immunodeficient mice
- **Subtypes:** ER+, HER2+, and triple-negative (TN) tumors represented; both primary and metastatic origins
- **Bulk sequencing:** WGS on 47 tumor/xenograft/normal samples (median depth 45.1×); deep targeted amplicon sequencing across 56 additional xenograft passages validating 3,187 somatic SNVs and 132 SVs; Affymetrix SNP6.0 CNA/LOH
- **Single-cell sequencing:** 210 nuclei from PDX lines SA494 and SA501 (40–45 SNV + 7–10 germline amplicons per cell via microfluidic isolation)
- **Reference genome:** hg19

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md): bulk WGS (median 45.1×) across tumor, normal, and xenograft samples
- [targeted-dna-seq](../methods/targeted-dna-seq.md): deep amplicon sequencing of 3,187 SNVs and 132 SVs across 56 additional passages
- [single-cell-dna-seq](../methods/single-cell-dna-seq.md): microfluidic-isolation-based single-cell targeted re-sequencing of 210 nuclei
- [affymetrix-snp6](../methods/affymetrix-snp6.md): copy number alteration and LOH profiling
- [pyclone](../methods/pyclone.md): Bayesian SNV clustering for clonal inference
- [titan-cna](../methods/titan-cna.md): CNA/LOH clonal inference
- [phylogenetic-tree-reconstruction](../methods/phylogenetic-tree-reconstruction.md): MrBayes 3.2 for single-cell Bayesian phylogenetics

## Papers using this cohort

- [PMID:25470049](../papers/25470049.md) — Eirew, Steif, Khattra et al., *Nature* 2015. "Dynamics of genomic clones in breast cancer patient xenografts at single cell resolution."

## Notable findings derived from this cohort

- Clonal selection at engraftment was universal across all 15 tumor–xenograft series examined, ranging from extreme selective expansion of minor (<5%) clones to moderate polyclonal engraftment; 6.5–32.1% of high-confidence SNVs were prevalent in the xenograft but at or below detection in the originating tumor [PMID:25470049](../papers/25470049.md).
- Replicate transplants of the same tumor into independent mice produced concordant clonal expansion patterns (median Pearson r 0.91–0.94 across same-passage replicates in SA501, SA535, SA532, SA429), demonstrating that clonal fitness is largely deterministic and reproducible rather than stochastic [PMID:25470049](../papers/25470049.md).
- Single-cell Bayesian phylogenetic inference on 210 nuclei validated that bulk-population PyClone mutation clusters correspond to real clonal genotypes; in SA494, a <5% originating clone (PyClone cluster 3) expanded to dominance by passage X4 [PMID:25470049](../papers/25470049.md).
- A xenograft-specific [TP53](../genes/TP53.md) deletion was identified in SA500, coinciding with retention of a somatic SNV, demonstrating structural events arising or selected post-engraftment [PMID:25470049](../papers/25470049.md).
- Two modes of clonal dynamics across serial passages were identified: early-stabilizing (SA500, SA530, SA494, SA535) and progressive (SA501), with both modes occurring across ER+, HER2+, and triple-negative subtypes [PMID:25470049](../papers/25470049.md).

## Sources

- cBioPortal study: `brca_bccrc_xenograft_2014`
- EGA accession: EGAS00001000952
- Citation: Eirew et al. Nature 2015 [PMID:25470049](../papers/25470049.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
