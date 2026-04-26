# Create a list of movie genres for our recommendation logic
genres = [
    "Action",
    "Sci-Fi",
    "Comedy",
    "Drama",
    "Horror",
]


# Define a professional function to check if a genre exists in our list
def validate_genre(user_input):
    # Convert input to title case to match our list (e.g., 'action' becomes 'Action')
    formatted_input = user_input.title()

    # Check if the genre is in our approved list
    if formatted_input in genres:
        # Return a success message
        return f"✅ {formatted_input} is a valid genre for our engine."
    else:
        # Return an error message
        return f"❌ {formatted_input} is not in our database."


# Test the function with a user input
test_result = validate_genre("sci-fi")

# Print the final result to the terminal
print(test_result)
