# Decision Log

## Template
```
Decision:
Date:
Options considered:
Selected approach:
Reason:
Evidence:
Rejected alternative:
Consequences:
```

## D1 - Algorithm choice (DRAFT: fill in with your own evidence)
Decision: Use naive exact matching as the assessed algorithm.
Date: [9-11-26]
Options considered: naive; KMP; [others you examined]
Selected approach: naive
Reason: Project 28 specifically assesses simple exact matching, and the project
studies its behaviour (operation counts) on synthetic DNA families.
Evidence: [TODO - operation counts / comparison once experiments exist]
Rejected alternative: KMP - rejected *for this project's scope*, NOT because it is
worse. KMP has O(n+m) worst-case time versus naive O(nm); that is a theoretical
fact, separate from what we observe on small synthetic data.
Consequences: worst-case O(nm); repetitive inputs can be costly (see stress case).

## D2 - Operation counting rule (DRAFT: provisional until the instructor confirms)
Decision: Count one comparison for each character comparison, including the
first mismatching comparison that ends a window.
Date: 2026-11-24
Options considered: count only successful character matches; count all
character evaluations; count only windows examined.
Selected approach: count all character evaluations performed, including the
failing comparison.
Reason: This makes comparisons observable and distinguishes early mismatches
from successful windows in repetitive and non-matching inputs.
Evidence: Hand-derived cases:
ATATA/ATA -> positions [0, 2], 7 comparisons, 3 positions examined;
ACGT/TT -> positions [], 3 comparisons, 3 positions examined;
AAAA/AA -> positions [0, 1, 2], 6 comparisons, 3 positions examined.
The motif-longer-than-sequence case has 0 comparisons and 0 positions examined.
Rejected alternative: counting only successful matches would hide the cost of
failed character comparisons and would not reflect the implemented loop.
Consequences: comparisons range from at least n-m+1 for a failing first
character in every window to at most (n-m+1)*m. This rule remains provisional
until the instructor confirms the counting interpretation.

## D3 - Generation rules and master seed (TODO, Phase 7)
