"""Query router for the auto retrieval mode.

Picks one of the three retrieval strategies (``hybrid`` / ``rag`` /
``agentic``) for a free-form question. The routing *policy* is derived from
the full-corpus eval (``eval/results/2026-06-07-*``): on a shared 377-paper
corpus,

- **lookup** and **definition** questions are answered at near-parity
  accuracy/citation by the cheap **hybrid** leg at a fraction of the tokens —
  so route them there.
- **list** and **synthesis** questions need whole-page reading / enumeration,
  where only the **agentic** graph-walk pays off (hybrid's completeness and
  recall collapse) — so route them there.

``rag`` is the middle ground; the policy keeps it as the configurable fallback
mode rather than a default destination.

Two classifiers produce the *category* that the policy maps to a mode:

1. **kNN** (primary) — embed the query with the same Vertex
   ``gemini-embedding-001`` model the dense index uses, then majority-vote the
   *k* nearest labeled questions in ``eval/questions/v1.yaml``. This grounds
   routing in the same labeled data the eval scored, and the bank embeddings
   are cached to disk so the cost is paid once.
2. **heuristic** (fallback) — a lexical cue scorer used when embeddings are
   unavailable (no ``GCP_PROJECT``, offline, or the bank fails to load).

Set ``CBIO_ROUTER_STRATEGY=heuristic`` to skip embeddings entirely.
"""
from __future__ import annotations

import hashlib
import os
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

import numpy as np

# --------------------------------------------------------------------------
# Policy: eval-derived category -> retrieval mode
# --------------------------------------------------------------------------

#: Maps a question category to the retrieval mode the eval found best on the
#: cost/quality frontier. See module docstring for the justification.
MODE_BY_CATEGORY: dict[str, str] = {
    "lookup": "hybrid",
    "definition": "hybrid",
    "list": "agentic",
    "synthesis": "agentic",
}

#: Mode used when no category can be determined at all.
_DEFAULT_MODE = "hybrid"
_DEFAULT_CATEGORY = "lookup"

_REPO_ROOT = Path(__file__).resolve().parent.parent
_QUESTIONS_PATH = Path(
    os.environ.get("CBIO_ROUTER_QUESTIONS", _REPO_ROOT / "eval" / "questions" / "v1.yaml")
)
_CACHE_PATH = Path(
    os.environ.get("CBIO_ROUTER_CACHE", _REPO_ROOT / "data" / "router_qbank.npz")
)
_DEFAULT_K = int(os.environ.get("CBIO_ROUTER_KNN_K", "7"))
_STRATEGY = os.environ.get("CBIO_ROUTER_STRATEGY", "knn").lower()


@dataclass
class RouteDecision:
    """The router's choice plus enough provenance to explain it."""

    mode: str                       # hybrid | rag | agentic
    category: str                   # lookup | list | synthesis | definition
    method: str                     # knn | heuristic
    confidence: float               # 0..1
    rationale: str
    neighbors: list[dict] = field(default_factory=list)  # knn: nearest labeled Qs
    cues: list[str] = field(default_factory=list)         # heuristic: matched keywords

    def to_dict(self) -> dict:
        return asdict(self)


# --------------------------------------------------------------------------
# Heuristic classifier (fallback — no network)
# --------------------------------------------------------------------------

# Cue patterns per category. Synthesis and list cues are intentionally strong
# (they describe *intent*), so a question like "compare X and Y across studies"
# scores synthesis over the weaker definitional "what is".
_CUES: dict[str, list[str]] = {
    "list": [
        r"\blist\b",
        r"\benumerate\b",
        r"\bwhich (?:papers|studies|datasets|cohorts|genes|drugs|trials)\b",
        r"\bwhat (?:papers|studies|datasets|cohorts)\b",
        r"\ball (?:of )?the (?:papers|studies|datasets|genes)\b",
        r"\bname (?:all|the|every)\b",
        r"\bevery (?:paper|study|dataset)\b",
    ],
    "synthesis": [
        r"\bcompare\b",
        r"\bcontrast\b",
        r"\bcontradic",
        r"\bconsensus\b",
        r"\bacross (?:papers|studies|cohorts|the corpus|datasets)\b",
        r"\brelationship between\b",
        r"\bhow do(?:es)?\b.*\bdiffer\b",
        r"\btrend\b",
        r"\bversus\b",
        r"\bvs\.?\b",
        r"\bwhy (?:do|does|is|are)\b",
        r"\bimplication",
    ],
    "definition": [
        r"\bwhat is\b",
        r"\bwhat are\b",
        r"\bdefine\b",
        r"\bdefinition of\b",
        r"\bexplain\b",
        r"\bdescribe (?:the|how)\b",
        r"\bwhat does\b.*\b(?:stand for|mean|measure)\b",
        r"\bpurpose of\b",
        r"\bhow does\b.*\bwork\b",
    ],
    "lookup": [
        r"\bwhat percentage\b",
        r"\bhow many\b",
        r"\bwhat was the\b",
        r"\bwhat fraction\b",
        r"\bin the\b.*\bstudy\b",
        r"\bhow frequent",
        r"\breported\b",
    ],
}

