# Import necessary modules to inspect the environment
import os
import sys
import platform

# Define the checklist of folders we created in Topic 6
required_folders = ["data", "scripts", "notebooks", "models", ".venv"]


def run_final_audit():
    print("🚀 STARTING MISSION CONTROL CHECK...")
    print("-" * 40)

    # 1. Check Python Version
    print(f"OS Detected: {platform.system()} {platform.release()}")
    print(f"Python Brain: {sys.version.split()[0]}")

    # 2. Check Virtual Environment
    if ".venv" in sys.executable:
        print("✅ Environment: ISOLATED (Virtual Environment Active)")
    else:
        print("❌ Environment: GLOBAL (Warning: Not in .venv)")

    # 3. Check Folder Structure
    missing = [f for f in required_folders if not os.path.exists(f)]
    if not missing:
        print("✅ Structure: ARCHITECTED (All folders present)")
    else:
        print(f"❌ Structure: INCOMPLETE (Missing: {missing})")

    # 4. Check for Movie Logic File from Topic 7
    if os.path.exists("scripts/movie_logic.py"):
        print("✅ Scripts: INITIALIZED (movie_logic.py found)")
    else:
        print("❌ Scripts: EMPTY (movie_logic.py missing)")

    print("-" * 40)
    if not missing and ".venv" in sys.executable:
        print("RESULT: YOU ARE GO FOR LAUNCH! 🎬")
    else:
        print("RESULT: NO-GO. Please fix the red items above.")


# Execute the audit
if __name__ == "__main__":
    run_final_audit()
