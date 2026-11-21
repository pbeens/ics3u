system = "Linux"
if system == "Windows":
    print("Start menu")
elif system == "Darwin":
    print("Dock")
else:
    print("Panel")
print(type(system == "Linux"))
