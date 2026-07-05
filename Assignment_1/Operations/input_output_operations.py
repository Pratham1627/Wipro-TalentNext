# Read the entire content from a text file and display it to the user.
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()


# Read the first n lines from a text file.
n = int(input("Enter the number of lines to read: "))

file = open("sample.txt", "r")

for i in range(n):
    line = file.readline()

    if line == "":
        break

    print(line, end="")

file.close()


# Accept input from the user and append it to a text file.
text = input("Enter the text to append: ")

file = open("sample.txt", "a")

file.write(text + "\n")

file.close()

print("Text appended successfully.")


# Read contents from a text file line by line and store each line into a list.
file = open("sample.txt", "r")

lines = file.readlines()

file.close()

print("List of lines:")
print(lines)


# Find the longest word from the text file contents.
file = open("sample.txt", "r")

content = file.read()

file.close()

words = content.split()

longest = ""

for word in words:

    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)


# Count the frequency of a user-entered word in a text file.
word = input("Enter the word to search: ")

file = open("sample.txt", "r")

content = file.read()

file.close()

words = content.split()

count = words.count(word)

print("Frequency of", word, "=", count)
