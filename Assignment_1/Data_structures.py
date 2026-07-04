// Create a list of 5 integers and display the list items. Access individual elements through index.
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("First Element:", numbers[0])
print("Second Element:", numbers[1])
print("Third Element:", numbers[2])
print("Fourth Element:", numbers[3])
print("Fifth Element:", numbers[4])


// Append a new item to the end of the list.
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

item = int(input("Enter a number to append: "))

numbers.append(item)

print("Updated List:", numbers)


// Reverse the order of the items in the list.
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

numbers.reverse()

print("Reversed List:", numbers)


// Print the number of occurrences of a specified element in a list.
numbers = [10, 20, 30, 20, 40, 20, 50]

element = int(input("Enter the element to count: "))

count = numbers.count(element)

print("Occurrences:", count)


// Append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("List1:", list1)
print("List2:", list2)

list2 = list1 + list2

print("Updated List2:", list2)


// Insert a new item before the second element in an existing list.
numbers = [10, 20, 30, 40]

print("Original List:", numbers)

item = int(input("Enter the new item: "))

numbers.insert(1, item)

print("Updated List:", numbers)


// Remove the item from a specified index in a list.
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

index = int(input("Enter the index to remove: "))

numbers.pop(index)

print("Updated List:", numbers)


// Remove the first occurrence of a specified element from a list.
numbers = [10, 20, 30, 20, 40, 20]

print("Original List:", numbers)

element = int(input("Enter the element to remove: "))

numbers.remove(element)

print("Updated List:", numbers)
