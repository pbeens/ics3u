"""
Mirror the rendered Quarto site (site/_site) into the repository's docs/ folder.

Quarto runs this automatically after every render (post-render in _quarto.yml),
so GitHub Pages always serves an exact copy of the latest build.
"""
import shutil
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent
SOURCE = SITE_DIR / "_site"
TARGET = SITE_DIR.parent / "docs"

if not SOURCE.is_dir():
    raise SystemExit(f"Rendered site not found: {SOURCE}")

if TARGET.exists():
    shutil.rmtree(TARGET)
shutil.copytree(SOURCE, TARGET)
print(f"Copied {SOURCE} -> {TARGET}")
