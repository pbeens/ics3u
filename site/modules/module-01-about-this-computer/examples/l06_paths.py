import os

folder = os.getcwd()
print("Running in:", folder)
print("This folder's name:", os.path.basename(folder))
print("The folder it's inside:", os.path.dirname(folder))
print(os.path.join(folder, "toolkit", "report_card.py"))
