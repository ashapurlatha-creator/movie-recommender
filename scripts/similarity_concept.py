# Import the NumPy library for mathematical operations
import numpy as np

# Let's define two movies as simple vectors
# [Action Score, Sci-Fi Score]
# Movie A is a short description of a Space Movie
movie_a = np.array([1, 1])

# Movie B is a very LONG description of a similar Space Movie
# It has the same 'direction' (equal parts Action/Sci-Fi) but higher values
movie_b = np.array([5, 5])

# Movie C is a purely Action movie with no Sci-Fi
movie_c = np.array([1, 1.1])


# Function to calculate 'Euclidean Distance' (Measuring the feet)
def get_euclidean(v1, v2):
    # Calculates the straight-line distance between points
    return np.linalg.norm(v1 - v2)


# Function to calculate 'Cosine Similarity' (Measuring the angle)
def get_cosine(v1, v2):
    # This formula calculates the 'closeness' of the direction
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


print("--- Distance vs. Similarity ---")

# Compare Movie A (Short Space) to Movie B (Long Space)
print(f"A vs B - Euclidean Distance: {get_euclidean(movie_a, movie_b):.2f}")
print(f"A vs B - Cosine Similarity: {get_cosine(movie_a, movie_b):.2f}")

# Compare Movie A (Short Space) to Movie C (Action)
print(f"\nA vs C - Euclidean Distance: {get_euclidean(movie_a, movie_c):.2f}")
print(f"A vs C - Cosine Similarity: {get_cosine(movie_a, movie_c):.2f}")

print("\nConclusion: Cosine Similarity sees A and B as IDENTICAL (1.00) in taste!")
