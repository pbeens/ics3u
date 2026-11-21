# Tasks

## Current Focus

### Module 1, Lesson 3: Getting Output Right (started 2026-11-21)

The seven-module plan is approved (`decisions.md`, 2026-11-21). Lesson 3 is the first lesson built to the new rules: a practical opening problem, reading first, and a Quick Build (System Banner) as its Make product.

- [ ] Example programs in `examples/` (`l03_*.py`), each run on Python 3 before publishing
- [ ] Lesson plan `lesson-03-getting-output-right.qmd` (75 min; For teachers banner, At a Glance, teacher prompts for `sep`, `end`, and escape characters)
- [ ] Slides `lesson-03-getting-output-right-slides.qmd`
- [ ] Practice section for Lesson 3, and the System Banner Quick Build page
- [ ] Answer key in `answer-keys/module-01-about-this-computer/`
- [ ] Module 1 overview, sidebar, and Scope and Sequence links; Lesson 2 → Lesson 3 Previous/Next
- [ ] Rebuild notebooks; render; check links, steppers, and slides in headless Chrome

### Next

1. Build `make_sample_folder.py` (planned for `site/tools/`): standard library only; fixed and per-student seeds; safe reset; optional `--download` from files hosted on the site. Needed by Module 1 Lesson 6.
2. Quizzes for Lessons 1–2, in `answer-keys/module-01-about-this-computer/` (public in the repo, off the site).
3. Documents for written work: Word (`.docx`) and fillable PDF versions of longer written parts. Recommendation: Quarto's `docx` output from the same source (uploads to Drive convert to Google Docs); fillable PDFs only for fixed forms such as the test plan table. Decide before Module 2's assignment.
4. Confirm the Colab values in Lesson 1's teacher notes by running the program in Colab (needs the author's account).
5. After the next push, test the notebook Open in Callysto | Colab links.
6. As modules are built: remove "(planned)" labels and Draft callouts; give each module a sidebar like Module 1's; check network lessons against school IT constraints.

### Later

