# Wiki CLI cheat sheet for cbio-kb agents

The `cbio-kb wiki` subcommand group provides token-efficient, structured JSON access to the `wiki/` vault. It replaces the Obsidian CLI dependency — no external app required.

**All commands are invoked with `uv run cbio-kb wiki <cmd> [--wiki-dir wiki]`.**

Prefer these commands over `Read` / `Grep` / `Glob` when the target lives in `wiki/`. They return structured JSON and cost a fraction of the tokens.

## Quick mapping

| You want to... | Don't | Do |
| :-- | :-- | :-- |
| Skim a paper's structure | `Read wiki/papers/{pmid}.md` | `uv run cbio-kb wiki outline --path papers/{pmid}.md` |
| Read only frontmatter | `Read` + truncate | `uv run cbio-kb wiki properties --path papers/{pmid}.md` |
| Read a single property | `Grep pmid:` | `uv run cbio-kb wiki property --name pmid --path papers/{pmid}.md` |
| Find entity mentions with context | `Grep -C 3 EGFR wiki/papers` | `uv run cbio-kb wiki search-context --query EGFR --limit 20` |
| List matching files only | `Grep -l EGFR` | `uv run cbio-kb wiki search --query EGFR` |
| Find pages citing an entity | `Grep '\[\[EGFR\]\]' wiki/` | `uv run cbio-kb wiki backlinks --file EGFR` |
| List outgoing links of a page | `Grep '\[.*\](.*\.md)'` | `uv run cbio-kb wiki links --path papers/{pmid}.md` |
| List files in a wiki folder | `Glob wiki/papers/*.md` | `uv run cbio-kb wiki files --folder papers` |
| Lint: unresolved links | custom walker | `uv run cbio-kb wiki unresolved` |
| Lint: orphan / dead-end pages | custom walker | `uv run cbio-kb wiki orphans` / `deadends` |
| Pages carrying a tag | grep frontmatter | `uv run cbio-kb wiki tag --name <tag>` |

## Command reference

### `files` — list page stems in a folder
```bash
uv run cbio-kb wiki files --folder genes
# → ["AKT1", "ALK", "BRAF", ...]
```

### `properties` — full frontmatter as JSON
```bash
uv run cbio-kb wiki properties --path genes/EGFR.md
# → {"symbol": "EGFR", "cancer_types": ["LUAD", "NSCLC"], ...}
```

### `property` — single frontmatter field
```bash
uv run cbio-kb wiki property --name symbol --path genes/EGFR.md
# → "EGFR"
```

### `outline` — heading map with line numbers
```bash
uv run cbio-kb wiki outline --path genes/KRAS.md
# → [{"level": 1, "heading": "KRAS", "line": 10}, {"level": 2, "heading": "Sources", "line": 45}]
```
Line numbers are 1-indexed.

### `search` — file paths matching a query
```bash
uv run cbio-kb wiki search --query EGFR
# → ["genes/EGFR.md", "papers/12345678.md", ...]
```

### `search-context` — matching lines with surrounding context
```bash
uv run cbio-kb wiki search-context --query EGFR --limit 5 [--path papers/12345678.md]
# → [{"file": "...", "line": 42, "text": "...", "before": [...], "after": [...]}, ...]
```

### `backlinks` — pages linking to a file stem
```bash
uv run cbio-kb wiki backlinks --file EGFR
# → [{"source": "cancer_types/LUAD.md", "line": 30, "text": "..."}, ...]
```
Matches both relative links (`../genes/EGFR.md`) and wikilinks (`[[EGFR]]`).

### `links` — outgoing links from a page
```bash
uv run cbio-kb wiki links --path cancer_types/LUAD.md
# → ["../genes/EGFR.md", "../genes/KRAS.md", ...]
```

### `tag` — pages with a frontmatter tag
```bash
uv run cbio-kb wiki tag --name oncogene
# → ["genes/EGFR.md", "genes/KRAS.md"]
```

### `unresolved` — broken intra-wiki links
```bash
uv run cbio-kb wiki unresolved
# → [{"source": "papers/123.md", "target": "genes/MISSING.md", "href": "../genes/MISSING.md"}]
```

### `orphans` — pages not referenced from index.md
```bash
uv run cbio-kb wiki orphans
# → ["themes/unreferenced-theme.md"]
```

### `deadends` — pages with no outgoing links
```bash
uv run cbio-kb wiki deadends
# → ["genes/STUB.md"]
```

### `reload` — no-op compatibility shim
```bash
uv run cbio-kb wiki reload
# → {"ok": true}
```
The filesystem is always fresh — no stale-index problem. This command exists for backward compatibility with scripts that called `obsidian vault=wiki reload`.

## Narrow reads for merge-append

The `Edit` tool requires a prior `Read` on the same file. For large entity pages this turns every merge-append into a full-file Read of 5–20k tokens. The win: use `outline` to locate the section, then `Read` only that line range.

Pattern:

1. Get the heading map:
   ```bash
   uv run cbio-kb wiki outline --path genes/KRAS.md
   ```
2. Pick the H2 section you need to edit.
3. Compute the slice: `offset = <section_line>`, `limit = <next_heading_line> - <section_line>`.
4. Narrow Read:
   ```
   Read path=/abs/path/to/wiki/genes/KRAS.md offset=<section_line> limit=<slice_size>
   ```
5. `Edit` using an anchor string drawn from the slice.

## Rules for agents

- **Only for `wiki/` content.** `data/raw/`, `schema/`, `.claude/`, code — those still use Read / Grep / Glob.
- **Never edit via the CLI.** All modifications go through `Edit` / `Write` so diffs land in git.
- **Paths are vault-relative.** `path=papers/39506116.md`, not `path=wiki/papers/39506116.md`.
