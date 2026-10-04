# Course / Project Specification (working summary)

Source: instructor brief, CS-251, Project 28. Max group size: 2.

## Task
Exact motif finder in synthetic DNA using **naive exact string matching**
(assessed algorithm). Report all zero-based start positions, including
overlaps. Reject invalid characters and empty motif; motif longer than the
sequence -> no matches. Example: `ATATA`, `ATA` -> `[0, 2]`.

## Forbidden for the assessed algorithm
`str.find`, regex, external sequence-search libraries, Biopython search,
any built-in/external matcher. A separate simple oracle is allowed for
verification only.

## Learning outcomes and evidence
| CLO | Evidence |
|---|---|
| CLO1 / C3 | short inductive correctness argument; live trace |
| CLO2 / C4 | operation counts; justified time & space analysis; interpreted experiments |
| CLO3 / C6 | justified design implemented and tested in Python |

## Experiments (official scope)
n in {50, 100, 200, 400}; m in {2, 4, 8}; families: motif-rich, motif-poor,
random/synthetic. Store seed, parameters, motif, n, m, family, data.
Operation counts primary; timing secondary (perf_counter, 1 warm-up, 5 runs,
median, record Python/machine). Never infer complexity from timing alone.

## Personal contribution checklist
- [ ] Hand-created dataset(s)            - [ ] Reproducible generated dataset(s)
- [ ] Seed + generation rules saved      - [ ] Design decision documented
- [ ] Alternatives compared with evidence - [ ] Rejected alternative documented
- [ ] Counterexample / boundary / stress case, predicted BEFORE running
- [ ] Explanation of what that case reveals
- [ ] Development log (date, question/defect, change, result, next decision), >= 3 snapshots

## Testing requirement
>= 8 named tests with independently defined expected outputs: 2 ordinary,
4 boundary/invalid, 2 personally constructed. Oracle kept outside the measured
algorithm.

## Required edge cases
Empty DNA; 1-char DNA; empty motif; motif longer than DNA; no match; single
match; multiple; overlapping; repeated single char; invalid DNA chars; invalid
motif chars; motif == whole sequence.

## Deliverables
Report <= 10 pages main text (6 sections, see docs/report/); presentation +
live demo + viva; interactive interface added at end of semester.

## Open contract decisions (confirm with instructor, then record in decision log)
1. Is the empty DNA sequence *valid with zero matches* or *rejected*? (skeleton assumes valid)
2. Is lowercase rejected or normalised? (skeleton assumes rejected)
3. Comparison counting: is the mismatching comparison counted? (skeleton assumes yes)
4. Hand-written dataset and generated dataset formats (txt/json).
