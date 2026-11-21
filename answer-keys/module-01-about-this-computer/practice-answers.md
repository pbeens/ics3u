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

## After Lesson 4

### Read and predict (`l04_practice_read.py`)

On the web page (Python version varies):

```text
·····LAB·REPORT·····
System:···Emscripten
Python:···3.11.4
Python 3.11.4 is running on Emscripten.
```

1. 20 characters: `LAB REPORT` (10) centred in 20, with 5 spaces each side.
2. Both labels are padded to 10 characters.
3. They make a string *inside* the hole. The single quotes are different from the f-string's double quotes, so Python doesn't think the f-string has ended. The value in the hole is just the text `LAB REPORT` or `System:`.

### Spot the mistakes (`l04_practice_mistake.py`)

1. No `f`, so it prints `CPU type: {cpu}`.
2. A run-time error (`NameError: name 'cores' is not defined`): line 4 printed before the program stopped.
3. `print(f"CPU type: {cpu}")`, and add `cores = 4` before line 5.

### Modify

```python
print(f"{'Laptop:':<21}{laptop:>5} GB")
print(f"{'Desktop:':<21}{desktop:>5} GB")
print(f"{'USB key:':<21}{64:>5} GB")
print(f"{'External hard drive:':<21}{4000:>5} GB")
```

```text
Laptop:                512 GB
Desktop:              2000 GB
USB key:                64 GB
External hard drive:  4000 GB
```

Any label width of 20 or more works for question 3 (`External hard drive:` is 20 characters).

### Make

Answers vary. Check that every label uses the same padding width, the values line up, and variable names are clear.

## After Lesson 5

### Read and predict (`l05_practice_read.py`)

```text
<class 'int'> <class 'float'> <class 'str'>
25.6
LAB-PC-14LAB-PC-14
8 cores
True
```

1. `int`, `float`, `str`.
2. `float` (an `int` times a `float` is a `float`).
3. `name * 2` repeats the string; `str(cores) + " cores"` joins two strings.
4. `True`, a `bool`.

### Spot the mistake (`l05_practice_mistake.py`)

1. Line 3; a run-time error (`TypeError`).
2. `unsupported operand type(s) for -: 'str' and 'int'`: you can't subtract an integer from a string.
3. Line 1: `storage_gb = 512`. Or line 3: `free_gb = int(storage_gb) - used_gb`. Output: `Free: 312 GB`.

### Modify

1. `float`, because `/` always gives a float (`113777.77777777778`).
2. `print("Photos that fit:", int(photos))` gives `113777`. (`int()` cuts off the decimal part; it doesn't round.)
3. `TypeError: unsupported operand type(s) for /: 'int' and 'str'`. The string `"4.5"` is text, not a number.

### Make (`lab_budget.py`)

```text
Before tax: $6599.70
HST: $857.96
Total: $7457.66
Per computer: $248.59
```

Check: a `TAX_RATE` constant, calculated (not typed) amounts, and `:.2f` throughout.

## After Lesson 6

### Read and predict (`l06_practice_read.py`)

On the web page:

```text
Home folder: /home/pyodide
Course folder: /home/pyodide/ics3u
Course folder exists: False
Last part: ics3u
```

1. The path of the home folder.
2. `False`, because the browser has no `ics3u` folder. On a classroom computer with a course folder in the home folder: `True` (and paths like `/Users/sam/ics3u` or `C:\Users\sam\ics3u`).
3. A `bool`.

### Spot the mistake (`l06_practice_mistake.py`)

1. `Building the path...`, then a run-time `TypeError`.
2. `year` is an `int`; `os.path.join` only joins strings (the message says `argument must be str, bytes, or os.PathLike object, not 'int'`).
3. `os.path.join("ics3u", "backups", str(year))`, or `year = "2026"`. Output: `ics3u/backups/2026`.

### Modify

1. `print(os.path.basename(os.path.dirname(path)))` gives `lesson-06`.
2. `print(os.path.join("/Users/sam/ics3u", "sample-folder", "photos"))` gives `/Users/sam/ics3u/sample-folder/photos`.
3. An empty string (shows as a blank line): after the final slash, there's no last part.

### Make (`where_is_python.py`)

```python
import os
import sys

print(sys.executable)
print(os.path.basename(os.path.dirname(sys.executable)))
```

Answers vary, e.g. `/usr/local/bin/python3` and `bin`, or `C:\Users\sam\AppData\Local\Programs\Python\Python313\python.exe` and `Python313`. Editors sometimes use a different Python from the terminal (Thonny bundles its own); that's the interesting finding.

## After Lesson 7

### Read and predict (`l07_practice_read.py`)

```text
Checking
Speed: 3.2
```

then `NameError: name 'cores' is not defined` on line 4.

1. Two.
2. Run-time: the code is written correctly (no syntax mistake); it only fails when line 4 runs and `cores` doesn't exist.
3. Running the bytecode. Compiling checks the grammar, not whether names exist.

### Spot the mistake (`l07_practice_mistake.py`)

1. It's a syntax error, so Python stops while compiling, before running any line.
2. `SyntaxError: unterminated string literal` on line 3. Fix: `print("RAM: 8 GB")`.

### Modify

1. `LOAD_NAME price`, `LOAD_CONST 3`, `BINARY_OP *`, `STORE_NAME total`.
2. `BINARY_OP` shows `+` (0) instead of `*` (5).
3. `LOAD_NAME print`, `LOAD_NAME total`, a `CALL`, and `POP_TOP` (exact names vary by version).

### Make (`explain_python.py`)

Look for the correct order: source code is compiled to bytecode (syntax checked here), the interpreter carries out the bytecode using machine code the CPU runs, and the operating system starts the interpreter and gives it memory, files, and screen output.

## After Lesson 8

### Read and predict (`l08_practice_read.py`)

```text
179.98 89.99
False
```

1. One value (89.99) and two names (`price`, `copy`) pointing at it.
2. No. Line 3 makes a new value (CPU multiplies; RAM stores it) and moves `price` to it; `copy` still points to 89.99.
3. `False`: it asks whether `price` and `copy` are now the same value in memory.

### Modify

1. 64-bit: `10**10` is 32 bytes, `10**20` is 36, `10**40` is 44. It grows in steps of 4 bytes (roughly every nine digits), not with every digit.
2. No. `sys.getsizeof` measures the value, not the name; the name is stored separately, once.

### Make (`my_computer_specs.py`)

Answers vary. Check: one variable per spec with clear names, an f-string report, and an upgrade recommendation that matches the person's use (e.g. RAM for many browser tabs, video card for gaming).
