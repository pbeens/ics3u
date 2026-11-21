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

## Part A2 (`m01_assignment_read2.py`; the user types `Sam`, then `3`)

5. ```text
   User:···Sam
   Weekly:·21·hours
   Daily:·3·hours
   ```
   (`User:` is padded to 8 characters, so three spaces; `Weekly:` is 7, so one.)
6. `hours` is a `str`: `input()` always gives a string. `weekly` is an `int`: `int(hours) * 7` converts first, and line 6 can only join `hours` with `+` because it's a string.
7. `Weekly: 3333333 hours`: `*` repeats the string `"3"` seven times.

## Part B

Check for: a header comment (name, date, purpose); an `input()` for the user's name used in a title line that also includes `platform.node()`; five different `platform` functions, each stored in a clearly named variable; every fact printed with an f-string, labels padded to one width so values line up; one number question converted with `int()` or `float()` and a correct calculation; at least one function not taught in class (e.g. `platform.version()`, `platform.architecture()`, `platform.python_implementation()`, `platform.uname()`); comments that explain.

Common problems: calculating with the `input()` string without converting it; labels padded to different widths; printing the function without calling it (`platform.system` with no parentheses prints `<function system at ...>`); reusing one variable name for every fact; labels that don't match the value.

## Part C

- **a.** The labels and the program are identical. In the browser, the CPU type, operating system, and computer name differ (`wasm32`, `Emscripten`, `emscripten`). The Python version may differ too.
- **b.** On the classroom computer, Python ran directly on that hardware. In the browser, Python (Pyodide) ran inside a small virtual computer in the browser tab, so `platform` described that.
- **c.** Answers vary. A strong answer quotes the error type and line, and explains the fix.

For Part C question 2, students replace each `input(...)` with a fixed value first: the browser boxes can't ask questions (they show `[Errno 29] I/O error`). Credit students who explain why.

## Part D

1. In order: the operating system loads the interpreter (machine code) from the storage drive into RAM and starts it; the interpreter reads `report_card.py` from the drive into RAM and compiles it to bytecode; the interpreter carries out the bytecode, with the CPU doing the work: values are fetched from RAM into the CPU, calculated, and stored back in RAM; `print()` asks the operating system to show the text (via the video card). When the program ends, its RAM is handed back.
2. A storing line (e.g. `cpu = platform.machine()`): CPU runs the function, RAM stores the answer. A calculating line (e.g. `weekly = int(hours) * 7`): RAM to CPU, the CPU converts and multiplies, the answer stored in RAM. A printing line: RAM, CPU, screen.
3. Both, but mainly interpreted: Python compiles the whole file to bytecode first (so a syntax error on the last line stops every line from running), then interprets the bytecode one instruction at a time; it never produces a standalone machine-code executable like a compiler would.
