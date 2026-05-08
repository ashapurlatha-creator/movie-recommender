# Import the necessary libraries
import pickle  # For loading our saved matrix and list
import pandas as pd  # For handling our movie data


# Function to load our pre-calculated brain
def load_assets():
    # Load the movie list dataframe
    with open("models/movies_list.pkl", "rb") as f:
        movies = pickle.load(f)
    # Load the similarity scores matrix
    with open("models/similarity.pkl", "rb") as f:
        sim = pickle.load(f)
    return movies, sim  # Return both to the main script


# The core recommendation engine function
def get_recommendations(movie_name, movies_df, sim_matrix):
    try:
        # Step 1: Find the index of the movie provided by the user
        idx = movies_df[movies_df["title"] == movie_name].index[0]

        # Step 2: Get the similarity row for that index and enumerate it
        # This staples (index, score) pairs together
        score_series = list(enumerate(sim_matrix[idx]))

        # Step 3: Sort the list based on the score (index 1 of the tuple)
        # reverse=True puts the highest scores at the top
        sorted_scores = sorted(score_series, reverse=True, key=lambda x: x[1])

        # Step 4: Slice the list to get the top 5 (skipping index 0)
        top_matches = sorted_scores[1:6]

        # Step 5: Display the results
        print(f"\n🎬 Recommendations for '{movie_name}':")
        for match in top_matches:
            # Look up the title using the index (match[0])
            print(f"✨ {movies_df.iloc[match[0]].title}")

    except IndexError:
        # Handle cases where the movie isn't in our dataset
        print(f"\n❌ Error: '{movie_name}' not found. Please check spelling!")


# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    # Load assets into variables
    m_list, s_matrix = load_assets()

    # THE FINAL TEST: The course goal query
    get_recommendations("The Dark Knight", m_list, s_matrix)
    # Bonus Test: Try a different genre
    get_recommendations("The Lion King", m_list, s_matrix)
