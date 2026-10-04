"""Plain data containers shared by the algorithm, tracing, experiments and UI.

No logic lives here. Keeping results as simple dataclasses means the terminal,
saved JSON/CSV files and the future UI can all consume the same objects.
"""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MatchResult:
    """Result of one motif search.

    positions:            zero-based start positions of every exact occurrence
                          (overlapping occurrences included), ascending.
    comparisons:          number of single-character comparisons performed.
    positions_examined:   number of alignment start positions tried.
    sequence_length:      n
    motif_length:         m
    """
    positions: list[int]
    comparisons: int
    positions_examined: int
    sequence_length: int
    motif_length: int

    @property
    def matches_found(self) -> int:
        return len(self.positions)


@dataclass(frozen=True)
class Comparison:
    """One character comparison inside one alignment."""
    dna_char: str
    motif_char: str
    equal: bool


@dataclass
class TraceStep:
    """One alignment (start position) of the naive algorithm."""
    position: int
    dna_window: str                      # DNA substring aligned with the motif
    comparisons: list[Comparison] = field(default_factory=list)
    matched: bool = False
