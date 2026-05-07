# Import the Abstract Syntax Trees (ast) library
import ast

# This is what a 'Genre' looks like in our raw CSV file
# It is actually a STRING that looks like a list
messy_cell = '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}]'

# Let's prove it is a string
print(f"Before Unwrapping: {type(messy_cell)}")

# Use ast.literal_eval to 'unwrap' the string into a real Python List
# This 'evaluates' the string and turns it into actual data structures
clean_list = ast.literal_eval(messy_cell)

# Now let's check the type again
print(f"After Unwrapping: {type(clean_list)}")

# Now that it's a list, we can easily grab the first 'name'
print(f"First Genre Found: {clean_list[0]['name']}")

# Example of why this is better:
for item in clean_list:
    # We can now loop through and print just the names
    print(f"Found Genre: {item['name']}")
    # --- New Unpacker Test ---

messy_keywords = '["superhero", "marvel", "billionaire"]'

clean_keywords = ast.literal_eval(messy_keywords)

print(clean_keywords[1])
