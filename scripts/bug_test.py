# Import our tools (assume data is loaded)
import pandas as pd

# Let's create a tiny dummy 'Similarity Row'
# Format: (Movie Index, Similarity Score)
# We want the highest score (0.98) to be the recommendation
mock_scores = [(0, 0.1), (1, 0.98), (2, 0.5), (3, 0.05)]

print("--- Start Bug Test ---")

# LOGIC ERROR: We 'forgot' to add reverse=True
# This will sort from LOWEST similarity to HIGHEST
# So our recommendation will be the most DIFFERENT movie, not the most similar!
broken_sort = sorted(mock_scores, key=lambda x: x[1])

# Let's print the 'top' recommendation
print(f"Engine Suggestion: Movie Index {broken_sort[0][0]}")
print(f"Similarity Score: {broken_sort[0][1]}")

# If this were a real app, the user would get a terrible recommendation
# and we wouldn't see a red error message in the terminal!
print("--- End Bug Test ---")
