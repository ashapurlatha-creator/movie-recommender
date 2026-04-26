# Import the pandas library as 'pd'
import pandas as pd

# Define the path to our movie dataset
file_path = "data/movies_5000.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# --- THE PEEK ---
print("--- TASK 1: PEEKING AT THE TOP 5 ROWS ---")
# .head() shows the first 5 rows by default
# This helps us see if the data looks 'correct' (no weird characters)
print(df.head())

# --- THE DIAGNOSIS ---
print("\n--- TASK 2: TECHNICAL DATA SUMMARY ---")
# .info() shows the number of rows, column names, and data types (int, float, object)
# It also shows if any data is 'Null' (Missing)
print(df.info())

# --- THE TAIL ---
print("\n--- TASK 3: PEEKING AT THE BOTTOM 2 ROWS ---")
# You can pass a number into the brackets to see a specific amount
print(df.tail(2))
