# Calculate happiness using command line arguments.
import sys

# Convert the command line arguments into lists.
like = sys.argv[1].split("-")
dislike = sys.argv[2].split("-")
numbers = sys.argv[3].split("-")

happiness = 0

# Calculate happiness.
for num in numbers:

    if num in like:
        happiness += 1

    elif num in dislike:
        happiness -= 1

# Display the final happiness.
print("Final Happiness =", happiness)
