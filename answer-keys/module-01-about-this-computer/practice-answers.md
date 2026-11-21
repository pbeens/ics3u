# Module 1 Practice — Answers

Teacher-only. Do not publish or link from the site.

## After Lesson 1

### Read and predict (`l01_practice_read.py`)

1. Four lines.
2. `Python report` and `Done` are the same everywhere. The labels `System:` and `Python version:` are also fixed.
3. The values after `System:` and `Python version:` change. For example, on an Apple silicon Mac with Python 3.11.4:

```text
Python report
System: Darwin
Python version: 3.11.4
Done
```

In the browser, `System:` shows `Emscripten` and the version is whatever Pyodide uses.

4. Line 6, `print("Done")`.

### Modify

1. Add `print("CPU:", platform.machine())`, anywhere after the `import`.
2. `print("Python report by Sam")`.
3. `Done` prints first, because Python runs lines from top to bottom. The program still works: `print("Done")` doesn't need anything from `platform`.

### Make

Any program like:

```python
import platform

print("My computer")
print("CPU type:", platform.machine())
print("Operating system:", platform.system())
print("Version:", platform.release())
```

## After Lesson 2

### Trace (`l02_practice_trace.py`), on macOS with Python 3.11.4

| Line | `system` | `version` | Output |
|---|---|---|---|
| 1 | — | — | — |
| 3 | `Darwin` | | |
| 4 | `Darwin` | `3.11.4` | |
| 5 | `Darwin` | `3.11.4` | `Running on Darwin` |
| 6 | `my computer` | `3.11.4` | |
| 7 | `my computer` | `3.11.4` | `Python 3.11.4 on my computer` |

1. After line 3: the operating system's name (e.g. `Darwin`, `Windows`). After line 6: `my computer`.
2. Line 6 replaced the value in `system`. A variable holds only its most recent value, and line 7 uses whatever it holds at that moment.

### Spot the mistake (`l02_practice_mistake.py`)

1. `AttributeError`.
2. Line 3, `version = platform.python_versions()`.
3. Python asks: `Did you mean: 'python_version'?` Fix: remove the `s`. (The suggestion appears in Python 3.10 and later; the browser's version shows it too.)

### Make

Answers vary. Check that the variable name describes the value, the output has a label, and the comment explains the function correctly.

## After Lesson 3

### Read and predict (`l03_practice_read.py`)

On the web page (tab expanded):

```text
+--------------------+
|   LAB INVENTORY    |
+--------------------+
Name:   emscripten
Checked today
```

1. Five lines.
2. A tab (`sep="\t"`). On screen, the name starts at column 8.
3. Line 8 has `end=" "`, so it ends with a space instead of a new line.
4. Yes, all 22 characters. If one line is shorter or longer, the right side of the box is jagged.

### Spot the mistake (`l03_practice_mistake.py`)

1. No. It's a syntax error, so Python can't understand the program and doesn't run any line.
2. `SyntaxError: '(' was never closed`, pointing to line 3.
3. Add the closing parenthesis: `print("Operating system:", platform.system())`.

### Modify

1. `print("CPU type", platform.machine(), sep=" -> ")`
2. `print("Checking", end=" ")` then `print("done")`, giving `Checking done` (any `end` value is fine).
3. `print('It\'s "fast"')` or `print("It's \"fast\"")`.

### Make

The System Banner Quick Build; see `quick-build-system-banner-marking.md`.
