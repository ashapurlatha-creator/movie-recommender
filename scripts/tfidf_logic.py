# Import the TfidfVectorizer from Scikit-Learn
from sklearn.feature_extraction.text import TfidfVectorizer

# Import pandas to display our mathematical results
import pandas as pd

# Two sample movie descriptions
# Note that 'space' appears in both, but 'jedi' is unique to one
movie_plots = ["A movie about a jedi in space", "A movie about a pilot in space"]

# Initialize the TF-IDF Machine
# We will include 'english' stop words as well for a clean result
tfidf_vectorizer = TfidfVectorizer(stop_words="english")

# Transform the text into a TF-IDF matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(movie_plots)

# Get the feature names (the words)
words = tfidf_vectorizer.get_feature_names_out()

# Create a DataFrame to see the scores
# These numbers represent the 'importance' of each word
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=words)

print("--- TF-IDF Importance Scores ---")
print(df_tfidf)

# Explain the result
print("\nLogic Check:")
print("Notice how 'jedi' and 'pilot' have higher scores than 'space'?")
print("Because 'space' is in both movies, the machine knows it is less unique!")
