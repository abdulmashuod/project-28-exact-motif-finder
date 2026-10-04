"""Step-by-step trace of the naive algorithm.

Produces TraceStep objects (data) and a text formatter. No printing happens in
trace_search itself, so terminal output, saved files and the future UI can all
reuse it. The trace must follow exactly the same alignment/comparison logic as
algorithm.find_motifs (a test will check that trace comparison totals equal
MatchResult.comparisons).
"""
from .models import TraceStep


def trace_search(sequence: str, motif: str) -> list[TraceStep]:
    """Return one TraceStep per examined start position.

    TODO (Phase 5): implement (validate first, same loop structure as the
    assessed algorithm).
    """
    raise NotImplementedError("Phase 5: implement trace_search")


def format_trace(steps: list[TraceStep], motif: str) -> str:
    """Render steps as text, e.g.

        Position 0
        DNA substring: ATA
        Motif: ATA
        Comparisons:
        A == A
        T == T
        A == A
        Result: MATCH

    TODO (Phase 5): implement.
    """
    raise NotImplementedError("Phase 5: implement format_trace")
