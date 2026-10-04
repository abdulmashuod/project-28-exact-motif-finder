# Interactive UI (Phase 13 - NOT implemented yet)

Boundary rule: the UI may only call the public API of `motif_finder`
(`validate_*`, `find_motifs`, `trace_search`, `format_trace`) and read files in
`data/` / `results/`. It must never reimplement matching and the core must never
import anything from `ui/`.

Planned features: paste DNA + motif, validation messages, match positions,
comparison count, n and m, highlighted (including overlapping) occurrences,
step-by-step trace, complexity note, load generated examples, motif-rich vs
motif-poor comparison.

Technology: undecided (e.g. Streamlit, Flask, or Tkinter). Decide in the
decision log when Phase 13 starts.
