# Module 1, Lesson 9 — Answers

**Lesson:** Talking Back, and a First Look Ahead · **Expectations:** A1.1, A2.1, A2.2, A4.4

Teacher-only. Do not publish or link from the site.

Web page values: `Emscripten`, `wasm32`, `emscripten`. The step-through boxes type the preset answers shown under each one.

## Review

1. `cores = 4`: RAM. `threads = cores * 2`: RAM and CPU. `print(threads)`: RAM, CPU, screen.
2. Nowhere: its part of RAM was handed back when the program ended.

## Teach (`l09_greeter.py`, typed answer `Sam`)

```text
What's your name? Sam
Hi, Sam! This computer runs Emscripten.
Its processor is wasm32.
```

## Predict, Then Step (`l09_ram_upgrade.py`, typed answers `8` and `8`)

```text
How many GB of RAM now? 8
How many GB are you adding? 8
Total: 88 GB
Total: 16 GB
```

1. Line 3 joins two strings (`88`); line 4 converts both to integers and adds (`16`).
2. `'8'`, with quotation marks: a string.

## Investigate: Decisions (`l09_if_system.py`)

| Computer | Output |
|---|---|
| Windows | `Open File Explorer to see your files.` then `Your course folder is called ics3u.` |
| Mac | `Open Finder to see your files.` then the course folder line |
| Web page | `Open your file browser to see your files.` then the course folder line |

1. Web page: the box highlights lines 1, 3, 4, 6, 9, 10. The `if` (4) and `elif` (6) checks are tested and fail; lines 5 and 7 are skipped. The `else:` line (8) is never highlighted, because there's nothing to check: Python goes straight to line 9.
2. See the table.
3. Yes. It isn't part of any branch.

## Investigate: Loops (`l09_for_facts.py`)

```text
- wasm32
- Emscripten
- emscripten
Done: 3 facts
```

1. Three. 2. Three times. 3. `'wasm32'`, then `'Emscripten'`, then `'emscripten'`.

## Investigate: Spot the Problem (`l09_mistake_input.py`, typed answer `4`)

1. Logic error (no crash, wrong answer): `Threads: 44`.
2. `input()` gives the string `"4"`, and `*` repeats a string. Fix: `print("Threads:", int(cores) * 2)`.

## Modify

1. e.g. `grade = input("What grade are you in? ")` and add `{grade}` to an f-string.
2. `elif system == "Linux":` with `print("Open Files to see your files.")`, placed before `else`.
3. Four times.

## Make (`welcome.py`)

```python
import platform

name = input("What's your name? ")
hours = input("How many hours a day do you use a computer? ")
weekly = int(hours) * 7
print(f"Welcome, {name}!")
print(f"This computer runs {platform.system()} on a {platform.machine()} processor.")
print(f"{hours} hours a day is {weekly} hours a week.")
if weekly > 28:
    print("Remember to take breaks.")
```

## Exit Ticket (`l09_exit_ticket.py`)

1. ```text
   Dock
   Ready
   ```
2. `"33"`: `input()` gives a string, and `*` repeats it.
