"""
Mirror every lesson example program as a Jupyter notebook.

Reads site/modules/module-NN-*/examples/lLL_name.py and writes
notebooks/NN-LL-name.ipynb with a read-first scaffold: a title cell,
a read-and-predict prompt, a prediction cell, the program, and a
compare prompt. Notebooks whose source program no longer exists are
removed. Run from anywhere:

    python3 scripts/build_notebooks.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "site" / "modules"
OUT = ROOT / "notebooks"
GENERATED = re.compile(r"^\d{2}-\d{2}-[a-z0-9-]+\.ipynb$")


def front_matter(path):
    """
    Return the lesson's title, subtitle, and expectation codes from its YAML header.
    """
    text = path.read_text(encoding="utf-8")
    header = text.split("---", 2)[1]
    info = {"title": "", "subtitle": "", "expectations": ""}
    for line in header.splitlines():
        key, _, value = line.partition(":")
        key = key.strip()
        if key in ("title", "subtitle"):
            info[key] = value.strip().strip('"')
        elif key == "expectations":
            info[key] = ", ".join(c.strip() for c in value.strip(" []").split(","))
    return info


def lesson_file(module_dir, lesson):
    """
    Find the lesson page (not the slides) for a two-digit lesson number.
    """
    for path in sorted(module_dir.glob(f"lesson-{lesson}-*.qmd")):
        if not path.stem.endswith("-slides"):
            return path
    raise FileNotFoundError(f"No lesson-{lesson} page in {module_dir}")


def markdown(text):
    """
    Build a markdown cell.
    """
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code(text):
    """
    Build an empty-output code cell.
    """
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text.rstrip("\n").splitlines(keepends=True),
    }


def build(program, lesson_info, rel_source):
    """
    Return the notebook dictionary for one example program.
    """
    source = program.read_text(encoding="utf-8")
    name = program.stem.split("_", 1)[1]
    is_mistake = name.startswith("mistake")
    heading = name.replace("_", " ").capitalize()
    heading = re.sub(r"\bcpu\b", "CPU", heading, flags=re.IGNORECASE)
    if is_mistake:
        heading = "Mistake: " + name.split("_", 1)[1].replace("_", " ")

    title = (
        f"# {heading}\n\n"
        f"**{lesson_info['subtitle']}** · {lesson_info['title']}  \n"
        f"**Expectations:** {lesson_info['expectations']}\n\n"
        f"*Generated from `{rel_source}`. Edit that file, not this notebook.*\n"
    )

    if is_mistake:
        predict = (
            "## Read and predict\n\n"
            "This program has a mistake. Read it **without running it**. "
            "What will happen when it runs: will it print something, show an error, or both? "
            "Write your prediction in the cell below.\n"
        )
        compare = (
            "## Compare\n\n"
            "Run the code cell. Was your prediction right?\n\n"
            "- If there is an error, read it from the bottom up: what type of error is it, "
            "and which line does it point to?\n"
            "- Fix the mistake, then run it again.\n"
        )
    else:
        predict = (
            "## Read and predict\n\n"
            "Read the code below **without running it**. What will it print? "
            "Write your prediction in the cell below.\n"
        )
        compare = (
            "## Compare\n\n"
            "Run the code cell. Was your prediction right? "
            "If not, which line surprised you, and why?\n"
        )

    if "platform" in source:
        compare += (
            "\n> **Where does this code run?** In Colab or the Callysto Hub, `platform` "
            "describes a server in a data centre, not the computer in front of you.\n"
        )

    cells = [
        markdown(title),
        markdown(predict),
        markdown("*My prediction:*\n"),
        code(source),
        markdown(compare),
    ]
    for number, cell in enumerate(cells, start=1):
        cell["id"] = f"cell-{number}"

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main():
    """
    Generate all notebooks and remove stale ones.
    """
    OUT.mkdir(exist_ok=True)
    written = set()
    for module_dir in sorted(MODULES.glob("module-[0-9][0-9]-*")):
        module = module_dir.name.split("-")[1]
        for program in sorted((module_dir / "examples").glob("l[0-9][0-9]_*.py")):
            lesson = program.stem[1:3]
            info = front_matter(lesson_file(module_dir, lesson))
            name = program.stem.split("_", 1)[1].replace("_", "-")
            target = OUT / f"{module}-{lesson}-{name}.ipynb"
            notebook = build(program, info, program.relative_to(ROOT).as_posix())
            target.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            written.add(target.name)
            print(f"wrote {target.relative_to(ROOT)}")
    for old in OUT.glob("*.ipynb"):
        if GENERATED.match(old.name) and old.name not in written:
            old.unlink()
            print(f"removed {old.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
