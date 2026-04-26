# Import the NumPy library (The industry standard for math)
import numpy as np

# Let's define two movies using three categories: [Action, Sci-Fi, Comedy]
# Movie 1: 'Avengers' (High Action, High Sci-Fi, Medium Comedy)
avengers = np.array([10, 9, 5])

# Movie 2: 'Iron Man' (High Action, High Sci-Fi, High Comedy)
iron_man = np.array([9, 10, 8])

# Movie 3: 'The Notebook' (No Action, No Sci-Fi, Medium Comedy)
the_notebook = np.array([0, 0, 20])

# Manual Dot Product Calculation (The Grocery List logic)
# (10*9) + (9*10) + (5*8) = 90 + 90 + 40 = 220
overlap_score_marvel = np.dot(avengers, iron_man)

# Calculate overlap between Avengers and The Notebook
# (10*0) + (9*0) + (5*5) = 0 + 0 + 25 = 25
overlap_score_romance = np.dot(avengers, the_notebook)

print("--- The Handshake Test (Dot Product) ---")
print(f"Overlap Score (Avengers & Iron Man): {overlap_score_marvel}")
print(f"Overlap Score (Avengers & The Notebook): {overlap_score_romance}")

# Conclusion logic
if overlap_score_marvel > overlap_score_romance:
    print(
        "\nResult: Avengers and Iron Man have a much stronger mathematical handshake!"
    )
