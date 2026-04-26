# Import pandas to manage our data structures
import pandas as pd

# Define the file path
file_path = "data/movies_5000.csv"

# Load the full dataset into memory
df = pd.read_csv(file_path)

# List the 'High-Value' columns that describe a movie's content
# We keep 'id' and 'title' to identify the movie
# We keep 'genres', 'keywords', and 'overview' to build our recommendations
columns_to_keep = ["movie_id", "title", "overview", "genres", "keywords"]

# Create a new, filtered DataFrame containing only our survivors
# Note: Ensure 'movie_id' matches the column name in your CSV (some use 'id')
df_lean = df[["id", "title", "overview", "genres", "keywords"]]

# Print a professional summary of the operation
print("--- Data Slimming Operation ---")
print(f"Columns before: {len(df.columns)}")
print(f"Columns after:  {len(df_lean.columns)}")

# Display the first few rows to verify the columns are correct
print("\nFinal Lean Dataset Preview:")
print(df_lean.head())

# Show memory usage comparison
print("\n--- Memory Usage Comparison ---")
print(f"Original: {df.memory_usage().sum() / 1024:.2f} KB")
print(f"Lean:     {df_lean.memory_usage().sum() / 1024:.2f} KB")
