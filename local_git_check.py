# Import the subprocess module to run Git commands from Python
import subprocess


def verify_local_git():
    # Check if there is a .git folder in the current directory
    print("🔍 Checking if local Git is initialized...")

    # Run 'git status' and capture the result
    result = subprocess.run(["git", "status"], capture_output=True, text=True)

    # If 'fatal' is in the error message, Git isn't set up locally yet
    if "fatal" in result.stderr:
        print("❌ Local Git NOT found. Run 'git init' in the terminal first!")
    else:
        print("✅ Local Git is active and ready to be linked to GitHub.")


# Run the verification
if __name__ == "__main__":
    verify_local_git()
