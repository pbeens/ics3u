# Module 1, Lesson 6 — Answers

**Lesson:** Where Do My Programs Live? · **Expectations:** A4.3, C2.1, C3.1

Teacher-only. Do not publish or link from the site.

On the web page, the current folder and home folder are both `/home/pyodide`. Classroom examples use a student called `sam`.

## Review

1. `str`, `int`, `float`, `bool`.
2. `+` can't join a string and an integer (`TypeError`). Fix: `print("RAM: " + str(8))` or `print(f"RAM: {8}")`, or `print("RAM:", 8)`.

## Teach (`l06_where_am_i.py`)

Web page: `/home/pyodide`. Classroom: depends on the editor, e.g. `/Users/sam/ics3u/module-01/lesson-06` (Thonny, IDLE) or the opened workspace folder (VS Code).

## Predict, Then Step (`l06_paths.py`)

```text
Running in: /home/pyodide
This folder's name: pyodide
The folder it's inside: /home
/home/pyodide/toolkit/report_card.py
```

2. `basename` gives the last part of a path; `dirname` gives everything before it (the folder it's in).
3. No. `os.path.join` only builds the text of the path; it doesn't check the disk.

## Investigate: The Parts of Your Editor

| Part | Thonny | IDLE | VS Code |
|---|---|---|---|
| Code editor | Main pane | The file's own window | Editor tabs |
| Shell or terminal | Shell (bottom) | Shell window | Terminal panel |
| Run button | Green Run button (F5) | Run → Run Module (F5) | Run button (top right) |
| Debugger | Bug button; Step over / into | Debug → Debugger | Run and Debug (side bar) |
| File browser | View → Files | (none; use the operating system's) | Explorer (side bar) |

## Investigate: Run It From the Terminal

4. A folder called `sample-folder` full of practice files; it never deletes a folder it didn't make itself (one without its marker file), and only rebuilds its own with `--reset`.
5. It prints `Made 156 files (6.9 MB) in .../ics3u/sample-folder` and the seed (2026).
6. Inside `ics3u`, because that was the terminal's current folder when the program started.
7. The current folder is where the program was *started* (the terminal was in `ics3u`), not where the file is stored.

## Investigate: Spot the Problem (`l06_mistake_folder.py`)

1. Run-time error: `Looking for the toolkit...` printed first.
2. `FileNotFoundError: [Errno 44] No such file or directory: 'toolkit'` (Errno 2 on a real computer): there's no folder called `toolkit` in the current folder.
3. `"toolkit"` is a relative path, looked up from the current folder. From `ics3u` it exists. Double-clicking runs the program in `lesson-06`, where there's no `toolkit` folder.

## Modify (`l06_folder_contents.py`)

1. The editor and the terminal started the program in different current folders (e.g. `lesson-06` vs. `ics3u`), so `os.listdir` and `os.path.isdir("toolkit")` looked in different places. In `ics3u`: `True` once the toolkit folder exists.
2. `os.path.isdir("sample-folder")`.
3. `print(items)` prints a list of names in square brackets, e.g. `['module-01', 'toolkit', 'sample-folder', 'make_sample_folder.py']`. Order varies by operating system.

## Make (`folder_check.py`)

One version:

```python
import os

folder = os.getcwd()
items = os.listdir(folder)
print(f"Current folder: {folder}")
print(f"Folder name: {os.path.basename(folder)}")
print(f"Items: {len(items)}")
print("toolkit here:", os.path.isdir("toolkit"))
print("sample-folder here:", os.path.isdir("sample-folder"))
```

From the terminal in `ics3u`: the `ics3u` path, `ics3u`, the item count, `True`, `True`. From Thonny or IDLE: the `toolkit` path, `toolkit`, its count, `False`, `False`.

## Exit Ticket (`l06_exit_ticket.py`)

1. ```text
   toolkit
   ics3u/module-01/lesson-06
   ```
2. `ics3u\module-01\lesson-06`
