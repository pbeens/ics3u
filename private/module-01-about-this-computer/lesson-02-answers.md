# Module 1, Lesson 2 — Answers

**Lesson:** Exploring the platform Library · **Expectations:** A1.1, A3.1, A4.3, A4.4, C1.1

Teacher-only. Do not publish or link from the site.

## Review

1. The classroom computer's CPU type (e.g. `arm64`, `AMD64`); the web page prints `wasm32`.
2. The dot means "the `machine` tool from the `platform` module". The parentheses mean "use (call) it now".

## Predict, Then Step

1. Lines 3–5 ask questions and store the answers; lines 7–9 print.
2. `Computer report for` followed by the computer's name (`emscripten` on the web page).
3. The answers are stored in variables first. The output is the same kind of report, now with the computer's name on the first line.

On the web page the output is:

```text
Computer report for emscripten
CPU type: wasm32
Operating system: Emscripten
```

## Investigate: What the Variables Hold

1. After line 3: `cpu` exists, holding `'wasm32'` on the web page (the classroom computer's CPU type when run there).
2. They were stored in the variables `cpu`, `system`, and `name`, to be printed later.
3. Python would stop with a `NameError`, because `name` would not exist yet. (Students may try this in the Modify box.)
4. Trace table (web page values):

| Line | `cpu` | `system` | `name` | Output |
|---|---|---|---|---|
| 3 | `'wasm32'` | | | |
| 4 | `'wasm32'` | `'Emscripten'` | | |
| 5 | `'wasm32'` | `'Emscripten'` | `'emscripten'` | |
| 7 | `'wasm32'` | `'Emscripten'` | `'emscripten'` | `Computer report for emscripten` |
| 8 | `'wasm32'` | `'Emscripten'` | `'emscripten'` | `CPU type: wasm32` |
| 9 | `'wasm32'` | `'Emscripten'` | `'emscripten'` | `Operating system: Emscripten` |

## Investigate: Spot the Problem

1. Program A is missing the parentheses after `platform.machine`, so Python prints the function itself, e.g. `<function machine at 0xa61558>`, instead of calling it.
2. Line 3. `AttributeError: module 'platform' has no attribute 'cpu'` means the `platform` module has no tool named `cpu`.
3. `dir(platform)` lists every available name, so it would show that `cpu` does not exist (and that `machine` does).
4. The full traceback names the file and line 3, shows the line of code with markers under the problem, and ends with the same `AttributeError` message.

## Modify

```python
import platform

cpu = platform.machine()
system = platform.system()
name = platform.node()
version = platform.python_version()
release = platform.release()

print("Computer report for", name)
print("CPU type:", cpu)
print("Operating system:", system)
print("OS version:", release)
print("Python version:", version)
```

## Exit Ticket

1. Output:

```text
CPU: AMD64
Again: AMD64
```

2. Once, on line 3. Line 5 reuses the stored answer.
