import pandas as pd

# Load files
movies = pd.read_csv("data/movies_5000.csv")
credits = pd.read_csv("data/credits_5000.csv")

# Merge using title
merged = movies.merge(credits, on="title")

# Save new file
merged.to_csv("data/movies_5000_new.csv", index=False)

print("✅ Merge complete!")
print(merged.head())
