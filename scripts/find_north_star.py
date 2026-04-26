# Import pandas to handle our movie table
import pandas as pd

# Import TfidfVectorizer to recreate our mathematical matrix
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Load the dataset
df = pd.read_csv("data/movies_5000.csv")

# Step 2: Clean the data just like we did in Module 3
df["overview"] = df["overview"].fillna("")

# Step 3: Create the Matrix (The 'DNA' of all movies)
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
tfidf_matrix = tfidf.fit_transform(df["overview"])

# Step 4: Define our North Star movie title
target_movie = "The Avengers"

# Step 5: Find the 'Index' (row number) of our North Star
# We look for the row where the title matches our target
try:
    movie_index = df[df["title"] == target_movie].index[0]

    # Step 6: Pull out the Vector for this specific movie
    # This is the list of numbers that represents 'Iron Man'
    north_star_vector = tfidf_matrix[movie_index]

    print(f"--- North Star Located: {target_movie} ---")
    print(f"Index Position: {movie_index}")
    print(f"Vector Shape: {north_star_vector.shape}")
    print("\nThis movie is now ready for head-to-head comparison!")

except IndexError:
    print(f"❌ Error: Movie '{target_movie}' not found in the dataset.")
    print("Check your spelling! (e.g., 'Avatar' or 'Spectre')")
