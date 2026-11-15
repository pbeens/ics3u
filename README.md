# ICS3U: Introduction to Computer Science

A complete teacher website for Ontario **ICS3U — Introduction to Computer Science, Grade 11, University Preparation** (2008 curriculum). It provides lessons, readings, code examples, worksheets, quizzes, and tests in Python, with an emphasis on reading code before writing it.

The website is public. This repository is private and also holds material that must not be published, such as tests and answer keys.

## Folders

- [references/](references/README.md) — the official curriculum and other source material.
- [project-docs/](project-docs/README.md) — teaching approach and project notes.
- [site/](site/README.md) — Quarto source for the public website.
- [private/](private/README.md) — tests, answer keys, and teacher-only material. Never published.
- `docs/` — the built website served by GitHub Pages. Generated; do not edit.

## Project Files

- [AGENTS.md](AGENTS.md) — instructions for people and AI agents working here.
- [tasks.md](tasks.md) — current work and next steps.
- [decisions.md](decisions.md) — key decisions and why they were made.
- [prompts.md](prompts.md) — log of project requests.

## Building the Site

Requires [Quarto](https://quarto.org/).

```sh
quarto preview site   # live preview while editing
quarto render site    # build into docs/ for publishing
```

Commit the updated `docs/` folder. GitHub Pages serves it from the `docs/` folder of the default branch.
