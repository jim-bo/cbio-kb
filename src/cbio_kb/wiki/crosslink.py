"""Deterministic crosslinker: rewrite bare entity mentions as Markdown links.

Driven by the filesystem — only links to pages that actually exist on disk.
Eliminates the family-completion hazard (e.g. crosslinker inventing FGFR1.md
from "pan-FGFR" prose) that plagued the agent-based crosslinker.

Rules:
- Only link entities whose wiki page exists under wiki/{genes,cancer_types,datasets,drugs,methods}/.
- Case-sensitive, word-boundary matches only. Gene symbols must match verbatim.
- Skip content inside:
  * YAML frontmatter (between leading ---\\n and the next ---\\n)
  * fenced code blocks (``` ... ```)
  * inline code (`...`)
  * existing markdown links ([text](url)) — match the literal display text only
  * headings (to keep them clean)
- Only link the FIRST occurrence of each entity per page.
- Never self-link (a gene page doesn't link to itself).
- Skip very short / ambiguous tokens unless they are the primary kind — see STOPWORDS.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

KINDS = ["genes", "cancer_types", "datasets", "drugs", "methods"]

# Short uppercase tokens that are real genes but also common English words.
# Only link them if they're clearly the gene (we keep them — but flag here if needed later).
STOPWORDS = {"A", "I", "IT", "OR", "AS", "IS", "BE", "AN", "TO", "OF", "ON", "IN", "BY"}


def _load_entities(wiki: Path) -> dict[str, dict[str, Path]]:
    out: dict[str, dict[str, Path]] = {k: {} for k in KINDS}
    for k in KINDS:
        for p in sorted((wiki / k).glob("*.md")):
            out[k][p.stem] = p
    return out


def _mask_protected_regions(text: str) -> list[tuple[int, int]]:
    """Return a list of (start, end) ranges that must not be modified."""
    protected: list[tuple[int, int]] = []

    # YAML frontmatter
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            protected.append((0, end + 5))

    # Fenced code blocks ```...```
    for m in re.finditer(r"```.*?```", text, re.DOTALL):
        protected.append(m.span())

    # Inline code `...`
    for m in re.finditer(r"`[^`\n]+`", text):
        protected.append(m.span())

    # Existing markdown links [text](url) — protect the whole link
    for m in re.finditer(r"\[[^\]]+\]\([^)]+\)", text):
        protected.append(m.span())

    # Headings (whole line)
    for m in re.finditer(r"^#{1,6} .*$", text, re.MULTILINE):
        protected.append(m.span())

    # Footer italic provenance line
    for m in re.finditer(r"^\*This page was processed by .*$", text, re.MULTILINE):
        protected.append(m.span())

    return protected


def _in_protected(pos: int, protected: list[tuple[int, int]]) -> bool:
    for s, e in protected:
        if s <= pos < e:
            return True
    return False


def _rel_link(from_page: Path, target: Path) -> str:
    """Produce a relative link from from_page to target."""
    # Both are under wiki/<kind>/<name>.md, same depth.
    # from wiki/genes/X.md → wiki/drugs/Y.md == "../drugs/Y.md"
    up = "../" * (len(from_page.relative_to(from_page.parents[1]).parts) - 1)
    rel = up + target.relative_to(from_page.parents[1]).as_posix()
    return rel


def crosslink_file(path: Path, entities: dict[str, dict[str, Path]]) -> tuple[int, str]:
    """Return (links_added, new_text)."""
    text = path.read_text()
    protected = _mask_protected_regions(text)

    # Track which entities we've already linked in this file (first-occurrence only).
    already_linked: set[tuple[str, str]] = set()

    # Build a flat list of (name, kind, target_path), sorted longest-first to prefer
    # "enfortumab-vedotin" over "vedotin" if both existed.
    flat: list[tuple[str, str, Path]] = []
    for kind, d in entities.items():
        for name, p in d.items():
            if p == path:
                continue  # never self-link
            if name in STOPWORDS:
                continue
            flat.append((name, kind, p))
    flat.sort(key=lambda x: -len(x[0]))

    # We do a single left-to-right scan and track new protected regions as we insert links.
    # Because inserting changes offsets, we instead collect (start, end, replacement)
    # in original coordinates and apply in reverse.
    edits: list[tuple[int, int, str]] = []

    for name, kind, target in flat:
        if (kind, name) in already_linked:
            continue
        # Escape for regex; require word boundaries
        pat = re.compile(rf"(?<![\w/-]){re.escape(name)}(?![\w/-])")
        for m in pat.finditer(text):
            if _in_protected(m.start(), protected):
                continue
            # Check overlap with existing edits
            if any(not (m.end() <= s or m.start() >= e) for s, e, _ in edits):
                continue
            link = f"[{name}]({_rel_link(path, target)})"
            edits.append((m.start(), m.end(), link))
            already_linked.add((kind, name))
            break  # first occurrence only

    # Apply edits in reverse
    edits.sort(key=lambda x: -x[0])
    new_text = text
    for s, e, repl in edits:
        new_text = new_text[:s] + repl + new_text[e:]

    return len(edits), new_text


def run(wiki_dir: Path, paths: list[Path] | None = None, *, dry_run: bool = False) -> int:
    wiki_dir = wiki_dir.resolve()
    entities = _load_entities(wiki_dir)

    if paths:
        targets = [p.resolve() for p in paths]
    else:
        targets = sorted(wiki_dir.rglob("*.md"))
        # Skip index.md
        targets = [p for p in targets if p.name != "index.md"]

    total_links = 0
    changed = 0
    for p in targets:
        if not p.exists():
            print(f"skip (missing): {p}")
            continue
        n, new_text = crosslink_file(p, entities)
        if n == 0:
            continue
        changed += 1
        total_links += n
        if dry_run:
            print(f"  would add {n:3d} links → {p.relative_to(wiki_dir.parent)}")
        else:
            p.write_text(new_text)
            print(f"  added {n:3d} links → {p.relative_to(wiki_dir.parent)}")

    print(f"[crosslink] {total_links} links across {changed} pages"
          + (" (dry run)" if dry_run else ""))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="cbio-kb crosslink")
    ap.add_argument("--wiki-dir", default="wiki")
    ap.add_argument("--paths", nargs="*", help="Specific pages to crosslink (default: all)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    return run(Path(args.wiki_dir),
               [Path(p) for p in args.paths] if args.paths else None,
               dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
