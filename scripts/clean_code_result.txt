# This code is intentionally messy to test the formatter
def calculate_movie_rating(score, reviews):
    # Notice the bad spacing above? The formatter will fix it!
    final_score = score * reviews  # Squished math is hard to read
    return final_score


# Calling the function with more messy spacing
print(calculate_movie_rating(8.5, 100))

# If 'Format on Save' is on, hit Ctrl+S and watch the code jump into place!
