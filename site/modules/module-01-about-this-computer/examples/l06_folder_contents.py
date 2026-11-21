import os

folder = os.getcwd()
items = os.listdir(folder)
print(f"{folder} has {len(items)} items")
print("Is there a toolkit folder?", os.path.isdir("toolkit"))
