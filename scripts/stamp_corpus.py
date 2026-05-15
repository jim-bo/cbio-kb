"""Stamp every wiki/papers/*.md with a `corpus:` frontmatter tag.

Classifier rules (in order):
  - any referenced study_id / dataset contains "robin"          → `robin`
  - any referenced study_id / dataset matches imaging patterns  → `imaging`
    (prefix `tcia-`, contains `radcure`, contains `radiogenomics`,
     contains `gpcchn`)
  - otherwise                                                   → `cbioportal`

Edits frontmatter in place using line-level surgery — does not round-trip
the YAML, so existing field ordering and quoting are preserved. Idempotent:
re-runs only rewrite a file when the computed value differs from the
existing `corpus:` line.

Usage:
    uv run python scripts/stamp_corpus.py             # write
    uv run python scripts/stamp_corpus.py --dry-run   # report only
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_PAPERS = REPO_ROOT / "wiki" / "papers"


def classify(study_id: str | None, datasets: list[str] | None) -> str:
    refs = [study_id] + list(datasets or [])
    refs = [r for r in refs if isinstance(r, str) and r]
    blob = " ".join(refs).lower()
    if "robin" in blob:
        return "robin"
    imaging_markers = ("tcia-", "radcure", "radiogenomics", "gpcchn")
    if any(m in blob for m in imaging_markers):
        return "imaging"
    return "cbioportal"


def _split_frontmatter(text: str) -> tuple[str, str, str] | None:
    """Return (head, body, tail) where head is the YAML block including the
    trailing newline and tail is the rest of the file. None if no frontmatter."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[4:end], text[: end + 5], text[end + 5 :]


def stamp_file(path: Path, *, dry_run: bool) -> tuple[str, str | None]:
    """Returns (action, corpus_value).

    action ∈ {"skip", "set", "update", "noop"}.
    """
    text = path.read_text()
    parts = _split_frontmatter(text)
    if parts is None:
        return ("skip", None)
    fm_yaml, fm_block, body = parts
    try:
        fm = yaml.safe_load(fm_yaml) or {}
    except yaml.YAMLError:
        return ("skip", None)

    corpus = classify(fm.get("study_id"), fm.get("datasets"))
    existing = fm.get("corpus")

    if existing == corpus:
        return ("noop", corpus)

    # Find an existing `corpus:` line and replace it. Otherwise insert after
    # the line starting with `study_id:`. Otherwise insert after `pmid:`.
    fm_lines = fm_block.splitlines(keepends=True)
    corpus_line = f"corpus: {corpus}\n"
    action: str
    new_lines: list[str] = []
    replaced = False
    for line in fm_lines:
        if re.match(r"^corpus:\s*", line):
            new_lines.append(corpus_line)
            replaced = True
        else:
            new_lines.append(line)
    if replaced:
        action = "update"
    else:
        # Insert after study_id: (or pmid:) line.
        inserted = False
        out: list[str] = []
        for line in new_lines:
            out.append(line)
            if not inserted and re.match(r"^study_id:\s*", line):
                out.append(corpus_line)
                inserted = True
        if not inserted:
            out = []
            for line in new_lines:
                out.append(line)
                if not inserted and re.match(r"^pmid:\s*", line):
                    out.append(corpus_line)
                    inserted = True
        if not inserted:
            # Worst case: prepend after opening `---\n`.
            out = new_lines[:1] + [corpus_line] + new_lines[1:]
        new_lines = out
        action = "set"

    if not dry_run:
        path.write_text("".join(new_lines) + body)
    return (action, corpus)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = sorted(WIKI_PAPERS.glob("*.md"))
    counts = {"skip": 0, "noop": 0, "set": 0, "update": 0}
    by_corpus: dict[str, int] = {}
    changes: list[tuple[Path, str, str]] = []
    for p in files:
        action, value = stamp_file(p, dry_run=args.dry_run)
        counts[action] += 1
        if value is not None:
            by_corpus[value] = by_corpus.get(value, 0) + 1
        if action in ("set", "update") and value is not None:
            changes.append((p, action, value))

    print(f"papers: {len(files)}")
    print(f"  skip (no/invalid frontmatter): {counts['skip']}")
    print(f"  noop (already correct):        {counts['noop']}")
    print(f"  set (no prior corpus field):   {counts['set']}")
    print(f"  update (value changed):        {counts['update']}")
    if changes:
        print("\nchanges:")
        for path, action, value in changes:
            print(f"  [{action:6s}] {path.stem} → corpus: {value}")
    if by_corpus:
        print("\ncorpus distribution:")
        for v, n in sorted(by_corpus.items(), key=lambda kv: -kv[1]):
            print(f"  {v:12s} {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
