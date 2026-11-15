# Notebooks

Every lesson example program, mirrored as a Jupyter notebook. These are not published on the site. Share them with students directly (e.g., Google Drive, or by uploading to Colab or the Callysto Hub).

- **Names:** `MM-LL-name.ipynb`, where `MM` is the module and `LL` is the lesson. For example, `01-02-report-variables.ipynb` mirrors `site/modules/module-01-about-this-computer/examples/l02_report_variables.py`.
- **Layout (read first):** a title cell (module, lesson, expectations), a "Read and predict" prompt, a cell for the student's prediction, the program, and a "Compare" prompt. Programs named `mistake_*` get prompts about reading the error and fixing it.
- **Generated:** don't edit these by hand. Change the `.py` file in the module's `examples/` folder, then run:

```sh
python3 scripts/build_notebooks.py
```

The script rewrites every notebook and removes any whose program no longer exists.
