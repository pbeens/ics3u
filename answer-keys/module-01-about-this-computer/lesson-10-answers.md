# Module 1, Lesson 10 — Answers

**Lesson:** Error Clinic · **Expectations:** A4.1, A4.3, A4.4

Teacher-only. Do not publish or link from the site.

## Review

1. `"55"`: `input()` gives a string, and `+` joins strings.
2. Exactly one.

## Predict, Then Step (`l10_library_error.py`)

1. The student wrote `l10_library_error.py`. `<frozen posixpath>` and `<frozen genericpath>` are Python's own files (built into Python, hence "frozen").
2. Line 4 of `l10_library_error.py`: it passes `year`, an integer, to `os.path.join`.
3. `join()` only accepts strings (or paths), not an `int`. Fix: `os.path.join("ics3u", "backups", str(year))`, or `year = "2026"`. Output: `ics3u/backups/2026` (backslashes on Windows).

## Investigate: The Clinic

| Patient | Kind | Line | Message / symptom | Fix |
|---|---|---|---|---|
| 1 | Run-time | 4 | `NameError: name 'Cpu' is not defined` (classroom adds `Did you mean: 'cpu'?`). Names are case-sensitive | `print("CPU:", cpu)` |
| 2 | Syntax | 4 | `SyntaxError: expected ':'`; nothing runs | `if system == "Windows":` |
| 3 | Run-time | 2 | `ValueError: invalid literal for int() with base 10: '8 GB'`: `int()` can't read the letters | `ram_text = "8"` (or `int(ram_text.split()[0])`, a Module 4 idea). Output `Doubled: 16 GB` |
| 4 | Logic | 2 | Prints `Storage: 0.512 MB`, but 512 GB is about 512,000 MB | `storage_mb = storage_gb * 1000`, giving `Storage: 512000 MB` |
| 5 | Run-time | 4 | `Checking the system...` prints, then `AttributeError: module 'platform' has no attribute 'sytem'` (classroom adds `Did you mean: 'system'?`) | `platform.system()` |

## Make (`error_guide.txt`)

Check each entry has a correct kind: `SyntaxError` and `IndentationError` are syntax errors (found before running); `NameError`, `AttributeError`, `TypeError`, `ValueError`, `FileNotFoundError`, `ZeroDivisionError` are run-time errors. The logic-error section should mention predicting the output first and comparing.

## Exit Ticket (`l10_exit_ticket.py`)

1. Line 4: run-time error, `TypeError: unsupported operand type(s) for /: 'str' and 'int'`.
2. `Total GHz: 3.23.23.23.2`: a logic error (`*` repeats the string `"3.2"` four times).
3. `speed = 3.2` (no quotation marks). Output: `Total GHz: 12.8` and `Per core: 0.8`.
