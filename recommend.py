# Import the necessary libraries
import pickle # For loading our saved matrix and list
import pandas as pd # For handling our movie data

# Function to load our pre-calculated brain
def load_assets():
    # Load the movie list dataframe
    with open('models/movies_list.pkl', 'rb') as f:
        movies = pickle.load(f)
    # Load the similarity scores matrix
    with open('models/similarity.pkl', 'rb') as f:
        sim = pickle.load(f)
    return movies, sim # Return both to the main script

# The core recommendation engine function
def get_recommendations(movie_name, movies_df, sim_matrix):
    # --- WE WANT TO SET A BREAKPOINT ON THE LINE BELOW ---
    idx = movies_df[movies_df['title'] == movie_name].index[0] # Step 1: Find index
    
    # After pausing, we can check if 'idx' is correct before sorting
    score_series = list(enumerate(sim_matrix[idx])) # Step 2: Get similarity row
    
    sorted_scores = sorted(score_series, reverse=True, key=lambda x: x[1]) # Step 3: Sort
    
    top_matches = sorted_scores[1:6] # Step 4: Slice top 5
    
    print(f"\n🎬 Recommendations for '{movie_name}':") # Step 5: Header
    for match in top_matches: # Step 6: Loop through results
        print(f"✨ {movies_df.iloc[match[0]].title}") # Print titles

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    m_list, s_matrix = load_assets() # Load the assets
    get_recommendations("Avatar", m_list, s_matrix) # Run the test query

