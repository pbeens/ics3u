import os

home = os.path.expanduser("~")
course = os.path.join(home, "ics3u")
print("Home folder:", home)
print("Course folder:", course)
print("Course folder exists:", os.path.isdir(course))
print("Last part:", os.path.basename(course))
