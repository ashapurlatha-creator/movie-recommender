# Import the 'os' module to interact with the Operating System
import os

# Import the 'platform' module to see what kind of computer you are using
import platform

# Get the current folder path where the terminal is active
current_location = os.getcwd()

# Get the name of your Operating System (Windows, Mac, or Linux)
system_type = platform.system()

# Print a decorative separator
print("-" * 30)

# Print the name of your system
print(f"DEVICE DETECTED: {system_type}")

# Print the folder the terminal is currently 'looking' at
print(f"TERMINAL LOCATION: {current_location}")

# Print a tip for the student
print("TIP: If the location doesn't end in 'movie-recommender', your terminal is in the wrong place!")

# Print a closing decorative separator
print("-" * 30)

