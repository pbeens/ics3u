# Module 1, Lesson 8 — Answers

**Lesson:** Inside the Computer: RAM and CPU · **Expectations:** A1.1, C1.1, C1.4

Teacher-only. Do not publish or link from the site.

Byte counts below are for 64-bit CPython 3.11 on a classroom computer. The web page (32-bit WebAssembly) gives smaller numbers.

## Review

1. Python compiles the whole file before running any of it, and the syntax error stops the compiling.
2. `LOAD`: fetch a value (from memory). `STORE`: save a value under a name (in memory).

## Predict, Then Step (`l08_ram_cpu.py`)

| Line | Components |
|---|---|
| 1 `cores = 8` | RAM (stores 8 as `cores`) |
| 2 `speed_ghz = 3.2` | RAM |
| 3 `total_ghz = cores * speed_ghz` | RAM → CPU (multiplies) → RAM (stores `total_ghz`) |
| 4 `print(...)` | RAM → CPU → screen (via the operating system and video card) |

Output: `Total: 25.6 GHz`

## Investigate: How Big Is a Value? (`l08_sizes.py`)

Classroom computer (64-bit):

```text
8: 28 bytes
8 with 21 zeros: 36 bytes
3.2: 24 bytes
'8': 50 bytes
'LAB-PC-14': 58 bytes
```

Web page (32-bit): 16, 24, 16, 22, and 30 bytes. The same patterns hold.

1. `'8'` (50) is bigger than `8` (28): a string stores extra information (its length, how its characters are encoded) as well as the characters.
2. 8 bytes more, for 8 extra characters: one byte per extra ASCII character.
3. The web page runs in a 32-bit virtual computer (WebAssembly), which uses smaller pieces of memory for each value's extra information.

## Investigate: Where Is It? (`l08_ids.py`)

Example output (numbers vary every run):

```text
4369166832 4369166832
4369170096 4369166832
2000 1000
```

1. Both names point to the same value in RAM.
2. A new value, 2000, was stored somewhere else in RAM, and the name `cores` now points there.
3. `backup` still points to the old value. Giving `cores` a new value doesn't change `backup`.

## Investigate: Which Part Would You Upgrade?

1. RAM. 2. CPU (and, for some editing software, the video card). 3. Storage drive (bigger, or clean it up). 4. Video card. 5. Power supply.

## Modify

1. `"LAB"` is 52 bytes, `"LAB" * 10` is 79, `"LAB" * 100` is 349: 49 bytes plus one per character.
2. `"🖥"` is 80 bytes, much more than `"A"` (50): Python stores strings with characters outside ASCII using more bytes per character. Module 4 explains.
3. Yes: `True` and `1` are both 28 bytes. (A Boolean is a special kind of integer in Python.)

## Make (`receipt_traced.py`)

Look for: assignments labelled RAM; calculations labelled CPU with values fetched from RAM and the answer stored in RAM; `print` lines including the screen. Top comment: the drive when off; copied into RAM when it starts; the CPU carries out the instructions while values live in RAM.

## Exit Ticket (`l08_exit_ticket.py`)

1. Line 1: RAM. Line 2: CPU (multiplies) and RAM (fetches `ram_gb`, stores `upgraded`). Line 3: RAM, CPU, screen.
2. `parts_receipt.py` is on the storage drive. The value of `ram_total` is nowhere: it only existed in RAM while the program ran.
