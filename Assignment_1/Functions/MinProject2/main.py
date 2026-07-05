# Import the module
import name_module

# Take input from the user
name = input("Enter a name: ")

# Check palindrome
if name_module.ispalindrome(name):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")

# Count vowels
print("No of vowels:", name_module.count_the_vowels(name))

# Print frequency of letters
print("Frequency of letters:")

frequency = name_module.frequency_of_letters(name)

for key, value in frequency.items():
    print(key, "-", value)
