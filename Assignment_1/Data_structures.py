============================================================
Program 1: Create a List of 5 Integers and Access Elements
============================================================
# Program 1: Create a List of 5 Integers and Display the List Items

# Creating a list
numbers = [10, 20, 30, 40, 50]

# Displaying the complete list
print("List:", numbers)

# Accessing elements using index
print("First Element :", numbers[0])
print("Second Element:", numbers[1])
print("Third Element :", numbers[2])
print("Fourth Element:", numbers[3])
print("Fifth Element :", numbers[4])
============================================================
Program 2: Append a New Item to the List
============================================================
# Program 2: Append a New Item to the End of the List

# Creating a list
numbers = [10, 20, 30, 40, 50]

# Display original list
print("Original List:", numbers)

# Taking input from user
item = int(input("Enter a number to append: "))

# Appending item
numbers.append(item)

# Display updated list
print("Updated List:", numbers)
============================================================
Program 3: Reverse the List
============================================================
# Program 3: Reverse the Order of Items in the List

# Creating a list
numbers = [10, 20, 30, 40, 50]

# Display original list
print("Original List:", numbers)

# Reversing the list
numbers.reverse()

# Display reversed list
print("Reversed List:", numbers)
============================================================
Program 4: Count Occurrences of an Element
============================================================
# Program 4: Count the Number of Occurrences of an Element

# Creating a list
numbers = [10, 20, 30, 20, 40, 20, 50]

# Display list
print("List:", numbers)

# Taking input
element = int(input("Enter the element to count: "))

# Counting occurrences
count = numbers.count(element)

# Display result
print("Number of Occurrences:", count)
============================================================
Program 5: Append List1 to the Front of List2
============================================================
# Program 5: Append Items of List1 to the Front of List2

# Creating two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Display original lists
print("List1:", list1)
print("List2:", list2)

# Adding list1 before list2
list2 = list1 + list2

# Display updated list2
print("Updated List2:", list2)
============================================================
Program 6: Insert an Item Before the Second Element
============================================================
# Program 6: Insert a New Item Before the Second Element

# Creating a list
numbers = [10, 20, 30, 40]

# Display original list
print("Original List:", numbers)

# Taking input
item = int(input("Enter the new item: "))

# Insert at index 1 (before second element)
numbers.insert(1, item)

# Display updated list
print("Updated List:", numbers)
============================================================
Program 7: Remove an Item Using Index
============================================================
# Program 7: Remove an Item from a Specified Index

# Creating a list
numbers = [10, 20, 30, 40, 50]

# Display original list
print("Original List:", numbers)

# Taking index input
index = int(input("Enter index to remove: "))

# Remove item using pop()
numbers.pop(index)

# Display updated list
print("Updated List:", numbers)
============================================================
Program 8: Remove the First Occurrence of an Element
============================================================
# Program 8: Remove the First Occurrence of a Specified Element

# Creating a list
numbers = [10, 20, 30, 20, 40, 20]

# Display original list
print("Original List:", numbers)

# Taking input
element = int(input("Enter element to remove: "))

# Remove first occurrence
numbers.remove(element)

# Display updated list
print("Updated List:", numbers)

