# Import the os module to handle file paths
import os

# Define the path to our mini dataset
# This tells Python to look inside the 'data' folder for our CSV
file_path = "data/mini_movies.csv"

# We open the file in 'read' mode (r)
with open(file_path, "r") as file:
    # Read all lines from the file and store them in a list
    lines = file.readlines()

# Print a header for our output
print("--- Raw CSV Data View ---")

# Loop through each line in the list
for line in lines:
    # Use .strip() to remove the hidden 'newline' character at the end
    # Use .split(',') to break the line into a list wherever a comma appears
    columns = line.strip().split(",")

    # Print the result so we can see the 'Tabular' structure
    print(columns)

# Final check: How many movies did we find? (Minus the header row)
print(f"\nTotal movies found: {len(lines) - 1}")
