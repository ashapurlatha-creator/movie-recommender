# Import the 'os' module to check file sizes and paths
import os

# Define the path to our newly downloaded dataset
data_file = "data/movies_5000.csv"

# Start the verification process
print("--- Dataset Arrival Check ---")

# 1. Check if the file actually exists in the data folder
if os.path.exists(data_file):
    # 2. Get the size of the file in bytes
    file_size = os.path.getsize(data_file)

    # 3. Convert bytes to Megabytes (MB) for easier reading
    size_in_mb = file_size / (1024 * 1024)

    # Print success messages
    print(f"✅ File Found: {data_file}")
    print(f"✅ File Size: {size_in_mb:.2f} MB")

    # If the file is very small, it might be corrupted or empty
    if size_in_mb > 0.1:
        print("✅ Status: Dataset looks healthy and ready for processing!")
    else:
        print("⚠️ Warning: File exists but seems too small. Check the download.")
else:
    # Print a failure message if the path is wrong
    print("❌ Error: Could not find 'movies_5000.csv' in the data folder.")
    print("TIP: Did you remember to drag-and-drop it into the 'data' folder?")

print("-" * 30)
