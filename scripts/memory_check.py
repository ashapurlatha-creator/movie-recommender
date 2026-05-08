# Import sys to access system-level information like memory size
import sys

# Import pickle to load our actual similarity matrix
import pickle

# Import numpy to demonstrate a 'Dense' version of the matrix
import numpy as np

# Load our pre-calculated similarity matrix
print("📂 Loading the similarity matrix...")
with open("models/similarity.pkl", "rb") as f:
    sim_matrix = pickle.load(f)

# --- MEMORY AUDIT START ---

# Step 1: Check the size of our current matrix (likely a NumPy array or Sparse matrix)
# sys.getsizeof() returns the size in bytes. We divide by 1024*1024 to get Megabytes (MB).
actual_size = sys.getsizeof(sim_matrix) / (1024 * 1024)
print(f"📊 Current Matrix Memory Usage: {actual_size:.2f} MB")

# Step 2: Compare it to the Movie List (Text data)
with open("models/movies_list.pkl", "rb") as f:
    movies_list = pickle.load(f)
list_size = sys.getsizeof(movies_list) / (1024 * 1024)
print(f"📄 Movie List Memory Usage: {list_size:.2f} MB")

# Step 3: Discussion - Why do we care?
# If we 'densified' our 4803x4803 matrix, it would take up significantly more space.
# Every float64 number takes 8 bytes. 4803 * 4803 * 8 bytes = ~184 MB.
# While 184MB is small for a PC, imagine 50,000 movies: that would be 20GB!
print(
    "\n💡 Optimization Tip: Keep your matrices sparse to prevent RAM crashes as data grows."
)
