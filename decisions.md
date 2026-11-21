# Decisions

Consequential project decisions, newest first. Current files and newer instructions take precedence if an entry is stale.

---

## 2026-11-19 — Quick Builds are lesson Make products; every module has a work period

- **Decision:** Each module's two Quick Builds are the graded Make products of named lessons, so they cost no extra class time. In Modules 1–6 the period before the test is "Review and assignment work period". To make room without changing hours (110 total), lessons were merged: Module 1 Lessons 9–10 (`input()` and the first look at `if`/`for`), Module 3 "Plan Before You Code" + "Your First Functions", Module 4 "Reusable Code" into "Password Strength Checker", Module 5 "Who Am I on the Network?" + "IP Addresses", Module 6 "Counting by Type" + "Where Did My Space Go?".
- **Context:** Round 2 audit (Antigravity): modules filled every period with lessons and a test, leaving no class time for Quick Builds or assignments.
- **Alternatives:** Take the work periods from Module 7 (16 → about 12 h); rejected because the project is the final 30%.
- **Revisit if:** Merged lessons run long once written.

---

## 2026-11-19 — Module navigation in a left sidebar

- **Decision:** The navbar is Home · Getting Started · Modules · About. Each built module gets a left sidebar (overview; For teachers; For the class; For students) shown only on its own pages, defined in `site/_quarto.yml`. Module 1 has one now; the separate "Module 1" menu is gone. Every page ends with Previous and Next links.
- **Context:** Round 2 audits: two module menus side by side were confusing, and many pages had no way forward.
- **Alternatives:** Wait until Module 2 has lessons.
- **Revisit if:** Sidebars get crowded once a module has 10+ lessons (group by lesson, not by audience).

---

## 2026-11-19 — Open computers: lead with the minimum

- **Decision:** The "This course needs open computers" callout stays blunt but opens with the minimum: Modules 1–4 run on any computer with Python and files that stay saved; the whole course needs open computers. Home card 1 says the same.
- **Context:** Both round 2 audits worried that teachers in managed labs would stop reading before learning that the early modules work.
- **Revisit if:** Teachers report the message is still off-putting, or that Modules 1–4 also fail on their lab computers.

---

## 2026-11-18 — Where students write answers

- **Decision:** Students write predictions, trace tables, and short answers in a paper *tracing notebook*, in class and on Practice pages. Anything handed in has its written answers as comments at the top of the `.py` file; assignments supply a starter file with a space for each answer. Every reading task says where to write. "Notebook" alone means Jupyter on this site.
- **Context:** Pages said "answer the questions" without saying where, and "notebooks" was ambiguous.
- **Alternatives:** A `.py` answer file for every Practice section; Google Docs worksheets; answer boxes on the page that save in the browser.
- **Revisit if:** Teachers want Practice work collected digitally (then add answer files per Practice section).

---

## 2026-11-18 — Seven practical modules (approved 2026-11-21)

- **Decision:** Reorganize the course into seven modules, all about the student's own computer, its use, and its connections: About This Computer (14 h), Spec Checker (15), Benchmark Lab (15, replaces Games of Chance), Passwords and Secret Messages (15), On the Network (14, new), Data Detective (15, now about files, backups, and energy), Software Development Project (16, down from 20, starting with a teacher-led class project), plus Computer Science in the World (6). Each module has an overview page with planned lessons and a practical assignment.
- **Context:** The author asked for plans for every module, with practical assignments for students who want to learn about their computers and computer use, and earlier asked where networking projects fit.
- **Alternatives:** Keep six modules and fold networking into Secret Messages (too crowded); keep Games of Chance (less tied to computers).
- **Revisit if:** The author prefers the original six, or the network module is impractical on school networks.
- **Update (same day, approved by the author):** Basics get deliberate practice (Skill Builders, Quick Builds, spaced warm-ups); students build one "My Computer Toolkit" across modules; assignments must pass the "would a non-programmer use this?" test; file work uses a generated sample folder (`make_sample_folder.py`), not students' own files. Module 1 is 15 h and Module 3 is 14 h. Some ideas came from a ChatGPT review the author shared.
- **Approved (2026-11-21):** the author approved all five open points: Benchmark Lab replaces Games of Chance; On the Network is a new module; seven modules, with the project cut from 20 h to 16 h; Module 7 opens with the teacher-led "Lab Health Check" class project; lists are taught in Module 5, not Module 6.

