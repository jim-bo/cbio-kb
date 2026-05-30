"""Run a question through the hybrid (dense + BM25 + graph) mode."""
from __future__ import annotations

from .base import run_question


def run(question: str, **kwargs) -> dict:
    return run_question(question, mode="hybrid", **kwargs)
