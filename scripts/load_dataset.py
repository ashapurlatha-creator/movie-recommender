# Import the pandas library to read the spreadsheet
import pandas as pd

# Define the path to where our file is sitting
file_path = "data/movies_5000.csv"

# Use pandas to load the CSV data into a 'DataFrame' (a table)
# We wrap this in a try/except block to catch 'File Not Found' errors
try:
    # Load the dataset
    movies_df = pd.read_csv(file_path)

    # Print a success message
    print("✅ Dataset loaded successfully!")

    # Check the 'Shape' (Rows, Columns) of the data
    # This tells us if we actually have all 4803 movies
    print(f"📊 Dataset Dimensions: {movies_df.shape}")

    # Look at the 'Columns' to see what kind of data we have
    print(f"📋 Columns found: {list(movies_df.columns)}")

    # Display the first 3 rows to see the raw data
    print("\n--- Quick Peek at Data ---")
    print(movies_df[["title", "genres", "vote_average"]].head(3))

except FileNotFoundError:
    # This runs if the file isn't in the 'data' folder
    print("❌ ERROR: Could not find 'movies_5000.csv' in the 'data' folder.")
