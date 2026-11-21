import platform

system = platform.system()
version = platform.python_version()
print(f"{'LAB REPORT':^20}")
print(f"{'System:':<10}{system}")
print(f"{'Python:':<10}{version}")
print(f"Python {version} is running on {system}.")
