# Create a small sample list of movies
available_movies = []


# Define a function to find a movie's position (index)
def get_movie_index(target):
    # The 'try' block: Python will attempt to run this code
    try:
        # We try to find the index of the target movie
        index = available_movies.index(target)
        # If successful, we return the index
        return f"✅ Found! {target} is at position {index}."

    # The 'except' block: This runs ONLY if the 'try' block fails
    # 'ValueError' is the specific type of error Python throws for missing items
    except ValueError:
        # Instead of crashing, we return a helpful message
        return (
            f"❌ Sorry, '{target}' is not in our database. Please check your spelling."
        )


# --- TESTING THE SAFETY NET ---

# Test 1: A movie that exists (The 'Try' succeeds)
print(get_movie_index("Iron Man"))

# Test 2: A movie that DOES NOT exist (The 'Except' catches the fall)
print(get_movie_index("Batman"))

# This line will still run because the program didn't crash!
print("\n🚀 Program finished successfully without crashing.")
