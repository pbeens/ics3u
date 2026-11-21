# Module 1 Test — Answers and Marking

Teacher-only. Do not publish or link from the site. Every code answer below was produced by running the code with Python 3.11.

## Part 1 (30)

**1. (3)** One mark per line, including the blank line.

```text
Lab-PC 14

Room:→214
```

**2. (3)**

```text
[x86_64···]
[···6]
··OS··|
```

**3. (6)** Four marks for the table (rows 1–4), two for the output.

| Line | `storage` | `used` | `free` | Output |
|---|---|---|---|---|
| 1 | `"512"` | | | |
| 2 | `"512"` | 200 | | |
| 3 | `"512"` | 200 | 312 | |
| 4 | `"512"` | 250 | 312 | |
| 5 | `"512"` | 250 | 312 | `312 250` |
| 6 | `"512"` | 250 | 312 | `512512` |

**4. (3)** 35: `OK` then `Checked`. 90: `Full` then `Checked`. 20: `Plug in` then `Checked` (20 is not greater than 20). Half marks if `Checked` is missing throughout.

**5. (3)** Three times (1).

```text
Checking CPU
Checking RAM
Checking SSD
3 parts checked
```

**6. (4)** a. Run-time: `Report starting` printed first, then a traceback. b. Line 4. c. `+` can't join a string and an integer; `cores` is an `int`. d. `print("Cores: " + str(cores))`, `print("Cores:", cores)`, or `print(f"Cores: {cores}")`.

**7. (6)** One mark for the kind, one for the reason. a. Syntax: nothing ran, so Python found it while compiling. b. Logic: no error message, but the output is wrong (512 GB is about 512,000 MB). c. Run-time: some output, then it stopped while running.

**8. (2)** `Threads: 44`. `input()` gives the string `"4"`, and `*` repeats a string.

## Part 2 (16)

**9. (3)** Line 1: RAM. Line 2: RAM and CPU (fetch, divide, store). Line 3: RAM, CPU, screen.

**10. (2)** On the storage drive. In RAM (until the program ends).

**11. (2)** Source code is the program as people write it, as text. Machine code is the numbered instructions a CPU actually runs, specific to its CPU family.

**12. (4)** A compiler translates a whole program ahead of time into machine code (an executable) that runs later (1). An interpreter reads a program and carries it out as it goes (1). Python compiles the whole file to bytecode first, which is why a syntax error on the last line stops every line from running (1); then it interprets the bytecode one instruction at a time (1).

**13. (3)** Half a mark each. Applications: Chrome, Thonny. Languages: Python, JavaScript. Operating systems: Android, Windows.

**14. (2)** `"sample-folder"` is a relative path, looked up from the current folder. From the terminal, the current folder is `ics3u`, which contains `sample-folder`. Double-clicking starts the program in `toolkit`, which doesn't.

## Part 3 (14)

**15. (8)** Two `input()`s (1); `int()` on the tab count (1); correct calculation (1); f-strings (1); labels padded to one width (2); gigabytes with `:.1f` (1); runs without error (1).

```python
name = input("Your name? ")
tabs = int(input("How many browser tabs are open? "))
ram_mb = tabs * 150
print(f"{'User:':<12}{name}")
print(f"{'Tabs:':<12}{tabs}")
print(f"{'RAM used:':<12}{ram_mb / 1000:.1f} GB")
```

With `Sam` and `40`:

```text
User:       Sam
Tabs:       40
RAM used:   6.0 GB
```

**16. (6)** Two problems.

1. **Syntax error (2):** line 4 is missing its closing `)`. Python shows `SyntaxError: '(' was never closed` and nothing runs (1 for finding and fixing, 1 for the kind and what Python shows).
2. **The price is never converted (4):** `input()` gives the string `"24.99"`. Line 3 doesn't crash, it repeats the string (`"24.9924.99"`), and line 4 then stops with `ValueError: Unknown format code 'f' for object of type 'str'`, a **run-time** error. Fix: `price = float(input("Price of the part? "))`. One mark each: finding it, the fix, naming it a run-time error (accept "logic error on line 3" if explained), and explaining why line 3 doesn't crash.

Fixed program output with `24.99`: `Total: 49.98`.

**Bonus (2):** RAM: each tab holds its page in memory, and when RAM runs out the computer swaps to the much slower drive.
