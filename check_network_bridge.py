# Import the subprocess module to talk to the system terminal
import subprocess


def check_network_bridge():
    # Print a status message for the student
    print("🛰️ Testing connection to GitHub 'Remote'...")

    # Run 'git remote -v' to see where the code is headed
    # capture_output=True allows us to read the result in Python
    result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)

    # Check if the output contains 'github.com'
    if "github.com" in result.stdout:
        print("✅ Connection Path Found:")
        # Print the actual URL found in the Git settings
        print(result.stdout.strip())
        print("\n🚀 You are cleared for launch!")
    else:
        # If the output is empty or wrong, the bridge is down
        print("❌ Error: No GitHub remote found. Did you link your repo in Topic 6?")


# Execute the bridge check
if __name__ == "__main__":
    check_network_bridge()
