# Project 2: Find the runner-up score.

scores = list(map(int, input("Enter the scores separated by space: ").split()))

# Remove duplicate scores
scores = list(set(scores))

# Sort the scores
scores.sort()

# Print the second highest score
print("Runner-up Score:", scores[-2])
