# Import pandas for our data table
import pandas as pd


# --- THE DRY STATION (The reusable function) ---
# We define a function that handles the cleaning task once
def clean_column(dataframe, column_name):
    # Fill any empty cells in the specified column with "Unknown"
    dataframe[column_name] = dataframe[column_name].fillna("Unknown")
    # Tell the user which column was just fixed
    print(f"✨ Cleaned the {column_name} column!")
    # Return the fixed dataframe
    return dataframe


# --- THE PROCESS ---

# 1. Load our movie dataset
df = pd.read_csv("data/movies_5000.csv")

# 2. Instead of writing '.fillna' over and over for different columns...
# We just call our 'video recording' (the function)
df = clean_column(df, "overview")
df = clean_column(df, "tagline")
df = clean_column(df, "homepage")
df = clean_column(df, "original_language")

# 3. Prove it worked by showing the top 5 rows of these columns
print("\n--- Cleaning Complete ---")
print(df[["title", "overview", "tagline"]].head())
