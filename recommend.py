import pickle
import pandas as pd

with open("models/movies_list.pkl", "rb") as f:
    movies_list = pickle.load(f)

with open("models/similarity.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)


# --- (Previous logic for loading, indexing, and enumerating remains above) --
# This is a sample of our 'stapled_scores' from Topic 5
# Format: [(Index, Score), (Index, Score), ...]
user_input = "Avatar"

movie_idx = movies_list[movies_list["title"] == user_input].index[0]
similarity_row = similarity_matrix[movie_idx]
stapled_scores = list(enumerate(similarity_row))

# --- NEW TOPIC 6 LOGIC START ---

# We use the 'sorted' function to reorganize our list
# 1. 'reverse=True' means we want Descending order (Highest score first)
# 2. 'key=lambda x: x[1]' tells Python: "Sort by the second item in the pair (the score)"
sorted_matches = sorted(stapled_scores, reverse=True, key=lambda x: x[1])
# Print the results to see the 'Winners'
print("--- Sorting Results ---")
print(sorted_matches[:3])
# Explain the winner
winner_index = sorted_matches[0][0]  # Get the index of the top match
winner_score = sorted_matches[0][1]  # Get the score of the top match
print(f"\n🏆 The winner is Movie Index {winner_index} with a score of {winner_score}")
top_5_indices = sorted_matches[1:6]

print("--- The Final 5 Recommendations (Indices & Scores) ---")
print(top_5_indices)

print("\nRec # | Movie Index | Similarity")

for i, movie in enumerate(top_5_indices):
    print(f"  {i+1}   |      {movie[0]}      |    {movie[1]}")
