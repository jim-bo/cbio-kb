---
name: TCGA Pheochromocytoma and Paraganglioma (PCPG, Cancer Cell 2017)
studyId: pcpg_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 173
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-sequencing
  - rna-seq
  - mirna-seq
  - dna-methylation-array
  - snp-array
  - rppa
panels: []
tags:
  - TCGA
  - pheochromocytoma
  - paraganglioma
  - pcpg
  - neuroendocrine
  - multi-platform
processed_by: crosslinker
processed_at: 2026-05-14
---

# TCGA Pheochromocytoma and Paraganglioma (PCPG, Cancer Cell 2017)

## Overview

The pcpg_tcga_pub dataset is the TCGA pheochromocytoma and paraganglioma (PCPG) publication cohort, comprising multi-platform molecular profiling of 173 PCC/PGL tumors. Published in Cancer Cell (2017) by the TCGA PCPG Analysis Working Group, it represents the largest integrated genomic characterization of these rare neuroendocrine tumors. The study defines four molecular subtypes (kinase signaling, pseudohypoxia, Wnt-altered, cortical admixture), identifies [CSDE1](../genes/CSDE1.md) as a novel somatically-mutated driver, and discovers recurrent fusion genes involving [MAML3](../genes/MAML3.md), [BRAF](../genes/BRAF.md), [NGFR](../genes/NGFR.md), and [NF1](../genes/NF1.md). Head and neck paragangliomas were excluded due to insufficient post-embolization tumor tissue.

## Composition

- **173 patients** with pheochromocytoma ([PHC](../cancer_types/PHC.md)) or paraganglioma ([PGNG](../cancer_types/PGNG.md)).
- 57% female, 43% male; mean age at diagnosis 47 years (range 19–83).
- 11/173 (6%) had distant metastases; 16/173 (9%) had aggressive disease (distant metastases, positive regional lymph nodes, or local recurrence).
- Plasma/urine biochemistry available for 144/173 (83%); clinical genetic testing results for 116/173 (67%).
- Head and neck PGLs excluded (often embolized prior to surgery).
- Geographic mix includes sporadic and hereditary cases.

## Assays / panels (linked)

- [whole-exome sequencing](../methods/whole-exome-seq.md) — matched normal + tumor pairs.
- [Affymetrix SNP6 arrays](../methods/affymetrix-snp6.md) — somatic copy-number analysis.
- [mRNA sequencing](../methods/rna-seq.md) — expression profiling and subtype discovery.
- [miRNA sequencing](../methods/mirna-seq.md).
- [DNA methylation arrays](../methods/dna-methylation-array.md) — HM450.
- [Reverse phase protein arrays](../methods/rppa.md) (RPPA).
- Driver detection: [MutSig2](../methods/mutsig.md) (q<0.05); copy-number peaks by [GISTIC2](../methods/gistic.md); clonality by [ABSOLUTE](../methods/absolute.md); subtype discovery by [consensus hierarchical clustering](../methods/consensus-hierarchical-clustering.md).
- Ki-67 by [immunohistochemistry](../methods/immunohistochemistry.md) in a subset (n=62).

## Papers using this cohort

- [PMID:28162975](../papers/28162975.md) — TCGA PCPG Analysis Working Group 2017. Multi-platform characterization of 173 PCC/PGLs; identified [CSDE1](../genes/CSDE1.md) as a novel driver, discovered recurrent MAML3/BRAF/NGFR/NF1 fusions, defined four molecular subtypes, and established the Wnt-altered subtype ([MAML3](../genes/MAML3.md) fusions + CSDE1 mutations) as a marker of aggressive/metastatic disease.

## Notable findings derived from this cohort

- A driver mutation, fusion gene, or copy-number alteration was identified in 95% of PCC/PGLs [PMID:28162975](../papers/28162975.md).
- Pathogenic germline mutations in eight known susceptibility genes detected in 46/173 (27%): [SDHB](../genes/SDHB.md) (9%), [RET](../genes/RET.md) (6%), [VHL](../genes/VHL.md) (4%), [NF1](../genes/NF1.md) (3%); rarer germline events in [SDHD](../genes/SDHD.md), [MAX](../genes/MAX.md), [EGLN1](../genes/EGLN1.md), [TMEM127](../genes/TMEM127.md) [PMID:28162975](../papers/28162975.md).
- Low somatic mutation rate (mean 0.67 mutations/Mb), among the lowest across TCGA cancer types [PMID:28162975](../papers/28162975.md).
- Five MutSig2-significant somatic driver genes (q<0.05): [HRAS](../genes/HRAS.md), [NF1](../genes/NF1.md), [EPAS1](../genes/EPAS1.md), [RET](../genes/RET.md), and newly identified [CSDE1](../genes/CSDE1.md) [PMID:28162975](../papers/28162975.md).
- Recurrent fusion genes: [UBTF](../genes/UBTF.md)–[MAML3](../genes/MAML3.md) (7 tumors), [TCF4](../genes/TCF4.md)–[MAML3](../genes/MAML3.md) (1 tumor), KIAA1737–[NGFR](../genes/NGFR.md), RUNDC1–[BRAF](../genes/BRAF.md), [NF1](../genes/NF1.md)–RAB11FIP4; 10 tumors total were MAML3 fusion-positive [PMID:28162975](../papers/28162975.md).
- Four mRNA expression subtypes: kinase signaling (NF1/RET/HRAS/TMEM127-enriched), pseudohypoxia (SDH/VHL/EPAS1-enriched), Wnt-altered (MAML3 fusions + CSDE1 mutations, associated with aggressive disease and metastasis), cortical admixture (elevated adrenocortical markers, [MAX](../genes/MAX.md) germline mutations) [PMID:28162975](../papers/28162975.md).
- Wnt-altered subtype MAML3 fusion-positive tumors overexpressed MAML3 2.7-fold (p<5e-6), showed expansive hypomethylation (4,229 significant probes), and activated Wnt/Hedgehog signaling ([WNT4](../genes/WNT4.md), [WNT5A](../genes/WNT5A.md), [GLI2](../genes/GLI2.md)) [PMID:28162975](../papers/28162975.md).
- Markers of poor aggressive-disease-free survival: MAML3 fusion, [SDHB](../genes/SDHB.md) germline mutation, somatic [SETD2](../genes/SETD2.md) or [ATRX](../genes/ATRX.md) mutation, high somatic mutation total, Wnt-altered and pseudohypoxia mRNA subtypes, hypermethylated DNA methylation subtype [PMID:28162975](../papers/28162975.md).

## Sources

- cBioPortal study: pcpg_tcga_pub
- Published: TCGA PCPG Analysis Working Group, Cancer Cell 2017.

*This page was processed by **crosslinker** on **2026-05-14**.*
