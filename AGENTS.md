# AGENTS.md — ICS3U: Introduction to Computer Science

## Purpose

Build a complete, public teacher website for Ontario ICS3U (Grade 11 Introduction to Computer Science, University Preparation, 2008 curriculum): lessons, readings, code examples, worksheets, quizzes, and tests aligned to the curriculum expectations.

## Scope and Deliverables

- Quarto website: source in `site/`, built to `docs/`, published with GitHub Pages.
- Editable worksheets and assessments, distributed as Google Docs.
- Python 3 is the primary language; other languages appear only as clearly marked extensions.

## Folder Map

- `references/official-curriculum/` — Ministry PDF, raw extraction, verified expectations.
- `project-docs/` — teaching approach, lesson template, style and process notes.
- `site/` — Quarto source for everything published. Public.
- `notebooks/` — every example program mirrored as a Jupyter notebook (`MM-LL-name.ipynb`). Generated; not published.
- `.github/` — the feedback issue form.
- `scripts/` — shared utilities, e.g. `build_notebooks.py`.
- `answer-keys/` — answer keys, marking notes, teacher-only notes. In the public repository, but never on the website.
- `docs/` — generated site. Never edit by hand; `quarto render site` overwrites it.

## Rules for Agents

- Read this file first, then `tasks.md`. Check `decisions.md` before consequential changes.
- Keep this file concise and durable. Do not turn it into a session log or changelog.
- Store active plans and changing tasks in `tasks.md`.
- Record program-related user prompts in `prompts.md`: newest first, paraphrased, with timestamp, goal, summary, hostname, and agent.
- Record new durable decisions in `decisions.md`.
- For non-trivial work, write a short plan in `tasks.md` and get approval before substantial or structural changes. Update `tasks.md` after verifying the work.
- Ask before major structural changes.

## Reading First (Core Principle)

Students read code before they write code. This applies to every lesson, worksheet, and assessment:

- Each new concept is met first through reading, tracing, and predicting existing code.
- Writing new code from scratch comes last, after the reading and modifying stages.
- Every worksheet opens with code-reading tasks; every quiz and test includes a code-reading and tracing section.
- Add a teacher prompt (what the teacher says aloud) the first time students meet a tool or idea; see the teaching approach.
- Spiral, not silos: modules are built around themes and anchor programs, and introduce many ideas early through reading; do not organize content as one-construct units.
- Start deep: prefer authentic, interesting examples over toy ones (e.g., the first `print()` program reports the computer's own hardware, not "Hello, World"), and tie them to other expectations where it fits.
- Full details and the lesson template: [project-docs/teaching-approach.md](project-docs/teaching-approach.md).

## Audiences

- Lesson plans (one page per lesson) are for teachers: they open with a "For teachers" banner and an At a Glance summary.
- Students use the slides, the `.py` files and notebooks, and each module's Practice and Assignment pages. Keep exit tickets off student pages.
- See [site/how-a-lesson-works.qmd](site/how-a-lesson-works.qmd) and the lesson template in [project-docs/teaching-approach.md](project-docs/teaching-approach.md).

## Curriculum Alignment

- Take expectation codes and wording only from `references/official-curriculum/ics3u-expectations.md`, never from the raw `sections/` extraction.
- Tag every lesson, worksheet, and assessment with the expectation codes it addresses.
- Do not publish Ministry text on the site beyond short expectation quotations.

## Public vs Private

- Anything in `site/` is published on the website. Never place answer keys, solutions, marking notes, or teacher-only notes there, and never link to them from the site.
- The GitHub repository (https://github.com/pbeens/ics3u) is public, including `answer-keys/`. The author accepts that answer keys are visible in the repo; they just stay off the website. Lesson plans may name the folder in plain text (no link) so teachers can find it.
- Quizzes and tests that must stay secret have no home yet; ask before creating one.
- The project is MIT licensed ([LICENSE](LICENSE)); Ministry documents in `references/official-curriculum/` are excluded.
- Every site page gets a "Report an error or suggest a change" link (from `site/_feedback.html`) that opens the GitHub feedback form (`.github/ISSUE_TEMPLATE/feedback.yml`) with the page filled in.

## Code Examples

- Every code example must run on Python 3 exactly as shown. Run it before publishing.
- Keep each lesson's example programs as files in the module's `examples/` folder; step-through boxes (`{{< stepper >}}`) and Python Tutor embeds read them directly. See [site/README.md](site/README.md) for runnable code and visualizer conventions.
- After adding or changing an example program, run `python3 scripts/build_notebooks.py` to refresh `notebooks/`. Never edit the notebooks by hand.
- Keep reading examples short enough to trace by hand.

## Conventions

- Lowercase kebab-case for files and folders (e.g. `unit-02-selection/`).
- Canadian spelling.
- Every new folder gets a short `README.md`; link new documents from the nearest index.
- Shared utilities go in `scripts/`; reusable agent workflows go in `skills/` (create it only when needed).
- When a task recurs (e.g. building a lesson), propose a `skills/` workflow for it.
- Update the relevant README and this file when structure changes.

> [!NOTE]
> This project was initialized using the agentic master prompt provided by [AgenticProjectInitializer](https://github.com/pbeens/AgenticProjectInitializer/blob/main/master-prompt.md).
