# 2. Design

## Algorithm

def find_motifs(sequence: str, motif: str) -> MatchResult:
    Return every exact (including overlapping) occurrence of `motif`

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
            if sequence[start+j] != motif[j]:
                matched = False 
                break
        if matched:
            positions.append(start)

    return MatchResult(positions = positions, comparisons = comparisons,
                       positions_examined = positions_examined,
                       sequence_length = n, motif_length= m)



## Pseudocode
TODO (final version matching algorithm.py)

## Complexity
n = sequence length, m = motif length. Worst case O(nm).
TODO: best case, expected case, why worst case occurs, auxiliary space.

## Design decision
TODO (see docs/decisions/decision_log.md)

## Rejected alternative
TODO (e.g. KMP: scope vs theory vs observation - do not claim naive is universally better)
