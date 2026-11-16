# Module 1, Lesson 1 — Answers

**Lesson:** Ask the Computer About Itself · **Expectations:** A2.2, A3.1, C1.1

Teacher-only. Do not publish or link from the site.

## Teach

`print(platform.machine())` prints one word, e.g. `arm64` on an Apple silicon Mac or `AMD64` on a Windows PC with an Intel or AMD processor.

## Predict, Then Run

1. Three lines.
2. `CPU type:`, `Operating system:`, and `Computer name:` appear exactly as written.
3. The values after each label depend on the computer. For example, on an Apple silicon Mac:

```text
CPU type: arm64
Operating system: Darwin
Computer name: (the Mac's name)
```

Common errors to listen for:

- Predicting the code itself as output, e.g. `CPU type: platform.machine()`.
- Leaving out the space Python adds between comma-separated items.

## Investigate: Where Does My Code Run?

| | Classroom computer | This web page | Google Colab |
|---|---|---|---|
| CPU type | e.g. `arm64`, `x86_64`, `AMD64` | `wasm32` | typically `x86_64` |
| Operating system | e.g. `Darwin`, `Windows`, `Linux` | `Emscripten` | `Linux` |
| Computer name | the computer's name | `emscripten` | a random-looking machine ID |

Run the program in Colab before class to confirm its current values.

1. The web page runs Python inside the browser, in a small virtual computer (WebAssembly). It is not describing the classroom computer, although it runs on it.
2. Only the classroom computer (Thonny, IDLE, or VS Code) and, underneath, the web page. Colab runs elsewhere.
3. (If Colab was shown) Colab describes a Google server in a data centre, owned by Google.

## Modify

- Changing labels changes only the fixed text.
- `print("Python version:", platform.python_version())` adds a line such as `Python version: 3.11.4` (the browser reports its own Python version, e.g. `3.13.2`).
- Swapping two `print()` lines swaps the order of the output lines; the values stay the same.

## Make

```python
import platform

print("Operating system:", platform.system())
print("Version:", platform.release())
```

## Exit Ticket

```text
Report
CPU: AMD64
```

Accept `x86_64` with a note: Windows reports Intel and AMD processors as `AMD64`.
