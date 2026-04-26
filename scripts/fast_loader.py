# Import the pickle library to load our saved files
import pickle

# Import time to measure the loading speed
import time

# Record the start time
start_time = time.time()

print("🕒 Starting the Fast Loader...")

# Step 1: Load the Movie List
# 'rb' means Read Binary (required for .pkl files)
with open("models/movies_list.pkl", "rb") as f:
    movies = pickle.load(f)

# Step 2: Load the Similarity Matrix
with open("models/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Record the end time
end_time = time.time()

# Step 3: Verify the data is alive

print(f"✅ Fast Loading Complete in {end_time - start_time:.4f} seconds!")
print(f"📊 Verified: Loaded {len(movies)} movies and a {similarity.shape} matrix.")

# Step 4: Show a sample recommendation logic check
# Let's peek at the first movie in the list
print(f"🎬 Ready to recommend for: {movies.iloc[0]['title']}")
