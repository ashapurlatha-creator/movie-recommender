# Import pandas to look at our data structures
import pandas as pd

# Define a mock row that looks like our real raw data
# Real data is often trapped in lists or has unnecessary spaces
raw_movie_row = {
    "title": "Iron Man",
    "genres": '[{"name": "Action"}, {"name": "Sci-Fi"}]',  # Messy JSON string
    "keywords": "marvel superhero billionaire",
    "overview": "After being held captive, Tony Stark builds a suit.",
    "cast": "Robert Downey Jr.",
}

# Step 1: The 'Unpacker' (Goal)
# We want to turn that messy 'genres' string into a simple list
clean_genres = ["Action", "Sci-Fi"]

# Step 2: The 'Normalizer' (Goal)
# We want to make sure 'Iron Man' and 'Action' are lowercase
overview_lower = raw_movie_row["overview"].lower()

# Step 3: The 'Blender' (The Pipeline Result)
# We merge everything into one long string of 'Tags'
tags = f"{overview_lower} {' '.join(clean_genres)} {raw_movie_row['keywords']} {raw_movie_row['cast']}"

print("--- Data Cleaning Pipeline Visualization ---")
print(f"RAW GENRES: {raw_movie_row['genres']}")
print(f"CLEANED GENRES: {clean_genres}")
print("-" * 30)
print(f"FINAL BLENDED TAGS FOR THE ENGINE:")
print(tags)
