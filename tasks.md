# Tasks

## Current Focus

### Module 1, Lesson 3: Getting Output Right (built 2026-11-21; awaiting author review)

The seven-module plan is approved (`decisions.md`, 2026-11-21). Lesson 3 is the first lesson built to the new rules: a practical opening problem, reading first, and a Quick Build (System Banner) as its Make product.

- [x] Eight example programs (`l03_*.py`), run on Python 3; browser outputs checked with the `platform` values the web page reports
- [x] Lesson plan (75 min: Review 5, Teach 15, Predict 10, Investigate 20, Modify 10, Make 10, Check 5); real system tool (`systeminfo`, `system_profiler`, `hostnamectl`) as the opening problem; first-use teacher prompts for keyword arguments, escape characters, and syntax errors
- [x] Slides (13), with speaker notes
- [x] Practice section "After Lesson 3" on the existing Practice page (one page per lesson still deferred); new student page `quick-build-system-banner.qmd`
- [x] Answer keys: `lesson-03-answers.md`, Lesson 3 practice answers, `quick-build-system-banner-marking.md` (sample solution run)
- [x] Links: home table, Module 1 overview (Lesson 3 moved out of Planned; Lesson 4 row now "put the facts inside the banner"), sidebar, Lesson 2 Previous/Next
- [x] Notebooks rebuilt; render with no warnings; no broken links; all five steppers run in Chromium (Playwright) with expected output, including the `SyntaxError`
- [ ] Author review of Lesson 3

### Module 1, Lessons 4–5 (built 2026-11-21; awaiting author review)

- [x] Lesson 4, Better Reports with f-strings: plan, slides (14), ten example programs; padding (`:<`, `:>`, `:^`) inside the System Banner's box; names and comments (A4.2); syntax vs. run-time errors; Make is System Banner version 2 (ungraded)
- [x] Lesson 5, Values and Types: plan, slides (13), nine example programs; `str`/`int`/`float`/`bool`, `type()`, `/` gives a float, floating-point error and `:.2f`, `int()`/`float()`/`str()`, constants; Make is the Parts Receipt Quick Build (new student page `quick-build-parts-receipt.qmd`)
- [x] Practice sections for Lessons 4 and 5; answer keys (`lesson-04-answers.md`, `lesson-05-answers.md`, practice answers, `quick-build-parts-receipt-marking.md` with a run sample solution)
- [x] Links: home table, Module 1 overview (both moved out of Planned), sidebar, Previous/Next
- [x] Notebooks rebuilt; render clean; no broken links; all steppers on Lessons 4–5 and the Practice page run in Chromium with expected output (the browser runs Python 3.13)
- [ ] Author review of Lessons 4–5

### Module 1, Lesson 6 and the sample folder tool (built 2026-11-21; awaiting author review)

- [x] `site/tools/make_sample_folder.py` (published via `resources`; README in `site/tools/`): 156 files, about 7 MB, in documents, data, photos (real PNGs, dated sub-folders, 8 duplicate copies), music (WAV), projects, logs (with a zip), downloads (large filler and an empty file), old-stuff (up to 8 years old), and an empty folder. Tested: same seed gives byte-identical files and dates (also identical on Python 3.9 and 3.11); `--seed` changes it; refuses unmarked folders and files; `--reset` rebuilds only its own. `--download` still planned.
- [x] Lesson 6, Where Do My Programs Live?: plan, slides (12), seven example programs; paths, `os.getcwd()`, `os.path`; parts of the editor and its debugger (C3.1); first terminal use and first run of the sample folder tool; `FileNotFoundError`; Make starts the `toolkit` folder with `folder_check.py`
- [x] Practice section, answer keys (`lesson-06-answers.md`), links, sidebar; Scope and Sequence and Module 6 now link the tool
- [x] Render clean; no broken links; all steppers checked in Chromium
- [ ] Author review of Lesson 6; check the sample folder tool on Windows (paths, `py` launcher, OneDrive)

### Module 1, Lesson 7 (built 2026-11-21; awaiting author review)

- [x] Lesson 7, What Python Actually Runs: plan, slides (12), seven example programs; source vs. machine code, compiler vs. interpreter (C3.3, C3.4), the two error kinds as evidence that Python compiles first, live `dis` bytecode box, `platform.python_compiler()`, sorting applications / languages / operating systems (C3.5); Make is `what_runs_this.py`
- [x] Practice section, answer keys (`lesson-07-answers.md`), links, sidebar; steppers and the live `dis` box checked in Chromium
- [ ] Author review of Lesson 7

### Module 1, Lesson 8 (built 2026-11-21; awaiting author review)

- [x] Lesson 8, Inside the Computer: RAM and CPU: plan, slides (11), five example programs; component tour (C1.1) and a program's journey from drive to RAM to CPU; labelling lines RAM / CPU / screen (C1.4); `sys.getsizeof` (64-bit vs. the browser's 32-bit sizes) and `id()`; upgrade scenarios; Make annotates the Parts Receipt
- [x] Practice section, answer keys (`lesson-08-answers.md`), links, sidebar; steppers checked in Chromium
- [ ] Author review of Lesson 8

### Next

1. Sample folder tool: add `--download` (files hosted on the site, licence-checked, falling back to local generation) before Module 5 Lesson 7 reads its download code.
2. Quizzes for Lessons 1–2, in `answer-keys/module-01-about-this-computer/` (public in the repo, off the site).
3. Documents for written work: Word (`.docx`) and fillable PDF versions of longer written parts. Recommendation: Quarto's `docx` output from the same source (uploads to Drive convert to Google Docs); fillable PDFs only for fixed forms such as the test plan table. Decide before Module 2's assignment.
4. Confirm the Colab values in Lesson 1's teacher notes by running the program in Colab (needs the author's account).
5. After the next push, test the notebook Open in Callysto | Colab links.
6. As modules are built: remove "(planned)" labels and Draft callouts; give each module a sidebar like Module 1's; check network lessons against school IT constraints.

### Later

- From the audits: screen-reader duplication in line-highlight fragments; skip link; wide tables on phones (rubric, Scope and Sequence); expectation-code glosses; one practice page per lesson (decide when Lesson 3's practice is added); dark-mode check of steppers and live editors; cycle diagram at 390 px.
- Lesson plans name the `answer-keys` folder in plain text (no link). Confirm that's wanted.

## Open Questions

- **Parked (2026-11-21, author away for a week): generic name, ICS3U as the main alignment.** Before announcing the site, consider renaming it so the URL isn't tied to ICS3U ("design to one, map to many"): ICS3U stays the backbone (hours, pacing, assessment, Strand D) and its codes stay on the pages; other curricula get alignment pages built from compliance audits (first: TEJ4M, once the author has the curriculum PDF; later other provinces and states). Steps: (1) author picks a name and URL slug; (2) rename the repo, update about 30 files with repo or URL references (site config, feedback script, notebook Colab/Callysto links, READMEs), add redirect pages for old `/ics3u/` links, retitle the site, record the decision; (3) TEJ4M audit and alignment page; (4) then send the ACSE email. Ontario-specific details (HST, electricity rates, Computers for Schools; about 11 places) need only "use your local rate" notes.
- **ACSE reviewer email** (`acse-review-request-email.md`, draft, not committed): on hold until the naming question is settled. Update the URL, the lesson count, and the TEJ4M angle before sending; the draft is git-ignored (author's change).

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
