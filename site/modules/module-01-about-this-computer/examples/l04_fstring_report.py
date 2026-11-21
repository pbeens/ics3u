import platform

name = platform.node()
cpu = platform.machine()
print(f"Name: {name}")
print(f"CPU: {cpu}")
print(f"{name} has a {cpu} processor.")
print("{name} has a {cpu} processor.")