- From the audits: screen-reader duplication in line-highlight fragments; skip link; wide tables on phones (rubric, Scope and Sequence); expectation-code glosses; one practice page per lesson (decide when Lesson 3's practice is added); dark-mode check of steppers and live editors; cycle diagram at 390 px.
- Lesson plans name the `answer-keys` folder in plain text (no link). Confirm that's wanted.

## Open Questions

- **Idea to consider (2026-11-18): two tracks.** Track 1 (current plan) builds computer-related utilities. Track 2 would teach the same ideas through creating media and art, the way Turing graphics did for Ontario beginners. Notes for discussion:
  - Standard-library options: `turtle` (closest to Turing's drawing commands), `tkinter` Canvas (shapes, animation, simple games), writing SVG files as plain text (they open and edit in Inkscape), and generating sound with the `wave` module. Third-party options as extensions: Pillow (images), pygame-ce (games and animation), py5 (Processing-style).
  - Fits the curriculum well: pixels, colour codes, and image and sound file sizes cover A1.2 (data representation); graphics cards and monitors connect to C1.
  - MCP: the official Python MCP SDK makes small MCP servers possible, but MCP connects an AI assistant to an app, so it suits a Module 7 project or extension more than core lessons. For students' own code to control an app directly, the app's scripting interface (e.g., Inkscape's command line and Python extensions) is simpler. Candidate apps: the ArtCraft suite (e.g., PhotoCraft, a Photoshop alternative, and an Illustrator alternative) and Affinity; check which have MCP servers or scripting interfaces.
  - Cost: two full tracks doubles the materials. A lighter version keeps shared lessons and skills, and gives each module a Track 1 and a Track 2 anchor program and assignment.
  - Parked for now because of the extra work. If pursued, it may live in a separate GitHub repository rather than this one.

- (Resolved 2026-11-21: Module 5, On the Network.) Networking projects: the author wants programming projects about computer networks (e.g., programs that report the computer's address and name). Decide whether and where they fit in the scope and sequence. Resources:
  - [netsim](https://cs.uwaterloo.ca/~m2mazmud/netsim/) (University of Waterloo): a browser game about how packets move across the Internet. Suggested on the ACSE list (2026-11-16) for Grade 10s.
  - [errorinn/netsim](https://github.com/errorinn/netsim): its source code, MIT licensed, written in PHP, last updated 2020. A school can host its own copy. The public site slows down when a whole class registers at once, which could also be a teaching point about server load.

- How worksheets reach Google Docs: see the Documents task above (Word and fillable PDF, 2026-11-18).
- Whether the GitHub account has Pro (needed for Pages from a private repository; free for verified teachers through GitHub Education).
- This Mac has a global Jupyter kernel pointing to a missing environment (`/Volumes/Extreme-SSD/.../.venv`). Lesson pages avoid it with `engine: markdown`, but it may affect other Quarto projects.

## Recently Completed

- 2026-11-21: Author approved the seven-module plan (all five open points).
- 2026-11-19: Round 2 audit fixes (`audits/audit-response_2.md`): assignment file names, Lesson 2 Make time, Make filenames on slides, Quick Builds as lesson Make products, a work period in Modules 1–6 (five lesson merges), World on-ramps, Previous/Next on every page, open-computers lead line, Module 1 sidebar replacing the Module 1 menu.
- 2026-11-18: Planned overview pages for all seven modules and Computer Science in the World; Scope and Sequence for seven modules; Skill Builders, Quick Builds, toolkit thread; open-computers messaging; private feedback link in the margin; tracing notebooks and `.py` comments for answers; course folder page and Handing In Work section.
- 2026-11-16: Round 1 audit fixes (`audits/audit-response.md`): Lesson 1 Compare and Make slides, Lesson 2 variable-change stepper, slide footers, speaker notes, trace-table rule, practice and assignment layout, Previous/Next on lesson pages; `private/` renamed `answer-keys/` and tracked.

- 2026-11-16: Research references (About page and `teaching-approach.md`) expanded to full APA 7 with DOI links, after Grok's reference audit (`audits/references-audit.md`); all details confirmed against Crossref. In-text citations for three or more authors now use "et al.".

- 2026-11-15: Overviews, practice, and assignments. New How a Lesson Works page (who each piece is for; before, during, and after class; cycle diagram). Lesson plans now open with a "For teachers" banner and At a Glance summary, and gain an After the Lesson section. New Module 1 overview, student Practice page (Lessons 1–2, reading first, interactive, code tables without exit tickets), and draft Module 1 Assignment (Computer Report Card) with rubric. Slides end with an "After class" slide. Getting Started and Module 1 menus reorganized by audience. Private answer keys for practice and the assignment. New example programs run and verified.

- 2026-11-15: Lessons now end with "Code for This Lesson" (`.py` downloads, notebooks, Open in Callysto | Colab, via `{{< lesson-code >}}`) and "Feedback" (`{{< feedback >}}`) sections; added a Buy Me a Coffee link (top right); Ontario Computers for Schools link and a "Who This Course Is For" section on About.

- 2026-11-15: Repo published at github.com/pbeens/ics3u. Found `private/` (answer keys) had been pushed; added it to `.gitignore` and untracked it locally (history rewrite pending author approval). Added MIT LICENSE; feedback issue form plus per-page "Report an error or suggest a change" links prefilled with page title and URL (verified in headless Chrome on all pages); Open in Callysto | Colab links in every notebook. Slimmed the home page to quick-start cards and a lesson table; moved philosophy, research, feedback, and license to a new About page. Added a VS Code and agentic programming section to Before You Begin.

- 2026-11-15: Added `notebooks/`: every example program mirrored as a read-first Jupyter notebook (`MM-LL-name.ipynb`), generated by `scripts/build_notebooks.py`. All 7 Module 1 notebooks validated with nbformat and their code run.

- 2026-11-15: Added the Before You Begin page (teacher setup): a local Python demonstration computer; student computers in order of preference (real computers, refurbished, Raspberry Pi); Colab and Callysto Hub as backups, with why online Python reports a different machine; pre-Lesson 1 checklist. Linked from the navbar, home page, and Lesson 1 teacher notes.

- 2026-11-14: Built the predict-and-step box (`stepper` shortcode) and replaced Python Tutor and the separate Predict/Run sections in Lessons 1–2 with it; it runs the real programs, including `platform`. Added teacher prompts (step-through colours, Variables panel, reading an error) on lesson pages and in slide notes. Fixed the hidden source showing on slides and widened the code panel. All steppers verified in headless Chrome on pages and slides.

- 2026-11-14: Rebuilt Lesson 1 around `platform` only (one line → labelled report → where code runs: classroom, browser, Colab) and added Lesson 2, Exploring the platform Library (`dir()`, documentation, variables, Python Tutor trace, reading errors). New tested examples, slides, and private answer keys for both; every code cell verified in headless Chrome. Moved `os` and `shutil` to Module 2 in the scope and sequence.

- 2026-11-14: Built Module 1, Lesson 1 (lesson page, Reveal.js slides, tested example programs, private answer key). Installed quarto-live for runnable Python and added a `pytutor` shortcode for Python Tutor (Python 3.11). Verified both in headless Chrome: code cells run and print correct output; Python Tutor loads the example. Added a Module 1 menu to the site.
- 2026-11-14: Rewrote the scope and sequence as a spiral of six themed modules plus Computer Science in the World; added a spiral table (read, modify, write, design); coverage of all 57 expectations and 110 hours verified by script.
- 2026-11-14: Drafted the first scope and sequence, removed the unreliable `sections/` extraction, and switched the site build to render into `site/_site/` and mirror into `docs/`.
- 2026-11-14: Created `ics3u-expectations.md` (14 overall, 57 specific expectations), checked against PDF pages 39–46.
- 2026-11-14: Project initialized; curriculum PDF copied into `references/official-curriculum/`; teaching approach documented.