# Tie-break order when scores are equal: prefer the more specific intent.
_PRECEDENCE = ["list", "synthesis", "definition", "lookup"]


def classify_heuristic(query: str) -> tuple[str, list[str]]:
    """Return ``(category, matched_cues)`` from lexical cues alone."""
    q = query.lower()
    scores: dict[str, int] = {c: 0 for c in _CUES}
    matched: dict[str, list[str]] = {c: [] for c in _CUES}
    for category, patterns in _CUES.items():
        for pat in patterns:
            m = re.search(pat, q)
            if m:
                scores[category] += 1
                matched[category].append(m.group(0).strip())
    best_score = max(scores.values())
    if best_score == 0:
        return _DEFAULT_CATEGORY, []
    # Among categories tied for the top score, take the highest precedence.
    top = [c for c in _PRECEDENCE if scores[c] == best_score]
    best = top[0]
    return best, matched[best]


# --------------------------------------------------------------------------
# kNN classifier (primary — embedding-backed)
# --------------------------------------------------------------------------


def _load_questions() -> list[dict]:
    """Read ``(question, category, id)`` triples from the eval YAML."""
    import yaml

    data = yaml.safe_load(_QUESTIONS_PATH.read_text())
    out: list[dict] = []
    for q in data.get("questions", []):
        text = " ".join(str(q.get("question", "")).split())
        cat = q.get("category")
        if text and cat in MODE_BY_CATEGORY:
            out.append({"id": q.get("id"), "question": text, "category": cat})
    return out


def _fingerprint(questions: list[dict]) -> str:
    h = hashlib.sha1()
    for q in questions:
        h.update(q["id"].encode())
        h.update(b"\x00")
        h.update(q["question"].encode())
        h.update(b"\x00")
    return h.hexdigest()


class QuestionBank:
    """Lazy singleton holding labeled-question embeddings for kNN routing.

    Embeddings are cached to ``data/router_qbank.npz`` keyed by a fingerprint
    of the question set, so the Vertex call happens only when the eval set
    changes.
    """

    _instance: "QuestionBank | None" = None

    def __init__(self) -> None:
        self.questions = _load_questions()
        if not self.questions:
            raise RuntimeError(f"No labeled questions found in {_QUESTIONS_PATH}")
        self.fingerprint = _fingerprint(self.questions)
        self.categories = np.array([q["category"] for q in self.questions])
        self.ids = [q["id"] for q in self.questions]
        self.embeddings = self._load_or_build_embeddings()

    def _load_or_build_embeddings(self) -> np.ndarray:
        if _CACHE_PATH.exists():
            try:
                cached = np.load(_CACHE_PATH, allow_pickle=False)
                if str(cached["fingerprint"]) == self.fingerprint:
                    return cached["embeddings"].astype("float32")
            except Exception:
                pass  # corrupt / stale cache — rebuild
        from cbio_kb.index.papers import embed_texts

        texts = [q["question"] for q in self.questions]
        embeddings = embed_texts(texts, task_type="RETRIEVAL_QUERY").astype("float32")
        try:
            _CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
            np.savez(
                _CACHE_PATH,
                embeddings=embeddings,
                fingerprint=np.array(self.fingerprint),
            )
        except Exception:
            pass  # caching is best-effort
        return embeddings

    @classmethod
    def get(cls) -> "QuestionBank":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def classify(self, query: str, k: int = _DEFAULT_K) -> tuple[dict[str, float], list[dict]]:
        """Similarity-weighted vote over the ``k`` nearest labeled questions.

        Returns ``(weighted, neighbors)`` — ``weighted`` maps each category to
        its summed (clamped) cosine similarity, ``neighbors`` is the ranked
        nearest-question list for provenance. The winner / confidence are left
        to the caller so the policy layer can blend in lexical cues.
        """
        from cbio_kb.index.papers import embed_texts

        qvec = embed_texts([query], task_type="RETRIEVAL_QUERY").astype("float32")[0]
        # Embeddings are L2-normalized, so dot product == cosine similarity.
        sims = self.embeddings @ qvec
        k = min(k, len(sims))
        top_idx = np.argpartition(-sims, k - 1)[:k]
        top_idx = top_idx[np.argsort(-sims[top_idx])]

        weighted: dict[str, float] = {}
        neighbors: list[dict] = []
        for i in top_idx:
            cat = str(self.categories[i])
            sim = float(sims[i])
            # Clamp negatives so an off-topic neighbor cannot subtract votes.
            weighted[cat] = weighted.get(cat, 0.0) + max(sim, 0.0)
            neighbors.append({"id": self.ids[i], "category": cat, "score": round(sim, 4)})
        return weighted, neighbors


