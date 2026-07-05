# Find the meeting time and meeting place from a text file.

file = open("sample.txt", "r")

lines = file.readlines()

file.close()

# Find meeting time using the number of lines.
line_count = len(lines)

if line_count <= 12:
    time = str(line_count) + " AM"
else:
    time = str(line_count - 12) + " PM"

# Find the most frequently occurring word.
words = []

for line in lines:

    line = line.replace(".", "")
    line = line.replace(",", "")
    line = line.lower()

    words.extend(line.split())

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

max_word = ""
max_count = 0

for word, count in frequency.items():

    if count > max_count:
        max_count = count
        max_word = word

# Display the result.
print("Meeting Time:", time)
print("Meeting Place:", max_word.capitalize() + " Street")
