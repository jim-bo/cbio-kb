---
name: MSK-ACCESS (liquid biopsy, generic)
slug: msk-access
kind: method
canonical_source: corpus
unverified: true
tags: [ctdna, liquid-biopsy, targeted-sequencing, msk]
processed_by: crosslinker
processed_at: 2026-04-30
---

# MSK-ACCESS (liquid biopsy, generic)

## Overview

MSK-ACCESS is a targeted next-generation sequencing panel for cell-free DNA from plasma, used at MSK for ctDNA profiling. The canonical 129-gene version is [ACCESS129](../methods/ACCESS129.md). This page serves as a generic slug used where the specific version is not distinguished [PMID:38922339](../papers/38922339.md).

## Used by

- [PMID:38922339](../papers/38922339.md) — MSK-ACCESS was one of three sequencing platforms (alongside [MSK-IMPACT](../methods/msk-impact-panel.md) and MSK-Fusion) used to sequence 97,024 samples from 69,337 patients at MSK between January 2014 and November 2022; samples contributed to identification of 212 patients with oncogenic [BRAF](../genes/BRAF.md) fusions across 52 histologies [PMID:38922339](../papers/38922339.md).
- [PMID:39289779](../papers/39289779.md) — MSK-ACCESS ([ACCESS129](../methods/ACCESS129.md), 129-gene cfDNA panel) was applied to a paired plasma subset of 31 patients from the CSF ctDNA cohort to compare liquid-biopsy compartments; CSF VAFs were markedly higher than matched plasma (median 36.4% vs 2.3%, p<0.01); 75% of OncoKB level 1–3A alterations were shared between CSF and plasma [PMID:39289779](../papers/39289779.md).
- [PMID:40256659](../papers/40256659.md) — MSK-ACCESS (ACCESS129, 129-gene tumor-uninformed cfDNA panel, depth >15,000×) applied to pretreatment plasma from 201 patients with metastatic urothelial carcinoma in the CALGB 90601 trial; higher pretreatment ctDNA VAF (³√VAF₇₅ₚc) was independently associated with shorter [OS](../cancer_types/OS.md) (multivariable HR 2.51, p=0.009) and PFS; [TERT](../genes/TERT.md) promoter (57%), [PIK3CA](../genes/PIK3CA.md) (11%), and [ERBB2](../genes/ERBB2.md) (14%) alterations identified as candidate prognostic biomarkers [PMID:40256659](../papers/40256659.md).

## Notes

- For the canonical 129-gene panel, see [ACCESS129](../methods/ACCESS129.md).
- Corpus-grown slug; the specific gene-panel version is `ACCESS129` in `schema/ontology/gene_panels.json`.

## Sources

- [PMID:38922339](../papers/38922339.md)
- [PMID:39289779](../papers/39289779.md)
- [PMID:40256659](../papers/40256659.md)

*This page was processed by **crosslinker** on **2026-04-30**.*
