# --- (Previous logic for loading, indexing, and enumerating remains above) ---

# This is a sample of our 'stapled_scores' from Topic 5
# Format: [(Index, Score), (Index, Score), ...]
sample_stapled = [(0, 0.12), (1, 0.99), (2, 0.45), (3, 0.01)]

# --- NEW TOPIC 6 LOGIC START ---

# We use the 'sorted' function to reorganize our list
# 1. 'reverse=True' means we want Descending order (Highest score first)
# 2. 'key=lambda x: x[1]' tells Python: "Sort by the second item in the pair (the score)"
sorted_matches = sorted(sample_stapled, reverse=True, key=lambda x: x[1])

# Print the results to see the 'Winners'
print("--- Sorting Results ---")
print(f"Before Sort: {sample_stapled}")
print(f"After Sort:  {sorted_matches}")

# Explain the winner
winner_index = sorted_matches[0][0]  # Get the index of the top match
winner_score = sorted_matches[0][1]  # Get the score of the top match
print(f"\n🏆 The winner is Movie Index {winner_index} with a score of {winner_score}")
