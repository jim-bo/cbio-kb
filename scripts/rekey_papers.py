"""Re-key wiki paper pages that were filed under the wrong PMID.

Background (see notes/REKEY_2026-09.md): before commit 2ac63992 the
PMID->PMCID elink fallback could return the PMC record of a paper *citing*
the requested PMID. 35 such citing papers were downloaded, extracted, and
compiled under the cited paper's PMID. This script moves each one to its
true PMID and drops the cBioPortal study link it inherited from the wrong
PMID, while keeping every dataset link the paper's own text supports.

Driven by ``notes/rekey_2026-09-10.csv``
(old_pmid,new_pmid,pmcid,doi,...,datasets_dropped,datasets_kept).

For each row:
  1. ``git mv`` wiki/papers/{old}.md (+ .claims.json) -> {new}.
  2. Paper frontmatter: pmid -> new, study_id cleared, doi filled if empty,
     ``datasets_dropped`` removed from ``datasets:``. Body links to dropped
     dataset pages are unlinked; the compiler's "PMID mismatch" caveat
     bullets are removed (the mismatch is what this fixes).
  3. Every wiki page: ``papers/{old}.md|html`` and ``PMID:{old}`` citations
     -> new (word-boundary replace; audited to have no other contexts).
  4. Dataset pages for dropped links: lines citing the paper are removed;
     a page left with no paper citations is deleted and inbound links to it
     are unlinked (or, for list lines that only described the false link,
     removed).
  5. Eval corpus lists / gold PMIDs, ontology _observed.md, and the index
     template's News section: old -> new.
  6. Local (gitignored) artifacts: data/raw/papers/{old}.md, fetch_log.json,
     data/paper_index/meta.jsonl.

Usage:
    uv run python scripts/rekey_papers.py --dry-run
    uv run python scripts/rekey_papers.py
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI = REPO_ROOT / "wiki"
MAPPING = REPO_ROOT / "notes" / "rekey_2026-09-10.csv"

# Tracked non-wiki text files whose PMID references follow the paper page.
# Deliberately excluded: data/seed/*.csv and schema/ontology/studies.json
# (they hold cBioPortal's own study->PMID facts, which were never wrong),
# eval/corpus_pmids_v1_56.txt and eval/results|verify (historical records).
FOLLOW_FILES = [
    "eval/corpus_pmids.txt",
    "eval/all_pmids.txt",
    "eval/questions/v1.yaml",
    "eval/list_gold_proposals_377.md",
    "schema/ontology/_observed.md",
    "schema/templates/index.md",
]

# Caveat bullets paper-compiler wrote when it noticed the ID/text mismatch.
_MISMATCH_BULLET = re.compile(
    r"^- \*\*(Raw-file metadata mismatch|PMID / publication-year mismatch|"
    r"Frontmatter mismatch in source record|Frontmatter-vs-text dataset mismatch)"
    r"[^\n]*\n",
    re.M,
)


def _git(*args: str, dry: bool) -> None:
    if dry:
        print("  $ git", " ".join(args))
        return
    subprocess.run(["git", *args], cwd=REPO_ROOT, check=True)


def _wiki_pages() -> list[Path]:
    out = []
    for p in sorted(WIKI.rglob("*.md")):
        rel = p.relative_to(WIKI)
        if rel.parts[0].startswith(("_", ".")) or rel.name == "index.md" and len(rel.parts) == 1:
            continue
        out.append(p)
    return out


def _sub_pmid(text: str, old: str, new: str) -> str:
    return re.sub(rf"(?<![\d]){old}(?![\d])", new, text)


def _unlink(text: str, target: str) -> str:
    """Turn ``[label](../datasets/x.md)`` links to *target* into plain labels."""
    return re.sub(rf"\[([^\]]+)\]\((?:\.\./)?{re.escape(target)}\)", r"\1", text)


def _drop_from_fm_list(text: str, key: str, drop: set[str]) -> str:
    """Remove *drop* items from a block-style YAML list in the frontmatter."""
    head, sep, body = text.partition("\n---\n")
    lines = head.split("\n")
    out, in_key, kept = [], False, 0
    for line in lines:
        if re.match(rf"^{key}:\s*$", line):
            in_key, kept = True, 0
            out.append(line)
            continue
        if in_key:
            m = re.match(r"^\s+-\s+\"?([^\"]+?)\"?\s*$", line)
            if m:
                if m.group(1) not in drop:
                    out.append(line)
                    kept += 1
                continue
            in_key = False
            if kept == 0:
                out[-1] = f"{key}: []"
        out.append(line)
    return "\n".join(out) + sep + body


def _set_fm(text: str, key: str, value: str) -> str:
    return re.sub(rf"^{key}:.*$", f"{key}:{(' ' + value) if value else ''}", text, count=1, flags=re.M)


def rekey(rows: list[dict], dry: bool) -> int:
    pages = _wiki_pages()
    changed: set[Path] = set()
    deleted: list[str] = []

    # 1-2. Move + rewrite each paper page.
    for r in rows:
        old, new = r["old_pmid"], r["new_pmid"]
        src, dst = WIKI / "papers" / f"{old}.md", WIKI / "papers" / f"{new}.md"
        if not src.exists():
            if dst.exists():
                print(f"[skip] {old} already re-keyed -> {new}")
                continue
            print(f"[!] missing {src}")
            return 1
        print(f"[paper] {old} -> {new}")
        _git("mv", str(src.relative_to(REPO_ROOT)), str(dst.relative_to(REPO_ROOT)), dry=dry)
        claims = WIKI / "papers" / f"{old}.claims.json"
        drop = set(filter(None, r["datasets_dropped"].split(";")))
        if claims.exists():
            _git("mv", str(claims.relative_to(REPO_ROOT)),
                 str(claims.with_name(f"{new}.claims.json").relative_to(REPO_ROOT)), dry=dry)
            if not dry:
                items = json.loads(claims.with_name(f"{new}.claims.json").read_text())
                items = [c for c in items if c.get("study") not in drop]
                claims.with_name(f"{new}.claims.json").write_text(json.dumps(items, indent=2) + "\n")
        path = src if dry else dst
        text = path.read_text(encoding="utf-8")
        text = _set_fm(text, "pmid", new)
        text = _set_fm(text, "study_id", "")
        if not re.search(r"^doi:\s*\S", text, re.M) and r["doi"]:
            text = _set_fm(text, "doi", r["doi"])
        if drop:
            text = _drop_from_fm_list(text, "datasets", drop)
            for s in drop:
                text = _unlink(text, f"datasets/{s}.md")
        text = _MISMATCH_BULLET.sub("", text)
        if not dry:
            dst.write_text(text, encoding="utf-8")

    # 3. Citation rewrite across the vault (the moved pages included).
    pages = _wiki_pages()
    for p in pages:
        if dry and p.name.removesuffix(".md") in {r["new_pmid"] for r in rows}:
            continue
        text = orig = p.read_text(encoding="utf-8")
        for r in rows:
            if r["old_pmid"] in text:
                text = _sub_pmid(text, r["old_pmid"], r["new_pmid"])
        if text != orig:
            changed.add(p)
            if not dry:
                p.write_text(text, encoding="utf-8")

    # 4. Dataset pages whose link to a re-keyed paper was false.
    for r in rows:
        new = r["new_pmid"]
        for sid in filter(None, r["datasets_dropped"].split(";")):
            dpage = WIKI / "datasets" / f"{sid}.md"
            if not dpage.exists():
                continue
            text = dpage.read_text(encoding="utf-8")
            if dry:
                text = _sub_pmid(text, r["old_pmid"], new)
            stripped = "".join(
                ln for ln in text.splitlines(keepends=True)
                if not re.search(rf"papers/{new}\.(md|html)", ln)
            )
            others = set(re.findall(r"papers/(\d+)\.(?:md|html)", stripped))
            if others:
                print(f"[dataset] strip {new} from datasets/{sid}.md (still cited by {sorted(others)})")
                if not dry:
                    dpage.write_text(stripped, encoding="utf-8")
                changed.add(dpage)
            else:
                print(f"[dataset] delete datasets/{sid}.md (only supported by the false link)")
                _git("rm", "-q", "-f", str(dpage.relative_to(REPO_ROOT)), dry=dry)
                deleted.append(sid)

    # Inbound links to deleted dataset pages: list lines that describe the
    # deleted dataset (link at the start of a bullet) go; other mentions keep
    # their label as plain text.
    for sid in deleted:
        target = f"datasets/{sid}.md"
        for p in _wiki_pages():
            if not p.exists():
                continue
            text = orig = p.read_text(encoding="utf-8")
            if target not in text:
                continue
            text = re.sub(rf"^- \[[^\]]+\]\((?:\.\./)?{re.escape(target)}\)[^\n]*\n", "", text, flags=re.M)
            text = _unlink(text, target)
            if text != orig:
                print(f"[unlink] {p.relative_to(WIKI)} -> {target}")
                changed.add(p)
                if not dry:
                    p.write_text(text, encoding="utf-8")

    # 5. Tracked non-wiki followers.
    for rel in FOLLOW_FILES:
        f = REPO_ROOT / rel
        text = orig = f.read_text(encoding="utf-8")
        for r in rows:
            text = _sub_pmid(text, r["old_pmid"], r["new_pmid"])
        if rel.endswith("pmids.txt"):
            ids = sorted({ln.strip() for ln in text.splitlines() if ln.strip()}, key=int)
            text = "\n".join(ids) + "\n"
        if text != orig:
            print(f"[follow] {rel}")
            if not dry:
                f.write_text(text, encoding="utf-8")

    # 6. Local artifacts (gitignored).
    raw = REPO_ROOT / "data" / "raw" / "papers"
    for r in rows:
        old, new = r["old_pmid"], r["new_pmid"]
        src, dst = raw / f"{old}.md", raw / f"{new}.md"
        if src.exists() and not dry:
            text = src.read_text(encoding="utf-8")
            text = _set_fm(_set_fm(text, "pmid", new), "study_id", "")
            dst.write_text(text, encoding="utf-8")
            src.unlink()
    fetch_log = REPO_ROOT / "data" / "raw" / "fetch_log.json"
    if fetch_log.exists() and not dry:
        log = json.loads(fetch_log.read_text())
        for r in rows:
            if r["old_pmid"] in log:
                log[r["new_pmid"]] = log.pop(r["old_pmid"])
        fetch_log.write_text(json.dumps(log, indent=2, sort_keys=True))
    meta = REPO_ROOT / "data" / "paper_index" / "meta.jsonl"
    if meta.exists() and not dry:
        remap = {r["old_pmid"]: r["new_pmid"] for r in rows}
        out = []
        for line in meta.read_text().splitlines():
            rec = json.loads(line)
            rec["pmid"] = remap.get(str(rec.get("pmid")), rec.get("pmid"))
            out.append(json.dumps(rec, ensure_ascii=False))
        meta.write_text("\n".join(out) + "\n")

    print(f"\n[done] {len(rows)} papers re-keyed, {len(changed)} pages rewritten, "
          f"{len(deleted)} dataset pages deleted{' (dry run)' if dry else ''}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mapping", type=Path, default=MAPPING)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    rows = list(csv.DictReader(args.mapping.open(encoding="utf-8")))
    return rekey(rows, dry=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
