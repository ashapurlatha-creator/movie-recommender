# Import the CountVectorizer tool from Scikit-Learn
from sklearn.feature_extraction.text import CountVectorizer

# Import pandas to help us see the result as a nice table
import pandas as pd

# Step 1: Create a tiny 'dataset' of movie descriptions
movie_plots = [
    "A space space battle in a galaxy far away",
    "A fast car chase in the city",
    "A space explorer finds a new galaxy",
]

# Step 2: Initialize the 'Machine' (The Bag-of-Words Creator)
# We call it 'vectorizer' because it turns text into vectors
vectorizer = CountVectorizer()

# Step 3: Train the machine and transform our text into numbers
# 'fit_transform' does both steps at once!
bow_matrix = vectorizer.fit_transform(movie_plots)

# Step 4: Get the 'Vocabulary' (The list of unique words the machine found)
feature_names = vectorizer.get_feature_names_out()

# Step 5: Convert the results into a readable DataFrame (Table)
# 'toarray()' turns the mathematical matrix into a standard grid of numbers
df_bow = pd.DataFrame(bow_matrix.toarray(), columns=feature_names)

# Print our Bag-of-Words table
print("--- Our First Bag-of-Words Matrix ---")
print(df_bow)

# Print the vocabulary to see which word belongs to which column index
print("\nMachine Vocabulary Index:")
print(vectorizer.vocabulary_)
