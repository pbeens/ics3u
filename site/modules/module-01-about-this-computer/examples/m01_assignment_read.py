import platform

name = platform.node()
cpu = platform.machine()
print("Report card for", name)
print("CPU:", cpu)
cpu = "unknown"
print("Checked:", cpu)