# --------------------------------------------------------------------------
# Public entry point
# --------------------------------------------------------------------------


#: kNN confidence below which a clear lexical cue for a complex category is
#: allowed to override the embedding vote. Tuned so confident kNN wins but
#: borderline votes defer to an explicit "compare/list/across" signal.
_KNN_OVERRIDE_BELOW = 0.55

#: Categories whose *misrouting is expensive* — the eval showed list/synthesis
#: sent to hybrid collapse on completeness/recall, while an easy question sent
#: to agentic only wastes tokens. So a cue for these can override unsure kNN.
_COMPLEX_CATEGORIES = {"list", "synthesis"}


def _blend(weighted: dict[str, float], cue_cat: str, cues: list[str]) -> tuple[str, float, str]:
    """Combine the kNN vote with the lexical cue into a final category.

    Returns ``(category, confidence, note)``. The asymmetric override only ever
    *upgrades* an unsure kNN call to a complex (agentic-routed) category when
    the cues clearly say so — it never downgrades a confident vote.
    """
    total = sum(weighted.values()) or 1.0
    knn_cat = max(weighted, key=weighted.__getitem__)
    knn_conf = weighted[knn_cat] / total

    if (
        cues
        and cue_cat in _COMPLEX_CATEGORIES
        and cue_cat != knn_cat
        and knn_conf < _KNN_OVERRIDE_BELOW
    ):
        note = (
            f"kNN leaned '{knn_cat}' (conf {knn_conf:.2f}) but lexical cues "
            f"{cues} signal '{cue_cat}'; deferred to the cue to avoid cheaply "
            "misrouting a complex question"
        )
        return cue_cat, round(knn_conf, 4), note
    return knn_cat, round(knn_conf, 4), ""


def _rationale(category: str, mode: str, method: str) -> str:
    why = {
        "hybrid": (
            "hybrid reaches near-parity accuracy/citation on factual and "
            "definitional questions at ~1/3 the tokens of RAG and far less than agentic"
        ),
        "agentic": (
            "enumeration/synthesis needs whole-page reading where the agentic "
            "graph-walk is the only mode that holds completeness and recall"
        ),
        "rag": "dense single-shot retrieval as the configured middle-ground fallback",
    }[mode]
    return f"classified as '{category}' via {method}; {why}"


def route(query: str, *, strategy: str | None = None, k: int = _DEFAULT_K) -> RouteDecision:
    """Choose a retrieval mode for ``query``.

    ``strategy`` is ``"knn"`` (default), ``"heuristic"``, or ``"auto"`` (try
    kNN, fall back to heuristic on any failure). Falls back to the heuristic
    automatically when the embedding path raises.
    """
    strat = (strategy or _STRATEGY).lower()

    if strat in ("knn", "auto"):
        try:
            weighted, neighbors = QuestionBank.get().classify(query, k=k)
            cue_cat, cues = classify_heuristic(query)
            category, confidence, blend_note = _blend(weighted, cue_cat, cues)
            mode = MODE_BY_CATEGORY.get(category, _DEFAULT_MODE)
            method = "knn+cue" if blend_note else "knn"
            rationale = _rationale(category, mode, "kNN over labeled eval questions")
            if blend_note:
                rationale = f"{blend_note}; {rationale}"
            return RouteDecision(
                mode=mode,
                category=category,
                method=method,
                confidence=confidence,
                rationale=rationale,
                neighbors=neighbors,
                cues=cues if blend_note else [],
            )
        except Exception as e:
            if strat == "knn":
                # Explicit kNN request still degrades gracefully rather than
                # failing the tool call, but record why in the rationale.
                category, cues = classify_heuristic(query)
                mode = MODE_BY_CATEGORY.get(category, _DEFAULT_MODE)
                return RouteDecision(
                    mode=mode,
                    category=category,
                    method="heuristic",
                    confidence=0.5 if cues else 0.0,
                    rationale=(
                        f"kNN unavailable ({type(e).__name__}); fell back to "
                        + _rationale(category, mode, "lexical heuristic")
                    ),
                    cues=cues,
                )
            # strat == "auto": fall through to heuristic block below.

    category, cues = classify_heuristic(query)
    mode = MODE_BY_CATEGORY.get(category, _DEFAULT_MODE)
    return RouteDecision(
        mode=mode,
        category=category,
        method="heuristic",
        confidence=0.5 if cues else 0.0,
        rationale=_rationale(category, mode, "lexical heuristic"),
        cues=cues,
    )
