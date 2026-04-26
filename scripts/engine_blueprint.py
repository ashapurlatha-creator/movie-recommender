# Function 1: The 'Data Station'
def load_movie_data():
    # In a real app, this would load the CSV
    # For this blueprint, we are just returning a status message
    print("📦 Station 1: Data loaded successfully.")
    return "Movie Database"


# Function 2: The 'Math Station'
def transform_to_math(data):
    # This station takes the 'data' from Station 1
    print(f"🧮 Station 2: Transforming {data} into Vectors...")
    return "Mathematical Matrix"


# Function 3: The 'Recommendation Station'
def get_recommendations(matrix, user_choice):
    # This station takes the 'matrix' from Station 2 and the user's input
    print(f"🎯 Station 3: Searching matrix for movies like '{user_choice}'...")
    return ["Movie 1", "Movie 2", "Movie 3"]


# --- THE MASTER LOGIC (The Flow) ---
# This is where we connect the stations together
print("--- Starting Recommendation Engine Flow ---")

# Step 1: Get the data
raw_materials = load_movie_data()

# Step 2: Pass raw materials to the math station
math_vectors = transform_to_math(raw_materials)

# Step 3: Get final results based on a user's choice
final_list = get_recommendations(math_vectors, "Iron Man")


def send_notification():
    print("📲 Sending recommendation to user's phone...")


print(f"✅ Final Output for User: {final_list}")
send_notification()
