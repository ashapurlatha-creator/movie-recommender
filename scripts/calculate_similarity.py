# Import pandas for data loading
import pandas as pd

# Import the tool that turns text into a numerical matrix
from sklearn.feature_extraction.text import TfidfVectorizer

# Import the tool that calculates the 'angle' between movie vectors
from sklearn.metrics.pairwise import cosine_similarity

# Import 'time' to see how long this big calculation takes
import time

# Load our cleaned dataset from Module 6
df = pd.read_csv("data/processed_movies.csv")

# Initialize the Vectorizer with English stop words (ignoring 'the', 'is', etc.)
tfidf = TfidfVectorizer(stop_words="english")

# Transform the 'tags' column into a Sparse Matrix
tfidf_matrix = tfidf.fit_transform(df["tags"])

# --- THE BIG CALCULATION ---

print("🚀 Starting the Big Calculation (Comparing 4,803 movies)...")

# Record the start time
start = time.time()

# Run the cosine similarity function on our matrix
# This compares the matrix against itself
similarity = cosine_similarity(tfidf_matrix)

# Record the end time
end = time.time()

# Print the success message and time taken
print(f"✅ Finished! Calculation took {end - start:.2f} seconds.")

# Print the shape of the result
# It should be (4803, 4803) because it's a square grid of every movie vs every movie
print(f"📊 Similarity Matrix Shape: {similarity.shape}")
