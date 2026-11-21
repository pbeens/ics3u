"""
Make a realistic, messy sample folder for the course's file lessons.

Usage (run from your ics3u course folder):

    python3 make_sample_folder.py            # builds ./sample-folder
    python3 make_sample_folder.py --seed 42  # a different folder, same kind of mess
    python3 make_sample_folder.py --reset    # delete the old one and rebuild it

On Windows, type py instead of python3.

The folder holds text notes, CSV data, Python programs, log files, real PNG
images, WAV sounds, zip archives, sub-folders, awkward file names, duplicate
files, and files with old dates. With the same seed, everyone gets exactly the
same folder, down to the dates, so answers can be checked.

Safety: the script only ever deletes a folder that it made itself (one that
contains its marker file, .sample-folder). It never touches anything else.

Uses only Python's standard library. Needs Python 3.8 or later.
"""

import argparse
import datetime
import math
import os
import random
import shutil
import struct
import sys
import wave
import zipfile
import zlib

MARKER = ".sample-folder"
DEFAULT_SEED = 2026
DEFAULT_FOLDER = "sample-folder"
# Dates are measured back from a fixed day, not from today, so the same seed
# gives the same dates whenever the folder is built.
REFERENCE_DAY = datetime.datetime(2026, 9, 1, 12, 0, 0)

FIRST_NAMES = ["sam", "alex", "jordan", "priya", "wei", "maya", "omar", "lucas", "ava", "noah"]
SUBJECTS = ["math", "science", "english", "history", "french", "cs", "art", "music"]
TOPICS = ["cells", "volcanoes", "poetry", "fractions", "the-war-of-1812", "robots",
          "climate", "budgets", "photosynthesis", "binary"]
COMPUTERS = ["LAB-PC-01", "LAB-PC-02", "LAB-PC-07", "LAB-PC-14", "LIBRARY-03", "OFFICE-MAC"]


def make_png(width, height, colour, rng):
    """
    Return the bytes of a small, valid PNG image: a coloured background with
    random noise, so files differ in size the way real photos do.
    """
    rows = bytearray()
    for _ in range(height):
        rows.append(0)  # PNG filter type 0 (none) for each row
        for _ in range(width):
            for channel in colour:
                rows.append(max(0, min(255, channel + rng.randint(-40, 40))))

    def chunk(kind, data):
        """
        Wrap data in a PNG chunk: length, type, data, and checksum.
        """
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)  # 8-bit RGB
    # Level 0 stores the pixels without compressing them. Compressed bytes can
    # differ between zlib versions, and every computer must build the same file.
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header)
            + chunk(b"IDAT", zlib.compress(bytes(rows), 0)) + chunk(b"IEND", b""))


def write_wav(path, seconds, pitch):
    """
    Write a short WAV file: a pure tone at the given pitch (in hertz).
    """
    rate = 8000
    with wave.open(path, "wb") as sound:
        sound.setnchannels(1)
        sound.setsampwidth(2)
        sound.setframerate(rate)
        frames = bytearray()
        for i in range(int(rate * seconds)):
            value = int(12000 * math.sin(2 * math.pi * pitch * i / rate))
            frames += struct.pack("<h", value)
        sound.writeframes(bytes(frames))


def notes_text(rng, subject, topic):
    """
    Return a few lines of class notes.
    """
    lines = [f"{subject.title()} notes: {topic.replace('-', ' ')}", ""]
    for number in range(1, rng.randint(4, 12)):
        lines.append(f"{number}. Point about {topic.replace('-', ' ')} (see page {rng.randint(10, 300)})")
    return "\n".join(lines) + "\n"


def csv_text(rng, rows):
    """
    Return CSV data: daily screen time for one student, in minutes.
    """
    lines = ["date,school_minutes,gaming_minutes,video_minutes"]
    day = REFERENCE_DAY - datetime.timedelta(days=rows)
    for _ in range(rows):
        day += datetime.timedelta(days=1)
        lines.append(f"{day:%Y-%m-%d},{rng.randint(30, 240)},{rng.randint(0, 180)},{rng.randint(0, 200)}")
    return "\n".join(lines) + "\n"


def python_text(rng, number):
    """
    Return a short Python program, as a student might have saved it.
    """
    item = rng.choice(["RAM stick", "SSD", "mouse", "keyboard", "monitor"])
    return (f"# Practice program {number}\n"
            f"price = {rng.randint(10, 300)}.99\n"
            f"print(\"The {item} costs\", price)\n")


