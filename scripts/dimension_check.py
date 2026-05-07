# Import pandas for data loading
import pandas as pd

# Import the Vectorizer to create our high-dimensional data
from sklearn.feature_extraction.text import TfidfVectorizer

# Import the similarity tool
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the dataset
df = pd.read_csv("data/movies_5000.csv")
df["overview"] = df["overview"].fillna("")

# Step 2: Create a High-Dimensional Vector Matrix (5000 features)
# Every movie is now a point in a 5,000-dimensional space!
tfidf = TfidfVectorizer(max_features=5000, stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["overview"])

# Step 3: Calculate similarity
# We are doing 4803 x 4803 comparisons across 5000 dimensions
sim_matrix = cosine_similarity(tfidf_matrix)

# Step 4: Stop point for the debugger
print("--- Check the Variables View Now ---")
print(f"Matrix Rows: {sim_matrix.shape[0]}")
print(f"Matrix Columns: {sim_matrix.shape[1]}")
