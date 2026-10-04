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
Date: [TODO]
Options considered: naive; KMP; [others you examined]
Selected approach: naive
Reason: Project 28 specifically assesses simple exact matching, and the project
studies its behaviour (operation counts) on synthetic DNA families.
Evidence: [TODO - operation counts / comparison once experiments exist]
Rejected alternative: KMP - rejected *for this project's scope*, NOT because it is
worse. KMP has O(n+m) worst-case time versus naive O(nm); that is a theoretical
fact, separate from what we observe on small synthetic data.
Consequences: worst-case O(nm); repetitive inputs can be costly (see stress case).

## D2 - Input contract details (TODO)
Empty sequence, lowercase, counting rule: see open questions in
docs/course_specification.md.

## D3 - Generation rules and master seed (TODO, Phase 7)
