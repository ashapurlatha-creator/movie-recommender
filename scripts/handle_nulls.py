# Import pandas to manage our movie table
import pandas as pd

# Define the file path
file_path = "data/movies_5000.csv"

# Load the dataset
df = pd.read_csv(file_path)

# --- TASK 1: THE NULL HUNT ---
# .isnull() finds holes, and .sum() counts them up for each column
null_report = df.isnull().sum()

print("--- Missing Data Report (Before Cleaning) ---")
print(null_report)

# --- TASK 2: VISUAL INSPECTION ---
# We use a dummy variable to pause here for the VS Code Variables view
check_point = "Open the Variables View now"

# --- TASK 3: CLEANING ---
# We will drop rows where the 'overview' is missing
# because we can't recommend a movie without a description!
df_cleaned = df.dropna(subset=["overview"])

# Verify the fix
print("\n--- Missing Data Report (After Cleaning) ---")
print(df_cleaned.isnull().sum())

# Final tally
print(f"\nMovies removed due to missing descriptions: {len(df) - len(df_cleaned)}")
