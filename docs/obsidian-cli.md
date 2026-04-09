# Obsidian CLI cheat sheet for cbio-kb agents

The Obsidian app ships an official CLI (`obsidian` on PATH). It is a remote-control for a running Obsidian instance, operating on a named vault. For this repo the vault is `wiki` (mapped to `wiki/` on disk).

**Always pass `vault=wiki` as the first argument** so commands don't resolve against whichever vault happens to be active.

Prefer these commands over `Read` / `Grep` / `Glob` when the target lives in `wiki/`. They return structured JSON and cost a fraction of the tokens.

Two non-obvious rules apply once you start writing files:

- **Call `obsidian vault=wiki reload` after any `Write` into `wiki/`.** Otherwise the CLI will return "File not found" against just-written paths. See "Reload after Write" below.
- **Use outline-guided narrow Reads for merge-append edits.** The `Edit` tool's "must Read first" precondition would otherwise force full-file Reads that dwarf the CLI savings. See "Narrow reads for merge-append" below.

## Quick mapping

| You want to... | Don't | Do |
| :-- | :-- | :-- |
| Skim a paper's structure | `Read wiki/papers/{pmid}.md` | `obsidian vault=wiki outline path=papers/{pmid}.md format=json` |
| Read only frontmatter | `Read` + truncate | `obsidian vault=wiki properties path=papers/{pmid}.md format=json` |
| Read a single property | `Grep pmid:` | `obsidian vault=wiki property:read name=pmid path=papers/{pmid}.md` |
| Find entity mentions with context | `Grep -C 3 EGFR wiki/papers` | `obsidian vault=wiki search:context query=EGFR format=json limit=20` |
| List matching files only | `Grep -l EGFR` | `obsidian vault=wiki search query=EGFR format=json` |
| Find pages citing an entity | `Grep '\[\[EGFR\]\]' wiki/` | `obsidian vault=wiki backlinks file=EGFR format=json` |
| List outgoing links of a page | `Grep '\[.*\](.*\.md)'` | `obsidian vault=wiki links path=papers/{pmid}.md` |
| List files in a wiki folder | `Glob wiki/papers/*.md` | `obsidian vault=wiki files folder=papers` |
| Lint: unresolved wikilinks | custom walker | `obsidian vault=wiki unresolved format=json` |
| Lint: orphan / dead-end pages | custom walker | `obsidian vault=wiki orphans` / `deadends` |
| Pages carrying a tag | grep frontmatter | `obsidian vault=wiki tag name=<tag>` |

## Full-content reads

The CLI can also read the body (`obsidian vault=wiki read path=...`), but for token efficiency prefer `outline` + targeted `search:context` to jump straight to the lines you need. Only fall back to a full read when you actually need surrounding prose.

## Reload after Write

The Obsidian CLI is a remote-control for a running Obsidian app. When you create a new file via `Write` (or modify the filesystem outside of Obsidian), the running app does **not** see the change until it re-scans the vault. Subsequent `outline` / `properties` / `search` / `backlinks` calls against the new path will return "File not found" — a silent failure that wastes tool calls.

**Rule: after every `Write` into `wiki/`, call `obsidian vault=wiki reload`.** This is a bare command with no arguments:

```bash
obsidian vault=wiki reload
```

One call is enough for any number of file changes; it does not need to be per-file. In practice, run it once at the end of a batch of Writes, or once before the next CLI read against a just-written path.

**Worktree caveat.** Obsidian registers the `wiki` vault at a single absolute path (see `~/Library/Application Support/obsidian/obsidian.json`). Typically that path is the main checkout (`…/cbio-vec/wiki`). When you run an agent from a git worktree (`…/cbio-vec/.worktrees/<branch>/wiki`), the CLI continues to talk to the main-repo vault — so `reload` still exits 0 and prints "Reloading..." but never sees files you wrote inside the worktree. In that case the CLI is effectively unusable for just-written files regardless of reload; you must fall back to `Read` / `Glob` / `ls` for anything touched in the current session. Either (a) run the paper-compilation workflow from the main checkout, (b) temporarily re-register the vault at the worktree's wiki path, or (c) accept the staleness and use Read/Glob for your own Writes. The CLI's non-Write operations (outline, properties, search on pre-existing pages) still work from a worktree as long as those pages exist in main.

## Narrow reads for merge-append

The `Edit` tool requires a prior `Read` on the same file before it will accept an edit. For large entity pages (genes, cancer types) this turns every merge-append into a full-file Read of 5–20k tokens just to find a unique anchor string, which defeats most of the CLI savings.

The win: use `outline` to locate the section you're editing, then `Read` only the line range that section covers. A 10–30 line slice is ~1–2k tokens.

Pattern:

1. Get the heading map:
   ```bash
   obsidian vault=wiki outline path=genes/KRAS.md format=json
   ```
   Returns `[{level, heading, line}, …]` — the `line` fields are 1-indexed line numbers in the file.
2. Pick the H2 section you need to edit. For entity-page-writer merges this is usually `## Alterations observed in the corpus`, `## Cancer types (linked)`, or `## Sources`.
3. Compute the slice: `offset = <section_line>`, `limit = <next_heading_line> - <section_line>` (or a safe upper bound like 30 for the final `## Sources` section, which is always the last H2 before the footer).
4. Narrow Read:
   ```
   Read path=/abs/path/to/wiki/genes/KRAS.md offset=<section_line> limit=<slice_size>
   ```
5. `Edit` using an anchor string drawn from the slice.

**Caveat:** `Edit`'s `old_string` must be unique in the *whole* file, not just in the slice. H2 headings and PMID-tagged bullet text are normally unique, but if `Edit` fails with "not unique", fall back to a full-file `Read` and retry with a longer anchor. This should be rare.

For the two most common merge-append operations:

- **Append a PMID to `## Sources`**: `## Sources` is always the last H2. Offset to its line, `limit=30`, and the slice will cover the full list + footer.
- **Append a bullet to `## Alterations observed in the corpus`**: outline gives both the Alterations line and the next H2 line; Read exactly that range.

## Hard rules for agents

- **Only use for `wiki/` content.** `data/raw/`, `schema/`, `.claude/`, code — those still use Read / Grep / Glob.
- **Never edit via the CLI.** Agents that modify pages (paper-compiler, entity-page-writer, crosslinker) must use `Edit` / `Write` on the underlying file so diffs land in git. The CLI is read-only from our perspective.
- **Paths are vault-relative**, not filesystem-relative. `path=papers/39506116.md`, not `path=wiki/papers/39506116.md`.
- **`file=` resolves like a wikilink** (by stem, no extension). `file=EGFR` → `genes/EGFR.md`. Use `path=` when you need to be exact.
- **JSON please.** Pass `format=json` on every command that supports it — the default TSV is harder to parse and wastes tokens.

## Preconditions

- `obsidian` must be on PATH (`/usr/local/bin/obsidian` on this machine).
- The Obsidian app must be running; the CLI will auto-launch it otherwise.
- The `wiki` vault must be registered with Obsidian. Check with `obsidian vaults`.
