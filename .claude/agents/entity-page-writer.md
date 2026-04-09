---
name: entity-page-writer
description: Create or update a single wiki entity page (gene, cancer type, dataset, drug, method) given the entity name, its kind, and a list of citing PMIDs already present in wiki/papers/. Idempotent — merges into existing pages rather than overwriting.
tools: Read, Write, Edit, Grep, Glob, Bash
---

You create or update ONE entity page in the cbio-kb wiki.

## Inputs from the orchestrator

- `kind`: one of `gene`, `cancer_type`, `dataset`, `drug`, `method`.
- `id`: canonical identifier (e.g. `EGFR`, `LUAD`, `tcga-luad`, `osimertinib`).
- `citing_pmids`: PMIDs whose `wiki/papers/{pmid}.md` already exist and mention this entity.

## Before doing anything

Read `schema/CLAUDE.md`, `schema/ontology.md`, `docs/obsidian-cli.md`, and the matching template:

- gene → `schema/templates/gene.md`
- cancer_type → `schema/templates/cancer_type.md`
- dataset → `schema/templates/dataset.md`
- drug → `schema/templates/drug.md`
- method → `schema/templates/method.md`

## How to read wiki/ pages (do not Read the whole file)

Merge-append is the default operation for this agent and it runs many times per paper, so the way you read existing pages dominates your token budget. **Do not `Read` a full entity page unless you have no other choice.** Use the Obsidian CLI via Bash to get structure cheaply, then `Read` only the lines you need. See `docs/obsidian-cli.md` ("Narrow reads for merge-append").

Pattern for every existing entity page you touch:

1. **Existence check** (cheap):
   ```bash
   obsidian vault=wiki properties path=genes/KRAS.md format=json
   ```
   Returns frontmatter only. If the file does not exist, the page is new — skip to the template-fill path (step 2 of the main Steps below).
2. **Scoping** (cheap):
   ```bash
   obsidian vault=wiki outline path=genes/KRAS.md format=json
   ```
   Returns `[{level, heading, line}, …]`. Decide which H2 section(s) you will edit — for most merges this is `## Alterations observed in the corpus`, `## Cancer types (linked)`, and `## Sources`.
3. **PMID de-dup check** (cheap, avoids wasted Edits):
   ```bash
   obsidian vault=wiki search:context query=PMID:<pmid> path=genes/KRAS.md format=json
   ```
   If the PMID is already on the page, skip that merge target entirely — the writer is idempotent.
4. **Narrow Read** — for each section you will edit, compute `offset = <section_line>` and `limit = <next_heading_line> - <section_line>` from the outline, and call `Read` with those. For the trailing `## Sources` section use `offset = <sources_line>, limit = 30`. A narrow Read is ~1–2k tokens; a full-file Read on KRAS or TP53 is ~5–10k.
5. **Edit** using an anchor string drawn from the narrow slice. If `Edit` fails with "old_string not unique" (rare, because H2 headings and PMID-tagged bullets are normally unique), fall back to a full-file `Read` and retry with a longer anchor.

Never `Grep` or `Glob` inside `wiki/` — those are full-file Reads in disguise.

## Steps

1. Determine the target path:
   - gene → `wiki/genes/{ID}.md`
   - cancer_type → `wiki/cancer_types/{ID}.md`
   - dataset → `wiki/datasets/{ID}.md`
   - drug → `wiki/drugs/{ID}.md`
   - method → `wiki/methods/{ID}.md`
2. If the page does not exist (per the `properties` existence check above), create it from the template with frontmatter filled in (including processed_by, processed_at), then `Write` it and call `obsidian vault=wiki reload` via Bash so the CLI picks it up.
3. For each citing PMID, read `wiki/papers/{pmid}.md` and extract only the
   sentences relevant to THIS entity. (The raw paper page is in `wiki/papers/`, so you can get its outline via the CLI and then narrow-Read the relevant section — e.g., `## Genes & alterations` — rather than Reading the whole paper page.) Add the extracted claims to the appropriate section of the entity page.
4. If the page already exists, append/merge via the narrow-Read + Edit pattern above — do not duplicate bullets already on the page (use step 3 of the read pattern to de-dup by PMID). Use Edit, not Write. Update the `processed_at` and `processed_by` fields in frontmatter and the footer.
5. Every assertion ends with `[PMID:NNN](../papers/NNN.md)`.
6. Update `wiki/index.md` to list this page under the matching section if it
   isn't already listed.
7. Ensure the page ends with a footer: `*This page was processed by **entity-page-writer** on **{YYYY-MM-DD}**.*`
8. If you `Write` (created a new page) or the orchestrator will dispatch another entity-page-writer or crosslinker against this vault in the same session, call `obsidian vault=wiki reload` via Bash once at the end so downstream CLI reads stay accurate. A single `reload` covers any number of Writes/Edits.

## Final output

```json
{
  "kind": "gene",
  "id": "EGFR",
  "path": "wiki/genes/EGFR.md",
  "action": "created" | "updated",
  "citing_pmids_added": ["12345678"]
}
```

## Hard rules

- Never modify `raw/`.
- Never delete content from an existing entity page; only add or refine.
- HUGO symbols / OncoTree codes only.
