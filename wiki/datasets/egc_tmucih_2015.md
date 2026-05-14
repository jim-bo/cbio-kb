---
name: Gastric Adenocarcinoma (TMUCIH, PNAS 2015)
studyId: egc_tmucih_2015
institution: Tianjin Medical University Cancer Institute and Hospital
size: 294
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
panels: []
tags:
  - gastric-cancer
  - stomach-adenocarcinoma
  - stad
  - egc
  - whole-exome-seq
  - targeted-dna-seq
  - clonal-heterogeneity
  - chinese-cohort
  - tianjin
processed_by: crosslinker
processed_at: 2026-05-14
---

# Gastric Adenocarcinoma (TMUCIH, PNAS 2015)

## Overview

Multi-tier sequencing cohort of gastric adenocarcinoma (GC) from the Tianjin Medical University Cancer Institute and Hospital (TMUCIH). Comprises a whole-exome sequencing discovery cohort (78 primary GCs with matched blood), a whole-genome sequencing sub-cohort (2 patients with multi-region tumor + lymph node samples), and a targeted resequencing validation cohort (216 additional GC cases). Total study population: 294 patients (after 5 excluded for discrepant pathology). All patients are treatment-naive northern Chinese adults; primary aims were to characterize the somatic landscape, define clonal heterogeneity subtypes, discover novel drivers in the ERBB and Wnt pathways, and validate findings against the TCGA [STAD](../cancer_types/STAD.md) cohort. Sequence data deposited at EGA under accession EGAS00001001056.

## Composition

- **Cancer type:** Gastric adenocarcinoma ([STAD](../cancer_types/STAD.md))
- **Total patients:** 294 (78 WES discovery + 216 targeted-seq validation; 2 WGS sub-cases)
- **Anatomic location:** Antrum 64 (21.77%), body 118 (40.14%), cardia 112 (38.10%)
- **Histology:** 124 intestinal-type, 152 diffuse-type, 18 mixed (Lauren classification)
- **Stage:** I 6 (2.05%), II 85 (28.91%), III 97 (32.99%), IV 106 (36.05%)
- **Follow-up:** Median 13.84 months overall; 25.08 months for WES series
- **Treatment:** Treatment-naive; no prior chemotherapy or radiotherapy
- **Population:** Northern Chinese; differences vs. Russian TCGA [STAD](../cancer_types/STAD.md) cohort observed for anatomic-location mutation enrichments
- **Reference genome:** hg19

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md): 78 tumor/normal pairs on Illumina HiSeq 2000 with Agilent SureSelect capture; mean coverage 167× tumor / 170× normal; 85% of exons ≥20×
- [whole-genome-seq](../methods/whole-genome-seq.md): 2 patients (Pt1, Pt2), each with 3 primary-tumor regions + 2 matched lymph-node metastases
- [targeted-dna-seq](../methods/targeted-dna-seq.md): 216-case validation cohort, 103 recurrent genes on the Ion Torrent PGM platform
- [mutsig](../methods/mutsig.md): MutSigCV for significantly mutated gene discovery
- [phylogenetic-tree-reconstruction](../methods/phylogenetic-tree-reconstruction.md): multi-region phylogenetics for clonal evolution

## Papers using this cohort

- [PMID:25583476](../papers/25583476.md) — Chen et al., *PNAS* 2015. "Genomic landscape of gastric cancer from a northern Chinese population."

## Notable findings derived from this cohort

- SciClone clonality analysis identified a high-clonality (HiC, >4 clones, n=9) subtype with significantly shorter survival vs. low-clonality (LoC, ≤4 clones, n=68); HiC–survival association was an independent prognostic factor after multivariate adjustment (adjusted HR 4.69, 95% CI 1.62–13.6, P=0.0043) [PMID:25583476](../papers/25583476.md).
- [NRG1](../genes/NRG1.md) or [ERBB4](../genes/ERBB4.md) mutations were detected in 34/294 (11.6%) of cases, with EGF-like domain clustering in [NRG1](../genes/NRG1.md) (p.A221T, p.A225P, p.E223G, p.R224Q, p.S226P) and kinase/receptor-domain mutations in [ERBB4](../genes/ERBB4.md); ERBB/NRG family mutations were mutually exclusive (permutation P=0.02), defining a candidate lapatinib-targetable subset [PMID:25583476](../papers/25583476.md).
- [BRCA2](../genes/BRCA2.md) mutations in 17/294 Tianjin cases (5.8%); pooling with TCGA [STAD](../cancer_types/STAD.md) (28/289 cases) yielded log-rank P=0.03 survival benefit for BRCA2-mutant GC patients; adjusted HR 0.37 (95% CI 0.13–0.96, P=0.05), establishing [BRCA2](../genes/BRCA2.md) as an independent prognostic marker [PMID:25583476](../papers/25583476.md).
- MutSigCV identified 16 significantly mutated genes (q<0.2) including [TP53](../genes/TP53.md), [ARID1A](../genes/ARID1A.md), [CDH1](../genes/CDH1.md), [APC](../genes/APC.md), [RHOA](../genes/RHOA.md), [PIK3CA](../genes/PIK3CA.md), [SMAD4](../genes/SMAD4.md), [MYC](../genes/MYC.md), and [KRAS](../genes/KRAS.md); [TP53](../genes/TP53.md) was enriched in HiC and present only as minor subclones (<15% VAF), implying single-agent therapy could select for TP53-wild-type populations [PMID:25583476](../papers/25583476.md).
- Anatomic-location-specific mutation enrichments (antrum, body, cardia) were observed in this northern Chinese cohort but did not replicate in the Russian TCGA [STAD](../cancer_types/STAD.md) cohort, suggesting population-specific or environmental contributions to mutational distribution [PMID:25583476](../papers/25583476.md).

## Sources

- cBioPortal study: `egc_tmucih_2015`
- EGA accession: EGAS00001001056
- Citation: Chen et al. PNAS 2015 [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
