# Import the pandas library to save our data
import pandas as pd

# Mock data representing our final cleaned dataset from this module
data = {
    "movie_id": [19995, 285],
    "title": ["Avatar", "Pirates of the Caribbean"],
    "tags": [
        "action adventure fantasy marine soldier alien",
        "adventure fantasy ocean captain pirate",
    ],
}

# Create a DataFrame (The table we worked so hard to clean)
df_clean = pd.DataFrame(data)

# Step 1: Define the export path
# We save it in the 'data' folder with a new name
export_path = "data/processed_movies.csv"

# Step 2: Export the file
# index=False ensures we don't add an extra column of row numbers
df_clean.to_csv(export_path, index=False)

# Step 3: Verification print
print(f"✅ Success! Your clean data has been saved to: {export_path}")

# Step 4: Prove we can load the clean file back
test_load = pd.read_csv(export_path)
print("\n--- Verifying Exported File ---")
print(test_load.head())
