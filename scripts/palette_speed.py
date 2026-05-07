# Import the 'time' module to measure how fast our search is
import time

# A simulated 'database' of movies for our search engine
movie_database = [
    "Iron Man",
    "The Incredible Hulk",
    "Iron Man 2",
    "Thor",
    "Captain America",
]


# A function to search for a movie by keyword
def search_movie(keyword):
    # Record the exact time the search starts
    start_time = time.time()

    # Use a 'list comprehension' to find movies containing the keyword
    # It checks every movie title for the search word
    results = [movie for movie in movie_database if keyword.lower() in movie.lower()]

    # Record the exact time the search finishes
    end_time = time.time()

    # Calculate the total time taken (End - Start)
    duration = end_time - start_time

    # Print the results and the speed
    print(f"Search Results for '{keyword}': {results}")
    print(f"Search completed in {duration:.6f} seconds.")


# Run our search for 'Iron'
if __name__ == "__main__":
    search_movie("Iron")
