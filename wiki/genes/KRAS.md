---
symbol: KRAS
aliases: []
cancer_types: [LUAD, LUSC, APAD, LCH, ECD, NSCLC, PAAD]
tags: [oncogene, mapk, driver, allele-specific]
processed_by: crosslinker
processed_at: 2026-04-10
---

# KRAS

## Overview

KRAS is a canonical RAS-family oncogene and one of the most frequently mutated drivers in human cancer, with prominent roles in [LUAD](../cancer_types/LUAD.md), colorectal, and pancreatic cancers.

## Alterations observed in the corpus

- Advanced [NSCLC](../cancer_types/NSCLC.md): detection of pathogenic KRAS alterations in ctDNA (vs tissue only) was associated with worse prognosis in the prospective ctDx Lung cohort (n=1,127) [PMID:36357680](../papers/36357680.md).
- Appendiceal adenocarcinoma: KRAS/NRAS mutations in the absence of [GNAS](../genes/GNAS.md) and [TP53](../genes/TP53.md) alterations mark the clinically indolent RAS-mut predominant MAAP subtype with lowest mutational and chromosomal burden and best [OS](../cancer_types/OS.md) [PMID:36493333](../papers/36493333.md).
- Histiocytosis: KRAS mutated in 7% of profiled cases; one case had co-occurring KRAS G12D and [BRAF](../genes/BRAF.md) D594H [PMID:36862133](../papers/36862133.md).
- Female germ cell tumors: KRAS among oncogenic mutations observed in a minority of cases [PMID:36862133](../papers/36862133.md).
- [LUAD](../cancer_types/LUAD.md) metastasis: KRAS G12C elevated (21%) in primaries that metastasized to liver vs the matched liver lesions (6%, p<0.001); mutually exclusive with [EGFR](../genes/EGFR.md) [PMID:37084736](../papers/37084736.md).
- [NSCLC](../cancer_types/NSCLC.md) brain metastases: KRAS commonly shared (truncal) between BM and matched primary or extracranial metastasis [PMID:37591896](../papers/37591896.md).
- KRAS was included in [LUAD](../cancer_types/LUAD.md) pathway/metastasis analyses in MSK-CHORD (n=24,950) [PMID:39506116](../papers/39506116.md).
- KRAS alterations characterized "biliary-class" intrahepatic cholangiocarcinoma (along with [SMAD4](../genes/SMAD4.md) and [CDKN2A](../genes/CDKN2A.md) loss), associated with markedly worse OS [PMID:38864854](../papers/38864854.md).
- In 1,360 resected [PAAD](../cancer_types/PAAD.md) patients at MSK (`pancreas_msk_2024`, 397 sequenced on [MSK-IMPACT](../methods/msk-impact-panel.md)), KRAS was altered in 90%; allele distribution G12D 36.5% / G12V 32.5% / G12R 13.9% / other 8.1% / WT 9.1%. KRAS^G12R^ was enriched in stage I (23% vs 11% in stage II–III, p=0.022), more often node-negative (47% vs 26% for G12D, p=0.019), and associated with improved OS and decreased distant recurrence; bulk RNA-seq (n=100) and [CosMx SMI](../methods/cosmx-smi.md) spatial profiling (n=20) identified enhanced KRAS signaling / EMT in KRAS^G12D^ tumors and increased TNF/NF-κB signaling in KRAS^G12R^; isogenic Kras^G12R/+^;Trp53^KO^ mouse PDAC organoids recapitulated reduced migration and improved orthotopic survival [PMID:39214094](../papers/39214094.md).
- KRAS mutations were detected in CSF ctDNA from [NSCLC](../cancer_types/NSCLC.md) patients with CNS involvement in the [csf_msk_2024](../datasets/csf_msk_2024.md) cohort (1,007 CSF samples, 711 patients); KRAS appeared as an off-target resistance alteration in EGFR-mutant patients [PMID:39289779](../papers/39289779.md).

## Cancer types (linked)

- [LUAD](../cancer_types/LUAD.md) — KRAS G12C enrichment in liver-metastasizing primaries and truncal KRAS in brain-metastatic trajectories [PMID:37084736](../papers/37084736.md) [PMID:37591896](../papers/37591896.md).
- [APAD](../cancer_types/APAD.md) — RAS-mut predominant MAAP subtype has best prognosis and 50% first-line chemotherapy response [PMID:36493333](../papers/36493333.md).
- [LCH](../cancer_types/LCH.md) / [ECD](../cancer_types/ECD.md) — KRAS mutated in 7% of histiocytosis [PMID:36862133](../papers/36862133.md).
- Advanced [NSCLC](../cancer_types/NSCLC.md) — ctDNA-detected KRAS associated with worse prognosis [PMID:36357680](../papers/36357680.md).
- [PAAD](../cancer_types/PAAD.md) — KRAS altered in 90% of resected PDAC; G12R is prognostically favorable (early-stage, node-negative, longer OS) while G12D drives canonical KRAS/EMT programs [PMID:39214094](../papers/39214094.md).

## Co-occurrence and mutual exclusivity

- [LUAD](../cancer_types/LUAD.md): KRAS alterations mutually exclusive with [EGFR](../genes/EGFR.md) alterations [PMID:37084736](../papers/37084736.md).
- [APAD](../cancer_types/APAD.md) MAAP: defining subtype requires KRAS/NRAS mutation in the absence of [GNAS](../genes/GNAS.md) and [TP53](../genes/TP53.md) [PMID:36493333](../papers/36493333.md).

## Therapeutic relevance

- ctDNA-guided matching to targeted therapy in [NSCLC](../cancer_types/NSCLC.md) (including KRAS-directed regimens) yielded OS benefit vs untreated ctDNA-positive patients (HR 0.63, 95% CI 0.52–0.76, P<0.001) [PMID:36357680](../papers/36357680.md).
- RAS-mut predominant MAAP shows 50% first-line chemotherapy response vs 6% in GNAS-mut predominant MAAP (P=.03) [PMID:36493333](../papers/36493333.md).

## Open questions

- Mechanistic basis for apparent loss of KRAS G12C clones in matched liver metastases of [LUAD](../cancer_types/LUAD.md) is unresolved [PMID:37084736](../papers/37084736.md).
- Mechanistic basis for reduced metastatic propensity of KRAS^G12R^ [PAAD](../cancer_types/PAAD.md) beyond the NF-κB / EMT axis identified by spatial profiling and organoids remains to be resolved [PMID:39214094](../papers/39214094.md).

## Sources

- [PMID:36357680](../papers/36357680.md)
- [PMID:36493333](../papers/36493333.md)
- [PMID:36862133](../papers/36862133.md)
- [PMID:37084736](../papers/37084736.md)
- [PMID:37591896](../papers/37591896.md)
- [PMID:39506116](../papers/39506116.md)
- [PMID:38864854](../papers/38864854.md)
- [PMID:39214094](../papers/39214094.md)
- [PMID:39289779](../papers/39289779.md)

*This page was processed by **crosslinker** on **2026-04-10**.*
