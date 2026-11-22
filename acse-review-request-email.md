# Draft email: ACSE list, looking for site reviewers

**Subject:** Looking for reviewers (teachers or a strong ICS4U student) for a free, open-source ICS3U Python course

---

Hi everyone,

I'm developing a free, open-source ICS3U course in Python, and I'm looking for a few people to help review it: to find mistakes, try the lessons out, and tell me what doesn't work.

The site is here: https://peter.beens.ca/ics3u/

**Who I'm hoping to find**

- **Teachers** who'd be willing to read a lesson or two with a critical eye.
- **A student doing independent work**, ideally an ICS4U student with a strong interest in Python, who could work through the lessons as a student would and report what's wrong or confusing. A TEJ4M student would also be a good fit, since the course leans heavily on hardware: processors, storage, networks, and benchmarking. This could make a good independent project. It's real reviewing work on a real course.

The one firm requirement for a student reviewer: **a standalone computer they fully control**, not a board-imaged lab machine. More on why below.

**What the course is about**

The course is built around the student's own computer. The first program students read reports the computer's processor type, not "Hello, World". From there, each module is a practical theme, and the programs students write are small utilities they could actually use:

1. About This Computer: asking the computer about itself
2. Spec Checker: will this program or game run on this machine?
3. Benchmark Lab: how fast is this computer?
4. Passwords and Secret Messages: password strength, hashing, why simple ciphers fail
5. On the Network: IP addresses, DNS, timing connections, logging results
6. Data Detective: scanning folders, finding what's filling the drive, verified backups
7. Software Development Project: a class project, then each student's own

Students build a "toolkit" of these programs across the semester. The course is also reading-first: students read, trace, and predict code before they modify it, and write their own code last. Every expectation in the 2008 curriculum is mapped. The full plan is on the Scope and Sequence page. Module 1 has three lessons built so far; the other modules have planned overviews.

**Why a standalone computer matters**

These programs do the things locked-down lab computers are set up to prevent: using the terminal, keeping files between classes, opening network connections, running a small web server, and creating and scanning folders of sample files. They also only mean something when they run on the computer in front of the student. A program that reports "this computer's" processor needs to run on a real computer, not on a server somewhere. Refurbished computers are ideal. The site's Before You Begin page has a table of what the programs need and what managed computers often block.

**Some features of the site**

- **Python in the browser.** Lessons use Pyodide, so students can run and edit code right on the page with nothing installed. Step-through boxes run a program one line at a time, showing the output and the variables as they change. That makes them good for predicting and tracing. (Browser Python is also a teaching point: it reports a different "computer" than the classroom machine, which leads to a lesson on where code actually runs.)
- **Downloadable Python files and Jupyter notebooks.** Every example program can be downloaded as a `.py` file to run in Thonny, IDLE, or VS Code. Each one is also a notebook.
- **Notebooks in Callysto or Colab.** Each notebook opens in Callysto or Google Colab with one click, for classes that need an online option.
- **Separate materials for teachers and students.** Lesson plans include teacher prompts and timings, students work from slides with speaker notes, and each lesson has a practice page. Answer keys are kept off the website.

**What I'd love feedback on**

- Mistakes of any kind: code that doesn't run, wrong output, typos, broken links
- Anything confusing, from a student's or a teacher's point of view
- Pacing: does a lesson really fit a 75-minute period?
- Ideas and recommendations for the modules that are still in the planning stage

**How to send feedback**

Every page has two links in the margin, and either one fills in the page you're on:

- **GitHub:** "Report an error or suggest a change" opens a short issue form, if you have a GitHub account. The repository is https://github.com/pbeens/ics3u (MIT licence).
- **Google Form:** "Send feedback privately" needs no account.

Or just reply to me directly. Even one or two comments help.

If you, or a student of yours, would be interested, please let me know. I'm happy to talk about what a review project could look like.

Thanks,

Peter Beens
