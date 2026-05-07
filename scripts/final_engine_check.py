# Import the pickle library to load binary files
import pickle

# Import os to check if files exist on the hard drive
import os

# Define the paths to our 'Serialized Brain'
model_files = ["models/movies_list.pkl", "models/similarity.pkl"]


# Define a function to perform the final audit
def run_final_audit():
    print("🕵️  Starting Final Engine Audit...")

    # Check if the models folder exists
    if not os.path.exists("models"):
        print("❌ Error: 'models' folder is missing!")
        return

    # Loop through each required file to check its health
    for file_path in model_files:
        if os.path.exists(file_path):
            # Get the file size in Megabytes for the report
            file_size = os.path.getsize(file_path) / (1024 * 1024)
            print(f"✅ Found {file_path} ({file_size:.2f} MB)")
        else:
            print(f"❌ Error: {file_path} is missing!")
            return

    # Try to 'Wake Up' the brain one last time
    try:
        with open("models/movies_list.pkl", "rb") as f:
            movies = pickle.load(f)
        print(f"🧠 Brain Wake-up Success: {len(movies)} movies ready in memory.")
        print("🚀 STATUS: READY FOR PRODUCTION")
    except Exception as e:
        print(f"❌ Brain Wake-up Failed: {e}")


# Run the audit
run_final_audit()
