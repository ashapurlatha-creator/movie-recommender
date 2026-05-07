# Import pandas to manage our movie table
import pandas as pd

# Define the file path
file_path = "data/movies_5000.csv"

# Load the full dataset
df = pd.read_csv(file_path)

# List out the columns we want to investigate
# We are looking for 'Content' columns
potential_features = [
    "genres",
    "id",
    "keywords",
    "title",
    "overview",
    "cast",
    "crew",
    "runtime",
]

# Create a new, smaller table (DataFrame) with just these columns
# This is called 'Subsetting'
movies = df[potential_features]

# Print the top 5 rows of our selected features
print("--- Selected Features for the Engine ---")
print(movies.head())

# Let's see how much memory we saved by dropping useless columns
print("\n--- Efficiency Check ---")
print(f"Original Column Count: {df.shape[1]}")
print(f"Feature Column Count: {movies.shape[1]}")
