# Tasks

## Current Focus

### Audit follow-up (approved 2026-11-16; audits are in the git-ignored `audits/` folder)

Approved: the quick fixes, and the recommended options for Decision 1 (Lesson 1), Decision 2 (reassignment in Lesson 2), and Decision 5 (VS Code placement; later reduced to one sentence at the author's request). Item numbers match `audits/audit-response.md`.

**Done (verified in a fresh render and headless Chrome):**

- [x] D1 Lesson 1: new "Compare: where did it run?" slide (classroom vs. web page; Colab optional in notes), new Make slide; plan's Investigate trimmed to 10 min, Make now 10 min on the classroom computer (#1, #2)
- [x] D2 Lesson 2: new `l02_change_variable.py` stepper ("A variable can change", 5 min) on plan and slides, teacher prompt, learning goal; Teacher Note rewritten; Investigate 20 → 25 min (#3)
- [x] D5 Before You Begin: agentic section replaced by one sentence (VS Code is the editor to choose for experimenting with agentic programming)
- [x] #4 Slide footer "← Lesson N plan · Module 1" on both decks
- [x] #5 Speaker notes (`S`) and two-screen setup in How a Lesson Works and lesson plans
- [x] #6 Stepper on slides 0.5em → 0.6em; wasm32 note 0.6em, darker. Note: one long line now wraps on the Lesson 1 Predict slide; acceptable
- [x] #7 Trace tables have a line-1 "—" row and the rule "every line that runs gets a row" (Lesson 2, practice, assignment, answer keys)
- [x] #10 Stepper long lines wrap
- [x] #11 Practice: code-files tables moved to the end of each lesson's section
- [x] #12 Assignment Part A: numbered lines and a trace grid
- [x] #13 `examples/m01_report_card_starter.py` download (runs; one file to hand in)
- [x] #14 Banner now "Ready to use for Lessons 1–2"; #15 first-load note by the Part C box
- [x] #17 Suggested hand-in in each lesson plan's After the Lesson
- [x] #19 `site/styles.css`: `scroll-margin-top` (heading lands at 85 px, below the 61 px navbar)
- [x] #20 Cycle diagram now vertical with short labels (readable on desktop)
- [x] #21 Previous / Next links at the bottom of lesson plans and the module page
- [x] #22 "Module 1 overview" link on lesson, practice, and assignment pages
- [x] #26 "What to give students" section in How a Lesson Works
- [x] #28 Feedback (and Previous/Next) headings `{.unlisted}`, so they're out of the page TOC
- [x] Notebooks rebuilt (new `01-02-change-variable.ipynb`); answer keys updated

**Also done at the author's request:**

- [x] Renamed `private/` to `answer-keys/` and tracked it in the public repo (off the website, never linked). Updated `.gitignore`, AGENTS, README files, decisions, About, How a Lesson Works, and lesson Teacher Notes. Replaced the author's computer name in the marking notes with `LAB-PC-14`.
- [x] Moved the audit files to `audits/` (git-ignored).

**Outstanding: needs discussion or a decision:**

- ~~D3~~ Resolved 2026-11-16: nothing in the repo needs to be secret. Quizzes and tests go in `answer-keys/` with their answers; revisit only if teachers report problems.
- ~~D4~~ Resolved 2026-11-16: every page also links a private Google Form ("send it privately") with the page address pre-filled (`entry.1446477366`). Form and response sheet live in the Drive folder `peter.beens.ca-ics3u/Feedback`.
- Lesson plans now name the `answer-keys` folder in plain text (no link). Confirm that's wanted, given the goal of not drawing attention to it.

**Outstanding: verify first, then fix if real:**

- #8 Pyodide "Downloading" notice on slides (seen on the Compare and Predict slides in testing); check whether quarto-live can delay loading.
- #9 Grok's report that the "Two lines of Python" fragments duplicate the code.
- Cycle diagram on a phone (not re-checked at 390 px).

**Later:** #16 one practice page per lesson (at 3+ lessons), #18 rubric on phones, #23 Modules menu and sidebar (when Module 2 arrives), #24 expectation-code glosses, dark-mode check of stepper and live editors.

### Earlier focus

- Author review of Module 1, Lessons 1–2 (slower pacing, `platform` only, "Where does my code run?" comparison) and the draft scope and sequence.

## Next Tasks

1. Revise Lessons 1–2 from author feedback; decide whether Reveal.js slides, quarto-live, and Python Tutor stay.
2. Confirm the Colab values in Lesson 1's teacher notes by running the program in Colab.
3. Add quizzes for Lessons 1–2, in `answer-keys/module-01-about-this-computer/` (public in the repo, off the site). Later: downloadable versions of practice and assignments (Google Docs, Word, or PDF).
4. Revise the scope and sequence from author feedback; remove the "Draft" callout when approved.
5. Publish to GitHub Pages and confirm the site, runnable code, and Python Tutor work online.

## Open Questions

- After the next push, test the notebook Open in Callysto | Colab links. (GitHub Pages is on; the site is served at https://peter.beens.ca/ics3u/.)

- Networking: the author is considering programs that look at the network (e.g., the computer's address and name). Decide whether and where it fits in the scope and sequence.

- How worksheets reach Google Docs: Quarto `.docx` output uploaded to Drive, an export script, or manual copy.
- Whether the GitHub account has Pro (needed for Pages from a private repository; free for verified teachers through GitHub Education).
- Module themes and anchor programs: confirm or replace (e.g., Data Detective's data source).
- Whether Computer Science in the World (Strand D2–D3) runs alongside modules or as its own block.
- This Mac has a global Jupyter kernel pointing to a missing environment (`/Volumes/Extreme-SSD/.../.venv`). Lesson pages avoid it with `engine: markdown`, but it may affect other Quarto projects.

## Recently Completed

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
