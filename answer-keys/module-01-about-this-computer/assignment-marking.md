# Module 1 Assignment: Computer Report Card — Marking Notes

Teacher-only. Do not publish or link from the site.

## Part A (`m01_assignment_read.py`)

1. Three lines.
2. On an Apple silicon Mac named `LAB-PC-14`:

| Line | `name` | `cpu` | Output |
|---|---|---|---|
| 1 | — | — | — |
| 3 | `LAB-PC-14` | | |
| 4 | `LAB-PC-14` | `arm64` | |
| 5 | `LAB-PC-14` | `arm64` | `Report card for LAB-PC-14` |
| 6 | `LAB-PC-14` | `arm64` | `CPU: arm64` |
| 7 | `LAB-PC-14` | `unknown` | |
| 8 | `LAB-PC-14` | `unknown` | `Checked: unknown` |

3. `Checked: unknown`, because line 7 replaced the value in `cpu` before line 8 printed it.
4. Once, on line 4. Printing `cpu` later reuses the stored answer; it doesn't ask again.

Accept any computer's actual values in the trace, as long as they're consistent.

## Part B

Check for: a header comment (name, date, purpose); a title line that includes `platform.node()`; five different `platform` functions, each stored in a clearly named variable; a label on every printed fact; at least one function not taught in class (e.g. `platform.version()`, `platform.architecture()`, `platform.python_implementation()`, `platform.uname()`).

Common problems: printing the function without calling it (`platform.system` with no parentheses prints `<function system at ...>`); reusing one variable name for every fact; labels that don't match the value.

## Part C

- **a.** The labels and the program are identical. In the browser, the CPU type, operating system, and computer name differ (`wasm32`, `Emscripten`, `emscripten`). The Python version may differ too.
- **b.** On the classroom computer, Python ran directly on that hardware. In the browser, Python (Pyodide) ran inside a small virtual computer in the browser tab, so `platform` described that.
- **c.** Answers vary. A strong answer quotes the error type and line, and explains the fix.
