# Import the pandas library
import pandas as pd

# Load the full dataset
df = pd.read_csv("data/movies_5000.csv")

# Print the original column count
print(f"Initial columns: {len(df.columns)}")

# Define the 'Dead Weight' - columns that don't help with tags
# We don't need money, homepage links, or release dates for basic tag matching
dead_weight = [
    "budget",
    "homepage",
    "original_language",
    "original_title",
    "popularity",
    "production_companies",
    "production_countries",
    "release_date",
    "revenue",
    "runtime",
    "spoken_languages",
    "status",
    "tagline",
    "vote_average",
    "vote_count",
]

# Use .drop to remove these columns
# 'axis=1' tells pandas to look for column names, not row numbers
df_slim = df.drop(columns=dead_weight)

# Print the new column count
print(f"Columns after dropping dead weight: {len(df_slim.columns)}")

# Show the remaining 'Essential' columns
print("\n--- Essential Columns Remaining ---")
print(df_slim.columns.tolist())

# Pro-tip: Check your VS Code 'Variables' view while debugging to see memory usage drop!
