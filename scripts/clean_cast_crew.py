# Import the tool to turn strings into real Python lists
import ast


# Function 1: Extract the Top 3 Actors
def get_top_3(text):
    # Initialize an empty list for the actors
    actors = []
    # Convert the stringified list into a real list of dictionaries
    data = ast.literal_eval(text)
    # Loop through the list, but only for the first 3 items
    for i in data[0:3]:
        # Append the actor's real name to our list
        actors.append(i["name"])
    # Return the list of 3 names
    return actors


# Function 2: Extract ONLY the Director
def get_director(text):
    # Convert the stringified list into a real list of dictionaries
    data = ast.literal_eval(text)
    # Loop through every person in the crew
    for i in data:
        # Search for the person whose job title is 'Director'
        if i["job"] == "Director":
            # Return their name and stop searching
            return [i["name"]]
    # Return an empty list if no director is found
    return []


# --- TESTING THE VIP FILTER ---

# Mock data for a movie cast (usually very long)
messy_cast = '[{"name": "Robert Downey Jr."}, {"name": "Terrence Howard"}, {"name": "Jeff Bridges"}, {"name": "Gwyneth Paltrow"}]'
# Mock data for movie crew
messy_crew = '[{"job": "Director", "name": "Jon Favreau"}, {"job": "Producer", "name": "Kevin Feige"}]'

# Run our cleaning tools
print(f"Top 3 Actors: {get_top_3(messy_cast)}")
print(f"Director: {get_director(messy_crew)}")
