# Import pandas to load our movie list
import pandas as pd

# Import the tools for our calculation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the clean dataset
df = pd.read_csv("data/processed_movies.csv")

# Initialize the vectorizer
tfidf = TfidfVectorizer(stop_words="english")

# Create the sparse matrix (Words to Numbers)
tfidf_matrix = tfidf.fit_transform(df["tags"])

# Calculate the Similarity Matrix (Movie to Movie)
similarity = cosine_similarity(tfidf_matrix)

# --- DEBUGGER STOP POINT ---
# We are creating a variable just so we have a place to put a breakpoint
final_shape = similarity.shape

# Print the shape to the terminal
print(f"The Matrix Shape is: {final_shape}")
# Print a specific coordinate (Row 0, Column 0)
print(f"Similarity of first movie with itself: {similarity[0][0]}")
# I have confirmed the matrix is a square grid of 4803 by 4803 elements.
