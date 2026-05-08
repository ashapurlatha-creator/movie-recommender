# Import necessary libraries
import pickle
import pandas as pd


# Function to load our serialized data
def load_assets():
    with open("models/movies_list.pkl", "rb") as f:
        movies = pickle.load(f)  # Loading the movie list
    with open("models/similarity.pkl", "rb") as f:
        sim = pickle.load(f)  # Loading the similarity matrix
    return movies, sim


# Our main engine function
def get_recommendations(movie_name, movies_df, sim_matrix):
    # Find the index of the chosen movie
    idx = movies_df[movies_df["title"] == movie_name].index[0]

    # Get and sort similarity scores
    distances = sorted(
        list(enumerate(sim_matrix[idx])), reverse=True, key=lambda x: x[1]
    )

    # Slice the top 5 (skipping the first one)
    top_matches = distances[1:6]

    print(f"\nRecommendations for {movie_name}:")

    # The Loop: This is what we want to 'Watch'
    for match in top_matches:
        # We extract the title for the current match
        current_title = movies_df.iloc[match[0]].title
        # Print the title to terminal
        print(f"🎬 {current_title}")


# Execution block
if __name__ == "__main__":
    m_list, s_matrix = load_assets()
    get_recommendations("Iron Man", m_list, s_matrix)
