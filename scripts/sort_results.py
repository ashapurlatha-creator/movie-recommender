# Import pandas to handle our lists
import pandas as pd

# Step 1: Create a mock list of movies and their similarity scores to 'Iron Man'
# Imagine these scores came from our Matrix calculation
data = {
    "movie_title": [
        "The Avengers",
        "Finding Nemo",
        "Iron Man 2",
        "Toy Story",
        "Guardians of the Galaxy",
        "Captain America",
        "Thor",
    ],
    "similarity_score": [0.92, 0.05, 0.98, 0.12, 0.85, 0.88, 0.80],
}

# Step 2: Turn this into a Pandas DataFrame (a table)
results_df = pd.DataFrame(data)

# Step 3: SORT the table
# ascending=False means we want the HIGHEST numbers at the top
sorted_results = results_df.sort_values(by="similarity_score", ascending=False)

# Step 4: FILTER the top 3 results
top_5 = sorted_results.head(5)

print("--- Unsorted Results (Raw Pile) ---")
print(results_df)

print("\n--- Sorted Recommendations (Top 5) ---")
# This is what the user will eventually see in our app!
print(top_5)
