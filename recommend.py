# --- (Previous load_engine and find_movie_index code remains above) ---
import pickle
import pandas as pd

# 1. Load the engine assets (Movie list and Matrix)
with open("models/movies_list.pkl", "rb") as f:
    movies_list = pickle.load(f)
with open("models/similarity.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

# 2. Let's pick a target movie (Simulating user input)
user_input = "Iron Man"

# 3. Use our function from Topic 3 to find the Index
movie_idx = movies_list[movies_list["title"] == user_input].index[0]

# --- NEW TOPIC 4 LOGIC START ---

# 4. Extract the single row of similarity scores for 'Iron Man'
# We use the movie_idx to tell the matrix which row we want
similarity_row = similarity_matrix[movie_idx]

# 5. Print the results to verify
print(f"✅ Successfully accessed row for: {user_input}")
print(f"📊 Total scores in this row: {len(similarity_row)}")

# 6. Take a peek at the first 10 scores
# These are the decimals representing 'closeness'
print(f"🔢 Sample scores: {similarity_row[:10]}")

# Note: One of these scores will be 1.0 (The movie's similarity to itself!)
