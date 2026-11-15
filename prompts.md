# Prompt Log

Program-related prompts for this project, newest first. Paraphrased, not verbatim.

---

## User Prompt 25

- **Timestamp:** 2026-11-15T14:45
- **Goal:** Mirror each example program as a Jupyter notebook.
- **Summary:** Add a Notebooks folder in which each program is mirrored as a Jupyter notebook, named with a numeric prefix that follows the module and lesson numbers. Chose a top-level, unpublished folder; `01-01-name` naming; and a read-first scaffold (predict, run, compare).
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** `scripts/build_notebooks.py` generates `notebooks/MM-LL-name.ipynb` from `site/modules/*/examples/lLL_name.py`, taking lesson titles and expectations from the lesson front matter.

---

## User Prompt 24

- **Timestamp:** 2026-11-15T14:30
- **Goal:** Add teacher setup notes on having a working Python platform.
- **Summary:** Before the lessons, tell teachers why they need a working Python computer for demonstrations and why students need somewhere to run, debug, and modify programs. Colab and Callysto work in a pinch, but online Python can't give the hardware (and possibly networking) experience the course depends on. Recommend refurbished computers where possible, or Raspberry Pis and similar small computers.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** New `site/before-you-begin.qmd`, linked from the navbar, home page, and Lesson 1; checked Callysto Hub status (still online; Cybera and PIMS stepped back in 2024) and Computers for Schools Plus (Ontario: Renewed Computer Technology).

---

## User Prompt 23

- **Timestamp:** 2026-11-15T14:20
- **Goal:** Finish the renaming in the Quarto extensions.
- **Summary:** Update the author field in the two Quarto extensions to the new site name.
- **Host:** m4-mini
- **Agent:** Claude Code

---

## User Prompt 22

- **Timestamp:** 2026-11-15T14:15
- **Goal:** Match the project docs to the new site name.
- **Summary:** Update the README and AGENTS headings to use the new site name too.
- **Host:** m4-mini
- **Agent:** Claude Code

---

## User Prompt 21

- **Timestamp:** 2026-11-15T14:10
- **Goal:** Apply the agreed site naming.
- **Summary:** Approved the naming recommendation; apply it to the site.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Navbar title "ICS3U"; home title "ICS3U: Introduction to Computer Science"; subtitle "Grade 11, University Preparation · Taught in Python"; footer "ICS3U · Ontario Curriculum (2008)".

---

## User Prompt 20

- **Timestamp:** 2026-11-15T14:05
- **Goal:** Choose the site's home-page title.
- **Summary:** With the folder now named `ics3u`, decide what the site should be called on its main page.
- **Host:** m4-mini
- **Agent:** Claude Code

---

## User Prompt 19

- **Timestamp:** 2026-11-14T14:10
- **Goal:** Add teacher prompts to lessons.
- **Summary:** Include "teacher prompts": scripted explanations for key moments, such as explaining the visualizer's colour coding the first time students use it.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Teacher prompts added as green callouts on lesson pages and as `TEACHER PROMPT` speaker notes on slides; convention documented in the teaching approach.

---

## User Prompt 18

- **Timestamp:** 2026-11-14T14:00
- **Goal:** Visualize the programs students actually run, and predict inside the visualizer.
- **Summary:** Lesson 2's visualizer suddenly used a different program with typed-in variables. Visualize the programs students have been running instead, and combine predicting with the visualizer so students predict and then run right away.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Confirmed Python Tutor rejects `platform`; built a `stepper` shortcode (Pyodide, `sys.settrace`) with prediction box, line-by-line stepping, output, variables, and error highlighting; used it in Lessons 1–2 and their slides; verified in headless Chrome.

---

## User Prompt 17

- **Timestamp:** 2026-11-14T13:56
- **Goal:** Explain the course philosophy on the home page.
- **Summary:** Update the website's home page to present the philosophy of this course of study.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** `site/index.qmd` rewritten with five principles, the lesson sequence, interactive features, research basis with references, and site notes.

---

## User Prompt 16

- **Timestamp:** 2026-11-14T13:52
- **Goal:** Open external links in a new tab.
- **Summary:** Links that take visitors off the website should always open in a new tab.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Enabled `link-external-newwindow` and `link-external-icon` site-wide; verified in headless Chrome on lesson pages and slides.

---

## User Prompt 15

- **Timestamp:** 2026-11-14T13:48
- **Goal:** Rebuild Lesson 1 and add Lesson 2.
- **Summary:** Rebuild Lesson 1 with slower pacing around the `platform` module and a comparison of where code runs (including Colab), and add Lesson 2 on exploring the `platform` library.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** New example files, lesson pages, slides, and private answer keys for Lessons 1–2; scope and sequence Module 1–2 updated; all code cells verified in headless Chrome.

---

## User Prompt 14

- **Timestamp:** 2026-11-14T13:43
- **Goal:** Consider Google Colab as another place the hardware program runs.
- **Summary:** The author first ran the hardware program in Google Colab, which adds another perspective: the code reports on a cloud computer.
- **Host:** m4-mini
- **Agent:** Claude Code

---

## User Prompt 13

- **Timestamp:** 2026-11-14T13:40
- **Goal:** Slow down the first lesson and focus on one library.
- **Summary:** The direction is right but Lesson 1 moves too fast by using several libraries at once. Start simply, with just the CPU type, then investigate one library in more depth. Asked whether `platform` or `os` is more interesting to explore first.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Compared `platform` function output on macOS and in Pyodide to inform the recommendation.

