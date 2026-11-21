import platform
import sys

text_version = platform.python_version()
minor = sys.version_info.minor
print(text_version, type(text_version))
print(minor, type(minor))
print("Next version: 3." + str(minor + 1))
print("New enough for this course:", minor >= 8)
