# Import pandas to help us look up the index of a movie
import pandas as pd

# Import pickle to load our 'Warehouse Ledger'
import pickle

# --- STEP 1: LOAD THE ASSETS ---
# Load our movie list (The warehouse map)
with open("models/movies_list.pkl", "rb") as f:
    movies = pickle.load(f)

# Load our similarity matrix (The scores ledger)
with open("models/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# --- STEP 2: THE INDEX LOOKUP ---
# The user wants a recommendation for 'Avatar'
user_choice = "Avatar"

# Find the row number (index) where 'Avatar' lives in our table
# We look for the row where the 'title' column matches the user choice
movie_index = movies[movies["title"] == user_choice].index[0]

print(f"✅ User selected: {user_choice}")
print(f"📍 Location in Warehouse (Index): {movie_index}")

# --- STEP 3: ACCESS THE SCORES ---
# Pull the specific row of scores for Avatar
# This row contains 4,803 numbers (one for every movie)
distances = similarity[movie_index]

print(f"📊 Number of scores retrieved: {len(distances)}")
print(f"🔢 First 5 similarity scores in this row: {distances[0:5]}")

# --- STEP 4: THE CONCEPT OF SORTING (PREVIEW) ---
# We will sort these scores in the next lesson to find the Top 5
print("\nNext Step: We will sort these numbers to find the highest matches!")
