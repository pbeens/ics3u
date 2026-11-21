# Module 1 Test: About This Computer

**Time:** 75 minutes · **Total:** 60 marks · **Expectations:** A1.1, A2.1, A2.2, A4.1, A4.3, A4.4, C1.1, C1.4, C2.1, C3.3, C3.4, C3.5

Teacher-only until the test is given. Answers: `module-01-test-answers.md`. To make an editable copy, paste into a Google Doc and add your school's header.

---

**Name:** ______________________ **Date:** ____________

Answer without running any code. When a question asks for output, write it **exactly**: spaces, capitals, and blank lines count. Show a space as a dot (`·`) where the question says so.

## Part 1: Reading and Tracing (30 marks)

**1.** Write the exact output. Show the tab as an arrow (→). **(3)**

```python
print("Lab", "PC", sep="-", end=" ")
print("14")
print()
print("Room:\t214")
```

**2.** Write the exact output, showing every space as a dot. **(3)**

```python
cpu = "x86_64"
cores = 6
print(f"[{cpu:<9}]")
print(f"[{cores:>4}]")
print(f"{'OS':^6}|")
```

**3.** Complete the trace table, then write the output. Every line that runs gets a row. **(6)**

```python
1  storage = "512"
2  used = 200
3  free = int(storage) - used
4  used = 250
5  print(free, used)
6  print(storage * 2)
```

| Line | `storage` | `used` | `free` | Output |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |

**4.** What does this print when `battery` is 35? When it's 90? When it's 20? **(3)**

```python
if battery > 80:
    print("Full")
elif battery > 20:
    print("OK")
else:
    print("Plug in")
print("Checked")
```

**5.** How many times does line 3 run? Write the exact output. **(3)**

```python
1  parts = ["CPU", "RAM", "SSD"]
2  for part in parts:
3      print("Checking", part)
4  print(len(parts), "parts checked")
```

**6.** A student runs a program and sees this: **(4)**

```text
Report starting
Traceback (most recent call last):
  File "/Users/sam/ics3u/toolkit/report.py", line 4, in <module>
    print("Cores: " + cores)
          ~~~~~~~~~~^~~~~~~
TypeError: can only concatenate str (not "int") to str
```

a. What kind of error is it: syntax, run-time, or logic? How do you know?
b. Which line caused it?
c. Explain the message in your own words.
d. Write a corrected line 4.

**7.** For each, name the kind of error (syntax, run-time, or logic) and explain how you can tell. **(6)**

a. Nothing prints at all, and the message says `SyntaxError: expected ':'`.
b. A storage converter prints `512 GB is 0.512 MB`.
c. The program prints two lines, then stops with `FileNotFoundError: [Errno 2] No such file or directory: 'toolkit'`.

**8.** A student types `4` when this runs. What does it print? Why? **(2)**

```python
cores = input("How many cores? ")
print("Threads:", cores * 2)
```

## Part 2: Inside the Computer (16 marks)

**9.** Label each line with the components it uses: RAM, CPU, and/or screen. **(3)**

```python
ram_gb = 16
per_stick = ram_gb / 2
print(per_stick)
```

**10.** When the computer is switched off, where is `report_card.py`? While the program runs, where is the value of `per_stick`? **(2)**

**11.** Explain the difference between source code and machine code. **(2)**

**12.** Explain the difference between a compiler and an interpreter. Then explain why Python can be described as both, using what happens when a program has a syntax error on its last line. **(4)**

**13.** Sort each into application, programming language, or operating system: Chrome, Python, Android, Thonny, Windows, JavaScript. **(3)**

**14.** A program in `ics3u/toolkit` runs `os.listdir("sample-folder")`. It works when started from the terminal in `ics3u`, but crashes when started by double-clicking it in `toolkit`. Explain why. **(2)**

## Part 3: Basics (14 marks)

**15.** Write a program that: **(8)**

- asks the user's name, and how many browser tabs they have open;
- works out the RAM the tabs use, at 150 MB per tab;
- prints three labelled lines with f-strings, with the labels padded to the same width so the values line up: the name, the number of tabs, and the RAM in gigabytes to one decimal place (1 GB = 1000 MB).

**16.** This program doesn't work. Find and fix every problem, name the kind of each error, and explain what Python would show for each one. The user types `24.99`. **(6)**

```python
price = input("Price of the part? ")
quantity = 2
total = price * quantity
print(f"Total: {total:.2f}"
```

**Bonus (2):** Which component would you upgrade for a student whose laptop slows down with many browser tabs open? Why?