---

## 2026-11-15 — Lesson plans are for teachers; students use slides, code, and practice pages

- **Decision:** Each lesson has one page, the lesson plan, for teachers. It opens with a "For teachers" banner and an At a Glance summary. Students work from the slides, the `.py` files and notebooks, and each module's interactive Practice and Assignment pages on the site. Downloadable versions (Google Docs, Word, or PDF) may come later.
- **Context:** The interactive lesson plans looked student-facing, and nothing described what happens before or after the slides, or what students do after class.
- **Alternatives:** A separate student page per lesson (more to maintain); Google Docs worksheets only (loses interactivity).
- **Revisit if:** Teachers need printable or LMS-ready versions.

---

## 2026-11-16 — Answer keys public in the repo, off the website

- **Decision:** Rename `private/` to `answer-keys/` and track it in the public repository. Answer keys stay off the website and are never linked from it; lesson plans name the folder in plain text so teachers can find it.
- **Context:** A folder called "private" in a public repo attracts attention, and the author is comfortable with answer keys being public as long as they aren't on the site. This also removes the need to rewrite Git history and gives teachers a way to get the keys.
- **Alternatives:** Git-ignored local folder (no backup, no access for other teachers); a separate private repository.
- **Follow-up (same day):** Nothing in the repository needs to be secret, including quizzes and tests. They go in `answer-keys/` with their answers. Students who look up answers in the repository are not a concern.
- **Revisit if:** Teachers report problems and ask for assessments to be kept private.

---

## 2026-11-15 — Public repo, MIT license, feedback through GitHub issues

- **Decision:** The repository is public and MIT licensed (Ministry documents excluded). `private/` is git-ignored and kept only locally (superseded 2026-11-16: now `answer-keys/`, tracked). Feedback goes through a GitHub issue form, linked from every page with the page title and URL prefilled.
- **Context:** Publishing the repo makes GitHub Pages and the Colab/Callysto notebook links work; issues give one public place for corrections and ideas.
- **Alternatives:** Private repo with a separate public notebooks repo; CC BY 4.0 for course content.
- **Revisit if:** Teacher-only material needs version control (consider a separate private repo).

---

## 2026-11-15 — Short home page

- **Decision:** The home page is for getting started: three quick-start cards (set up, see the plan, teach) and a lesson table. Philosophy, lesson structure, and research live on the About page.
- **Context:** Teachers should be able to land on the site and start using it quickly.
- **Revisit if:** The lesson table gets long; then link to a module index instead.

---

## 2026-11-15 — Notebook mirrors of example programs

- **Decision:** Every example program is mirrored as a Jupyter notebook in top-level `notebooks/`, named `MM-LL-name.ipynb` and generated by `scripts/build_notebooks.py`. Notebooks use a read-first scaffold (predict, run, compare). They are not published on the site.
- **Context:** Gives teachers a ready file for Jupyter, Colab, or the Callysto Hub without maintaining two copies of each program.
- **Alternatives:** Publishing in `site/notebooks/` with Colab links; code-only notebooks; a subfolder per module.
- **Revisit if:** Students need to open notebooks straight from lesson pages.

---

## 2026-11-15 — Students run Python locally

