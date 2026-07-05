# Check whether the given name is a palindrome.
def ispalindrome(name):

    if name == name[::-1]:
        return True
    else:
        return False


# Count the number of vowels in the given name.
def count_the_vowels(name):

    count = 0

    vowels = "aeiouAEIOU"

    for ch in name:
        if ch in vowels:
            count += 1

    return count


# Count the frequency of each letter in the given name.
def frequency_of_letters(name):

    frequency = {}

    for ch in name:

        if ch != " ":

            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

    return frequency
