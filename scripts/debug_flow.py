# Function 1: Prepares the search word
def format_search(raw_input):
    # Convert text to lowercase for consistency
    clean_text = raw_input.lower()
    # Add a log message
    print(f"DEBUG: Formatted input to {clean_text}")
    # Return the cleaned text
    return clean_text


# Function 2: Simulates the recommendation
def get_recommendation(movie_name):
    # Use the first function to clean the name
    # This is a 'jump' from one station to another
    target = format_search(movie_name)
    # Return a mock recommendation
    return f"Since you liked {target}, you will like Avengers."


# --- MAIN EXECUTION ---
# Pick a movie with messy capitalization
user_query = "iRoN mAn"

# Call the main function
# We will pause the code here to watch it work!
final_result = get_recommendation(user_query)

# Print the output
print(final_result)
