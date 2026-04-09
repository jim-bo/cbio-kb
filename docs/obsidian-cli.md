# Obsidian CLI cheat sheet for cbio-kb agents

The Obsidian app ships an official CLI (`obsidian` on PATH). It is a remote-control for a running Obsidian instance, operating on a named vault. For this repo the vault is `wiki` (mapped to `wiki/` on disk).

**Always pass `vault=wiki` as the first argument** so commands don't resolve against whichever vault happens to be active.

Prefer these commands over `Read` / `Grep` / `Glob` when the target lives in `wiki/`. They return structured JSON and cost a fraction of the tokens.

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
