import platform

a = platform.node()
b = platform.system()
x2 = platform.python_version()
print(f"{a:<12}{b:<12}{x2}")
