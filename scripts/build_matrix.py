# Import pandas to handle our movie list
import pandas as pd

# Import the similarity tool from Scikit-Learn
from sklearn.metrics.pairwise import cosine_similarity

# Import the Vectorizer to create our movie DNA
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Load and clean the dataset
df = pd.read_csv("data/movies_5000.csv")
df["overview"] = df["overview"].fillna("")

# Step 2: Create the Vector Matrix (DNA for all movies)
# We limit to 5000 features to keep the math manageable for your PC
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
tfidf_matrix = tfidf.fit_transform(df["overview"])

# Step 3: CALCULATE THE FULL SIMILARITY MATRIX
# This compares every row in tfidf_matrix to every other row
# It creates a giant grid of (4803 x 4803) scores
print("⏳ Calculating the Relationship Map (This may take a few seconds)...")
similarity_matrix = cosine_similarity(tfidf_matrix)

# Step 4: Verify the results
print("--- Similarity Matrix Created ---")
# The shape should be square (Number of Movies by Number of Movies)
print(f"Matrix Shape: {similarity_matrix.shape}")

# Let's peek at the similarity score of the first movie with itself
# It should be 1.0 because every movie is 100% similar to itself!
print(f"Self-Similarity Check (Movie 0 vs Movie 0): {similarity_matrix[0][0]}")
