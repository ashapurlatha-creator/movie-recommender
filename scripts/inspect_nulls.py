# Import the pandas library to work with our data table
import pandas as pd

# Define the file path to our dataset
file_path = 'data/movies_5000.csv'

# Load the dataset into a DataFrame
df = pd.read_csv(file_path)

# Use .isnull() to check every cell for a 'Null' or 'NaN'
# Use .sum() to add them up for each column so we get a total count
null_report = df.isnull().sum()

# Print the header for our report
print("--- Missing Data Audit (Null Counts) ---")

# Display the report showing how many blanks are in each column
print(null_report)

# Find specific columns that are very messy
# Tagline and Homepage usually have the most nulls
print("\n🔍 Observation:")
print(f"The 'overview' column has {null_report['overview']} missing values.")
