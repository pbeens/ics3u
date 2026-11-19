# Teaching Approach

## Core Principle: Read Before You Write

Students read code before they write code. Every new concept is first met through reading, tracing, and predicting what existing code does. Writing new code from scratch comes last.

This is the main emphasis of the course, not a warm-up activity. It shapes the order of every lesson, the opening of every worksheet, and a required section of every quiz and test.

## Start Deep, Through Reading

Reading first means students can meet real, interesting code well before they could write it themselves. Use that: choose authentic examples over toy ones, and don't be afraid to start deep.

- The first `print()` lesson reads a program that reports the computer's own CPU type (`platform.machine()`) rather than printing "Hello, World".
- Deep, but one new thing at a time: start from a single line and one library, and add pieces gradually. Lessons 1–2 use only the `platform` module; other modules come later, one per lesson.
- Students are not expected to explain every line of a deep example on day one. They predict, run, and investigate the parts they can, and the rest becomes a reason to keep learning.
- Tie examples to other curriculum expectations where it fits naturally, such as hardware (C1), data representation (A1.2), or environmental impact (D1).
- Deep does not mean long: reading examples stay short enough to trace by hand.

## Spiral, Not Silos

The course is organized as a spiral, not as topic units. There is no "output unit" followed by an "input unit" and a "decisions unit".

- Modules are built around themes and anchor programs (e.g., About This Computer, Benchmark Lab), and each one uses most programming ideas at once.
- Every idea moves through four levels over the course: **read** it in existing code, **modify** code that uses it, **write** new code with it, then **design** with it in a project. The spiral table in the scope and sequence shows where each idea sits in each module.
- Reading examples may use ideas not yet taught explicitly. The teacher names them briefly ("this is a loop; we'll write our own later") and keeps going.
- This is not project-based learning: lessons stay teacher-led and structured, and the independent project comes at the end.
- **Spiral does not mean skipping practice.** Basics get deliberate practice until they are automatic: each module has a Skill Builder page of short drills, and small graded Quick Builds before the module assignment.
- **Retrieval across modules.** Every Review stage includes at least one question on something from two or more lessons back, often an earlier module. Module tests include a short basics section.
- **One growing toolkit.** Each module's assignment adds a part to the student's own "My Computer Toolkit", so students keep reopening and improving their earlier code instead of starting fresh each time.

## Practical First

Every assignment should pass one test: *would someone who isn't taking a programming course have a reason to use this program?* Games and puzzles can appear as short activities, but module assignments are useful tools.

- Open each lesson with the useful problem, not the construct: "How could we check 500 files without opening each one?" rather than "Today we learn `for` loops." Then show a working program and follow PRIMM.
- Use Python's standard library almost exclusively. Third-party libraries (e.g., Pillow) appear only as marked extensions.
- File work happens in a generated sample folder (`make_sample_folder.py`, planned), never in students' own files, unless an extension says otherwise.

## Why

- **Reading and tracing come before writing.** Studies of novice programmers found that many students who could not write working code also could not reliably trace or explain short code. Tracing and explaining ability is strongly related to writing ability (Lister et al., 2004; Lopez et al., 2008).
- **Novices learn more from explicit instruction and worked examples** than from open-ended discovery (Sweller & Cooper, 1985; Kirschner et al., 2006).
- **Direct instruction principles** — daily review, small steps, modelling, guided practice, checking for understanding, independent practice — give the lesson its shape (Rosenshine, 2012).
- **PRIMM** (Predict, Run, Investigate, Modify, Make) puts reading ahead of writing within each lesson (Sentance et al., 2019).

## Lesson Sequence

Times are a guide for a 75-minute period. A concept may span more than one lesson; the order stays the same.

| Stage | Who | What happens | Guide |
|---|---|---|---|
| 1. Review | Students | Short retrieval questions on earlier material, often reading or tracing code; at least one from two or more lessons back. Then the teacher poses the lesson's useful problem. | 5–10 min |
| 2. Teach | Teacher | Direct instruction: introduce the concept with a worked example, reading the code aloud and tracing it with a think-aloud. | 10–15 min |
| 3. Predict | Students | Read a new short program and write down what it will output, *before* running it. | 5–10 min |
| 4. Run | Students | Run the program and compare the result with their prediction. | 5 min |
| 5. Investigate | Students | Trace tables, line-by-line questions, explain the code in plain English. | 10–15 min |
| 6. Modify | Students | Change the existing program to do something slightly different. | 10–15 min |
| 7. Make | Students | Write a new program using the concept — only after stages 3–6. | 10–20 min |
| 8. Check | Students | Exit ticket: one reading or tracing question that shows whether the concept landed. | 5 min |

Over the course, the balance shifts: early modules are mostly reading (stages 3–5), and later modules give more time to Modify, Make, and independent projects (strand B4).

## Code-Reading Activity Types

Use a mix of these in lessons, worksheets, and assessments:

