# Module 1, Lesson 5 — Answers

**Lesson:** Values and Types · **Expectations:** A1.1, A2.1, A4.3, A4.4

Teacher-only. Do not publish or link from the site.

The web page runs a newer Python than many classroom computers; version numbers below will differ.

## Review

1. `[··arm64]` (two spaces, then the five letters).
2. The `f` is missing before the opening quotation mark.

## Predict, Then Step (`l05_types.py`)

```text
88
16
<class 'int'> <class 'float'> <class 'bool'> <class 'str'>
```

1. Line 3 joins two strings (`"8"` and `"8"`), giving `88`. Line 6 adds two integers, giving `16`.
2. After line 4, `ram` holds the integer `8`. The panel shows `'8'` (quotation marks: a string) before and `8` (no quotation marks: an integer) after.
3. See the last output line above. `ram` is an `int` by then, because line 4 replaced the string.

## Investigate: Calculating (`l05_arithmetic.py`)

```text
Total RAM: 16 GB
Per stick: 8.0 GB
Three drives: 269.96999999999997
Three drives: $269.97
```

1. `/` always gives a float.
2. 89.99 can't be stored exactly in binary, so the product has a tiny error. Python's arithmetic is correct for the numbers it actually stores.
3. Shows the value as a float rounded to two decimal places.

## Investigate: Same Fact, Different Types (`l05_version_numbers.py`)

Example with Python 3.11.4:

```text
3.11.4 <class 'str'>
11 <class 'int'>
Next version: 3.12
New enough for this course: True
```

1. `python_version()` gives a `str`; `version_info.minor` gives an `int`.
2. `+` can't join a string and an integer; `str(minor + 1)` turns the number into text first. Without it: `TypeError`.
3. `bool`. It's asking "is the minor version 8 or more?"

## Investigate: Spot the Problem

**Program A (`l05_mistake_concat.py`):** run-time error (`Checking memory` printed first). `TypeError: can only concatenate str (not "int") to str`: `+` can't join a string to an integer. Fixes: `print("RAM: " + str(ram_gb) + " GB")` or `print(f"RAM: {ram_gb} GB")`.

**Program B (`l05_mistake_repeat.py`):** prints `Total: 49.9949.99`. `*` with a string and an integer repeats the string. Fix: `price = 49.99`, or `float(price) * quantity` (gives `99.98`).

## Modify

```python
print(f"Mouse x {quantity}: {line_total:.2f}")
print(f"HST: {line_total * TAX_RATE:.2f}")
print(f"Total with HST: {line_total * (1 + TAX_RATE):.2f}")
```

With quantity 2: `49.98`, `6.50`, `56.48`. With quantity 3: `74.97`, `9.75`, `84.72`. Every line that uses `line_total` changes; the code itself only changes on line 3.

## Exit Ticket (`l05_exit_ticket.py`)

```text
555
15
<class 'float'>
```
