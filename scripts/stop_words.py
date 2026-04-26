# Import the CountVectorizer tool from Scikit-Learn
from sklearn.feature_extraction.text import CountVectorizer

# Import pandas to help us compare the results
import pandas as pd

# Our sample movie descriptions (Notice all the 'the', 'is', 'a')
movie_plots = [
    "The movie is a space battle in a galaxy far away",
    "This is a fast car chase in the city",
    "A space explorer finds a new galaxy",
]

# --- STEP 1: Vectorizer WITHOUT Stop-Words (The Noisy Way) ---
vec_noisy = CountVectorizer()
matrix_noisy = vec_noisy.fit_transform(movie_plots)

# --- STEP 2: Vectorizer WITH English Stop-Words (The Professional Way) ---
# We just add one parameter: stop_words='english'
vec_clean = CountVectorizer(stop_words="english")
matrix_clean = vec_clean.fit_transform(movie_plots)

# --- STEP 3: Compare the Results ---
print(f"Total words found WITH noise: {len(vec_noisy.get_feature_names_out())}")
print(f"Total words found WITHOUT noise: {len(vec_clean.get_feature_names_out())}")

print("\nWords ignored by the machine (Noise):")
# We use the set difference to see what was removed
noise = set(vec_noisy.get_feature_names_out()) - set(vec_clean.get_feature_names_out())
print(sorted(list(noise)))

print("\nMeaningful 'Tags' remaining:")
print(vec_clean.get_feature_names_out())
