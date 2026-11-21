# Module 1, Lesson 3 — Answers

**Lesson:** Getting Output Right · **Expectations:** A1.1, A2.1, A3.1, A4.3, A4.4

Teacher-only. Do not publish or link from the site.

Web page values: `platform.system()` is `Emscripten`, `platform.machine()` is `wasm32`, `platform.node()` is `emscripten`. Tabs are shown expanded to 8-column stops.

## Review

1. `CPU: wasm32`
2. Line 5, `system = "my computer"`. The old value is gone; a variable holds one value at a time. (Line 4 had already printed it.)

## Predict, Then Step (`l03_print_arguments.py`)

1. Output:

   ```text
   System Emscripten
   System: Emscripten
   Checking... done

   End of report
   ```

   With dots for spaces: `System·Emscripten`, `System:·Emscripten`, `Checking...·done`.
2. Line 8, `print()`: it prints only a new line, which makes the blank line.
3. Line 6 has `end="... "`, so it ends with `... ` instead of a new line, and line 7's output continues on the same line.

## Investigate: Special Characters (`l03_escapes.py`)

```text
Name:   LAB-PC-14
System: Windows
Computer name:  LAB-PC-14
Line one
Line two
```

1. Tab stops are every 8 characters. `Name:` (5) and `System:` (7) both jump to column 8. `Computer name:` is 14 characters, so its tab jumps to column 16.
2. Two lines: `\n` starts a new line in the middle of the string.

## Investigate: Quotes, Commas, and Plus (`l03_quotes_plus.py`)

```text
This computer's CPU is wasm32
The label says " wasm32 "
CPU:wasm32
CPU: wasm32
```

1. The string is inside double quotation marks, so an apostrophe (single quotation mark) doesn't end it.
2. The strings `'The label says "'` and `'"'` are inside single quotation marks, so double quotation marks can go inside them. The spaces come from `sep`: commas give `print()` three separate things, and it puts a space between each.
3. `+` joins the strings into one before printing, with nothing added, so line 6 has no space after the colon. Line 7 types the space inside the string. Line 7 (or the comma version) belongs in a report.
4. `print('The label says "', cpu, '"', sep="")` prints `The label says "wasm32"`.

## Investigate: Spot the Problem

**Program A (`l03_mistake_quote.py`)**

1. Line 3. The apostrophe in `It's` ends the string `'It'`; Python then can't make sense of the rest (`SyntaxError: unterminated string literal`). Nothing runs, not even line 1.
2. `print("It's a", platform.system(), "computer")` or `print('It\'s a', platform.system(), 'computer')`. Output on the web page: `It's a Emscripten computer`. (Students may notice "a Emscripten" reads badly; good observation.)

**Program B (`l03_mistake_path.py`)**

3. Output:

   ```text
   Save your work in C:    emp
   ew
   Done
   ```

   `\t` became a tab (eating the `t` of `temp`) and `\n` a new line (eating the `n` of `new`). Fix: `"C:\\temp\\new"`, or forward slashes `"C:/temp/new"`.

## Modify

One correct version:

```python
print("Computer report for", name)
print()
print("CPU type:", cpu, sep="\t\t")
print("Operating system:", system, sep="\t")
print("Checking...", end=" ")
print("Report finished")
```

Output on the web page:

```text
Computer report for emscripten

CPU type:               wasm32
Operating system:       Emscripten
Checking... Report finished
```

Why one tab isn't enough: `CPU type:` is 9 characters, so one tab reaches column 16; `Operating system:` is 17, so its tab reaches column 24. `CPU type:` needs a second tab. Accept `"CPU type:\t\t" + cpu` and similar.

## Exit Ticket (`l03_exit_ticket.py`)

1. `OS-check... done`
2. `print("CPU: " + cpu)` (space inside the string) or `print("CPU:", cpu)`.

Look for: the missing space after `check` being replaced by `-`, and `done` on the same line.
