# Import the pandas library to read our CSV
import pandas as pd


# Use the 'def' keyword to define a new function named 'load_and_clean_data'
def load_and_clean_data():
    # Define the path to our dataset
    file_path = "data/movies_5000.csv"

    # Load the data using pandas
    df = pd.read_csv(file_path)

    # Clean the 'overview' column by filling empty spots with blank text
    df["overview"] = df["overview"].fillna("")

    # Print a success message to the terminal
    print("✅ Success: Data loaded and Nulls handled!")

    # 'return' gives the finished table back to whoever called the function
    return df


def show_movie_count(data):
    print("Total movies:", len(data))


# --- THE EXECUTION ---
# This part of the code actually 'presses the button'
print("Starting the program...")

# Call our function and store the result in a variable called 'movie_data'
movie_data = load_and_clean_data()
show_movie_count(movie_data)

# Show the first 5 rows to prove it worked
print(movie_data.head())
