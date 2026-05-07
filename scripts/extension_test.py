# We are importing a math library to test IntelliSense
import math

# Creating a list of movies (Notice how VS Code colors these words)
movie_list = ["Iron Man", "Avengers", "Thor", "Hulk"]

# This function uses the math library to 'score' our list
def check_intelligence():
    # Get the number of movies in our list
    count = len(movie_list)
    
    # Calculate a fake 'Power Score' using math.sqrt (square root)
    # If Pylance is working, hovering over 'sqrt' will show you documentation!
    score = math.sqrt(count)
    
    # Print the result to the console
    print(f"Extension Check: Found {count} movies.")
    print(f"Mathematical Power Score: {score}")

# Run the function
if __name__ == "__main__":
    check_intelligence()

