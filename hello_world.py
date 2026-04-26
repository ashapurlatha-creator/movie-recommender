# Import the sys module to talk to your computer's system
import sys

# Define a variable to hold a greeting message
greeting = "Welcome to your Movie Engine Workspace!"

# Define a list of the 3 main tools we will use in VS Code
tools = ["Editor", "Terminal", "Source Control"]

# Print the greeting to the terminal
print(greeting)

# Print the specific version of Python your VS Code is using
print("You are running Python version: " + sys.version)

# Use a loop to print out each tool in our list
for tool in tools:
    print("Mastering tool: " + tool)

# Print a final confirmation message
print("System Check Complete. You are ready to build!")