def log_text(rng, computer, lines):
    """
    Return a system log with timestamped lines.
    """
    events = ["started", "user logged in", "update installed", "disk check passed",
              "Wi-Fi reconnected", "user logged out", "shut down"]
    moment = REFERENCE_DAY - datetime.timedelta(days=30)
    result = []
    for _ in range(lines):
        moment += datetime.timedelta(minutes=rng.randint(5, 600))
        result.append(f"{moment:%Y-%m-%d %H:%M} {computer} {rng.choice(events)}")
    return "\n".join(result) + "\n"


class Builder:
    """
    Creates the files, remembers each one's date, and counts what it made.
    """

    def __init__(self, root, rng):
        self.root = root
        self.rng = rng
        self.dates = {}
        self.files = 0
        self.bytes = 0

    def path(self, *parts):
        """
        Return a path inside the sample folder, making its folder if needed.
        """
        full = os.path.join(self.root, *parts)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        return full

    def add(self, parts, data, days_old):
        """
        Write a file (text or bytes) and remember how old it should look.
        """
        full = self.path(*parts)
        mode = "w" if isinstance(data, str) else "wb"
        with open(full, mode, **({"encoding": "utf-8", "newline": "\n"} if mode == "w" else {})) as f:
            f.write(data)
        self.remember(full, days_old)

    def remember(self, full, days_old):
        """
        Record a file's age; dates are applied at the end, after all writing.
        """
        self.dates[full] = days_old
        self.files += 1
        self.bytes += os.path.getsize(full)

    def age(self, low, high):
        """
        Return a random age in days, with a random time of day.
        """
        return self.rng.randint(low, high) + self.rng.random()

    def apply_dates(self):
        """
        Set every file's modified time to its remembered age.
        """
        for full, days_old in self.dates.items():
            moment = REFERENCE_DAY - datetime.timedelta(days=days_old)
            stamp = moment.timestamp()
            os.utime(full, (stamp, stamp))


