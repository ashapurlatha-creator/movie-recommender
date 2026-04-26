# We define a function to 'squish' names together
def collapse_names(name_list):
    # Create an empty list to store our squished names
    squished_list = []

    # Loop through every name in our input list
    for name in name_list:
        # Use the .replace() method to turn " " (space) into "" (nothing)
        # This turns "Tom Cruise" into "TomCruise"
        clean_name = name.replace(" ", "")

        # Add the squished name to our new list
        squished_list.append(clean_name)

    # Return the final list to the program
    return squished_list


# --- TESTING THE SQUISH ---

# Imagine these are our Top 3 Actors for a movie
actors = ["Tom Cruise", "Tom Hanks", "Scarlett Johansson", "Christopher Nolan"]

# Run our function
cleaned_actors = collapse_names(actors)

# Print the results to see the difference
print(f"Original: {actors}")
print(f"Squished: {cleaned_actors}")

# Logic check:
if "TomCruise" in cleaned_actors and "Tom" not in cleaned_actors:
    print("\n✅ Success: The 'Tom' confusion has been prevented!")
