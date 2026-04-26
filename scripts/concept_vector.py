# We will represent two movies as simple 'coordinates' (Vectors)
# Imagine the first number is 'Action Level' and the second is 'Space Level'
# Scale is 0 to 10

# Movie 1: 'Star Wars' (High Action, High Space)
star_wars = [9, 10]

# Movie 2: 'Fast & Furious' (High Action, Low Space)
fast_furious = [10, 1]

# Movie 3: 'Interstellar' (Low Action, High Space)
interstellar = [3, 9]

# Movie 3: 'Avatar' (Low Action, High Space)
avatar = [8, 8]


# A function to show the 'coordinates' in the terminal
def show_coordinates(name, vector):
    # Print the movie name and its mathematical address
    print(f"{name} lives at coordinates: {vector}")


print("--- The Movie Map (Vectorization Concept) ---")
show_coordinates("Star Wars", star_wars)
show_coordinates("Fast & Furious", fast_furious)
show_coordinates("Interstellar", interstellar)
show_coordinates("Avatar", avatar)

# Logic check: Which is closer to Star Wars?
# A computer simply looks at the numbers to decide!
print("\nRobot Logic:")
print("Star Wars and Interstellar both have high 'Space' numbers (10 and 9).")
print("Therefore, the robot recommends Interstellar to a Star Wars fan!")
