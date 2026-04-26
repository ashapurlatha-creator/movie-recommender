# Import the professional similarity tool from Scikit-Learn
from sklearn.metrics.pairwise import cosine_similarity

# Import numpy to create our sample vectors
import numpy as np

# Let's define two movie vectors: [Action, Sci-Fi, Adventure]
# Movie A: 'Iron Man'
movie_a = np.array(
    [[10, 10, 5]]
)  # We use double brackets [[ ]] because the tool expects a 2D grid

# Movie B: 'The Avengers' (Very similar to Iron Man)
movie_b = np.array([[10, 8, 10]])

# Movie C: 'Finding Nemo' (Not similar at all)
movie_c = np.array([[0, 0, 10]])
movie_d = np.array([[10, 10, 5]])
# Task 1: Calculate similarity between Iron Man and Avengers
# This returns a grid, so we take the first value [0][0]
score_ab = cosine_similarity(movie_a, movie_b)[0][0]

# Task 2: Calculate similarity between Iron Man and Finding Nemo
score_ac = cosine_similarity(movie_a, movie_c)[0][0]
score_ad = cosine_similarity(movie_a, movie_d)[0][0]
print("--- Scikit-Learn Similarity Results ---")
# Rounding to 2 decimal places for a clean look
print(f"Similarity (Iron Man vs. Avengers): {round(score_ab, 2)}")
print(f"Similarity (Iron Man vs. Finding Nemo): {round(score_ac, 2)}")
print(f"Similarity (Iron Man vs. Clone): {round(score_ad, 2)}")
# Logic Check
if score_ab > 0.8:
    print("\nResult: These movies are a great match for a recommendation!")
