# Import only what we need
import pickle
import pandas as pd


# Optimized loader: We load everything in one clear step
def load_assets():
    # Opening files in 'rb' (read binary) mode
    with open("models/movies_list.pkl", "rb") as f_list, open(
        "models/similarity.pkl", "rb"
    ) as f_sim:
        # Returning both immediately to save lines of code
        return pickle.load(f_list), pickle.load(f_sim)


# Refactored recommendation function
def get_recommendations(movie_name, movies_df, sim_matrix):
    try:
        # Find index - we do this in one line
        idx = movies_df[movies_df["title"] == movie_name].index[0]

        # REFACTOR: Instead of creating 5 temporary variables, we chain the logic.
        # We enumerate, sort, and slice [1:6] all in one smooth motion.
        distances = sorted(
            list(enumerate(sim_matrix[idx])), reverse=True, key=lambda x: x[1]
        )[1:6]

        # Clean output for the user (Removed all the "Debug" print statements)
        print(f"\n--- Recommendations for {movie_name} ---")

        # Final loop to print just the titles
        for i in distances:
            # Print only the essential result
            print(movies_df.iloc[i[0]].title)

    except Exception:
        # A simple, clean error message for the user
        print("Movie not found. Please try again.")


# Optimized execution block
if __name__ == "__main__":
    # Load assets once
    m_df, s_mat = load_assets()

    # Run a test query
    get_recommendations("Batman Begins", m_df, s_mat)
