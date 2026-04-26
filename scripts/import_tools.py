# Import pandas to handle our movie table
import pandas as pd

# From the Scikit-Learn library, import the text-to-math tool (TfidfVectorizer)
from sklearn.feature_extraction.text import TfidfVectorizer

# From the Scikit-Learn library, import the similarity calculator (cosine_similarity)
from sklearn.metrics.pairwise import cosine_similarity


# Define a function to verify our 'Industrial Tools' are working
def system_check():
    try:
        # Load the clean dataset we created in Module 6
        df = pd.read_csv("data/processed_movies.csv")

        # Initialize our 'Crane' (The Vectorizer)
        # stop_words='english' tells the tool to ignore boring words like 'the' or 'is'
        tfidf = TfidfVectorizer(stop_words="english")

        # Initialize our 'Laser Level' (A dummy check)
        # We are just checking if the function is recognized
        check_math = cosine_similarity

        # If we reached this point without an error, the tools are ready
        print("✅ Industrial Tools Imported Successfully!")
        print(f"✅ Dataset with {len(df)} movies loaded and ready for math.")

    except Exception as e:
        # If something is missing, this will tell us what went wrong
        print(f"❌ System Check Failed: {e}")


# Call the function to run the check
system_check()
