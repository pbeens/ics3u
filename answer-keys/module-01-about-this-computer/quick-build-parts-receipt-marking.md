# Quick Build: Parts Receipt — Marking Notes

**Module 1, after Lesson 5** · **Expectations:** A1.1, A2.1, A4.2

Teacher-only. Do not publish or link from the site.

## Quick checklist

| Requirement | Look for |
|---|---|
| Header comment | Name, date, what the program does |
| Three parts | Name, price, quantity for each, in clearly named variables |
| Calculated totals | Line totals, subtotal, tax, and total computed by the program. Typed-in totals (e.g. `print("69.98")`) don't count |
| Constant | `TAX_RATE` in capitals; used for the tax |
| Two decimal places | `:.2f` (or `round(x, 2)` plus formatting) on every amount |
| Lined up | Right-aligned numbers, decimal points in one column |
| Output comment | Output pasted at the bottom |

## Levels

- **Level 3:** all requirements met, totals correct.
- **Level 4:** also cleanly aligned, with realistic parts and prices. Extra credit in your judgement for students who notice and explain a one-cent rounding difference.
- **Level 1–2:** runs, but totals typed in or wrong, missing the constant, or amounts not to two decimal places.

## Common slips

- Prices stored as strings (`"34.99"`): `*` repeats them, or `TypeError`.
- Tax calculated on one item, or added before the subtotal.
- `:.2f` on some amounts but not others (often the tax).
- Left-aligned numbers, so decimal points don't line up.
- Total computed from rounded values in some places and unrounded in others: accept, but it can produce a cent's difference.

## Sample solution

```python
# Parts Receipt (Quick Build, Module 1 Lesson 5)
# Name: Sample Solution
# Date: 2026-11-21
# Prints a receipt for computer parts: line totals, subtotal, HST, and total.

TAX_RATE = 0.13  # Ontario HST

ram_name = "8 GB RAM stick"
ram_price = 34.99
ram_quantity = 2

ssd_name = "1 TB SSD"
ssd_price = 89.99
ssd_quantity = 1

cable_name = "USB-C cable"
cable_price = 12.49
cable_quantity = 3

ram_total = ram_price * ram_quantity
ssd_total = ssd_price * ssd_quantity
cable_total = cable_price * cable_quantity

subtotal = ram_total + ssd_total + cable_total
tax = subtotal * TAX_RATE
total = subtotal + tax

print(f"{'PARTS RECEIPT':^40}")
print("-" * 40)
print(f"{'Item':<18}{'Qty':>4}{'Price':>9}{'Total':>9}")
print(f"{ram_name:<18}{ram_quantity:>4}{ram_price:>9.2f}{ram_total:>9.2f}")
print(f"{ssd_name:<18}{ssd_quantity:>4}{ssd_price:>9.2f}{ssd_total:>9.2f}")
print(f"{cable_name:<18}{cable_quantity:>4}{cable_price:>9.2f}{cable_total:>9.2f}")
print("-" * 40)
print(f"{'Subtotal':<31}{subtotal:>9.2f}")
print(f"{'HST (13%)':<31}{tax:>9.2f}")
print(f"{'TOTAL':<31}{total:>9.2f}")
```

Output:

```text
             PARTS RECEIPT
----------------------------------------
Item               Qty    Price    Total
8 GB RAM stick       2    34.99    69.98
1 TB SSD             1    89.99    89.99
USB-C cable          3    12.49    37.47
----------------------------------------
Subtotal                          197.44
HST (13%)                          25.67
TOTAL                             223.11
```
