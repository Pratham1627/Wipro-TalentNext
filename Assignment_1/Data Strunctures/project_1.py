# Project 1: Dictionary of people and their interesting facts.

people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original Dictionary:")
for person, fact in people.items():
    print(person + ":", fact)

# Change Jeff's fact
people["Jeff"] = "Is afraid of heights."

# Add a new person
people["Jill"] = "Can hula dance."

print("\nUpdated Dictionary:")
for person, fact in people.items():
    print(person + ":", fact)