- **Predict the output** — read code, write the exact output.
- **Trace table** — track each variable's value line by line.
- **Explain in plain English** — describe what the code does in one or two sentences, not line by line.
- **Spot the bug** — find and explain the error in a short program.
- **Annotate** — add comments explaining each part.
- **Compare two versions** — explain how two programs differ in behaviour.
- **Parsons problem** — put scrambled lines of code in the correct order (a bridge between reading and writing).
- **Complete the code** — fill in missing lines in an otherwise finished program.

## Rules for Materials

- **Lessons** follow the sequence above. The first student activity is reading code, never writing it.
- **Predict and Run** happen together in the step-through box, so the prediction stays next to the real output. The box isn't saved.
- **Where answers go:** students write predictions, trace tables, and short answers in a paper *tracing notebook* (never just "notebook", which means Jupyter here). Anything handed in has its written answers as comments in the `.py` file; assignments supply a starter file with a space for each answer. Longer written parts (test plans, structure charts, protection plans, project documents) are handed in as documents: Word and fillable PDF versions are planned. Every reading task says where to write, and students save everything in their course folder (`site/course-folder.qmd`).
- **Worksheets** open with reading tasks (predict, trace, explain) before any writing tasks.
- **Quizzes and tests** include a code-reading and tracing section.
- **Code examples** are short enough to trace by hand and run on Python 3 exactly as shown.
- Each lesson lists the curriculum expectation codes it addresses (from `references/official-curriculum/ics3u-expectations.md`).

## Teacher Prompts

A teacher prompt is a short, scripted thing for the teacher to say aloud at a key moment. Prompts are most important the **first time** students meet a tool or idea: the step-through box and its colours, the Variables panel, an error message.

- On lesson pages, write prompts as a callout: `::: {.callout-tip title="Teacher prompt"}`. Add the occasion to the title when it helps, e.g. `Teacher prompt: the Variables panel (first use)`.
- Write them in the teacher's voice, in quotation marks, short enough to say in under a minute.
- On slides, put the same prompt in the speaker notes, starting with `TEACHER PROMPT`, so it is not projected.
- Teacher Notes (at the end of each lesson) are different: background for planning, not words to say.

## Step-Through Box

The predict-and-step box (`{{< stepper >}}`) is the main tool for the Predict and Run stages. Students type a prediction beside the code, then press **Step** to run one line at a time. The colours are used consistently across the course:

- **Yellow with a red arrow:** the next line to run.
- **Green:** the line that just ran.
- **Red:** the line where the program stopped with an error.

It runs real programs in the browser, including modules such as `platform`. Python Tutor remains available (`{{< pytutor >}}`) for programs that use only the modules it allows.

## Lesson Page Template

```md
---
title: "Lesson title"
expectations: [A2.1, A2.3]
---

(callout) For teachers banner: students use the slides, code files, and practice page
(callout) Time · Expectations · Slides · Previous/Next
## At a Glance             (big idea, students will, students make, prepare, after class, where it fits)
## Learning Goals
## Success Criteria
## Review
## Teach (worked example)
## Predict, Then Run   (step-through box: {{< stepper file="examples/....py" >}})
## Investigate
## Modify
## Make
## Check (exit ticket)
## After the Lesson       (practice link; what to look for in the exit tickets)
## Code for This Lesson   ({{< lesson-code >}}: .py downloads, notebooks, Open in Callysto | Colab)
## Teacher Notes
## Feedback               ({{< feedback >}}: link to the GitHub feedback form)
```

Each module also has an overview page (`index.qmd`, for teachers), a Practice page (students; one section per lesson, reading first, with `{{< lesson-code lesson="NN" hide="exit_ticket" >}}`), and an Assignment page (students). Slides end with an "After class" slide that links to the practice.

## References

- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. <https://doi.org/10.1207/s15326985ep4102_1>
- Lister, R., Adams, E. S., Fitzgerald, S., Fone, W., Hamer, J., Lindholm, M., McCartney, R., Moström, J. E., Sanders, K., Seppälä, O., Simon, B., & Thomas, L. (2004). A multi-national study of reading and tracing skills in novice programmers. In *Working Group Reports from ITiCSE on Innovation and Technology in Computer Science Education* (pp. 119–150). ACM. <https://doi.org/10.1145/1044550.1041673>
- Lopez, M., Whalley, J., Robbins, P., & Lister, R. (2008). Relationships between reading, tracing and writing skills in introductory programming. In *Proceedings of the Fourth International Workshop on Computing Education Research* (pp. 101–112). ACM. <https://doi.org/10.1145/1404520.1404531>
- Rosenshine, B. (2012). Principles of instruction: Research-based strategies that all teachers should know. *American Educator, 36*(1), 12–19, 39. <https://eric.ed.gov/?id=EJ971753>
- Sentance, S., Waite, J., & Kallia, M. (2019). Teaching computer programming with PRIMM: A sociocultural perspective. *Computer Science Education, 29*(2–3), 136–176. <https://doi.org/10.1080/08993408.2019.1608781>
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. <https://doi.org/10.1207/s1532690xci0201_3>
