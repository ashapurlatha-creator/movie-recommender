# Import the pandas library with the nickname 'pd'
import pandas as pd

# Define the file path to our 5000 movies dataset
# Ensure the file name matches exactly what is in your 'data' folder
file_path = "data/movies_5000.csv"

# Tell Pandas to read the CSV and store it in a variable called 'df'
# 'df' stands for 'DataFrame' - your new digital spreadsheet
df = pd.read_csv(file_path)

# Print a professional status message
print("--- Movie Database Loaded Successfully ---")

# Use 'shape' to see how many rows and columns we have
# Result will look like (rows, columns)
print(f"Total Movies (Rows): {df.shape[0]}")
print(f"Data Points per Movie (Columns): {df.shape[1]}")

# Use 'columns' to see the names of all the information we have
# This shows things like 'budget', 'genres', 'overview', etc.
print("\nHere are the columns available to our engine:")
print(df.columns.tolist())

# Use 'head()' to show only the first 3 rows so we don't overwhelm the terminal
print("\nPeeking at the first 3 movies:")
print(df[["title", "vote_average"]].head(3))
