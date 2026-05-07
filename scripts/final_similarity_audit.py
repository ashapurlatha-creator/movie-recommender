# Import pandas for data handling
import pandas as pd

# Import the vectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

# Import the similarity formula
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load and prepare the real data
df = pd.read_csv("data/movies_5000.csv")
df["overview"] = df["overview"].fillna("")
df["genres"] = df["genres"].fillna("")
df["keywords"] = df["keywords"].fillna("")

# Combine important text columns
df["tags"] = (
    df["overview"].astype(str)
    + " "
    + df["genres"].astype(str)
    + " "
    + df["keywords"].astype(str)
)

# Step 2: Create the Vector Matrix
tfidf = TfidfVectorizer(stop_words="english", max_features=10000)
tfidf_matrix = tfidf.fit_transform(df["tags"])

# Step 3: Calculate the full Similarity Matrix
# This is the heavy lifting we learned in Topic 6
sim_matrix = cosine_similarity(tfidf_matrix)


# Step 4: THE AUDIT FUNCTION
def run_audit(movie_a_title, movie_b_title):
    try:
        # Find the index for both movies
        idx_a = df[df["title"] == movie_a_title].index[0]
        idx_b = df[df["title"] == movie_b_title].index[0]

        # Look up their pre-calculated similarity score in our matrix
        score = sim_matrix[idx_a][idx_b]

        print(f"📊 AUDIT: Comparing '{movie_a_title}' and '{movie_b_title}'")
        print(f"📐 Mathematical Score: {round(score, 4)}")

        # Validation Logic
        if score > 0.2:
            print("✅ PASS: The engine recognizes these movies are related.")
        else:
            print("❌ FAIL: The score is too low. Check your vectorization settings.")

    except IndexError:
        print("❌ ERROR: One of the movies was not found. Check your spelling!")


# Step 5: Execute the Sanity Check
print("--- Starting Module 4 Final Audit ---")
run_audit("Iron Man", "Avengers: Age of Ultron")
run_audit("Iron Man", "Finding Nemo")
