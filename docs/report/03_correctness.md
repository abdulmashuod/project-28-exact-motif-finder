# 3. Correctness

## Claim
The algorithm reports every and only the exact occurrences of the motif.

## Loop invariant / base case
TODO

## Induction hypothesis
TODO

## Induction step
TODO

## Termination
TODO

## Supporting arguments
every valid start checked; match only if all m chars equal; overlaps not lost; invalid input rejected before matching.


## Hand-worked trace
(ATATA / ATA)
index:    0 1 2 3 4
text:     A T A T A
start 0:  A T A
start 1:    A T A
start 2:      A T A
