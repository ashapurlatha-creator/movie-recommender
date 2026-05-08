# Import the 'os' library to look at our computer's folders
import os

# Define the 'Checklist' of things a recruiter expects to see
professional_checklist = [
    "recommend.py",  # The main engine
    "models",  # The folder for our math 'brains'
    "data",  # The folder for our raw movies
    "README.md",  # The 'Instruction Manual' (We will create this soon!)
    ".gitignore",  # The 'Filter' for junk files (We will create this soon!)
]


def run_audit():
    # Print a professional header
    print("🕵️ Starting Project Audit for GitHub Readiness...")
    print("-" * 50)

    # Get a list of every file currently in your project folder
    current_files = os.listdir(".")

    # Loop through our checklist to see what is missing
    for item in professional_checklist:
        if item in current_files:
            # If the file exists, give it a checkmark
            print(f"✅ FOUND: {item}")
        else:
            # If it's missing, give it a warning
            print(f"❌ MISSING: {item} - Recruiter might be confused!")

    print("-" * 50)
    print("💡 Tip: A clean folder structure makes you look like a Senior Developer.")


# Run the audit function
if __name__ == "__main__":
    run_audit()
