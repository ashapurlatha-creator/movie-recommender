# Import necessary libraries for our engine
import pandas as pd  # Used for data manipulation
from sklearn.feature_extraction.text import TfidfVectorizer  # Used for text math
from sklearn.metrics.pairwise import cosine_similarity  # Used for comparison logic


# Function 1: Handle Data Loading with a Safety Net
def load_and_clean_data(path):
    try:
        # Load the CSV file from the provided path
        df = pd.read_csv(path)
        # Fill missing values in the overview column to prevent crashes
        df["overview"] = df["overview"].fillna("")
        # Return the clean dataframe
        return df
    except FileNotFoundError:
        # If the file is missing, print a helpful message
        print("❌ Error: The dataset file was not found!")
        return None


# Function 2: Perform the Vectorization (The Math Station)
def create_similarity_matrix(df):
    # Initialize the vectorizer with professional parameters
    tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
    # Transform text into a mathematical matrix
    tfidf_matrix = tfidf.fit_transform(df["overview"])
    # Calculate and return the full similarity grid
    return cosine_similarity(tfidf_matrix)


# Function 3: The Search Logic (The User Station)
def get_recommendations(movie_title, df, sim_matrix):
    try:
        # Find the row index of the movie the user typed
        idx = df[df["title"] == movie_title].index[0]
        # Get the list of similarity scores for that movie
        scores = list(enumerate(sim_matrix[idx]))
        # Sort scores from highest to lowest
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        # Return the top 3 (skipping the first one because it is the movie itself)
        return scores[1:4]
    except (IndexError, KeyError):
        # Handle cases where the movie is not found
        return "❌ Movie not found in database."


# --- MASTER LOGIC FLOW ---
# 1. Initialize data
movies = load_and_clean_data("data/movies_5000.csv")

# 2. If data loaded successfully, proceed
if movies is not None:
    # 3. Create the math engine
    matrix = create_similarity_matrix(movies)
    # 4. Test a search
    user_search = "Iron Man"
    recommendations = get_recommendations(user_search, movies, matrix)
    # 5. Output the result
    print(f"🎬 Recommendations for '{user_search}':")
    print(recommendations)
