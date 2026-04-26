# Import the 'pickle' library (Built into Python, no install needed)
import pickle

# Import os to create folders if they are missing
import os

# Step 1: Create a piece of 'Hard Work' (A mock similarity score)
# In our real project, this would be our giant 4803x4803 Matrix
engine_brain = {"Iron Man": 0.99, "Avengers": 0.85, "The Lion King": 0.12}

# Step 2: Ensure the 'models' directory exists
if not os.path.exists("models"):
    os.makedirs("models")  # Creates the folder if you forgot to do it manually

# Step 3: Pickling (Serialization)
# 'wb' means 'Write Binary' - we are writing computer-code, not text
print("📦 Packing the brain into a pickle file...")
with open("models/test_model.pkl", "wb") as file:
    pickle.dump(engine_brain, file)  # This 'dumps' the variable into the file

# Step 4: Clear the variable to prove it's gone from memory
engine_brain = None
print(f"Memory Check: Variable is now {engine_brain}")

# Step 5: Unpickling (Deserialization)
# 'rb' means 'Read Binary'
print("🔓 Unpacking the brain to use it again...")
with open("models/test_model.pkl", "rb") as file:
    restored_brain = pickle.load(file)  # This 'loads' the data back into a variable

# Verify it worked
print(f"Restored Data: {restored_brain}")