def build(root, seed):
    """
    Fill root with the sample files for this seed. Returns the Builder.
    """
    rng = random.Random(seed)
    b = Builder(root, rng)

    # Documents: notes with tidy and untidy names.
    for _ in range(rng.randint(28, 36)):
        subject, topic = rng.choice(SUBJECTS), rng.choice(TOPICS)
        name = rng.choice([
            f"{subject}-{topic}.txt",
            f"{subject.title()} {topic.replace('-', ' ').title()} FINAL.txt",
            f"{topic}_notes_v{rng.randint(1, 4)}.txt",
            f"{subject} {topic} ({rng.randint(1, 3)}).txt",
        ])
        b.add(["documents", subject, name], notes_text(rng, subject, topic), b.age(1, 900))
    b.add(["documents", "My Essay FINAL (2).txt"], notes_text(rng, "english", "poetry"), b.age(20, 60))
    b.add(["documents", "README.md"], "# Documents\n\nSchool work, sorted (mostly) by subject.\n", b.age(400, 500))

    # Data: CSV files of different lengths.
    for name in FIRST_NAMES[:rng.randint(5, 8)]:
        b.add(["data", f"screen-time-{name}.csv"], csv_text(rng, rng.randint(14, 120)), b.age(1, 200))
    b.add(["data", "lab-power-readings.csv"], csv_text(rng, 365), b.age(5, 15))

    # Photos: real PNG images, some in dated sub-folders, some duplicated.
    photos = []
    for year in (2023, 2024, 2025):
        for _ in range(rng.randint(14, 22)):
            number = rng.randint(1000, 9999)
            colour = (rng.randint(30, 225), rng.randint(30, 225), rng.randint(30, 225))
            side = rng.choice([32, 48, 64, 96, 128])
            data = make_png(side, side, colour, rng)
            parts = ["photos", str(year), f"IMG_{number}.png"]
            b.add(parts, data, (2026 - year) * 365 - rng.randint(0, 300) + rng.random())
            photos.append((parts, data))
    for parts, data in rng.sample(photos, 8):  # duplicates with "copy" names
        stem = parts[-1][:-4]
        copy_name = rng.choice([f"{stem} (1).png", f"{stem} copy.png", f"Copy of {stem}.png"])
        b.add(["photos", "to-sort", copy_name], data, b.age(1, 300))

    # Music: short WAV tones (the biggest files in the folder).
    for i in range(rng.randint(5, 9)):
        full = b.path("music", f"track-{i + 1:02d}.wav")
        write_wav(full, rng.uniform(4, 25), rng.choice([220, 262, 330, 392, 440, 523]))
        b.remember(full, b.age(100, 1500))

    # Projects: Python programs, including near-identical versions.
    for i in range(rng.randint(12, 18)):
        b.add(["projects", f"practice_{i + 1:02d}.py"], python_text(rng, i + 1), b.age(10, 400))
    for name in ["report_card.py", "report_card_old.py", "report card FINAL.py"]:
        b.add(["projects", "report-card", name],
              "import platform\n\nprint(\"Report card for\", platform.node())\n", b.age(30, 90))

    # Logs: one per computer, plus an old archive of them.
    for computer in COMPUTERS:
        b.add(["logs", f"{computer.lower()}.log"], log_text(rng, computer, rng.randint(40, 400)), b.age(0, 10))
    archive = b.path("logs", "old-logs.zip")
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_STORED) as z:
        for computer in COMPUTERS[:4]:
            # A fixed date inside the zip, so the same seed gives the same bytes.
            entry = zipfile.ZipInfo(f"{computer.lower()}-2024.log", date_time=(2024, 12, 31, 23, 0, 0))
            z.writestr(entry, log_text(rng, computer, 300))
    b.remember(archive, b.age(500, 700))

    # Downloads: the usual mess, including big files that are just filler.
    for name in ["setup-installer.bin", "game-patch.bin", "driver-update.bin"]:
        size = rng.randint(300_000, 2_000_000)
        b.add(["downloads", name], rng.getrandbits(size * 8).to_bytes(size, "little"), b.age(1, 700))
    for i in range(rng.randint(6, 12)):
        b.add(["downloads", f"download ({i}).txt"], notes_text(rng, "misc", rng.choice(TOPICS)), b.age(1, 365))
    b.add(["downloads", "photos-backup.zip"], b"", b.age(30, 60))  # an empty file

    # Old stuff: files untouched for years.
    for i in range(rng.randint(6, 10)):
        b.add(["old-stuff", f"old-notes-{i + 1}.txt"], notes_text(rng, rng.choice(SUBJECTS), rng.choice(TOPICS)),
              b.age(1500, 3000))

    # An empty folder: real folders have these too.
    os.makedirs(os.path.join(root, "empty-folder"), exist_ok=True)

    b.apply_dates()
    return b


def prepare(root, reset):
    """
    Make sure root is safe to build in. Returns an error message, or None.
    """
    if not os.path.exists(root):
        return None
    if not os.path.isdir(root):
        return f"{root} exists and is a file, not a folder. Choose another name."
    if os.path.exists(os.path.join(root, MARKER)):
        if not reset:
            return f"{root} already exists. To delete it and build it again, add --reset."
        shutil.rmtree(root)
        return None
    if os.listdir(root):
        return (f"{root} already exists and wasn't made by this script, so it won't be touched. "
                "Choose another folder name.")
    return None


def main():
    """
    Read the options, check the folder is safe, build it, and report.
    """
    parser = argparse.ArgumentParser(description="Make a realistic, messy sample folder for file lessons.")
    parser.add_argument("folder", nargs="?", default=DEFAULT_FOLDER,
                        help=f"folder to create (default: {DEFAULT_FOLDER})")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED,
                        help=f"a number that decides the contents (default: {DEFAULT_SEED}, the same for everyone)")
    parser.add_argument("--reset", action="store_true",
                        help="delete a sample folder made earlier by this script, then rebuild it")
    args = parser.parse_args()

    root = os.path.abspath(args.folder)
    problem = prepare(root, args.reset)
    if problem:
        print(problem)
        sys.exit(1)

    os.makedirs(root, exist_ok=True)
    with open(os.path.join(root, MARKER), "w", encoding="utf-8") as f:
        f.write(f"Made by make_sample_folder.py with seed {args.seed}. Safe to delete.\n")
    b = build(root, args.seed)

    print(f"Made {b.files} files ({b.bytes / 1_000_000:.1f} MB) in {root}")
    print(f"Seed: {args.seed}. The same seed always makes the same folder.")


if __name__ == "__main__":
    main()
