"""Collapse stranded provenance footers to one trailing footer per wiki page.

Until the fix in cbio_kb.wiki.append_citation, every `wiki append-citation`
call on a page whose last section is `## Sources` inserted the new source
after the existing footer and then appended a fresh footer, so heavily
cited pages accumulated dozens of `*This page was processed by …*` lines
interleaved with their Sources list (171 on methods/whole-exome-seq.md).

For each page with more than one footer, or a footer that isn't the last
line, this keeps the footer with the latest date (last one on ties), drops
the rest together with the blank spacer line before each, and writes the
kept footer back at the end. Nothing else on the page changes.

Usage:
    uv run python scripts/normalize_footers.py --dry-run
    uv run python scripts/normalize_footers.py
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI = REPO_ROOT / "wiki"
FOOTER = re.compile(r"^\*This page was processed by \*\*([^*]+)\*\* on \*\*([^*]+)\*\*\.\*\s*$")


def normalize(text: str) -> str:
    lines = text.splitlines()
    feet = [(i, m) for i, line in enumerate(lines) if (m := FOOTER.match(line))]
    if not feet:
        return text
    last_content = max((i for i, line in enumerate(lines) if line.strip()), default=-1)
    if len(feet) == 1 and feet[0][0] == last_content:
        return text
    keep = max(feet, key=lambda f: (f[1].group(2), f[0]))
    drop = {i for i, _ in feet}
    drop |= {i - 1 for i, _ in feet if i > 0 and not lines[i - 1].strip()}
    body = [line for i, line in enumerate(lines) if i not in drop]
    while body and not body[-1].strip():
        body.pop()
    return "\n".join(body + ["", lines[keep[0]].rstrip()]) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    changed = removed = 0
    for page in sorted(WIKI.rglob("*.md")):
        if page.relative_to(WIKI).parts[0].startswith(("_", ".")):
            continue
        text = page.read_text(encoding="utf-8")
        new = normalize(text)
        if new != text:
            changed += 1
            removed += sum(1 for ln in text.splitlines() if FOOTER.match(ln)) - 1
            if not args.dry_run:
                page.write_text(new, encoding="utf-8")
    verb = "would change" if args.dry_run else "changed"
    print(f"[normalize-footers] {changed} page(s) {verb}; {removed} stranded footer(s) removed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
