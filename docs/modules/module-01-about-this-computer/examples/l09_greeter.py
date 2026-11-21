import platform

name = input("What's your name? ")
print(f"Hi, {name}! This computer runs {platform.system()}.")
print(f"Its processor is {platform.machine()}.")
