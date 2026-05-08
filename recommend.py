# --- (Existing Load logic remains at the top) ---
import pickle
import pandas as pd

# Assume movies_list and similarity_matrix are loaded via load_engine()


def recommend(movie):
    try:
        # Step 1: Find the index of the user's movie
        index = movies_list[movies_list["title"] == movie].index[0]

        # Step 2: Get the similarity scores and sort them (stapled with indices)
        # We take the slice [1:6] to get the top 5 matches (skipping the movie itself)
        distances = sorted(
            list(enumerate(similarity_matrix[index])), reverse=True, key=lambda x: x[1]
        )
        top_5 = distances[1:6]

        # Step 3: The Display Header
        print(f"\n🌟 Because you liked '{movie}', you might also enjoy:")
        print("-" * 40)

        # --- NEW TOPIC 9 LOGIC START ---

        # Step 4: The Final Loop
        # We iterate through each 'tuple' (pair) in our top_5 list
        for i in top_5:
            # i[0] is the index of the recommended movie
            recommended_movie_index = i[0]

            # Use .iloc to find the title at that specific index in our DataFrame
            movie_title = movies_list.iloc[recommended_movie_index].title

            # Print the title to the terminal
            print(f"🎬 {movie_title}")

        print("-" * 40)

    except IndexError:
        print(f"❓ Movie '{movie}' not found. Please check your spelling!")


# --- TESTING THE FULL ENGINE ---
if __name__ == "__main__":
    # Ensure variables are populated
    with open("models/movies_list.pkl", "rb") as f:
        movies_list = pickle.load(f)
    with open("models/similarity.pkl", "rb") as f:
        similarity_matrix = pickle.load(f)

    # Test the final display logic
recommend("The Dark Knight Rises")
