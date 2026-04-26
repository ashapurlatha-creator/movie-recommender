# Import the sklearn library to check if it's installed
import sklearn

# Import the specific tool we will use for vectorization later
from sklearn.feature_extraction.text import CountVectorizer

# Print a professional status report
print("--- Scikit-Learn Installation Audit ---")

# Check the version of scikit-learn
print(f"✅ Scikit-Learn Version: {sklearn.__version__}")

# Try to initialize the 'Vectorizing Machine' (CountVectorizer)
# This proves the library isn't just there, but actually working
test_machine = CountVectorizer()

# If we reached this line, the machine is ready!
print("✅ Status: Vectorization tools are ONLINE.")
print("Result: You are ready to turn stories into numbers!")
