# Import pandas for our data inspection
import pandas as pd

# Import os to check if the file exists on the disk
import os

# Define the dataset path
file_path = "data/movies_5000.csv"


def run_data_audit():
    print("📋 STARTING DATA AUDIT CHECKPOINT...")
    print("-" * 40)

    # CHECK 1: Connectivity (Does the file exist?)
    if not os.path.exists(file_path):
        print("❌ FAILED: 'movies_5000.csv' not found in data folder.")
        return
    else:
        print("✅ PASS: Dataset file detected.")

    # Load the data for further checks
    df = pd.read_csv(file_path)

    # CHECK 2: Integrity (Are there Nulls in the critical 'overview' column?)
    # We count the missing values in 'overview'
    null_count = df["overview"].isnull().sum()
    if null_count == 0:
        print("✅ PASS: No missing values in 'overview'.")
    else:
        # Note: If this fails, it means you didn't save your cleaned version
        # but for this audit, we will just flag it.
        print(f"⚠️ WARNING: {null_count} movies are missing overviews.")

    # CHECK 3: Leaness (Are we keeping the right columns?)
    # Expected columns for our Content-Based Filtering engine
    required_cols = ["id", "title", "genres", "overview", "keywords"]
    # Check if these are all present
    found_cols = [col for col in required_cols if col in df.columns]

    if len(found_cols) == len(required_cols):
        print("✅ PASS: All critical feature columns are present.")
    else:
        print(f"❌ FAILED: Missing columns: {set(required_cols) - set(found_cols)}")

    print("-" * 40)
    print("AUDIT COMPLETE: Your data blueprints are ready for Phase 1: Module 3!")


# Run the function
if __name__ == "__main__":
    run_data_audit()
