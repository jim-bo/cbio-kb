---
name: Pheochromocytoma
oncotree_code: PHC
main_type: Pheochromocytoma
parent: ADRENAL_GLAND
tags: []
processed_by: crosslinker
processed_at: 2026-05-14
---

# Pheochromocytoma (PHC)

## Overview

Pheochromocytoma (PHC) is a neuroendocrine tumor arising from chromaffin cells of the adrenal medulla that secretes catecholamines (epinephrine, norepinephrine). It is classified within the PCPG (pheochromocytoma and paraganglioma) family. At least 40% of PCCs are hereditary, driven by germline mutations in [SDHB](../genes/SDHB.md), [SDHD](../genes/SDHD.md), [SDHC](../genes/SDHC.md), SDHAF2, [VHL](../genes/VHL.md), [RET](../genes/RET.md), [NF1](../genes/NF1.md), [MAX](../genes/MAX.md), [TMEM127](../genes/TMEM127.md), [EGLN1](../genes/EGLN1.md), or [FH](../genes/FH.md). Approximately 10–15% are malignant (defined by metastasis). The TCGA PCPG analysis defined four molecular subtypes with distinct molecular drivers and clinical behavior.

## Cohorts in the corpus

- [pcpg_tcga_pub](../datasets/pcpg_tcga_pub.md) — TCGA PCPG multi-platform analysis of 173 pheochromocytoma and paraganglioma samples [PMID:28162975](../papers/28162975.md).

## Recurrent alterations

- TCGA PCPG cohort (n=173 total PCC/PGL): 95% of tumors had a driver identified; 46/173 (27%) had pathogenic germline mutations in 8 susceptibility genes — highest rates: SDHB (9%), RET (6%), VHL (4%), NF1 (3%); somatic drivers: [HRAS](../genes/HRAS.md) Q61 hotspot (kinase signaling subtype), [EPAS1](../genes/EPAS1.md) hotspots A530/P531/Y532 (pseudohypoxia subtype), RET M918 somatic (vs germline C634), [CSDE1](../genes/CSDE1.md) truncating/splice-site mutations (novel driver, Wnt-altered subtype); recurrent fusions: UBTF-MAML3 and TCF4-MAML3 (10 tumors, all Wnt-altered subtype), RUNDC1-BRAF (5.2-fold [BRAF](../genes/BRAF.md) overexpression) [PMID:28162975](../papers/28162975.md).
- Mean somatic mutation rate 0.67/Mb — among the lowest of TCGA tumor types [PMID:28162975](../papers/28162975.md).
- [MAML3](../genes/MAML3.md) fusions, SDHB germline mutations, SETD2/ATRX somatic mutations, Wnt-altered and pseudohypoxia subtypes, and hypermethylated DNA-methylation subtype all independently associated with poor aggressive-disease-free survival [PMID:28162975](../papers/28162975.md).

## Subtypes

- Kinase signaling subtype: predominantly PCC; NF1, RET, TMEM127, HRAS mutations; highest epinephrine production; BRAF/NGFR fusions; best prognosis.
- Pseudohypoxia subtype: SDHB/SDHD/VHL/EPAS1 mutations; genome-doubled; hypermethylated; miR-210 overexpression; highest metastatic risk.
- Wnt-altered subtype: MAML3 fusions + CSDE1 mutations; sporadic adrenal PCCs; highest [CHGA](../genes/CHGA.md); poor prognosis; no germline susceptibility-gene mutations.
- Cortical admixture subtype: adrenal cortex marker overexpression; MAX germline mutations; elevated leukocyte infiltration.

## Therapeutic landscape

- Surgical resection is curative for localized disease.
- Malignant PHC: [sunitinib](../drugs/sunitinib.md) (VHL/kinase-pathway), [temozolomide](../drugs/temozolomide.md) + DTIC (SDHB-mutant, high [MGMT](../genes/MGMT.md) methylation), PRRT with Lu-DOTATATE (somatostatin-receptor expressing).
- MAML3 fusion/Wnt-altered: Wnt-pathway antagonists (beta-catenin inhibitors, [STAT3](../genes/STAT3.md) inhibitors) proposed [PMID:28162975](../papers/28162975.md).
- SDH-mutant: glutaminase inhibitors under investigation [PMID:28162975](../papers/28162975.md).

## Sources

- [PMID:28162975](../papers/28162975.md) — TCGA PCPG Analysis Working Group, multi-platform profiling of 173 PCC/PGL tumors.

*This page was processed by **crosslinker** on **2026-05-14**.*
