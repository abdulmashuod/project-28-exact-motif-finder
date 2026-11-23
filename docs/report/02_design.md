# 2. Design

## Algorithm

The naive matcher examines every valid start position in the DNA sequence.
At each start, it compares motif characters with the corresponding sequence
characters one at a time and records the start only if every character matches.
The search continues after a match so that overlapping occurrences are retained.

## Pseudocode
```
validate sequence
validate motif
for each start from 0 through n-m:
    positions_examined <- positions_examined + 1
    matched <- true
    for j from 0 through m-1:
        comparisons <- comparisons + 1
        if sequence[start+j] != motif[j]:
            matched <- false
            break
    if matched:
        append start to positions
return positions and counters
```

## Complexity
n = sequence length, m = motif length. Worst case O(nm).
TODO: best case, expected case, why worst case occurs, auxiliary space.

## Design decision
TODO (see docs/decisions/decision_log.md)

## Rejected alternative
TODO (e.g. KMP: scope vs theory vs observation - do not claim naive is universally better)
