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
    """Return every exact (including overlapping) occurrence of `motif`."""

    validate_sequence(sequence)                  # raises ValidationError
    validate_motif(motif)  
    
    n = len(sequence)
    m = len(motif)
    positions = [] 
    comparisons = 0
    positions_examined = 0 

    for start in range(n-m+1): 
        positions_examined += 1
        matched = True
        for j in range(m):
            comparisons += 1                # “every character comparison counts, including the mismatching one”
            if sequence[start+j] != motif[j]: #One comparison = one evaluation of sequence[start+j] against motif[j]; the mismatching comparison is counted
                matched = False 
                break
        if matched:
            positions.append(start)

    return MatchResult(positions = positions, comparisons = comparisons,
                       positions_examined = positions_examined,
                       sequence_length = n, motif_length= m)

