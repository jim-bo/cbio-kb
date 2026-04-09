"""Canonical ontology lookup and search logic.
Provides token-efficient validation for Hugo symbols, OncoTree codes, and Study IDs.
"""
from __future__ import annotations

import json
from pathlib import Path

# Mapping of file names to the key that should be searched for canonical IDs.
ON_DISK_SOURCES = [
    ("genes.json", "hugoGeneSymbol", "genes"),
    ("studies.json", "studyId", "datasets"),
    ("gene_panels.json", "genePanelId", "gene_panels"),
    ("cancer_types.json", "cancerTypeId", "cancer_types"),
    ("oncotree.json", "code", "cancer_types"),
]

def load_canonical(ontology_dir: Path) -> dict[str, set[str]]:
    """Loads all canonical ID sets from schema/ontology/*.json."""
    canonical: dict[str, set[str]] = {
        "genes": set(),
        "cancer_types": set(),
        "datasets": set(),
        "gene_panels": set(),
    }
    
    for fname, key, dest in ON_DISK_SOURCES:
        path = ontology_dir / fname
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text())
            # Handle both flat lists and OncoTree's nested children structure
            if fname == "oncotree.json":
                stack = list(data)
                while stack:
                    node = stack.pop()
                    if isinstance(node, dict):
                        code = node.get("code")
                        if code:
                            canonical[dest].add(code)
                        children = node.get("children") or {}
                        if isinstance(children, dict):
                            stack.extend(children.values())
                        elif isinstance(children, list):
                            stack.extend(children)
            else:
                for row in data:
                    v = row.get(key) if isinstance(row, dict) else None
                    if v:
                        canonical[dest].add(v)
        except (json.JSONDecodeError, Exception):
            continue
            
    return canonical

def search(ontology_dir: Path, query: str) -> dict:
    """Search for a query across all canonical ID sets and return matches."""
    canon = load_canonical(ontology_dir)
    results = {}
    query_upper = query.upper()
    
    for kind, ids in canon.items():
        if query in ids or query_upper in ids:
            results[kind] = {
                "found": True,
                "canonical_id": query if query in ids else query_upper,
                "kind": kind
            }
            
    if not results:
        # Fuzzy match (substring) if exact match fails
        for kind, ids in canon.items():
            matches = [id for id in ids if query_upper in id.upper()]
            if matches:
                results[kind] = {
                    "found": False,
                    "suggestions": sorted(matches)[:5],
                    "kind": kind
                }
                
    return results

def run_lookup(ontology_dir: Path, query: str) -> int:
    """CLI entry point for ontology lookup."""
    results = search(ontology_dir, query)
    print(json.dumps(results, indent=2))
    return 0 if any(v.get("found") for v in results.values()) else 1
