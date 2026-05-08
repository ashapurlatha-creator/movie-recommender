"""
Movie Recommendation Engine - Final Polished Version
Goal: Content-based filtering using Cosine Similarity.
"""

import pickle
import pandas as pd


def load_engine_assets():
    """Load the serialized dataframes and matrices from the models folder."""
    try:
        # Using a context manager to open both files safely
        with open("models/movies_list.pkl", "rb") as f_list, open(
            "models/similarity.pkl", "rb"
        ) as f_sim:
            return pickle.load(f_list), pickle.load(f_sim)
    except FileNotFoundError:
        # Professional error handling for missing files
        print("Error: Model files not found. Please run the training script.")
        return None, None


def get_recommendations(movie_title, movies_df, similarity_matrix):
    """
    Finds and prints the top 5 most similar movies based on input.
    """
    try:
        # Locate the numeric index for the requested movie
        movie_idx = movies_df[movies_df["title"] == movie_title].index[0]
        # Retrieve, sort, and slice the similarity scores
        # We skip index 0 as it is the movie itself
        similarity_scores = sorted(
            list(enumerate(similarity_matrix[movie_idx])),
            reverse=True,
            key=lambda x: x[1],
        )[1:6]

        print(f"\n--- Top Recommendations for {movie_title} ---")

        # Loop through the results and display titles
        for match in similarity_scores:
            print(f"🎬 {movies_df.iloc[match[0]].title}")

    except IndexError:
        print(f"❌ '{movie_title}' not found in database. Check spelling.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Initialize the engin
    movies, similarity = load_engine_assets()

    # If assets loaded successfully, run the query
    if movies is not None:
        get_recommendations("The Dark Knight Rises", movies, similarity)
