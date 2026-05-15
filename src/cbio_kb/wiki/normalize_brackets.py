"""Deterministic repair for malformed Obsidian-style links in wiki/ markdown.

Background: agents (paper-compiler in particular) sometimes reach for Obsidian
wiki-link syntax (`[[name]]`, `[[name](url)]]`, etc.) instead of plain Markdown
links. The unbalanced variants send pandoc into catastrophic backtracking and
hung the publish workflow for >3 hours in 2026-05. The cosmetic variants render
as literal `[[NFIB]]` text in the output HTML.

Patterns repaired (most-specific first):

  1. [[../path.md|[NAME](url)]]        ->  [NAME](url)
  2. [[[NAME](url1)|[NAME2](url2)]]    ->  [NAME2](url2)   (rare nested-link alias)
  3. [[[NAME](url)|alias]]              ->  [alias](url)
  4. [[[NAME](url)]]                    ->  [NAME](url)
  5. [[NAME](url)]                      ->  [NAME](url)
  6. [[NAME](url)   (no trailing ])     ->  [NAME](url)
  7. [[section/NAME]]                   ->  [NAME](../section/NAME.md)   (if file exists)
  8. [[NAME]]                           ->  [NAME](../<kind>/NAME.md)    (if file exists in any kind)

Patterns 1-6 are build-breaking (catastrophic-backtracking risk). Patterns 7-8
are cosmetic-only — bare wiki-links render as literal text.

Skips: `wiki/_site/`, `wiki/.quarto/`, `wiki/site_libs/`, vendored JS, and
qmd files that embed third-party JSON (Plotly hovertext etc.).
"""
from __future__ import annotations

import re
from pathlib import Path

KINDS = ("genes", "cancer_types", "datasets", "drugs", "methods")
EXCLUDE_DIR_PARTS = {"_site", ".quarto", "site_libs"}
EXCLUDE_NAME_GLOBS = ("vendor-*.js",)
EXCLUDE_FILES = {"experiments/rag-vs-agentic.qmd"}

_DANGEROUS_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    # 1. pipe-alias with target on LEFT, markdown link on RIGHT
    (re.compile(r"\[\[\.\.\/[^|\]]+\|(\[[^\]]+\]\([^)]+\))\]\]"), r"\1"),
    # 2. triple-bracket open with NESTED MARKDOWN LINK as alias
    (
        re.compile(r"\[\[\[[^\]]+\]\([^)]+\)\|(\[[^\]]+\]\([^)]+\))\]\]"),
        r"\1",
    ),
    # 3. triple-bracket open with plain alias on RIGHT of pipe
    (
        re.compile(r"\[\[\[([^\]]+)\]\(([^)]+)\)\|([^\]]+)\]\]"),
        r"[\3](\2)",
    ),
    # 4. triple-bracket open + double-bracket close
    (re.compile(r"\[\[\[([^\]]+)\]\(([^)]+)\)\]\]"), r"[\1](\2)"),
    # 5. double-bracket open + single-bracket close
    (re.compile(r"\[\[([^\]]+)\]\(([^)]+)\)\]"), r"[\1](\2)"),
    # 6. double-bracket open + NO close (only after rules 1-5 have run)
    (
        re.compile(r"\[\[([A-Za-z][^\]]*)\]\(([^)]+)\)"),
        r"[\1](\2)",
    ),
]


def _existing_pages_per_kind(wiki: Path) -> dict[str, set[str]]:
    return {k: {p.stem for p in (wiki / k).glob("*.md")} for k in KINDS}


def _normalize_dangerous(text: str) -> tuple[str, int]:
    total = 0
    for pat, repl in _DANGEROUS_PATTERNS:
        text, n = pat.subn(repl, text)
        total += n
    return text, total


def _normalize_bare(text: str, pages: dict[str, set[str]]) -> tuple[str, int]:
    n = 0

    def with_section(m: re.Match) -> str:
        nonlocal n
        section, name = m.group(1), m.group(2)
        if section in KINDS and name in pages[section]:
            n += 1
            return f"[{name}](../{section}/{name}.md)"
        return m.group(0)

    text = re.sub(
        r"\[\[(genes|cancer_types|datasets|drugs|methods)/([A-Za-z0-9._-]+)\]\]",
        with_section,
        text,
    )

    def bare(m: re.Match) -> str:
        nonlocal n
        name = m.group(1)
        for kind in KINDS:
            if name in pages[kind]:
                n += 1
                return f"[{name}](../{kind}/{name}.md)"
        return m.group(0)

    text = re.sub(r"\[\[([A-Za-z][A-Za-z0-9_-]*)\]\]", bare, text)
    return text, n


def normalize_text(text: str, pages: dict[str, set[str]]) -> tuple[str, dict[str, int]]:
    text, n_dangerous = _normalize_dangerous(text)
    text, n_bare = _normalize_bare(text, pages)
    return text, {"dangerous": n_dangerous, "bare": n_bare}


def _is_excluded(rel: str, parts: tuple[str, ...]) -> bool:
    if any(part in EXCLUDE_DIR_PARTS for part in parts):
        return True
    if rel in EXCLUDE_FILES:
        return True
    name = parts[-1] if parts else ""
    return any(Path(name).match(g) for g in EXCLUDE_NAME_GLOBS)


def _iter_targets(wiki: Path, paths: list[Path] | None):
    if paths:
        for p in paths:
            if p.suffix in {".md", ".qmd"} and p.exists():
                yield p
        return
    for p in wiki.rglob("*.md"):
        rel = p.relative_to(wiki).as_posix()
        if _is_excluded(rel, p.relative_to(wiki).parts):
            continue
        yield p


def run(
    wiki_dir: Path,
    paths: list[Path] | None = None,
    *,
    dry_run: bool = False,
) -> int:
    wiki_dir = wiki_dir.resolve()
    pages = _existing_pages_per_kind(wiki_dir)
    grand_dangerous = 0
    grand_bare = 0
    changed_files = 0

    for p in _iter_targets(wiki_dir, paths):
        orig = p.read_text(encoding="utf-8")
        new, counts = normalize_text(orig, pages)
        if new == orig:
            continue
        changed_files += 1
        grand_dangerous += counts["dangerous"]
        grand_bare += counts["bare"]
        try:
            rel = p.relative_to(wiki_dir.parent).as_posix()
        except ValueError:
            rel = str(p)
        action = "would normalize" if dry_run else "normalized"
        print(
            f"  {action} {rel}  dangerous={counts['dangerous']}  bare={counts['bare']}"
        )
        if not dry_run:
            p.write_text(new, encoding="utf-8")

    suffix = " (dry run)" if dry_run else ""
    print(
        f"[normalize-brackets] {changed_files} file(s) changed; "
        f"{grand_dangerous} build-breaker(s), {grand_bare} cosmetic bare link(s){suffix}"
    )
    return 0
