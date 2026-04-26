# Initial version of our script
# This function calculates a simple recommendation score
def get_simple_score(matches, total):
    # Calculate the percentage of matching tags
    score = round((matches / total), 2)
    # Return the score to the user
    return score


# Example calculation: 4 matches out of 10 tags
final_score = get_simple_score(4, 10)

# Print the result to the terminal
print(f"Confidence Score: {final_score}")
