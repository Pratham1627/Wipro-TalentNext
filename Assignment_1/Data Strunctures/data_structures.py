List
# Create a list of 5 integers and display the list items. Access individual elements through index.
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("First Element:", numbers[0])
print("Second Element:", numbers[1])
print("Third Element:", numbers[2])
print("Fourth Element:", numbers[3])
print("Fifth Element:", numbers[4])


# Append a new item to the end of the list.
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

item = int(input("Enter a number to append: "))

numbers.append(item)

print("Updated List:", numbers)


# Reverse the order of the items in the list.
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

numbers.reverse()

print("Reversed List:", numbers)


# Print the number of occurrences of a specified element in a list.
numbers = [10, 20, 30, 20, 40, 20, 50]

element = int(input("Enter the element to count: "))

count = numbers.count(element)

print("Occurrences:", count)


# Append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("List1:", list1)
print("List2:", list2)

list2 = list1 + list2

print("Updated List2:", list2)


# Insert a new item before the second element in an existing list.
numbers = [10, 20, 30, 40]

print("Original List:", numbers)

item = int(input("Enter the new item: "))

numbers.insert(1, item)

print("Updated List:", numbers)


# Remove the item from a specified index in a list.
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

index = int(input("Enter the index to remove: "))

numbers.pop(index)

print("Updated List:", numbers)


# Remove the first occurrence of a specified element from a list.
numbers = [10, 20, 30, 20, 40, 20]

print("Original List:", numbers)

element = int(input("Enter the element to remove: "))

numbers.remove(element)

print("Updated List:", numbers)


Dictionary
# Add a key and value to a dictionary.
dict1 = {0: 10, 1: 20}

dict1[2] = 30

print(dict1)


# Concatenate the following dictionaries to create a new one.
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

result = {}

result.update(dict1)
result.update(dict2)
result.update(dict3)

print(result)


# Check if a given key already exists in a dictionary.
dict1 = {1: "Apple", 2: "Banana", 3: "Mango"}

key = int(input("Enter the key: "))

if key in dict1:
    print("Key exists.")
else:
    print("Key does not exist.")


# Iterate over a dictionary using a for loop and print
# the keys, values, and key-value pairs.
dict1 = {
    1: "Apple",
    2: "Banana",
    3: "Mango"
}

print("Keys:")
for key in dict1:
    print(key)

print("\nValues:")
for value in dict1.values():
    print(value)

print("\nKeys and Values:")
for key, value in dict1.items():
    print(key, ":", value)


# Prepare a dictionary where the keys are numbers
# from 1 to 15 and the values are the squares of the keys.
dict1 = {}

for i in range(1, 16):
    dict1[i] = i * i

print(dict1)


# Sum all the values in a dictionary.
dict1 = {
    1: 10,
    2: 20,
    3: 30,
    4: 40
}

total = sum(dict1.values())

print("Sum of values =", total)


Tuple
# Print the 4th element from first and 4th element from last in a tuple.
tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)

print("4th element from first:", tuple1[3])
print("4th element from last:", tuple1[-4])


# Check whether an element exists in a tuple or not.
tuple1 = (10, 20, 30, 40, 50)

element = int(input("Enter the element to search: "))

if element in tuple1:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")


# Convert a list into a tuple.
list1 = [10, 20, 30, 40, 50]

tuple1 = tuple(list1)

print("Tuple:", tuple1)


# Find the index of an item in a tuple.
tuple1 = (10, 20, 30, 40, 50)

element = int(input("Enter the element: "))

if element in tuple1:
    print("Index:", tuple1.index(element))
else:
    print("Element not found.")


# Replace the last value of tuples in a list with 100.
list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result = []

for t in list1:
    new_tuple = t[:-1] + (100,)
    result.append(new_tuple)

print("Updated List:", result)


Set
# Remove a given item from the set.
set1 = {10, 20, 30, 40, 50}

print("Original Set:", set1)

item = int(input("Enter the item to remove: "))

if item in set1:
    set1.remove(item)
    print("Updated Set:", set1)
else:
    print("Item not found in the set.")


# Create an intersection of sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.intersection(set2)

print("Intersection:", result)


# Create a union of sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.union(set2)

print("Union:", result)


# Find the maximum and minimum value in a set.
set1 = {10, 20, 30, 40, 50}

print("Maximum Value:", max(set1))
print("Minimum Value:", min(set1))


String
# Count the number of upper and lower case letters in a string.
string = input("Enter a string: ")

upper = 0
lower = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# Check whether a given string is a palindrome or not.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Return a new string made of n copies of the first 2 characters of the original string.
string = input("Enter a string: ")

first_two = string[:2]
result = first_two * len(string)

print(result)


# Remove 'x' from the first and last position of a string.
string = input("Enter a string: ")

if len(string) > 0 and string[0] == 'x':
    string = string[1:]

if len(string) > 0 and string[-1] == 'x':
    string = string[:-1]

print(string)


# Return a string made of n repetitions of the last n characters of the string.
string = input("Enter a string: ")
n = int(input("Enter the value of n: "))

last_n = string[-n:]
result = last_n * n

print(result)
