# ICS3U: Introduction to Computer Science

A complete teacher website for Ontario **ICS3U — Introduction to Computer Science, Grade 11, University Preparation** (2008 curriculum). It provides lessons, readings, code examples, worksheets, quizzes, and tests in Python, with an emphasis on reading code before writing it.

Website: <https://pbeens.github.io/ics3u/> · Repository: <https://github.com/pbeens/ics3u>

Both the website and this repository are public. Tests, quizzes, and answer keys live in a local `private/` folder that is git-ignored and never pushed; back it up separately.

## Feedback

Feedback, corrections, and suggestions are appreciated. Use the "Report an error or suggest a change" link on any page of the site, or [open an issue](https://github.com/pbeens/ics3u/issues/new?template=feedback.yml). Please don't post assessment answers in issues; they're public.

## Folders

- [references/](references/README.md) — the official curriculum and other source material.
- [project-docs/](project-docs/README.md) — teaching approach and project notes.
- [site/](site/README.md) — Quarto source for the public website.
- `private/` — tests, answer keys, and teacher-only material. Local only: git-ignored, never pushed or published.
- [notebooks/](notebooks/README.md) — every example program as a Jupyter notebook, with Open in Callysto | Colab links.
- [scripts/](scripts/README.md) — shared utilities, e.g. the notebook generator.
- [.github/](.github/README.md) — the feedback issue form.
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

After changing example programs, run `python3 scripts/build_notebooks.py` to refresh `notebooks/`.

Commit the updated `docs/` folder. GitHub Pages serves it from the `docs/` folder of the default branch.

## License

[MIT](LICENSE) for this project's own lessons, code, and materials. The Ministry of Education curriculum documents in `references/official-curriculum/` are not covered; they remain the property of the King's Printer for Ontario.
