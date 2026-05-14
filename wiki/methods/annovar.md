---
name: ANNOVAR
slug: annovar
kind: method
canonical_source: corpus
unverified: true
tags: [variant-annotation, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-14
---

# ANNOVAR

## Overview

ANNOVAR (ANNOtate VARiation) is a bioinformatics tool for functionally annotating genetic variants identified by next-generation sequencing. It annotates SNVs and indels against multiple databases including gene function, conservation scores, disease associations, and population allele frequencies.

## Used by

- Applied in ICGC PedBrain pilocytic astrocytoma whole-genome sequencing study (96 cases) for functional annotation of somatic variants, used alongside [oncotator](../methods/oncotator.md); PCR + [sanger-sequencing](../methods/sanger-sequencing.md) achieved >98% SNV verification [PMID:23817572](../papers/23817572.md)
- Used for variant functional annotation in the grade II glioma exome sequencing study (n=23 paired initial/recurrent tumors) to annotate somatic mutations with gene, consequence, and population frequency information [PMID:24336570](../papers/24336570.md)
- Used for variant functional annotation in the rhabdomyosarcoma genomic landscape study (147 tumor/normal pairs, WGS + WES + RNA-seq); run alongside Oncotator to annotate somatic mutations with gene consequence and population frequency [PMID:24436047](../papers/24436047.md)
- Used for variant annotation in whole-genome and whole-exome sequencing of 28 uveal melanoma samples; identified [PLCB4](../genes/PLCB4.md) p.D630Y as a recurrent gain-of-function hotspot mutually exclusive with GNAQ/GNA11 [PMID:26683228](../papers/26683228.md).
- ANNOVAR used for functional annotation of somatic variants called by the HGSC Mercury pipeline in 160 periampullary tumors, alongside COSMIC and dbSNP databases [PMID:26804919](../papers/26804919.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Typically used downstream of alignment and variant calling (e.g., MuTect, Pindel), before biological interpretation.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26683228](../papers/26683228.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
