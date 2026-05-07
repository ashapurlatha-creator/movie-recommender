# Import pandas for data loading
import pandas as pd

# Import the Vectorizer tool
from sklearn.feature_extraction.text import TfidfVectorizer

# Load our cleaned dataset
df = pd.read_csv("data/processed_movies.csv")

# Initialize the vectorizer
tfidf = TfidfVectorizer(stop_words="english")

# Transform the tags into our matrix
# By default, TfidfVectorizer outputs a 'Sparse Matrix'
tfidf_matrix = tfidf.fit_transform(df["tags"])

# --- SYSTEM INSPECTION ---

# 1. Check the 'type' of the matrix in the terminal
print(f"Matrix Type: {type(tfidf_matrix)}")

# 2. Calculate how many items are actually stored (Non-Zeros)
# 'nnz' stands for Number of Non-Zeros
print(f"Number of non-zero entries: {tfidf_matrix.nnz}")

# 3. Compare this to the 'Total Cells' (Rows * Columns)
total_cells = tfidf_matrix.shape[0] * tfidf_matrix.shape[1]
print(f"Total possible cells: {total_cells}")

# 4. Calculate the 'Sparsity' (How much empty space we saved)
sparsity = (1 - tfidf_matrix.nnz / total_cells) * 100
print(f"Sparsity: {sparsity:.2f}% (This much of the matrix is empty zeros!)")
