# Import pandas to read our cleaned data
import pandas as pd

# Import the Vectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the processed dataset we exported in Module 6
df = pd.read_csv("data/processed_movies.csv")

# Step 1: Initialize the Vectorizer
# We use stop_words='english' to automatically ignore common words (the, a, is)
tfidf = TfidfVectorizer(stop_words="english")

# Step 2: Fit and Transform the data
# 'Fit' learns the vocabulary; 'Transform' calculates the weights (numbers)
tfidf_matrix = tfidf.fit_transform(df["tags"])

# Step 3: Inspect the 'Vocabulary'
# This is a list of every unique important word found in 5,000 movies
vocab = tfidf.get_feature_names_out()

# Print the total number of unique words found
print(f"✅ Total unique words in vocabulary: {len(vocab)}")

# Print a small slice of the vocabulary to see what the words look like
print("\n--- Sample of the Engine's Vocabulary ---")
# Display words from index 1000 to 1010
print(vocab[1000:1010])

# Step 4: Show the shape of the Matrix
# (Movies, Unique Words)
print(f"\n📊 Matrix Shape: {tfidf_matrix.shape}")
