# Create a list of movies to act as our mini-database
my_movies = ["Iron Man", "Avengers", "Black Panther", "Thor"]


# Define a function to suggest a movie based on its index (number)
def get_recommendation(index):
    # Retrieve the movie title from the list using the provided number
    # Note: IntelliSense should suggest 'my_movies' as you type it!
    selection = my_movies[index]

    # Return a formatted string with the recommendation
    return f"Since you liked Marvel, you should watch: {selection}"


# Create a variable for the movie we want to pick (0 is the first movie)
favorite_index = 1

# Call our function and store the result in a variable
result = get_recommendation(favorite_index)

# Print the result to the VS Code terminal
# Try hovering your mouse over 'print' to see the built-in documentation!
print(result)
