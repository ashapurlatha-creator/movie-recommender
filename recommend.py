# Import the tools we need
import pickle
import pandas as pd


# Load assets function
def load_assets():
    with open("models/movies_list.pkl", "rb") as f:
        movies = pickle.load(f)  # Load movie names
    with open("models/similarity.pkl", "rb") as f:
        sim = pickle.load(f)  # Load math scores
    return movies, sim


# Recommendation function
def get_recommendations(movie_name, movies_df, sim_matrix):
    # Find index of input movie
    idx = movies_df[movies_df["title"] == movie_name].index[0]
    # Get similarity row
    distances = sorted(
        list(enumerate(sim_matrix[idx])), reverse=True, key=lambda x: x[1]
    )
    # Take top 10 matches this time
    top_matches = distances[1:11]

    print(f"\nSearching for high-match relatives of {movie_name}...")

    # The Loop we will debug
    for match in top_matches:
        # 'match' is a tuple like (index, score)
        score = match[1]
        # --- WE WILL SET A CONDITIONAL BREAKPOINT ON THE LINE BELOW ---
        movie_title = movies_df.iloc[match[0]].title
        # Print the results
        print(f"Checking: {movie_title} (Score: {score})")


# Execution
if __name__ == "__main__":
    m_list, s_matrix = load_assets()
    get_recommendations("Iron Man", m_list, s_matrix)
