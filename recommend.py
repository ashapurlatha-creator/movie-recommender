# Import the pickle library to load our binary brain files
import pickle

# Import pandas to handle the movie data table
import pandas as pd


# Define a function to load our assets
def load_engine():
    # Print a status message to the terminal
    print("⏳ Loading the Recommendation Engine...")

    # Open and load the movie list dictionary/dataframe
    # 'rb' stands for 'Read Binary'
    with open("models/movies_list.pkl", "rb") as f:
        movies = pickle.load(f)

    # Open and load the similarity matrix (the big math grid)
    with open("models/similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    # Return both items so the rest of the script can use them
    return movies, similarity


# --- START THE SCRIPT ---
# We check if this is the main file being run
if __name__ == "__main__":
    # Call the loader function and store the results in variables
    movies_list, similarity_matrix = load_engine()

    # Print a success message with the data size
    print(f"✅ Engine Ready! Loaded {len(movies_list)} movies.")

    # Display the first 5 movie titles to confirm the data is correct
    print("\n--- Preview of Movie Library ---")
    print(movies_list["title"].head())
