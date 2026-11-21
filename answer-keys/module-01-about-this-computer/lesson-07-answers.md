# Module 1, Lesson 7 — Answers

**Lesson:** What Python Actually Runs · **Expectations:** A4.3, C3.3, C3.4, C3.5

Teacher-only. Do not publish or link from the site.

## Review

1. `ics3u`
2. The terminal's current folder was `ics3u` when the tool started, and the tool builds `sample-folder` in the current folder.

## Predict, Then Step

**Program A (`l07_runtime_error.py`)**: run-time error. Two lines print:

```text
Line 1 runs
Line 2 runs
```

then `ZeroDivisionError: division by zero` on line 3. Line 3's text never prints, because Python works out `10 / 0` before printing anything on that line.

**Program B (`l07_syntax_error.py`)**: syntax error (`'(' was never closed`, line 3). Nothing prints, even though lines 1 and 2 are fine: Python compiles the whole file first, and stops at the syntax error before running anything.

## Investigate: Looking at Bytecode

Python 3.11 output (the web page runs 3.13; names differ slightly):

```text
  1           2 LOAD_CONST               0 (8)
              4 STORE_NAME               0 (cores)

  2           6 LOAD_NAME                0 (cores)
              8 LOAD_CONST               1 (2)
             10 BINARY_OP                5 (*)
             14 STORE_NAME               1 (doubled)

  3          ...LOAD_NAME (print), LOAD_NAME (doubled), CALL ...
```

1. `LOAD_NAME cores`, `LOAD_CONST 2`, `BINARY_OP *`, `STORE_NAME doubled`.
2. `BINARY_OP` with `*` (5).
3. `STORE_NAME 1 (doubled)`.
4. Line 2 now loads `print` and `cores`, loads the constant `1`, does `BINARY_OP +`, and calls `print`; there's no `STORE_NAME doubled`.

## Investigate: Who Built Your Python?

1. Answers vary: e.g. `Clang 13.0.0` (macOS), `MSC v.1942 64 bit (AMD64)` (Windows), `GCC 12.2.0` (Linux). The web page reports a Clang version (Emscripten).
2. C (CPython is written in C, then compiled for each CPU and operating system).

## Investigate: Application, Language, or Operating System?

| Application | Programming language | Operating system |
|---|---|---|
| Chrome, Thonny, Minecraft, Microsoft Word, VS Code, `python.exe` (the interpreter), Scratch (the editor) | Python, JavaScript, Scratch (the language), Java | Windows, macOS, Linux, Android, iOS |

Accept reasoned answers for Scratch and `python.exe`. Key idea: a language is a set of rules for writing instructions; the interpreter is the application that carries them out; the operating system runs and shares the computer underneath every application.

## Modify

1. No lines print: line 1 now fails with `ZeroDivisionError` before printing.
2. Fixed (`print("Line 3 runs")`): three lines print.
3. Another `LOAD_NAME print`, `LOAD_NAME doubled`, `LOAD_NAME cores`, `BINARY_OP +`, and a `CALL`.

## Make (`what_runs_this.py`)

One version:

```python
import platform
import sys

print(f"CPU type: {platform.machine()}")                                  # hardware
print(f"Operating system: {platform.system()} {platform.release()}")     # operating system
print(f"Interpreter: {sys.executable}")                                   # interpreter (an application)
print(f"Language: {platform.python_implementation()} {platform.python_version()}")
print(f"Built by: {platform.python_compiler()}")                          # the compiler that made it
```

## Exit Ticket (`l07_exit_ticket.py`)

1. `Start` only, then a run-time error (`ZeroDivisionError` on line 3). Line 2 runs but prints nothing.
2. A compiler translates a whole program ahead of time into machine code (an executable) that runs later. An interpreter reads a program and carries it out as it goes.
