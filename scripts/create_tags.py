# Create a mock row of already cleaned data
# Note: Overview is a string, but the others are lists (thanks to our Unpacker)
movie_data = {
    "overview": "A billionaire builds a high-tech suit to fight crime.",
    "genres": ["Action", "Sci-Fi", "Adventure"],
    "keywords": ["superhero", "marvel", "billionaire"],
    "cast": ["RobertDowneyJr", "TerrenceHoward", "JeffBridges"],
    "director": ["JonFavreau"],
    "mood": ["Exciting", "Intense"],
}

# Step 1: Convert the 'overview' string into a list of words
# This makes it easier to combine with our other lists
overview_list = movie_data["overview"].split()

# Step 2: Combine all lists into one giant 'Master List'
# In Python, you can add lists together: [1] + [2] = [1, 2]
combined_list = (
    overview_list
    + movie_data["genres"]
    + movie_data["keywords"]
    + movie_data["cast"]
    + movie_data["director"]
    + movie_data["mood"]
)

# Step 3: Turn the 'Master List' back into one giant string
# We use " ".join() to put a space between every word
tags_string = " ".join(combined_list)

# Step 4: Make everything lowercase
# Our engine shouldn't care if it's 'Action' or 'action'
final_tags = tags_string.lower()

print("--- The Final Blend ---")
print(f"Final Tags Column Content:\n{final_tags}")
