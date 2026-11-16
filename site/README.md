# Site

Quarto source for the public ICS3U teacher website. Everything here is published.

- `_quarto.yml` — site settings and navigation.
- `index.qmd` — home page: quick start and lesson list.
- `how-a-lesson-works.qmd` — for teachers: who each piece is for, and the before / during / after class cycle.
- `about.qmd` — course philosophy, lesson structure, research, feedback, and license.
- `_extensions/lesson-tools/` — `{{< lesson-code >}}` (code downloads and notebook links) and `{{< feedback >}}` (Feedback section) shortcodes for lesson pages.
- `_feedback.html` — adds "Report an error or suggest a change" links that open the GitHub feedback form with the page filled in.
- `before-you-begin.qmd` — teacher setup: a local Python computer for demonstrations and for students, with online options as backups.
- `scope-and-sequence.qmd` — modules, hours, the spiral table, expectation coverage, and assessment overview.
- `modules/` — one folder per module: `index.qmd` (overview, for teachers), lesson plans (for teachers), slide decks (for the class), `practice.qmd` and `assignment.qmd` (for students), and `examples/` (program files; `lLL_*.py` per lesson, `mMM_*.py` for module assignments).
- `_extensions/r-wasm/live/` — the [quarto-live](https://github.com/r-wasm/quarto-live) extension: runnable Python in the browser (Pyodide). Installed with `quarto add r-wasm/quarto-live`.
- `_extensions/stepper/` — project shortcode for the predict-and-step box: prediction box, line-by-line stepping, output, and variables, running in the browser (Pyodide).
- `_extensions/pytutor/` — project shortcode that embeds a Python file in a [Python Tutor](https://pythontutor.com) visualizer (only for programs that use modules Python Tutor allows).
- `_scripts/sync_docs.py` — copies the build into `../docs/` after each render.
- `.nojekyll` — copied into `docs/` on every build so GitHub Pages serves Quarto's output as-is.

## Build

From the project root:

```sh
quarto preview site   # live preview
quarto render site    # build, then copy into ../docs/
```

Quarto builds into `_site/` (ignored by Git). After each render, `_scripts/sync_docs.py` replaces `../docs/` with an exact copy of `_site/`, so stale pages never linger on the published site.

## Lesson Files

Each lesson in `modules/module-NN-name/` has:

- `lesson-NN-name.qmd` — the lesson page (`format: live-html`).
- `lesson-NN-name-slides.qmd` — the slide deck (`format: live-revealjs`, `theme: default`, `toc: false`).
- `examples/*.py` — every example program, run and tested before publishing. Step-through boxes and Python Tutor embeds read these files directly. File names are `lLL_name.py` (lesson number first); `scripts/build_notebooks.py` mirrors each one into `../notebooks/`.

Answer keys for each lesson go in `../answer-keys/module-NN-name/`.

## Interactive Code

- **Runnable code:** a code block marked `{pyodide}` becomes an editor with a **Run Code** button. Python runs in the browser, in a small virtual computer (it reports `Emscripten`, `wasm32`, one core). The first run downloads about 10 MB.
- **Predict and step:** `{{< stepper file="examples/l01_computer_report.py" >}}` shows the file with a prediction box and Step / Back / Run all / Start over buttons. Python runs in the browser, so `platform` and other standard modules work. Colours: yellow with an arrow = next line, green = just ran, red = stopped with an error. It does not support `input()` yet.
- **Python Tutor:** `{{< pytutor file="examples/....py" height="500" >}}` embeds a file in Python Tutor (Python 3.11). It needs internet access, runs code on Python Tutor's server, and rejects many modules (including `platform`, `os`, and `shutil`).
- **Teacher prompts:** on lesson pages use `::: {.callout-tip title="Teacher prompt"}`; on slides put the prompt in speaker notes. See [../project-docs/teaching-approach.md](../project-docs/teaching-approach.md).
- Pages and decks that use `{pyodide}` blocks must set `engine: markdown` so Quarto does not try to run them with Jupyter at build time.

## Rules

- Only `.qmd` files are rendered, so README files like this one are not published.
- Never put answer keys, marking notes, or teacher-only notes here; they go in `../answer-keys/`, and the site never links to them.
- Lessons follow [../project-docs/teaching-approach.md](../project-docs/teaching-approach.md): reading code comes before writing code.
- Use lowercase kebab-case names, e.g. `modules/module-01-about-this-computer/lesson-01-ask-the-computer.qmd`.
- Links that leave the site always open in a new tab, with a small external-link icon (`link-external-newwindow` and `link-external-icon` in `_quarto.yml`). Write external links as normal Markdown links; no extra markup is needed.
- Shared theme options live at the top level of `_quarto.yml` so they apply to both `html` and `live-html` pages; slide decks override `theme` and `toc` in their own front matter.
