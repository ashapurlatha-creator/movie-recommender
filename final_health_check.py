# Import the os module to interact with the file system
import os

# Define the essential files for our final engine
core_files = ["recommend.py", "README.md", ".gitignore"]


def final_health_check():
    print("📋 Running Final File Health Check...")
    print("-" * 30)

    for file in core_files:
        # Check if file exists
        if os.path.exists(file):
            # Check the size of the file in bytes
            file_size = os.path.getsize(file)
            if file_size > 0:
                print(f"✅ {file} is present and has data ({file_size} bytes).")
            else:
                print(f"⚠️ {file} is EMPTY! You need to add content before committing.")
        else:
            print(f"❌ {file} is MISSING! This will break your portfolio.")

    print("-" * 30)
    print("Check complete. If all are green, head to the Source Control tab!")


# Execute the health check
if __name__ == "__main__":
    final_health_check()
