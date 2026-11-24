# Development Log

Keep newest entries at the bottom. At least 3 snapshots required (tie each to a
git commit hash if you like).

## Template
```
Date:
Question/Defect:
Attempted Change:
Observed Result:
Decision:
Next Step:
```

## Entries

### Entry 1
Date: 2026-11-09
Question/Defect: Need a repository skeleton that separates core, experiments, tests, UI.
Attempted Change: Created folder structure, stubs, docs templates (scaffolding assisted by an AI tool - declare in acknowledgement).
Observed Result: `pytest` runs: 1 passed, remaining tests skipped as TODO; placeholder scripts run.
Decision: Proceed to Phase 2 (validation).
Next Step: Implement and test `validate_sequence` / `validate_motif`.

### Entry 2
Date: 2026-11-09
Question/Defect: How should invalid input be rejected? The first version had
syntax and indentation errors and compared with `is None` instead of checking
the empty string.
Attempted Change: Fixed the syntax and indentation, and used `len(value) == 0`
for empty-string checks.
Observed Result: After saving the corrected file, validation tests passed:
10 passed and 16 skipped.
Decision: Validation was complete.
Next Step: Implement and test the Phase 3 matching loop.

### Entry 3
Date: 2026-11-09
Question/Defect: The loop range excluded the final possible start position.
Attempted Change: Changed the loop to cover every window with
`range(n - m + 1)`.
Observed Result: ATATA/ATA now found the occurrence at start 2 as well.
Decision: The inclusive window range was correct.
Next Step: Add hand-derived operation-counter tests.

### Entry 4
Date: 2026-11-24
Question/Defect: The operation counters had no independently checked evidence,
and the counter-test placeholder was skipped.
Attempted Change: Derived expected counts by hand for ATATA/ATA, ACGT/TT,
AAAA/AA, and ACG/ACGT; replaced the counter placeholder with explicit tests
and kept only the oracle placeholder skipped.
Observed Result: `python -m pytest -v` passed with 13 tests passed and 14
tests skipped.
Decision: Counting must include every character evaluation, including the
mismatching comparison.
Next Step: Run the test suite and correct the implementation or hand derivation
if either disagrees, then commit and open the Phase 4 pull request.