import pandas as pd
import ast

# Load dataset
df = pd.read_csv("data/movies_5000.csv")


# Convert genres JSON to normal text
def convert(obj):
    L = []
    try:
        for i in ast.literal_eval(obj):
            L.append(i["name"])
    except:
        return ""
    return " ".join(L)


# Apply conversion
df["genres"] = df["genres"].apply(convert)

# Handle missing values
df["overview"] = df["overview"].fillna("")

# Create tags column
df["tags"] = df["overview"] + " " + df["genres"]

# Keep only required columns
new_df = df[["id", "title", "tags"]]

# Rename id → movie_id (optional but better)
new_df = new_df.rename(columns={"id": "movie_id"})

# Save processed file
new_df.to_csv("data/processed_movies.csv", index=False)

print("✅ Processed dataset created!")
print("Shape:", new_df.shape)
