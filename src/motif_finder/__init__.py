"""motif_finder: naive exact motif matching in synthetic DNA (CS-251, Project 28).

Public API (stable boundary for experiments, tests and the future UI):
    find_motifs(sequence, motif) -> MatchResult
    trace_search(sequence, motif) -> list[TraceStep]
    validate_sequence / validate_motif / ValidationError
"""
from .models import MatchResult, TraceStep, Comparison
from .validation import ValidationError, validate_sequence, validate_motif
from .algorithm import find_motifs
from .tracing import trace_search, format_trace

__all__ = [
    "MatchResult", "TraceStep", "Comparison",
    "ValidationError", "validate_sequence", "validate_motif",
    "find_motifs", "trace_search", "format_trace",
]
