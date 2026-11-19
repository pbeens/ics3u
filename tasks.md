# Tasks

## Current Focus

### Module plans for the whole course (draft, 2026-11-18): awaiting author review

Built planned overview pages for every module (no lessons yet) so the author can judge the direction. Verified: site renders with no warnings, no broken internal links, and all 57 expectations covered (checked by script).

- [x] Module 1 overview: planned Lessons 3–11 and planned assignment additions; hours 15 → 14
- [x] New overview pages: Module 2 Spec Checker, 3 Benchmark Lab, 4 Passwords and Secret Messages, 5 On the Network, 6 Data Detective, 7 Software Development Project, and Computer Science in the World
- [x] Scope and Sequence rewritten for seven modules (hours, spiral with a files-and-folders row, module summaries, coverage table)
- [x] New "Modules" navbar menu; home page wording; teaching-approach example
- [ ] Author decisions: (1) Benchmark Lab replacing Games of Chance; (2) new On the Network module (resolves the networking open question); (3) seven modules with the project cut from 20 h to 16 h; (4) Module 7's teacher-led "Lab Health Check" class project; (5) lists in Module 5 rather than Module 6
- [x] Combined update (2026-11-18): Module 1 gains Getting Output Right and Values and Types (15 h); Benchmark Lab drops the guessing game, swaps dice for shuffle, and becomes 14 h; Skill Builders, Quick Builds, and spaced warm-ups in every module; My Computer Toolkit thread; file writing (Module 5 network log, analyzed in Module 6); hash-verified backups; Caesar cipher as a short activity; practical-first rules in `teaching-approach.md`. Verified: 110 h, all 57 expectations, lesson counts fit hours, no broken links or anchors.
- [x] Open computers (2026-11-18): Before You Begin now leads with a blunt "This course needs open computers" callout, a requirements table (what students' programs need vs. what managed computers block), standalone refurbished computers as first choice, opened-up lab computers second, and a students'-own-computers note (not recommended). Pointers on About, home, and Modules 5–6.
- [x] Margin feedback link (2026-11-18): the right-margin "Report an error or suggest a change (GitHub)" link now has a "Send feedback privately (no account)" link beside it, opening the Google Form with the page filled in. Verified in headless Chrome on three pages (one private link per margin copy).
- [x] Where answers go (2026-11-18): tracing notebook (paper) for in-class and Practice work; comments in the `.py` file for anything handed in. Assignment, Practice, Lessons 1–2 (plans and slides), How a Lesson Works, Before You Begin checklist, and `teaching-approach.md` updated.
- [x] Course folder and hand-ins (2026-11-18): new student page `site/course-folder.qmd` (home-folder location, module/lesson structure, toolkit, naming rules incl. underscores for importable `.py` files, saving downloads, weekly backup), in the Getting Started menu and linked from Lesson 1, Practice, and the assignment. New "Handing In Work" section in How a Lesson Works (what's handed in and in what format; `.ipynb` accepted; tips). Before You Begin checklist updated.
- [ ] Documents for written work: Word (`.docx`) and fillable PDF versions of longer written parts (test plans, structure charts, protection plan, project documents). Recommendation: Quarto's `docx` output from the same source for Word (uploads to Drive convert to Google Docs); fillable PDFs only for fixed forms such as the test plan table. Decide before Module 2's assignment.
- [ ] Build `make_sample_folder.py` (planned for `site/tools/`): standard library only; fixed and per-student seeds; safe reset; optional `--download` from files hosted on the site. Needed by Module 1 Lesson 6.
- [ ] When approved: remove "(planned)" labels and Draft callouts as modules are built; check network lessons with school IT constraints

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

- **Idea to consider (2026-11-18): two tracks.** Track 1 (current plan) builds computer-related utilities. Track 2 would teach the same ideas through creating media and art, the way Turing graphics did for Ontario beginners. Notes for discussion:
  - Standard-library options: `turtle` (closest to Turing's drawing commands), `tkinter` Canvas (shapes, animation, simple games), writing SVG files as plain text (they open and edit in Inkscape), and generating sound with the `wave` module. Third-party options as extensions: Pillow (images), pygame-ce (games and animation), py5 (Processing-style).
  - Fits the curriculum well: pixels, colour codes, and image and sound file sizes cover A1.2 (data representation); graphics cards and monitors connect to C1.
  - MCP: the official Python MCP SDK makes small MCP servers possible, but MCP connects an AI assistant to an app, so it suits a Module 7 project or extension more than core lessons. For students' own code to control an app directly, the app's scripting interface (e.g., Inkscape's command line and Python extensions) is simpler. Candidate apps: the ArtCraft suite (e.g., PhotoCraft, a Photoshop alternative, and an Illustrator alternative) and Affinity; check which have MCP servers or scripting interfaces.
  - Cost: two full tracks doubles the materials. A lighter version keeps shared lessons and skills, and gives each module a Track 1 and a Track 2 anchor program and assignment.
  - Parked for now because of the extra work. If pursued, it may live in a separate GitHub repository rather than this one.

- After the next push, test the notebook Open in Callysto | Colab links. (GitHub Pages is on; the site is served at https://peter.beens.ca/ics3u/.)

- (Proposed answer, 2026-11-18: Module 5, On the Network. See the module plan above.) Networking projects: the author wants programming projects about computer networks (e.g., programs that report the computer's address and name). Decide whether and where they fit in the scope and sequence. Resources:
  - [netsim](https://cs.uwaterloo.ca/~m2mazmud/netsim/) (University of Waterloo): a browser game about how packets move across the Internet. Suggested on the ACSE list (2026-11-16) for Grade 10s.
  - [errorinn/netsim](https://github.com/errorinn/netsim): its source code, MIT licensed, written in PHP, last updated 2020. A school can host its own copy. The public site slows down when a whole class registers at once, which could also be a teaching point about server load.

- How worksheets reach Google Docs: see the Documents task above (Word and fillable PDF, 2026-11-18).
- Whether the GitHub account has Pro (needed for Pages from a private repository; free for verified teachers through GitHub Education).
- Module themes and anchor programs: confirm or replace (now drafted on each module's overview page).
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
