"""Ripgrep-backed FTS over wiki/. Falls back to a Python scan if rg is missing."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def run(wiki_dir: Path, query: str) -> int:
    if not wiki_dir.exists():
        print(f"[!] wiki dir not found: {wiki_dir}")
        return 1
    rg = shutil.which("rg")
    if rg:
        return subprocess.call([rg, "-n", "--heading", "--color", "never", query, str(wiki_dir)])

    needle = query.lower()
    hits = 0
    for path in sorted(wiki_dir.rglob("*.md")):
        for i, line in enumerate(path.read_text().splitlines(), 1):
            if needle in line.lower():
                print(f"{path.relative_to(wiki_dir)}:{i}: {line.strip()}")
                hits += 1
    return 0 if hits else 1
