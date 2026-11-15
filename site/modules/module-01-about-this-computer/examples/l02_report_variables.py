import platform

cpu = platform.machine()
system = platform.system()
name = platform.node()

print("Computer report for", name)
print("CPU type:", cpu)
print("Operating system:", system)
