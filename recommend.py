# --- (Previous Load Engine Code remains above) ---
import pickle
import pandas as pd


def load_engine():
    # Loading logic from Topic 2
    with open("models/movies_list.pkl", "rb") as f:
        movies = pickle.load(f)
    with open("models/similarity.pkl", "rb") as f:
        similarity = pickle.load(f)
    return movies, similarity


# --- NEW TOPIC 3 CODE START ---


# Define a function to find the row number (index) of a movie
def find_movie_index(movie_title, movies_df):
    # Search the 'title' column for a match with the user's input
    # .iloc[0] ensures we get just the index value, not a whole series
    try:
        index = movies_df[movies_df["title"] == movie_title].index[0]
        # Return the numeric position
        return index
    except IndexError:
        # If the movie isn't in our 5k dataset, return None
        return None


# --- TESTING THE FINDER ---
if __name__ == "__main__":
    # Load the data
    movies_list, similarity_matrix = load_engine()

    # Test with a known movie
    target = "Iron Man"
    idx = find_movie_index(target, movies_list)

    if idx is not None:
        # Print the success message
        print(f"✅ Found it! '{target}' is located at Index: {idx}")
    else:
        # Print an error if misspelled or missing
        print(f"❌ Error: '{target}' was not found in our database.")
