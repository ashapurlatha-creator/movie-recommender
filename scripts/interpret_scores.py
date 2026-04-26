# Import the similarity tool
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# We define 3 distinct 'Genre vectors' [Action, Comedy, Sci-Fi]
# A 'Pure Action' movie
movie_pure_action = np.array([[10, 0, 0]])

# A 'Pure Comedy' movie (Completely different)
movie_pure_comedy = np.array([[0, 10, 0]])

# An 'Action-Comedy' movie (A mix of both)
movie_mix = np.array([[10, 2, 0]])

# Task 1: Compare Pure Action vs Pure Comedy (Expect 0)
score_opposite = cosine_similarity(movie_pure_action, movie_pure_comedy)[0][0]

# Task 2: Compare Pure Action vs the Mix (Expect somewhere in the middle)
score_partial = cosine_similarity(movie_pure_action, movie_mix)[0][0]

# Task 3: Compare Pure Action vs itself (Expect 1)
score_identical = cosine_similarity(movie_pure_action, movie_pure_action)[0][0]

# We will set a breakpoint on the next line to inspect these!
print("--- Check the 'Variables' tab on the left to see the scores! ---")
print(f"Opposite: {score_opposite}")
print(f"Partial: {score_partial}")
print(f"Identical: {score_identical}")
