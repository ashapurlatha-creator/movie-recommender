# Import the 'subprocess' library to run terminal commands from Python
import subprocess


def check_git_config():
    print("🔍 Checking your local Git identity...")

    # Run the command to find your git username
    user = subprocess.getoutput("git config user.name")
    # Run the command to find your git email
    email = subprocess.getoutput("git config user.email")

    # Print the results so you can see if they match your GitHub account
    print(f"👤 Current Name: {user}")
    print(f"📧 Current Email: {email}")

    if user == "" or email == "":
        print("⚠️ Warning: Your local Git identity is not set yet!")
    else:
        print("✅ Local identity found. Ready to link to GitHub!")


if __name__ == "__main__":
    check_git_config()
