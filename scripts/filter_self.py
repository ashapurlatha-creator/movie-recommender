# Import pandas to handle our recommendation table
import pandas as pd

# Step 1: Create a mock sorted result for 'Iron Man'
# Notice 'Iron Man' is at the top with a perfect 1.0 score
data = {
    "movie_title": [
        "Iron Man",
        "Iron Man 2",
        "Avengers: Age of Ultron",
        "Guardians of the Galaxy",
        "Ant-Man",
    ],
    "similarity_score": [1.0, 0.85, 0.82, 0.75, 0.60],
}

# Step 2: Create the DataFrame
df_results = pd.DataFrame(data)

# Step 3: THE FILTER
# We use slicing [1:6] to skip the first row (index 0) and take the next 5
# In Python, [1:] means "start from the second item and go to the end"
final_recommendations = df_results.iloc[2:6]

print("--- RAW MATH OUTPUT (The 'Silly' Way) ---")
print(df_results.head(3))

print("\n--- USER-READY RECOMMENDATIONS (The 'Smart' Way) ---")
# Now 'Iron Man' is gone, and 'Iron Man 2' is the #1 suggestion
print(final_recommendations)
