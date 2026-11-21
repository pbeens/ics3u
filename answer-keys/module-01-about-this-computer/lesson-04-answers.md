# Module 1, Lesson 4 — Answers

**Lesson:** Better Reports with f-strings · **Expectations:** A1.1, A2.1, A4.2, A4.3

Teacher-only. Do not publish or link from the site.

Web page values: `platform.system()` is `Emscripten`, `platform.machine()` is `wasm32`, `platform.node()` is `emscripten`.

## Review

1. `CPU: arm64!` (and no new line after it).
2. The computer's name is a different length on every computer, so putting it inside a box with a fixed right edge would push that edge out of line.

## Predict, Then Step (`l04_fstring_report.py`)

```text
Name: emscripten
CPU: wasm32
emscripten has a wasm32 processor.
{name} has a {cpu} processor.
```

2. Line 7 is an f-string, so the braces are filled with the values. Line 8 has no `f`, so the braces and names print as ordinary text.

## Investigate: Padding Inside a Box (`l04_padding.py`)

```text
+----------------------------+
|       SYSTEM BANNER        |
| Name:   emscripten         |
| System: Emscripten         |
+----------------------------+
```

1. Line 8: `|` + 28 (title centred in 28) + `|` = 30.
2. `| Name:   ` is 10 characters and ` |` is 2: 30 − 12 = 18.
3. No. Padding never cuts a value. The 26-character name is printed in full, so that line is 8 characters wider and the right edge sticks out:

   ```text
   +----------------------------+
   | Name:   student-laptop-in-room-214 |
   | CPU:    arm64              |
   +----------------------------+
   ```

4. At least 26, so the box would be at least 38 characters wide (10 + 26 + 2), with the borders lengthened to match.

## Investigate: Names and Comments

1. People read code: the teacher, classmates, the author weeks later. Clear names make it obvious what each value is without tracing.
2. The program already shows *what* it does; the comment explains a choice (the width) that the code can't explain by itself.
3. Python would read the space as the end of the name, so `computer name = ...` is a syntax error.

## Investigate: Spot the Problem

**Program A (`l04_mistake_brace.py`):** line 4; `SyntaxError: f-string: expecting '}'`. Fix: `print(f"CPU: {cpu}")`. Nothing ran.

**Program B (`l04_mistake_name.py`):** `Report starting` printed, then `NameError: name 'nme' is not defined` on line 5. There's no variable called `nme`; fix the typo to `name`. Thonny and IDLE add `Did you mean: 'name'?`.

3. A is a syntax error (no output at all; the program never started). B is a run-time error (line 4's output appeared before it stopped).

## Modify

One correct version (box widened to 34 for question 3):

```python
print("+================================+")
print(f"|{'SYSTEM BANNER':^32}|")
print("+================================+")
print(f"| Name:   {name:<22} |")
print(f"| System: {system:<22} |")
print("+================================+")
```

Students may keep the title as a plain string, or use a `title` variable. For question 3, everything changes together: the borders, the centring width, and every padding width grow by 4.

## Exit Ticket (`l04_exit_ticket.py`)

```text
[arm64···]
[···arm64]
[{cpu}]
```

Look for: three spaces on the correct side, and the literal `{cpu}` on the last line (no `f`).
