# --- (Previous logic for loading and accessing the row remains above) ---
import pickle
import pandas as pd

# Assume we have our similarity_row from Topic 4 (a list of scores)
# For this demo, we'll use a small dummy version of a similarity row
dummy_row = [0.12, 0.99, 0.45, 0.01]

# --- NEW TOPIC 5 LOGIC START ---

# Use enumerate() to staple the Index to the Score
# This creates a list of 'Tuples' like (index, score)
stapled_scores = list(enumerate(dummy_row))

# Print the result to the terminal
print("--- The Enumeration Hack ---")
print(f"Original Row: {dummy_row}")
print(f"Stapled Pairs: {stapled_scores}")

# Explain what we see
print(f"\nThe first item is {stapled_scores[0]}.")
print(f"This means Movie Index 0 has a similarity score of {stapled_scores[0][1]}.")

# This list of pairs is what we will sort in the next lesson!
