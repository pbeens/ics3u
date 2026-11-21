# Quick Build: System Banner — Marking Notes

**Module 1, after Lesson 3** · **Expectations:** A1.1, A2.1, A3.1, A4.2

Teacher-only. Do not publish or link from the site.

## Quick checklist

| Requirement | Look for |
|---|---|
| Header comment | Name, date, what the program does |
| Even box | Every box line the same length. Paste the output into a monospaced editor, or count; a jagged right edge is the most common slip |
| Blank line | `print()` or `\n` between box and facts |
| Four facts | Four different `platform` functions, each stored in a variable before printing, each labelled |
| Lined up | Values start in one column (tabs or spaces) |
| `sep`, `end`, escape | Each used at least once, and used sensibly (not `sep=" "` just to tick a box) |
| Output comment | Output pasted at the bottom |

## Levels

- **Level 3:** all requirements met.
- **Level 4:** also a polished, consistent design (aligned facts, sensible title, tidy names and comments). Don't reward length or ASCII art for its own sake.
- **Level 1–2:** runs but misses the box width, the variables, or two or more of `sep` / `end` / escape.

## Common slips

- Box lines differ by one character (usually the title line).
- Labels longer than 7 characters with one `\t`, so facts don't line up. Fine if they fixed it with a second tab or spaces.
- `print("Name:\t", name)`: the comma adds a space after the tab. Usually harmless (it still lines up when all lines do it).
- Trying to put `platform.node()` inside the box. The right edge only lines up on their own computer; acceptable, but point them to Lesson 4.

## Sample solution

```python
# System Banner (Quick Build, Module 1 Lesson 3)
# Name: Sample Solution
# Date: 2026-11-21
# Prints a boxed title banner, then four facts about this computer.
import platform

name = platform.node()
system = platform.system()
release = platform.release()
cpu = platform.machine()
python = platform.python_version()

print("+==============================+")
print("|        SYSTEM BANNER         |")
print("|   Computer Science Lab 214   |")
print("+==============================+")
print()
print("Name:", name, sep="\t")
print("System:\t" + system, release)
print("CPU:\t" + cpu)
print("Python:\t" + python)
print("Banner printed", end="... ")
print("done")
```

Output on an Apple silicon Mac (tabs expanded):

```text
+==============================+
|        SYSTEM BANNER         |
|   Computer Science Lab 214   |
+==============================+

Name:   LAB-MAC-03
System: Darwin 25.3.0
CPU:    arm64
Python: 3.11.4
Banner printed... done
```
