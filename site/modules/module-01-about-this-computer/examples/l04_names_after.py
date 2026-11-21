# Prints one row of a lab inventory: computer name, OS, Python version.
# Columns are 12 characters wide so rows from different computers line up.
import platform

computer_name = platform.node()
os_name = platform.system()
python_version = platform.python_version()
print(f"{computer_name:<12}{os_name:<12}{python_version}")
