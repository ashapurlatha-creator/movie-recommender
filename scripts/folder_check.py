# Import the 'os' module to check our computer's file system
import os

# Define a list of the folders we expect to see in a professional project
required_folders = ["data", "scripts", "notebooks", "models", ".venv"]

# Start a report message
print("--- Professional Structure Audit ---")

# Loop through each folder name in our list
for folder in required_folders:
    # Check if the folder exists in our current location
    if os.path.exists(folder):
        # Print a success message if the folder is found
        print(f"[FOUND]: {folder} - Great job!")
    else:
        # Print a helpful warning if a folder is missing
        print(f"[MISSING]: {folder} - Please create this folder in the Sidebar.")

# Count how many files are currently inside the 'scripts' folder
script_count = len(os.listdir('scripts'))
# Display the count to the user
print(f"Total scripts organized: {script_count}")

