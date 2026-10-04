"""THE ASSESSED ALGORITHM: naive exact string matching, written from scratch.

Rules (course requirement) - this module must NOT use:
    str.find / str.index / str.count / "in" substring search, regex,
    slicing-based equality tests such as sequence[i:i+m] == motif, Biopython,
    or any string-matching library.
It must also NOT import plotting, timing, data generation, the oracle or UI code.

Notation: n = len(sequence), m = len(motif).
Expected analysis (to be justified in docs/report/02_design.md & 03_correctness.md):
    worst-case time O(n*m); auxiliary space: TBD from the final implementation.
"""
from .models import MatchResult
from .validation import validate_sequence, validate_motif


def find_motifs(sequence: str, motif: str) -> MatchResult:
    """Return every exact (including overlapping) occurrence of `motif`.

    Pseudocode (to be finalised in Phase 3):
        validate inputs                         # raises ValidationError
        for start in 0 .. n-m (inclusive):      # positions_examined += 1
            for j in 0 .. m-1:
                comparisons += 1                # count EVERY comparison
                if sequence[start+j] != motif[j]: break
            else: record `start`
        If m > n the loop range is empty -> no positions, 0 comparisons.

    Counting rule (decide + document in Phase 4): one comparison = one
    evaluation of sequence[start+j] vs motif[j]; the mismatching comparison
    that triggers `break` IS counted.

    TODO (Phase 3-4): implement. Do not call the oracle from here.
    """
    raise NotImplementedError("Phase 3: implement naive matching with counters")
