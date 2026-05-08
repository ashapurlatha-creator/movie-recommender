# Import the tools we need
import pickle
import pandas as pd


# Function to load saved data
def load_assets():
    with open("models/movies_list.pkl", "rb") as f:
        movies = pickle.load(f)  # Read the movie dataframe
    with open("models/similarity.pkl", "rb") as f:
        sim = pickle.load(f)  # Read the similarity matrix
    return movies, sim  # Send them back to the caller


# The function we will 'Step' through
def get_recommendations(movie_name, movies_df, sim_matrix):
    # Step 1: Find index
    idx = movies_df[movies_df["title"] == movie_name].index[0]

    # Step 2: Get similarity row
    distances = sim_matrix[idx]

    # Step 3: Enumerate and Sort
    # Watch how this variable changes as you step over it!
    sorted_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]

    # Step 4: Final loop
    for i in sorted_list:
        print(movies_df.iloc[i[0]].title)  # Print the names one by one


# Main logic
if __name__ == "__main__":
    m_list, s_matrix = load_assets()  # Calling the loader
    get_recommendations("Batman Begins", m_list, s_matrix)  # Calling the engine
