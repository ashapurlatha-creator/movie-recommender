# Import the tools we need
import pickle  # Used for loading our serialized files
import pandas as pd  # Used for data manipulation


# Function to load our pre-calculated data
def load_assets():
    # Load the movie list from the models folder
    with open("models/movies_list.pkl", "rb") as f:
        movies = pickle.load(f)
    # Load the similarity scores matrix
    with open("models/similarity.pkl", "rb") as f:
        sim = pickle.load(f)
    # Return both assets to the caller
    return movies, sim


# Function to generate recommendations
def get_recommendations(movie_name, movies_df, sim_matrix):
    # --- SET BREAKPOINT HERE ---
    # We want to see how we arrived at this specific line of logic
    idx = movies_df[movies_df["title"] == movie_name].index[0]

    # Calculate similarity row
    distances = sim_matrix[idx]

    # Sort and slice top 5
    sorted_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]

    # Print results to terminal
    for i in sorted_list:
        print(f"🎬 {movies_df.iloc[i[0]].title}")


# The 'Entry Point' of our script
if __name__ == "__main__":
    # First, we call the loader
    m_list, s_matrix = load_assets()

    # Next, we call the engine
    # This is the 'Parent' call that starts the stack for the engine
    get_recommendations("Avatar", m_list, s_matrix)
