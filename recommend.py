# Import necessary tools
import pickle
import pandas as pd

# Standard loader function we've built
def load_assets():
    with open('models/movies_list.pkl', 'rb') as f:
        movies = pickle.load(f)
    with open('models/similarity.pkl', 'rb') as f:
        sim = pickle.load(f)
    return movies, sim

# Recommendation logic
def get_recommendations(movie_name, movies_df, sim_matrix):
    # --- STEP 1: SET A BREAKPOINT ON THE LINE BELOW ---
    idx = movies_df[movies_df['title'] == movie_name].index[0]
    
    # We will use the console to look at 'distances' before the code finishes
    distances = sim_matrix[idx]
    
    # Final sorting logic
    sorted_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    for i in sorted_list:
        print(movies_df.iloc[i[0]].title)

# Execution
if __name__ == "__main__":
    m_list, s_matrix = load_assets()
    get_recommendations("Batman Begins", m_list, s_matrix)
