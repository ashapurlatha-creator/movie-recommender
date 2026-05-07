# Import the pandas library and give it the nickname 'pd' (Industry Standard)
import pandas as pd

# Import the numpy library and give it the nickname 'np' (Industry Standard)
import numpy as np

# Print a status message to the terminal
print("--- Toolkit Verification ---")

# Check the version of Pandas we just installed
print(f"✅ Pandas Version: {pd.__version__}")

# Check the version of NumPy we just installed
print(f"✅ NumPy Version: {np.__version__}")

# Create a small 'Test Table' using Pandas to prove it works
# This is called a 'DataFrame' - think of it as a digital spreadsheet
test_data = pd.DataFrame({"Tool": ["Pandas", "NumPy"], "Status": ["Ready", "Ready"]})

# Display our small test table in the terminal
print("\nInstallation Check Summary:")
print(test_data)

print("\nResult: Your Data Science toolkit is fully operational!")
