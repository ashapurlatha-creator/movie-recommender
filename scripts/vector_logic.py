# Import the specialized tool for turning text into numbers
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Create a small 'Mini-Dataset' to visualize the logic
mini_data = {
    "title": ["Iron Man", "The Avengers", "The Lion King"],
    "tags": [
        "superhero billionaire marvel tech",
        "superhero marvel aliens team",
        "lion king jungle animation prince",
    ],
}

# Load this into a DataFrame
df = pd.DataFrame(mini_data)

# Step 1: Initialize the 'Vectorizer'
# This is our translator that turns words into coordinates
vectorizer = TfidfVectorizer()

# Step 2: Transform the 'tags' column into a Matrix of numbers
# This is the 'Vectorization' step
tfidf_matrix = vectorizer.fit_transform(df["tags"])

# Step 3: See the 'Vocabulary' the computer created
# Every word gets an ID number (a coordinate direction)
print("--- Vocabulary (Word Directions) ---")
print(vectorizer.get_feature_names_out())

# Step 4: Show the Matrix (The GPS Coordinates)
# Each row represents a movie; each column represents a word
print("\n--- The Vector Matrix ---")
print(tfidf_matrix.toarray())

# Note: In a real dataset, most numbers will be 0.0 because
# a single movie doesn't contain every single word in the world!
