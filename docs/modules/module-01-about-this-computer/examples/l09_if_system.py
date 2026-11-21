import platform

system = platform.system()
if system == "Windows":
    print("Open File Explorer to see your files.")
elif system == "Darwin":
    print("Open Finder to see your files.")
else:
    print("Open your file browser to see your files.")
print("Your course folder is called ics3u.")
