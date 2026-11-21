# Course tools

Programs students download and run, published with the site (listed under `resources` in `site/_quarto.yml`). Not example programs, so they aren't mirrored as notebooks.

- `make_sample_folder.py`: builds a realistic, messy sample folder for file lessons (Module 1 Lesson 6, Module 6). Standard library only, Python 3.8+. The same seed always gives a byte-identical folder, with the same dates (measured from a fixed reference day), so answer keys can give exact counts and sizes. PNG data and the zip archive are stored uncompressed so the bytes don't depend on the zlib version. It deletes only folders containing its `.sample-folder` marker. Planned: `--download`.

Test after any change: build twice with the same seed and compare file hashes and dates; build with another seed and confirm it differs; confirm it refuses an unmarked folder.