- **Decision:** The course assumes Python runs locally on teacher and student computers (lab, refurbished, or Raspberry Pi). Browser and cloud options (this site's runnable boxes, Colab, Callysto Hub) are backups and comparison points only. Setup guidance is on the site's Before You Begin page.
- **Context:** Hardware and system programs report a different machine when run online, and online notebooks can't see local files, drives, or the network.
- **Revisit if:** A school can only provide Chromebooks or browser access.
- **Update (2026-11-18):** The site now says bluntly that the course needs open computers: ideally standalone refurbished computers outside board management, with no software restrictions; managed lab computers only if IT opens them up. Students' own computers are mentioned but not recommended. Before You Begin lists what students' programs need and what managed computers usually block.

---

## 2026-11-15 — Site naming

- **Decision:** The navbar title is "ICS3U". The home page title is "ICS3U: Introduction to Computer Science", with the subtitle "Grade 11, University Preparation · Taught in Python". The footer reads "ICS3U · Ontario Curriculum (2008)".
- **Context:** The course code is what students and teachers search for, and the Ministry course title reads as official. A branded name would make the site harder to find.
- **Revisit if:** The site gets a distinctive tagline or covers more than one course.

---

## 2026-11-14 — Teacher prompts

- **Decision:** Lessons include short scripted teacher prompts at key moments, especially the first time students meet a tool or idea (e.g. the step-through box colours). On lesson pages they are green "Teacher prompt" callouts; on slides they go in speaker notes.
- **Context:** Suggested by the author; keeps explanations consistent across teachers and separates what to say from planning notes.
- **Revisit if:** Prompts make lesson pages too long to scan.

## 2026-11-14 — Custom predict-and-step box replaces Python Tutor in Module 1

- **Decision:** Build a project shortcode (`stepper`) that runs a real example file in the browser (Pyodide) one line at a time, beside a prediction box, showing output and variables. Use it for the Predict and Run stages. Keep Python Tutor only for programs using modules it allows.
- **Context:** Python Tutor rejects `platform` ("ImportError: platform not found or not supported"), so Lesson 2 had to visualize a different, typed-in program, which the author found confusing. The author also wanted students to predict inside the visualizer and then run immediately. Tested in headless Chrome on pages and slides.
- **Alternatives:** Python Tutor with typed-in values; separate static code and runnable boxes.
- **Revisit if:** Students need features Python Tutor has and the stepper lacks (e.g. drawings of lists and objects, `input()` support).

## 2026-11-14 — One library at a time; start with `platform`

- **Decision:** Module 1 starts from a single line (`print(platform.machine())`) and uses only the `platform` module for Lessons 1–2. `os` and `shutil` are introduced one at a time in Module 2. Lesson 1 ends by comparing where code runs: the classroom computer, the browser (Pyodide), and Google Colab.
- **Context:** The first Lesson 1 draft introduced three libraries at once, which the author found too much, too fast. `platform` uses one repeated pattern, is safe to explore, and every answer starts a discussion. `platform.machine()` is reliable across systems; `platform.processor()` is not.
- **Alternatives:** Starting with `os` (broad, abstract, and mostly about files); several libraries in the first lesson.
- **Revisit if:** Students move through `platform` faster than expected and need more challenge earlier.

## 2026-11-14 — Interactive code: quarto-live and Python Tutor (trial)

- **Decision:** Use the quarto-live extension for runnable, editable Python in lesson pages and slides, and a project shortcode that embeds example files in Python Tutor for step-through tracing. Both on trial with Module 1, Lesson 1.
- **Context:** Reading-first lessons need students to run, modify, and trace code without installing anything. quarto-live runs Python in the browser (Pyodide), with no server. Python Tutor shows variables changing line by line but needs internet and limits imports. Both were tested in headless Chrome on 2026-11-14.
- **Alternatives:** Linking out to an online editor; a custom trace-table widget built on Pyodide (possible later).
- **Revisit if:** Python Tutor's embedding or availability changes, Pyodide load times are a problem on school networks, or a custom trace-table widget becomes worth building.

## 2026-11-14 — Quarto Reveal.js for slides (trial)

- **Decision:** Build lesson slides with Quarto's `revealjs` format inside `site/`, as a trial. Slidev remains the fallback.
- **Context:** Reveal.js decks render in the same `quarto render site` build, need no Node.js, and are indexed slide by slide in site search (tested 2026-11-14). Slidev has stronger presenter features but would need a separate build step and is not searchable.
- **Alternatives:** Slidev decks built separately and copied into `docs/slides/`.
- **Revisit if:** The author finds Reveal.js slides not good enough in the classroom after the first sample lesson.

## 2026-11-14 — Spiral course built on themed modules

- **Decision:** Organize the course as a spiral of themed modules (About This Computer, Spec Checker, Games of Chance, Secret Messages, Data Detective, Software Development Project), not topic units. Most programming ideas appear from the first module through reading, then move through read, modify, write, and design levels.
- **Context:** The author found the first draft too traditional (output, then input, then decisions, each on its own) and wants many concepts introduced early and gently, without becoming fully project-based.
- **Alternatives:** Traditional one-construct units; fully project-based learning.
- **Revisit if:** Students struggle because too many ideas appear at once, or teachers find curriculum coverage hard to track.

## 2026-11-14 — Start deep with authentic examples; hardware in context

- **Decision:** Use authentic, interesting code from the first lesson instead of toy examples. The first `print()` program reports the computer's own hardware. Hardware expectations (C1.1–C1.4) are taught through the programs in Modules 1–2, not in a standalone unit.
- **Context:** The author does not want to shy away from depth. Reading first makes this practical: students can read and predict code they could not yet write.
- **Alternatives:** "Hello, World" start; hardware taught only as a standalone unit.
- **Revisit if:** Students find the opening examples too intimidating to engage with, even with teacher modelling.

## 2026-11-14 — Reading first, with direct instruction and PRIMM

- **Decision:** Students read, trace, and predict code before writing it. Lessons use explicit direct instruction and the PRIMM sequence (Predict, Run, Investigate, Modify, Make), moving gradually to independent work.
- **Context:** The author wants reading code before writing code to be the main emphasis. Research on novice programmers links tracing and reading ability to writing ability, and favours explicit instruction and worked examples for novices. See [project-docs/teaching-approach.md](project-docs/teaching-approach.md).
- **Alternatives:** Inquiry- or project-first approaches; writing-first tutorials.
- **Revisit if:** Classroom results show students can read code well but are not reaching independent writing and project work (strand B4).

## 2026-11-14 — Public site, private repository

- **Decision:** The site is public; the repository is private. Tests, quizzes, answer keys, and teacher-only notes live in `private/`, outside the Quarto project, and are never linked from the site.
- **Context:** A public site lets students find anything published on it.
- **Alternatives:** A password-protected site (not supported by GitHub Pages); a fully private site.
- **Revisit if:** A host with access control is adopted.

## 2026-11-14 — Quarto website published from `docs/` with GitHub Pages

- **Decision:** Quarto source in `site/`, rendered to `site/_site/`, then mirrored into `docs/` by a post-render script (`site/_scripts/sync_docs.py`). GitHub Pages serves the `docs/` folder of the default branch.
- **Context:** Quarto has built-in search and simple organization; Pages can serve a `docs/` folder with no build pipeline. Setting Quarto's `output-dir` to `../docs` (outside the project) triggered Quarto warnings and left stale files uncleaned, so the copy step replaced it.
- **Alternatives:** MkDocs; plain HTML; a GitHub Actions build.
- **Revisit if:** Rendering in CI becomes preferable to committing `docs/`, or Pages from a private repository is unavailable on the account.

## 2026-11-14 — Editable copies through Google Docs

- **Decision:** Worksheets and assessments are distributed as editable Google Docs, not PDFs. The exact pipeline is still open (see `tasks.md`).
- **Context:** Teachers need to print and adapt materials.
- **Alternatives:** PDF downloads; Word files only.
- **Revisit if:** Teachers report needing a different format.

## 2026-11-14 — Python 3 as the course language

- **Decision:** Python 3 is the primary language. Other languages may appear as marked extensions.
- **Context:** Author's choice; widely used for ICS3U in Ontario.
- **Revisit if:** The department standardizes on another language.

## 2026-11-14 — Course is ICS3U (2008 curriculum)

- **Decision:** The course is ICS3U, Grade 11 Introduction to Computer Science, University Preparation, from *The Ontario Curriculum, Grades 10 to 12: Computer Studies (Revised 2008)*.
- **Context:** The project folder was initially named ICS3M in error; no ICS3M course exists in this curriculum.
- **Revisit if:** Ontario releases a revised Computer Studies curriculum.
