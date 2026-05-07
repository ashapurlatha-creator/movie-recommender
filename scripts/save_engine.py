# Import the libraries we need for the final engine build
import pandas as pd  # To handle our movie table
import pickle  # To save our math to disk
from sklearn.feature_extraction.text import TfidfVectorizer  # For vectorization
from sklearn.metrics.pairwise import cosine_similarity  # For similarity calculation

# 1. Load the processed dataset from Module 6
print("📂 Loading clean data...")
df = pd.read_csv("data/processed_movies.csv")

# 2. Run the Vectorization (Turn tags into numbers)
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["tags"])

# 3. Calculate the Similarity Matrix (The heavy math)
print("🧠 Calculating similarity scores...")
similarity = cosine_similarity(tfidf_matrix)

# 4. Save the Movie List (We need this to match IDs to Titles later)
# We convert the dataframe to a dictionary to make it easier to load in the web app
print("💾 Saving movie list...")
with open("models/movies_list.pkl", "wb") as f:
    pickle.dump(df, f)  # Dump the dataframe into a file

# 5. Save the Similarity Matrix (The Engine's Brain)
print("💾 Saving similarity matrix... this might take a moment.")
with open("models/similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)  # Dump the big math grid into a file

print("✨ Done! Your engine is now saved in the 'models' folder.")
