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
Date: 
Question/Defect: Need a repository skeleton that separates core, experiments, tests, UI.
Attempted Change: Created folder structure, stubs, docs templates (scaffolding assisted by an AI tool - declare in acknowledgement).
Observed Result: `pytest` runs: 1 passed, remaining tests skipped as TODO; placeholder scripts run.
Decision: Proceed to Phase 2 (validation).
Next Step: Implement and test `validate_sequence` / `validate_motif`.

### Entry 2
Date:11/9/26

Question/Deffect: how do i reject invalid input? my first versioon had a SyntaxError and indention error and is None instead of an empty-string check.

Attempted Change: fixed the errors and instead of is None used len(str)==0 to check for empty string.

Observed Result: didnt saved the file at first so didnt observe any change but after saving 10 passed and 16, skipped.

Decision/ Next Step: validation is done, so phase 3: validation the matching loop is next.

#### Entry 4
Defect: the loop range range(0, n-m) skipped the last start position, so ATATA / ATA gave [0].
Defect: a leftover """ from the old docstring caused an IndentationError, which broke every test file at collection.
Fix and result: range(n - m + 1), the stray line removed, 11 passed, 15 skipped.
Next step: Phase 4, the hand-derived counter tests