"""Run a question through the RAG mode."""
from __future__ import annotations

from .base import run_question


def run(question: str, **kwargs) -> dict:
    return run_question(question, mode="rag", **kwargs)
