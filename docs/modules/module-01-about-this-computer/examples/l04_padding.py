import platform

title = "SYSTEM BANNER"
name = platform.node()
system = platform.system()

print("+----------------------------+")
print(f"|{title:^28}|")
print(f"| Name:   {name:<18} |")
print(f"| System: {system:<18} |")
print("+----------------------------+")