---

## User Prompt 12

- **Timestamp:** 2026-11-14T13:35
- **Goal:** Install the runnable-code extension and trial both visualizers on Lesson 1.
- **Summary:** Install quarto-live and try both it and Python Tutor in Module 1, Lesson 1.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** quarto-live installed in `site/_extensions/`; `pytutor` shortcode added; Lesson 1 page, slides, examples, and private answer key created; both tools verified in headless Chrome via puppeteer-core.

---

## User Prompt 11

- **Timestamp:** 2026-11-14T13:36
- **Goal:** Explore adding a Python code visualizer to the site.
- **Summary:** Asked whether the site can include a Python visualizer.
- **Host:** m4-mini
- **Agent:** Claude Code

---

## User Prompt 10

- **Timestamp:** 2026-11-14T13:33
- **Goal:** Choose a slide tool.
- **Summary:** Use Quarto Reveal.js slides to start; keep them if they work well, otherwise reconsider Slidev.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** A temporary Reveal.js deck was rendered inside the site to confirm it builds without warnings and that each slide is indexed in site search; the test deck was then removed.

---

## User Prompt 9

- **Timestamp:** 2026-11-14T13:30
- **Goal:** Check whether the site can combine Quarto and Slidev.
- **Summary:** Asked whether the published website can contain both Quarto pages and Slidev slide decks.
- **Host:** m4-mini
- **Agent:** Claude Code

---

## User Prompt 8

- **Timestamp:** 2026-11-14T13:25
- **Goal:** Restructure the course as a spiral instead of topic units.
- **Summary:** The draft scope and sequence felt like a traditional computer science course. Introduce many concepts early and gently, instead of separate units for output, input, decisions, and strings. Avoid going fully project-based, which would get heavy quickly.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Scope and sequence rewritten as six themed modules with anchor programs and a read/modify/write/design spiral table; coverage re-verified by script.

---

## User Prompt 7

- **Timestamp:** 2026-11-14T13:20
- **Goal:** Start deep with authentic examples tied to other expectations.
- **Summary:** Don't shy away from depth. For example, instead of a traditional "Hello, World", the first `print()` lesson should print information about the computer's hardware, which also ties in the hardware expectations.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Hardware expectations (C1.1–C1.3) threaded through Units 1–3; the principle added to the teaching approach, AGENTS.md, and decisions.md; a standard-library hardware program was tested.

---

## User Prompt 6

- **Timestamp:** 2026-11-14T13:14
- **Goal:** Remove the old extraction and draft the scope and sequence.
- **Summary:** Delete the unreliable section-by-section curriculum extraction and start the ICS3U scope and sequence.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Scope and sequence written as `site/scope-and-sequence.qmd`; expectation coverage verified by script; site build changed to a post-render copy from `site/_site/` into `docs/`.

---

## User Prompt 5

- **Timestamp:** 2026-11-14T13:12
- **Goal:** Replace the unusable curriculum extraction with a better source.
- **Summary:** The section-by-section extraction lacks usable text, so the author supplied a full-document Markdown conversion of the curriculum to use instead.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Full Markdown copied into `references/official-curriculum/`; ICS3U expectations transcribed and checked against rendered PDF pages 39–46 to create `ics3u-expectations.md`.

---

## User Prompt 4

- **Timestamp:** 2026-11-14T13:08
- **Goal:** Approve the project structure with a stronger reading-first emphasis.
- **Summary:** Approved the proposed folder structure and the PRIMM lesson model. Asked that reading code before writing code be the main teaching principle across lessons, worksheets, and assessments. Confirmed the built website should go in `docs/` for GitHub Pages.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Quarto project in `site/` renders to `../docs`.

---

## User Prompt 3

- **Timestamp:** 2026-11-14T13:07
- **Goal:** Correct the course code and locate the source PDF.
- **Summary:** Confirmed the course is ICS3U (Grade 11 Introduction to Computer Science, University Preparation), not ICS3M; the author will rename the project folder later. The original curriculum PDF is in the Downloads folder.
- **Host:** m4-mini
- **Agent:** Claude Code

---

## User Prompt 2

- **Timestamp:** 2026-11-14T13:06
- **Goal:** Set the sources, publishing stack, and teaching approach.
- **Summary:** Copy the extracted curriculum sections into a references folder. Publish a public Quarto website (chosen for its built-in search and easy organization) through GitHub Pages from a private repository, so private resources can live alongside the site source. Base the course on Python, with possible extensions in other languages. Emphasize reading code before writing it, and consider direct instruction unless there is a good argument against it. Teachers need editable, printable copies of worksheets and tests, likely through Google Docs, not PDF.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** The sections come from a PDF-to-Markdown export of the 2008 Ontario Computer Studies, Grades 10–12 curriculum.

---

## User Prompt 1

- **Timestamp:** 2026-11-14T13:04
- **Goal:** Define the project's purpose.
- **Summary:** Build a complete teacher-facing website for the Ontario ICS3U course (initially named ICS3M in error). It should give teachers every resource they need in one place: lesson plans, worksheets, quizzes, tests, and related materials, all aligned to the curriculum. The core workflow: an agent drafts course materials from the official curriculum, the author reviews and approves them, and teachers use the published site to find and use the resources.
- **Host:** m4-mini
- **Agent:** Claude Code
- **Technical context:** Project folder initialized with the AgenticProjectInitializer master prompt; the folder was empty at the start.
