# Import the sys module to inspect the Python interpreter
import sys

# Import the os module to check file paths
import os

# Get the path of the Python 'executable' (the brain) being used
python_path = sys.executable

# Check if the string '.venv' exists in that path
is_virtual = '.venv' in python_path

# Print a professional status report
print("--- Environment Security Check ---")

# If '.venv' is in the path, we are successfully isolated
if is_virtual:
    print("STATUS: SUCCESS")
    print(f"Your project is safely isolated in: {python_path}")
else:
    print("STATUS: GLOBAL")
    print("WARNING: You are using the global Python. Please select the .venv interpreter.")

# Print the version of Python inside this specific environment
print(f"Environment Python Version: {sys.version.split()[0]}")

