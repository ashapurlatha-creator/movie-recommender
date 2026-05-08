# --- (Existing Load logic remains at the top) ---
import pickle
import pandas as pd

# Assume movies_list and similarity_matrix are already loaded via load_engine()


def recommend(movie):
    # The 'Try' block: Python attempts to run this code first
    try:
        # Step 1: Attempt to find the index of the movie
        # If the movie name doesn't exist, this line triggers an 'IndexError'
        index = movies_list[movies_list["title"] == movie].index[0]

        # Step 2: If found, proceed with our similarity logic
        distances = sorted(
            list(enumerate(similarity_matrix[index])), reverse=True, key=lambda x: x[1]
        )

        # Step 3: Print a success message
        print(f"✅ Success! Showing recommendations for: {movie}")

    # The 'Except' block: This runs ONLY if something goes wrong in the Try block
    except IndexError:
        # If the index wasn't found, we catch the error and print a friendly message
        print(
            f"❓ Sorry! '{movie}' isn't in our 5,000-movie database. Check your spelling!"
        )

    # Optional: Catching any other unexpected errors
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# --- TESTING THE SAFETY NET ---
if __name__ == "__main__":
    # We load the data once
    with open("models/movies_list.pkl", "rb") as f:
        movies_list = pickle.load(f)
    with open("models/similarity.pkl", "rb") as f:
        similarity_matrix = pickle.load(f)

    # Test 1: A valid movie
    recommend("Avatar")

    # Test 2: A typo or fake movie (This would normally crash the app!)
    recommend("Avangers 12")
