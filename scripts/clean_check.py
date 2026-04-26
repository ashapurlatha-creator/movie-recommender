# Import the os module to look at our computer's folders
import os

# Define a function to check our workspace layout
def check_workspace():
    # Get the name of the folder we are currently sitting in
    current_folder = os.path.basename(os.getcwd())
    
    # List all the files and folders inside our project
    content_list = os.listdir('.')
    
    # Print a professional header
    print(f"--- Workspace Audit for: {current_folder} ---")
    
    # Check if we successfully created our 'scripts' folder
    if 'scripts' in content_list:
        print("SUCCESS: 'scripts' folder detected. Your workspace is organized!")
    else:
        print("WARNING: 'scripts' folder not found. Please check your Explorer sidebar.")

# This line tells the computer to run our function
if __name__ == "__main__":
    check_workspace()
